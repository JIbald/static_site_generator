from leafnode import LeafNode
from textnode import TextType, TextNode


def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError("Input must be a TextNode")
    if text_node.text_type == TextType.TEXT.value:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD.value:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC.value:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE.value:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK.value:
        if not text_node.url:
            raise ValueError("text_node_to_html(): Link TextNode must have a URL")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE.value:
        if not text_node.url:
            raise ValueError("text_node_to_html(): Image TextNode must have a URL")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(
            f"text_node_to_html(): Unknown TextType: {text_node.text_type}"
        )
