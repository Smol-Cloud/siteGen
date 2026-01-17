from texttohtml import text_node_to_html_node
from textnode import TextNode, TextType
import unittest

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_type(self):
        text_node = TextNode(text_type=TextType.TEXT, text="Hello, World!")
        html_node = text_node_to_html_node(text_node)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "Hello, World!")

    def test_bold_type(self):
        text_node = TextNode(text_type=TextType.BOLD, text="Bold Text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold Text")

    def test_italic_type(self):
        text_node = TextNode(text_type=TextType.ITALIC, text="Italic Text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic Text")

    def test_code_type(self):
        text_node = TextNode(text_type=TextType.CODE, text="print('Hello')")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('Hello')")

    def test_link_type(self):
        text_node = TextNode(text_type=TextType.LINK, text="OpenAI", url="https://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "OpenAI")
        self.assertEqual(getattr(html_node, "props", {}).get("href"), "https://example.com")

    def test_image_type(self):
        text_node = TextNode(text_type=TextType.IMAGE, text="An image", url="https://example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(getattr(html_node, "props", {}).get("src"), "https://example.com/image.png")
        self.assertEqual(getattr(html_node, "props", {}).get("alt"), "An image")

    def test_unsupported_type(self):
        text_node = TextNode(text_type="UNSUPPORTED", text="Unsupported") # pyright: ignore[reportArgumentType]
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(text_node)
        self.assertEqual(str(context.exception), "Unsupported TextType: UNSUPPORTED")

if __name__ == "__main__":
    unittest.main()