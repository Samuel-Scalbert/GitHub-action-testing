import os
import sys
from lxml import etree

def check_xml_files():
 
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
            sys.exit(1)  # Exit with a non-zero code

if __name__ == "__main__":
    check_xml_files()
