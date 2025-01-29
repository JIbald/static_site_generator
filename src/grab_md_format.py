import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    results = []

    pattern = """
        \*{1}(?P<italic>[^*]+)\*{1}|
        \*{2}(?P<bold>[^*]+)\*{2}|
        \`(?P<code>[^`]+)\`|
        \(?P<plain>[^*`]+)
    """

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            results.append(old_node)
            continue
    pass
