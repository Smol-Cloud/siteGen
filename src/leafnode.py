from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        # If the leaf node has no value, it should raise a ValueError. All leaf nodes must have a value.
        if self.value is None:
            raise ValueError("Leaf nodes must have a value.")
        # If there is no tag (e.g. it's None), the value should be returned as raw text.
        if self.tag is None:
            return self.value
        # Leaf node cannot have children, so we don't need to recurse.
        opening_tag = f"<{self.tag}{self.props_to_html()}>"
        closing_tag = f"</{self.tag}>"
        value_html = self.value if self.value else ""
        return f"{opening_tag}{value_html}{closing_tag}"
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"