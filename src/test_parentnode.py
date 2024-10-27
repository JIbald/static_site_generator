import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_init(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "bold text"),
                LeafNode(None, "basic text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "basic text2"),
            ],
        )
        assert (
            node.to_html()
            == "<p><b>bold text</b>basic text<i>italic text</i>basic text2</p>"
        )

    def nested_parent(self):
        nested = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "bold text"),
                        LeafNode(None, " and "),
                        LeafNode("i", "italic text"),
                    ],
                ),
                LeafNode(None, " and "),
                LeafNode("span", "normal"),
            ],
        )
        assert (
            nested.to_html()
            == "<div><p><b>bold text</b> and <i>italic text</i></p> and <span>normal</span></div>"
        )


if __name__ == "__main__":
    unittest.main()
