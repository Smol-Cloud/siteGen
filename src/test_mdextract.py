from mdextract import extract_markdown_images, extract_markdown_links
import unittest

from textnode import TextType

class TestMdExtract(unittest.TestCase):
    def test_extract_markdown_images_single(self):
        text = "Here is an image: ![Alt text](http://example.com/image.png)"
        images = extract_markdown_images(text)
        expected_images = [("Alt text", "http://example.com/image.png")]
        self.assertEqual(images, expected_images)

    def test_extract_markdown_images_multiple(self):
        text = "Images: ![First](http://example.com/first.png) and ![Second](http://example.com/second.png)"
        images = extract_markdown_images(text)
        expected_images = [
            ("First", "http://example.com/first.png"),
            ("Second", "http://example.com/second.png")
        ]
        self.assertEqual(images, expected_images)

    def test_extract_markdown_images_none(self):
        text = "This text has no images."
        images = extract_markdown_images(text)
        expected_images = []
        self.assertEqual(images, expected_images)

    def test_extract_markdown_links_single(self):
        text = "Here is a link: [Example](http://example.com)"
        links = extract_markdown_links(text)
        expected_links = [("Example", "http://example.com")]
        self.assertEqual(links, expected_links)

    def test_extract_markdown_links_multiple(self):
        text = "Links: [First](http://example.com/first) and [Second](http://example.com/second)"
        links = extract_markdown_links(text)
        expected_links = [
            ("First", "http://example.com/first"),
            ("Second", "http://example.com/second")
        ]
        self.assertEqual(links, expected_links)

    def test_extract_markdown_links_none(self):
        text = "This text has no links."
        links = extract_markdown_links(text)
        expected_links = []
        self.assertEqual(links, expected_links)

if __name__ == '__main__':
    unittest.main()