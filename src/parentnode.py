
from typing import Optional, List, Dict
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: Optional[List[HTMLNode]],
        props: Optional[Dict[str, str]] = None
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        # If there is no tag (e.g. it's None), raise a value error.
        if not self.tag:
            raise ValueError("Parent nodes must have a tag.")
        # If there are no children, raise a value error.
        if not self.children:
            raise ValueError("Parent nodes must have children.")
        opening_tag = f"<{self.tag}{self.props_to_html()}>"
        children_html = "".join(child.to_html() for child in self.children)
        closing_tag = f"</{self.tag}>"
        return f"{opening_tag}{children_html}{closing_tag}"

    def __repr__(self) -> str:
        children_repr = []
        if self.children:
            for child in self.children:
                children_repr.append(repr(child))
        return f"ParentNode(tag={self.tag}, children=[{', '.join(children_repr)}], props={self.props})"
