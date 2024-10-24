import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_empty_node(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_node_with_value(self):
        node = HTMLNode(tag="p", value="snacking something")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "snacking something")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_node_with_props(self):
        props = {"href": "https://www.boot.dev", "target": "_blank"}
        node = HTMLNode(tag="a", value="Boot", props=props)
        self.assertEqual(
            node.props_to_html(), ' href="https://www.boot.dev" target="_blank"'
        )


if __name__ == "__main__":
    unittest.main()
