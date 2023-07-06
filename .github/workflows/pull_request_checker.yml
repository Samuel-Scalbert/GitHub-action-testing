import sys
from bs4 import BeautifulSoup
from datetime import datetime

def xml_checker(file_path):
        with open(file_path, "r") as file:
            soup = BeautifulSoup(file, features="xml")
            error_msg = []

            tags = ['titleStmt', 'encodingDesc', 'text', 'TEI', 'lb', 'div', 'body', 'profileDesc',
                    'authority', 'principal', 'availability', 'publicationStmt']
            for tag in tags:
                    if not soup.find(tag):
                        error = ['lacking the tag :', tag]
                        error_msg.append(error)

            filedesc_tag = soup.find("fileDesc")
            if not filedesc_tag:
                error_msg.append("fileDesc tag not found.")

            titlestmt_tag = filedesc_tag.find("titleStmt") if filedesc_tag else None
            if not titlestmt_tag:
                error_msg.append("titleStmt is not a child of fileDesc.")
            else:
                author_tag = titlestmt_tag.find('author')
                principal_tag = titlestmt_tag.find('principal')
                if not (author_tag or principal_tag):
                    error_msg.append("In the titleStmt, either of <author> and <principal> tags are missing.")

                title_tag = titlestmt_tag.find("title", attrs={"xml:lang": "en"})
                if not title_tag:
                    error_msg.append("The title tag is missing within titleStmt.")
                elif "xml:lang" not in title_tag.attrs or title_tag["xml:lang"] != "en":
                    error_msg.append("The title tag is missing the attribute xml:lang='en'.")

            teiHeader_tag = soup.find('teiHeader')
            if not teiHeader_tag:
                error_msg.append("teiHeader tag not found.")
            else:
                p_tags = teiHeader_tag.find_all('p')
                for p_tag in p_tags:
                    if "xml:lang" not in p_tag.attrs or p_tag["xml:lang"] not in ["en", "fr", "de"]:
                        error_msg.append("A p tag within teiHeader is missing the attribute xml:lang with valid language values.")

            pb_tags = soup.find_all('pb')
            for pb_tag in pb_tags:
                if "facs" not in pb_tag.attrs and "n" not in pb_tag.attrs:
                    error_msg.append("A pb tag is missing the attribute 'facs' or 'n'.")

            p_tags = soup.find_all('p')
            for p_tag in p_tags:
                if p_tag.attrs == "rend":
                  if p_tag["rend"] not in ["right", "center", "left"]:
                    error_msg.append("A p tag is missing the a valid attributes values, it should either be @rend='right,center,left'")

            revisionDesc_tags = soup.find_all('revisionDesc')
            for revisionDesc_tag in revisionDesc_tags:
                if not revisionDesc_tag['status']:
                     error_msg.append("A revision Desc tag is missing the attributes 'status'")

            licence_tags = soup.find_all('licence')
            for licence_tag in licence_tags:
                if not licence_tag['target']:
                    error_msg.append("A Licence tag is missing the attributes 'target'")

            change_tags = soup.find_all("change")
            for change_tag in change_tags:
                if not change_tag['when-iso']:
                    error_msg.append("A change tag is missing the attributes 'when-iso'")
                else:
                    format_string = '%Y-%m-%d'
                    try:
                        datetime.strptime(change_tag['when-iso'], format_string)
                    except ValueError:
                        error_msg.append(f"this date: {change_tag['when-iso']} is not in a valid format")

            note_tags = soup.find_all('note')
            for note_tag in note_tags:
                if note_tag.get('type') in ['folliation', 'gloss'] or note_tag.attrs == {'hand': True}:
                    if note_tags['rend'] not in ['right', 'center', 'left'] or note_tag['place']=='top':
                        error_msg.append("A note tag with the attributes 'folliation' and a 'rend' attribute has a wrong rend values (either 'right', 'center', 'left' are allowed")

            hi_tags = soup.find_all('hi')
            for hi_tag in hi_tags:
                if hi_tag['rend'] not in ('underline', 'superscript', 'align(center)', 'latin'):
                    error_msg.append(f"The {hi_tag} tag is either missing the good values ('underline', 'superscript' 'underline', 'align(center)', 'latin') for the attributes 'rend' or it lacks the attributes 'n'")
                if hi_tag['rend'] == 'underline' and hi_tag.get('n') == "2":
                    error_msg.append(f"The {hi_tag} is missing the attributes 'n'")

            del_tags = soup.find_all('del')
            for del_tag in del_tags:
                rend_value = del_tag.get('rend')
                if rend_value is not None and rend_value not in ['overwritten', 'strikethrough']:
                    error_msg.append(
                        f"This {del_tag} is missing the good values ('overwritten', 'strikethrough') for the attribute 'rend'"
                    )

            tags_to_check = {
                'title': ['align(right)', 'align(center)', 'align(center) underline', 'align(right) underline'],
                'salute': ['align(right)', 'align(center)', 'align(left)', 'indent'],
                'dateline': ['align(right)', 'align(center)', 'align(left)', 'indent'],
                'addrLine': ['align(right)', 'align(center)', 'indent', 'align(left)', 'margin'],
                'list': ['align(right)', 'align(center)', 'align(left)'],
                'signed': ['align(right)', 'align(center)', 'align(left)'],
                'address': ['align(right)', 'align(center)', 'align(left)']
            }

            for tag_name, rend_formats in tags_to_check.items():
                tags = soup.find_all(tag_name)
                for tag in tags:
                    rend_value = tag.get('rend')
                    if rend_value is not None and rend_value not in rend_formats:
                        error_msg.append(
                            f"The <{tag_name}> tag '{tag.text}' '{rend_value}' has an incorrect format for the 'rend' attribute. Valid formats: {rend_formats}")

            tw_tags = soup.find_all('tw')
            for tw_tag in tw_tags:
                if tw_tag.get('type') == 'letterhead' and tw_tag.get('place') in ['top(right)', 'top(center)']:
                    rend_value = tw_tag.get('rend')
                    if rend_value is not None and rend_value not in ['align(right)', 'align(center)', 'align(left)']:
                        error_msg.append(
                            f"The <tw> tag '{tw_tag.text}' with type='letterhead' and place='{tw_tag.get('place')}' has an incorrect format for the 'rend' attribute. Valid formats: align(right), align(center), align(left)")

            metamark_tags = soup.find_all('metamark')
            for metamark_tag in metamark_tags:
                style_value = metamark_tag.get('style')
                rend_value = metamark_tag.get('rend')
                if style_value is not None and style_value not in ['x', 'horizontal_rule', 'crosses', 'dots', 'line',
                                                                   'double_line', 'vertical_rule',
                                                                   'curved_horizontal_line']:
                    error_msg.append(
                        f"The <metamark> tag '{metamark_tag.text}' has an incorrect format for the 'style' attribute. Valid formats: x, horizontal_rule, crosses, dots, line, double_line, vertical_rule, curved_horizontal_line")
                if rend_value is not None and rend_value not in ['align(right)', 'align(center)', 'align(left)']:
                    error_msg.append(
                        f"The <metamark> tag '{metamark_tag.text}' has an incorrect format for the 'rend' attribute. Valid formats: align(right), align(center), align(left)")

            date_tags = soup.find_all('date')
            for date_tag in date_tags:
                if not any(attr in date_tag.attrs for attr in ['when', 'when-iso']):
                    error_msg.append(f"The date tag '{date_tag}' is missing the 'when' or 'when-iso' attribute.")

            if len(error_msg) >= 1:
                return error_msg
            else:
                return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the XML file path as a command-line argument.")
        sys.exit(1)

    file_path = sys.argv[1]

    result = xml_checker(file_path)
    print(result)

