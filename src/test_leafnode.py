import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode(tag="div", value="Hello", props={"class": "my-class"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"class": "my-class"})

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_tag(self):
        node = LeafNode(tag="p", value="Paragraph", props={"style": "color:red;"})
        expected_html = '<p style="color:red;">Paragraph</p>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_without_tag(self):
        node = LeafNode(tag=None, value="Raw text")
        self.assertEqual(node.to_html(), "Raw text")

    def test_to_html_no_value_raises(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag="p", value=None)
            node.to_html()

    def test_repr(self):
        node = LeafNode(tag="p", value="Paragraph", props={"style": "color:red;"})
        expected_repr = "LeafNode(p, Paragraph, {'style': 'color:red;'})"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()