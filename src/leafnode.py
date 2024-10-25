from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, attributes=None):
        if value is None:
            raise ValueError(
                "LeafNode::__init__ object of type LeafNode must have a value attribute."
            )
        super().__init__(tag, value, attributes, [])

    def to_html(self):
        if self.value is None:
            raise ValueError(
                "LeafNode::to_html() object of type LeafNode must have a value attribute."
            )
        if self.tag is None:
            return f"{self.value}"
        else:
            str_attr = ""
            if self.attributes:
                for key, value in self.attributes.items():
                    str_attr = " ".join(f'{key}="{value}"')

            return f"<{self.tag}{str_attr}>{self.value}</{self.tag}>"
