"""Functions used to convert m3u to CSV."""

last_group = ''

def html_entities_to_unicode_chars(a_string: str) -> str:
    ent = {
        '&#039;': "'",
        '&#1110;': 'і',
        '&#225;': 'á',
        '&#227;': 'ã',
        '&#39;': "'",
        '&#47;': '/',
        '&#93;': ']',
        '&amp;': '&',
        '&apos;': "'",
        '&gt;': '>',
        '&quot;': '"',
        '&#xe1;': 'á',
    }
    for n in ent.keys():
        a_string = a_string.replace(n, ent[n])
    return a_string

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
    return html_entities_to_unicode_chars(out)

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
