import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def basic_leafnode(self):
        node = LeafNode("p", "some text.")
        assert node.to_html() == "<p>some text.</p>"

    def attr_leafnode(self):
        node = LeafNode("a", "link", {"href": "https://www.boot.dev"})
        assert node.to_html() == '<a href="https://www.boot.dev">link</a>'

    def no_tag_leafnode(self):
        node = LeafNode(None, "some text.")
        assert node.to_html() == "some text"

    def raise_valerror(self):
        try:
            LeafNode("p", None)
            assert False, "ValueError should be raised"
        except ValueError:
            pass

    def no_children_leafnode(self):
        node = LeafNode("p", "test")
        assert len(node.children) == 0

    def many_attr_leafnode(self):
        node = LeafNode(
            "img", "", {"src": "img.jpg", "alt": "nice img", "width": "100"}
        )
        assert (
            node.to_html() == '<img src="image.jpg" alt="nice img" width="100"></img>'
        )


if __name__ == "__main__":
    unittest.main()
