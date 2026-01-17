from platform import node
from texttohtml import text_node_to_html_node
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter
import unittest

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_delimiter_single_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_multiple_code(self):
        node = TextNode("Here is `code one` and here is `code two`.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("code one", TextType.CODE),
            TextNode(" and here is ", TextType.TEXT),
            TextNode("code two", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_single_code_no_text_after(self):
        node = TextNode("This is text with a `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_no_code(self):
        node = TextNode("This is text without code blocks.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text without code blocks.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_non_text_type(self):
        node = TextNode("This is bold text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is bold text", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_empty_parts(self):
        node = TextNode("Text with `` empty code `` blocks", TextType.TEXT)
        # Expecting ValueError due to empty text between delimiters
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_split_nodes_bold_delimiter(self):
        node = TextNode("This is **bold text** in a sentence.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" in a sentence.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_italic_delimiter(self):
        node = TextNode("This is *italic text* in a sentence.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" in a sentence.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_unmatched_delimiter(self):
        node = TextNode("This is text with an unmatched `code block word", TextType.TEXT)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(context.exception), "Unmatched delimiter '`' in text: This is text with an unmatched `code block word")

if __name__ == "__main__":
    unittest.main()