import sys
from bs4 import BeautifulSoup

def has_tags(file_path, tags):
    try:
        with open(file_path, "r") as file:
            soup = BeautifulSoup(file, "xml", features="xml")
            for tag in tags:
                if soup.find(tag):
                    return tag
            return False
    except Exception as e:
        error_message = str(e)
        return error_message

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the XML file path and tags as command-line arguments.")
        sys.exit(1)

    file_path = sys.argv[1]
    tags = ['p']
    result = has_tags(file_path, tags)
    print(result)
