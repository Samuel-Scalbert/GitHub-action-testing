import os
import sys
from lxml import etree
from github import Github, GithubException
import json

def check_xml_files(files):
    for file_path in files:
        try:
            tree = etree.parse(file_path)
            root = tree.getroot()
            if root.tag != "tei":
                raise Exception(f"File {file_path} does not contain a <tei> tag")
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
            sys.exit(1)  # Exit with a non-zero code

if __name__ == "__main__":
    files = json.loads(sys.argv[1])
    check_xml_files(files)
