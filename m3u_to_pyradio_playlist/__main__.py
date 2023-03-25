"""m3u_to_pyradio_playlist main function."""

import argparse
import os
import time

from .converter import convert_m3u_to_csv
from .utils import is_not_blank
from .downloader import get_huge_playlist


def main():
    """Run main function."""
    parser = argparse.ArgumentParser(
        prog="m3u_to_pyradio",
        description="""
This program converts .m3u files into pyradio playlists.

examples:
   m3u_to_pyradio -d\tDownloads and creates a huge stations.csv
   m3u_to_pyradio -a\tSame as -a and overrides current pyradio stations
   m3u_to_pyradio -i playlist.m3u -o playlist.csv
                    \tCreates playlist.csv file from your playlist.m3u file
""",
        usage=("m3u_to_pyradio [-h] [-i INPUT -o OUTPUT] [-d] [-a]"),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-i",
        "--input",
        help="The m3u input file",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="The output CSV file where playlist will be saved",
    )
    parser.add_argument(
        "-d",
        "--download-super-list",
        help=(
            "Download and convert the complete m3u list from "
            "https://github.com/junguler/m3u-radio-music-playlists."
        ),
        action="store_true",
    )
    parser.add_argument(
        "-a",
        "--auto",
        help=(
            "DANGER: Same as -dsl but OVERRIDES "
            "your ~/.config/pyradio/stations.csv"
        ),
        action="store_true",
    )

    args = vars(parser.parse_args())

    input_filename = args.get("input")
    output_filename = args.get("output")
    download_mode = args.get("download_super_list")
    auto_mode = args.get("auto")

    if not (input_filename or output_filename or download_mode or auto_mode):
        print("Error: you should provide options. See it with --help.")
        exit(1)

    if (input_filename or output_filename) and (download_mode or auto_mode):
        print("Error: you should use -i and -o only without -d or -a.")
        exit(1)

    if not (download_mode or auto_mode) and not (
        input_filename and output_filename
    ):
        print("Error: you should use both -i and -o at the same time.")
        print("Example: -i input.m3u -o playlist.csv")
        exit(1)

    if download_mode and auto_mode:
        print("Error: You should use -a or -d, not both.")
        exit(1)

    if (input_filename and output_filename) or (download_mode or auto_mode):
        try:

            if download_mode or auto_mode:
                get_huge_playlist()
                input_filename = "temp.m3u"
                output_filename = "stations.csv"

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

                if download_mode or auto_mode:
                    print("Removing temp.m3u...")
                    os.remove(input_filename)
                print(f"Output written to `{output_filename}`!")

            else:
                raise FileNotFoundError("Error: Invalid input filename.")

        except Exception as e:
            print(str(e))
            exit(1)

        finally:
            finished_at = time.perf_counter()
            print(
                (
                    f"Finished converting {len(m3u_file_as_list)} radio(s)"
                    f"in {round(finished_at - started_at, 2)} seconds(s)"
                )
            )

        try:
            if auto_mode:
                print("Moving stations.csv to pyradio config file...")
                home_dir = os.path.expanduser("~")
                pyradio_dir = os.path.join(home_dir, ".config", "pyradio")
                os.makedirs(pyradio_dir, exist_ok=True)

                src_path = "stations.csv"
                dest_path = os.path.join(pyradio_dir, "stations.csv")
                os.replace(src_path, dest_path)
                print(
                    "Finished moving stations.csv to your pyradio config file!"
                )
                print("Start `pyradio` and have fun :) !")

        except Exception:
            raise RuntimeError("Failed to move the stations.csv file.")
            exit(1)


if __name__ == "__main__":
    main()
