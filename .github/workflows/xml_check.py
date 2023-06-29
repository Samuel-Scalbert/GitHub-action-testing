import os
import sys
from bs4 import BeautifulSoup

def check_xml_files():
    xml_files = []
    for root, dirs, files in os.walk(".", topdown=False):
        for file in files:
            if file.endswith(".xml"):
                xml_files.append(os.path.join(root, file))

    for file_path in xml_files:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                soup = BeautifulSoup(content, "xml")
                if not soup.find("tei"):
                    raise Exception(f"File {file_path} does not contain a <tei> tag")
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
            sys.exit(1)  # Exit with a non-zero code

if __name__ == "__main__":
    check_xml_files()
