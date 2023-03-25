"""Functions used to convert m3u to CSV."""


def create_csv_line(index: int, line: str, fullList: list) -> str:
    """Format a CSV line from m3u."""
    if line.startswith("#"):
        return None

    title = fullList[index - 1].split(",")[-1]

    return f"{title},{line}"


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
