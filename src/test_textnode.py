import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("Samesies", TextType.CODE)
        node2 = TextNode("Samesies", TextType.CODE)
        self.assertEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("None url", TextType.LINK, None)
        node2 = TextNode("None url", TextType.LINK)
        self.assertEqual(node, node2)

    def test_diff_text_type(self):
        node = TextNode("smacking", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("smacking", TextType.TEXT, "https://www.boot.dev")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
