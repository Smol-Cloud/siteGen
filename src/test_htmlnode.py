import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "my-class"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "my-class"})

    def test_props_to_html(self):
        node = HTMLNode(props={"id": "header", "class": "main-header"})
        props_html = node.props_to_html()
        self.assertIn(' id="header"', props_html)
        self.assertIn(' class="main-header"', props_html)

    def test_props_to_html_empty(self):
        node = HTMLNode()
        props_html = node.props_to_html()
        self.assertEqual(props_html, "")
    
    def test_repr(self):
        node = HTMLNode(tag="p", value="Paragraph", children=None, props={"style": "color:red;"})
        expected_repr = "HTMLNode(tag=p, value=Paragraph, children=None, props={'style': 'color:red;'})"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()