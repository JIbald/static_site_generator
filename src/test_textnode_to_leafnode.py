import unittest
from textnode_to_leafnode import text_node_to_html_node
from leafnode import LeafNode
from textnode import TextType, TextNode


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_conversion(self):
        node = TextNode("Hello, world!", TextType.TEXT)
        html = text_node_to_html_node(node)
        self.assertIsInstance(html, LeafNode)
        self.assertIsNone(html.tag)
        self.assertEqual(html.value, "Hello, world!")
        self.assertEqual(html.props, {})

    def test_bold_conversion(self):
        node = TextNode("Bold text", TextType.BOLD)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "b")
        self.assertEqual(html.value, "Bold text")

    def test_italic_conversion(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "i")
        self.assertEqual(html.value, "Italic text")

    def test_code_conversion(self):
        node = TextNode("print('hello')", TextType.CODE)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "code")
        self.assertEqual(html.value, "print('hello')")

    def test_link_conversion(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "a")
        self.assertEqual(html.value, "Click here")
        self.assertEqual(html.props["href"], "https://example.com")

    def test_image_conversion(self):
        node = TextNode("Alt text", TextType.IMAGE, "image.jpg")
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "img")
        self.assertEqual(html.value, "")
        self.assertEqual(html.props["src"], "image.jpg")
        self.assertEqual(html.props["alt"], "Alt text")

    def test_link_without_url_raises_error(self):
        node = TextNode("Click here", TextType.LINK)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_image_without_url_raises_error(self):
        node = TextNode("Alt text", TextType.IMAGE)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_invalid_input_type_raises_error(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node("not a TextNode")


"""
    def test_unknown_text_type_raises_error(self):
        node = TextNode("Test", TextType.GERALD)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)
"""


if __name__ == "__main__":
    unittest.main()
