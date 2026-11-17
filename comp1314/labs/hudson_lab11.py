#!/usr/bin/env python3
"""Lab 11 - File I/O and Looping"""


def get_input_file():
    """Prompt for an existing, readable input file."""
    while True:
        filename = input("Input filename (default name_list.txt): ").strip()
        filename = filename or "name_list.txt"

        try:
            with open(filename, "r") as infile:
                names = infile.readlines()

            return filename, names

        except OSError as error:
            print(f"Unable to read '{filename}': {error}")


def get_output_file():
    """Prompt for an output filename that can be written."""
    while True:
        filename = input("Output filename (default alpha.txt): ").strip()
        filename = filename or "alpha.txt"

        try:
            with open(filename, "w") as outfile:
                pass

            return filename

        except OSError as error:
            print(f"Unable to write to '{filename}': {error}")


def convert_names(names, filename):
    """Convert names to last, first and alphabetize by last name."""
    sorted_names = [
        line.strip().split() for line in names if line.strip()
    ]

    sorted_names.sort(key=lambda name: (name[1], name[0]))

    with open(filename, "w") as outfile:
        for name in sorted_names:
            outfile.write(f"{name[1]}, {name[0]}\n")

    print(f"\nCreated alphabetized file: {filename}")


def find_name_line(names, name):
    """Return the original line number of an exact name match."""
    for line_number, line in enumerate(names, start=1):
        if line.strip().casefold() == name.casefold():
            return line_number

    return None


def find_name(names):
    """Prompt for a name and handle exact and partial matches."""
    while True:
        name = input("\nEnter name to find (default Mason Howard): ").strip()
        name = name or "Mason Howard"

        # Check for an exact match first
        line_number = find_name_line(names, name)

        if line_number:
            print(f"{name} found on line {line_number}.")
            return

        # Find partial matches
        matches = [
            (line_number, line.strip())
            for line_number, line in enumerate(names, start=1)
            if name.casefold() in line.casefold()
        ]

        if not matches:
            print(f"No matches found for '{name}'. Try again.")
            continue

        # Display partial matches
        print("\nPartial matches:")

        for index, (line_number, match) in enumerate(matches, start=1):
            print(f"{index}. {match} (line {line_number})")

        print("0. Search again")

        # Ask user to select a match
        while True:
            choice = input("Select a name (0 to search again): ").strip()

            try:
                selection = int(choice)

                if selection == 0:
                    break

                if 1 <= selection <= len(matches):
                    line_number, match = matches[selection - 1]
                    print(f"{match} found on line {line_number}.")
                    return

            except ValueError:
                pass

            print(f"Enter a number between 0 and {len(matches)}.")


def main():
    """Run Lab 11 exercises."""
    # Get input file
    input_filename, names = get_input_file()
    print(f"Read {len(names)} lines from {input_filename}.")

    # Get output file and convert names
    output_filename = get_output_file()

    while True:
        try:
            convert_names(names, output_filename)
            break

        except OSError as error:
            print(f"Unable to write to '{output_filename}': {error}")
            output_filename = input(
                "Enter another output filename: "
            ).strip()

            while not output_filename:
                output_filename = input(
                    "Output filename cannot be blank: "
                ).strip()

    # Find a name
    find_name(names)


if __name__ == "__main__":
    main()

