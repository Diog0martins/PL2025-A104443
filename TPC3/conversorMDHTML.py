import re

def count_header_num(match):
    hashtags = match.group(1) 
    header_level = len(hashtags)
    content = match.group(2).strip()
    return f"<h{header_level}>{content}</h{header_level}>"

def create_html_list(match):
    list_element_regex = r"^\d+\.(.+)$"
    
    elements_list = ""
    
    for element_match in re.finditer(list_element_regex, match.group(0), flags=re.MULTILINE):
        text_after_dot = element_match.group(1).strip()
        element = f"<li>{text_after_dot}</li>\n" 
        elements_list += element

    return f"<ol>\n{elements_list}</ol>\n"

def main():

    with open("convert_to_html.md") as file:
        markdown = file.read()

    header_regex = r"(#+)(.+?)$"
    bold_regex = r"\*\*(.*?)\*\*"
    italic_regex = r"\*(.*?)\*"
    link_regex = r"\[(.*?)\]\((.*?)\)"
    image_regex = r"!\[(.*?)\]\((.*?)\)"

    list_regex = r"(\d+\..+?\n)+"

    paragraph_regex = r"(?<=\n)(?!<)(?!\n)(.*)"

    markdown = re.sub(bold_regex, r"<b>\1</b>", markdown)

    markdown = re.sub(italic_regex, r"<i>\1</i>", markdown)

    markdown = re.sub(header_regex, count_header_num, markdown, flags=re.MULTILINE)

    markdown = re.sub(image_regex, r'<img src="\2" alt="\1">', markdown)
    
    markdown = re.sub(link_regex, r'<a href="\2">\1</a>', markdown)

    markdown = re.sub(list_regex, create_html_list, markdown)

    markdown = re.sub(paragraph_regex, r"<p>\1</p>", markdown)


    print(markdown)


if __name__ == '__main__':
        main()