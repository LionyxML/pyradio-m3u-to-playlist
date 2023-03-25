"""Functions used to convert m3u to CSV."""

last_group = ''

def create_csv_line(index: int, line: str, fullList: list) -> str:
    """Format a CSV line from m3u."""
    global last_group
    if line.startswith("#"):
        return None

    try:
        group, title = fullList[index - 1].split('" group-title="')[1].split('", ')
    except IndexError:
        title = fullList[index - 1].split(",")[-1]
        group = ''

    if group != last_group:
        out = f'"{group}",-\n"{title}",{line}'
        last_group = group
    else:
        out = f'"{title}",{line}'
    return out

def convert_m3u_to_csv(m3u_content: list) -> list:
    """Given the content of a m3u file, returns the contents for a CSV file."""
    if not isinstance(m3u_content, (list)):
        return []

    return list(
        filter(
            None,
            map(
                lambda x: create_csv_line(x[0], x[1], m3u_content),
                enumerate(m3u_content),
            ),
        )
    )
