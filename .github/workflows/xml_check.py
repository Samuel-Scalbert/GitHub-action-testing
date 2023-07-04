import sys

def get_first_line(file_path):
    try:
        with open(file_path, "r") as file:
            return file
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
