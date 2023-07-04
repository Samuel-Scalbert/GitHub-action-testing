import sys
from bs4 import BeautifulSoup

def has_tags(file_path, tags):
    try:
        with open(file_path, "r") as file:
            soup = BeautifulSoup(file, features="xml")
            all_tags = []
            for tag in tags:
                if not soup.find(tag):
                    all_tags.append(tag)
            return all_tags
    except Exception as e:
        error_message = str(e)
        return error_message

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the XML file path and tags as command-line arguments.")
        sys.exit(1)

    file_path = sys.argv[1]
    tags = [
        'TEI',
        'abbr',
        'add',
        'addrLine',
        'address',
        'affiliation',
        'analytic',
        'anchor',
        'argument',
        'att',
        'bibl',
        'biblStruct',
        'body',
        'cell',
        'change',
        'choice',
        'cit',
        'closer',
        'date',
        'dateline',
        'del',
        'delSpan',
        'desc',
        'div',
        'education',
        'eg',
        'egXML',
        'elementSpec',
        'emph',
        'encodingDesc',
        'event',
        'figure',
        'fileDesc',
        'floatingText',
        'foreign',
        'fw',
        'gap',
        'geo',
        'gi',
        'handShift',
        'head',
        'hi',
        'idno',
        'imprint',
        'item',
        'label',
        'lb',
        'licence',
        'list',
        'location',
        'metamark',
        'milestone',
        'moduleRef',
        'monogr',
        'name',
        'note',
        'opener',
        'org',
        'orgName',
        'p',
        'pb',
        'persName',
        'person',
        'place',
        'placeName',
        'postscript',
        'profileDesc',
        'pubPlace',
        'publicationStmt',
        'publisher',
        'quote',
        'ref',
        'relation',
        'revisionDesc',
        'row',
        'rs',
        'salute',
        'schemaSpec',
        'seg',
        'sex',
        'signed',
        'speaker',
        'specDesc',
        'specList',
        'stamp',
        'subst',
        'supplied',
        'table',
        'teiHeader',
        'term',
        'text',
        'title',
        'titleStmt',
        'trailer',
        'unclear'
    ]

    result = has_tags(file_path, tags)
    print(result)
