import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag_raises_value_error(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_no_children_raises_value_error(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_repr_single_leaf_node(self):
        leaf_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [leaf_node], props={"class": "container"})
        expected_repr = "ParentNode(tag=div, children=[LeafNode(tag=span, value=child, props=None)], props={'class': 'container'})"
        self.assertEqual(repr(parent_node), expected_repr)
    
    def test_repr_multiple_leaf_nodes(self):
        leaf_node1 = LeafNode("span", "child1")
        leaf_node2 = LeafNode("a", "child2")
        parent_node = ParentNode("div", [leaf_node1, leaf_node2], props={"class": "container"})
        expected_repr = "ParentNode(tag=div, children=[LeafNode(tag=span, value=child1, props=None), LeafNode(tag=a, value=child2, props=None)], props={'class': 'container'})"
        self.assertEqual(repr(parent_node), expected_repr)

    def test_repr_nested_parent_nodes(self):
        leaf_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [leaf_node])
        parent_node = ParentNode("div", [child_node], props={"id": "main"})
        expected_repr = "ParentNode(tag=div, children=[ParentNode(tag=span, children=[LeafNode(tag=b, value=grandchild, props=None)], props=None)], props={'id': 'main'})"
        self.assertEqual(repr(parent_node), expected_repr)

if __name__ == "__main__":
    unittest.main()