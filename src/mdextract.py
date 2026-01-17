import re

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    # This function extracts markdown image syntax from the given text
    # and returns a list of tuples containing the alt text and URL.

    image_pattern = r'!\[([^\[\]]*)\]\(([^\(\)]*)\)'
    matches = re.findall(image_pattern, text)
    
    image_nodes = []
    for alt_text, url in matches:
        image_nodes.append((alt_text, url))
    
    return image_nodes

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    # This function extracts markdown link syntax from the given text
    # and returns a list of tuples containing the link text and URL.

    link_pattern = r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)'
    matches = re.findall(link_pattern, text)
    
    link_nodes = []
    for link_text, url in matches:
        link_nodes.append((link_text, url))
    
    return link_nodes