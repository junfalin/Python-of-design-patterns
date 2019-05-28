# 组合模式
# 二叉树


class Node(object):
    def __init__(self, name: str):
        self.name = name
        self.parent = None
        self.children = []

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def add(self, node):
        self.children.append(node)

    def remove(self, node):
        self.children.remove(node)

    def get_children(self):
        return


class Tree(object):
    def __init__(self):
        self.root = Node('root')


if __name__ == '__main__':
    tree = Tree()
    leaf1 = Node('leaf1')
    leaf2 = Node('leaf2')

    leaf1.add(leaf2)
    tree.root.add(leaf1)
