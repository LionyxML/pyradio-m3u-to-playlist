"""m3u_to_pyradio_playlist main function."""

import argparse
import os
import sys
import time

from .converter import convert_m3u_to_csv
from .utils import is_not_blank


def main():
    """Run main function."""
    parser = argparse.ArgumentParser(
        prog="m3u_to_pyradio",
        description=(
            "This program converts m3u files"
            " into pyradio playlists. "
            "Generate your playlist.csv and add it to pyRadio."
        ),
        usage=(
            f"{os.path.basename(sys.argv[0])} "
            f"--input playlist.m3u"
            f"--output playlist.csv"
        ),
    )
    parser.add_argument(
        "-i", "--input", help="The m3u input file", required=True
    )
    parser.add_argument(
        "-o",
        "--output",
        help="The output CSV file where playlist will be saved.",
        required=True,
    )

    args = vars(parser.parse_args())

    input_filename = args.get("input")
    output_filename = args.get("output")

    try:
        started_at = time.perf_counter()

        if is_not_blank(input_filename) and is_not_blank(output_filename):
            m3u_file_as_list = []

            if os.path.exists(input_filename):
                with open(input_filename, "r") as file:
                    for line in file:
                        m3u_file_as_list.append(line.strip())

                    csv_file_as_list = convert_m3u_to_csv(m3u_file_as_list)

                with open(output_filename, "w") as file:
                    for item in csv_file_as_list:
                        file.write(str(item) + "\n")

            else:
                raise FileNotFoundError("Invalid input filename.")

    except Exception as e:
        print(str(e))
        exit(1)

    finally:
        finished_at = time.perf_counter()
        print(
            (
                f"Finished converting {len(m3u_file_as_list)} radio(s)"
                f"in {round(started_at-finished_at, 2)} seconds(s)"
            )
        )


if __name__ == "__main__":
    main()
