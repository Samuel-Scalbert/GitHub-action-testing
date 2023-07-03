import os
import sys
from lxml import etree
import subprocess

def check_xml_files(file_path):
    try:
        tree = etree.parse(file_path)
        root = tree.getroot()
        if root.tag != "{http://www.tei-c.org/ns/1.0}TEI":
            error_message = f"File {file_path} does not contain a <tei> tag"
            print(error_message)
            sys.exit(1)
        print(f"File {file_path} is valid.")
    except Exception as e:
        error_message = str(e)
        print(f"Error: {error_message}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the XML file path as a command-line argument.")
        sys.exit(1)

    file_path = sys.argv[1]
    check_xml_files(file_path)
