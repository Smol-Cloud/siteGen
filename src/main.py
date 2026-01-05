from textnode import TextNode, TextType

def main():
    # Create a text type object
    bold_type = TextType.BOLD

    # Create a text node object
    text_node = TextNode("Hello, World!", bold_type)

    # Display the text node
    print(text_node)

if __name__ == "__main__":
    main()