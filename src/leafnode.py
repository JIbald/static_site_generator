from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError(
                "LeafNode::__init__ object of type LeafNode must have a value attribute."
            )
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError(
                "LeafNode::to_html() object of type LeafNode must have a value attribute."
            )
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
