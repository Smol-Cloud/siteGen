from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        # If there is no tag (e.g. it's None), raise a value error.
        if not self.tag:
            raise ValueError("Parent nodes must have a tag.")
        # If there are no children, raise a value error.
        if not self.children:
            raise ValueError("Parent nodes must have children.")
        # Construct a string representing the HTML tag of the node and its children. 
        # This should be a recursive method (each recursion being called on a nested child node).
        # You can iterate over all the children and call to_html on each, concatenating the results and injecting them between the opening and closing tags of the parent.
        opening_tag = f"<{self.tag}{self.props_to_html()}>"
        children_html = "".join(child.to_html() for child in self.children)
        closing_tag = f"</{self.tag}>"
        return f"{opening_tag}{children_html}{closing_tag}"

    def __repr__(self):
        # Recursive function to represent the ParentNode and its children
        # We need to build a string representation of the children
        # We need to consider which whether the child is a ParentNode or LeafNode
        children_repr = []
        for child in self.children:
            children_repr.append(repr(child))
        return f"ParentNode(tag={self.tag}, children=[{', '.join(children_repr)}], props={self.props})"
