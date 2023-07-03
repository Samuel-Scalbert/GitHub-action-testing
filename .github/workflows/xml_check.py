import os
import sys
from lxml import etree
import subprocess

def check_xml_files(file_path):
    try:
        tree = etree.parse(file_path)
        root = tree.getroot()
        if root.tag != "{http://www.tei-c.org/ns/1.0}TEI":
            raise Exception(f"File {file_path} does not contain a <tei> tag")
            sys.exit(59)
        print(f"File {file_path} is valid.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the XML file path as a command-line argument.")
        sys.exit(1)

    file_path = sys.argv[1]
    check_xml_files(file_path)
