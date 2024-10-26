from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        self.children = children
        self.tag = tag
        if props is not None:
            self.props = props
        else:
            self.props = {}

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode::to_html() object has no tag attribute")
        elif self.children is None:
            raise ValueError("ParentNode::to_html() object has no children attribute")
        else:
            children_html = ""
            for child in self.children:
                children_html.join(child.to_html())
            return f"<{self.tag}>{children_html}</{self.tag}>"
