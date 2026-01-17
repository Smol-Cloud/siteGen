from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    # Splits TextNodes of a specific TextType by a given delimiter.
    new_nodes = []
    
    # Iterate through each node in the old_nodes list
    for node in old_nodes:
        # If the node is of the enum type text, we want to split
        if node.text_type == TextType.TEXT:
            # We need a way of confirming that there is always a matching delimiter
            # We count the occurrences of the delimiter in the text and check that it's even.
            if node.text.count(delimiter) % 2 == 0:
                parts = node.text.split(delimiter)
                for i, part in enumerate(parts):
                    if i % 2 == 0:
                        # Even index parts are normal text
                        if part:
                            new_nodes.append(TextNode(text=part, text_type=TextType.TEXT))
                    else:
                        # Odd index parts are of the specified text_type
                        # Check that the part has at least one character, if not raise an error.
                        if part:
                            new_nodes.append(TextNode(text=part, text_type=text_type))
                        else:
                            raise ValueError(f"Empty text between delimiters '{delimiter}' in text: {node.text}")
            else:
                raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")
        else:
            new_nodes.append(node)

    return new_nodes