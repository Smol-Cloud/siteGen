from typing import Optional, List, Dict, Any

class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[List["HTMLNode"]] = None,
        props: Optional[Dict[str, str]] = None
    ) -> None:
        self.tag: Optional[str] = tag
        self.value: Optional[str] = value
        self.children: Optional[List["HTMLNode"]] = children
        self.props: Optional[Dict[str, str]] = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        # return a formatted string representing the HTML attributes of the node.
        if not self.props:
            return ""
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"