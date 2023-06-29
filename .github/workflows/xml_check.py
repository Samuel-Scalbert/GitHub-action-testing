import os
import sys
from lxml import etree
import subprocess

def check_xml_files():
    xml_files = []
    for root, dirs, files in os.walk(".", topdown=False):
        for file in files:
            if file.endswith(".xml"):
                xml_files.append(os.path.join(root, file))

    for file_path in xml_files:
        try:
            tree = etree.parse(file_path)
            root = tree.getroot()
            if root.tag != "{http://www.tei-c.org/ns/1.0}TEI":
                raise Exception(f"File {file_path} does not contain a <tei> tag")
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
            # Revert the changes made to the file
            subprocess.run(["git", "checkout", "--", file_path])
            sys.exit(1)  # Exit with a non-zero code

    print("All XML files contain a <tei> tag.")

if __name__ == "__main__":
    check_xml_files()
