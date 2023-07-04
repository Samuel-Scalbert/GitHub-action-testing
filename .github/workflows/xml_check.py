import sys

def get_first_line(file_path):
    try:
        with open(file_path, "r") as file:
            # Skip the first line if it starts with '<?xml'
            first_line = next(file).strip()
            if first_line.startswith('<?xml'):
                first_line = next(file).strip()
                first_line_with_newline = first_line + "\n"
            return first_line_with_newline
    except Exception as e:
        error_message = str(e)
        return error_message

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the XML file path as a command-line argument.")
        sys.exit(1)

    file_path = sys.argv[1]
    first_line = get_first_line(file_path)
    print(first_line)
