from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    
    # It should handle each type of the TextType enum. 
    # If it gets a TextNode that is none of those types, it should raise an exception. 
    # Otherwise, it should return a new LeafNode object.

    # TextType.TEXT: This should return a LeafNode with no tag, just a raw text value.
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    # TextType.BOLD: This should return a LeafNode with a "b" tag and the text
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    # TextType.ITALIC: "i" tag, text
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    # TextType.CODE: "code" tag, text
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    # TextType.LINK: "a" tag, anchor text, and "href" prop
    elif text_node.text_type == TextType.LINK:
        if text_node.url is None:
            raise ValueError("Link TextNode must have a URL.")
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    # TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
    elif text_node.text_type == TextType.IMAGE:
        if text_node.url is None:
            raise ValueError("Image TextNode must have a URL.")
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")