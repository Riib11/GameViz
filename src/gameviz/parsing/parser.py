from gameviz.utils.split import split_with

class Graph:
    def __init__(self, root):
        self.root = root

    def tostring(self):
        return str(self.root)
    __str__ = tostring; __repr__ = tostring

class Node:
    def __init__(self, name, arrow, group, parent):
        self.name   = name
        self.arrow  = arrow
        self.group  = group
        self.parent = parent
        if parent: parent.children.append(self)

        self.children = []
        self.level = (parent.level if parent else 0) + 1

    def tostring(self):
        children = ", ".join(map(str,self.children))
        if self.parent:
            return f"{self.parent.name} -{self.arrow}-> {self.name}"
        else:
            return f"-{self.arrow}-> {self.name}"
    __str__ = tostring; __repr__ = tostring

seperators = ["->", "[","]", "(",")", "{","}"]

def parse(lines):
    parent = None

    for line in lines:
        line = split_with(line.strip(), seperators)
        group = line[line.index("(")+1].strip() if "(" in line else None

        # end of node
        if "}" == line[0]:
            parent = parent.parent if parent.parent else parent

        # at root
        elif "->" == line[0]:
            parent = Node(line[1].strip(), None, group, None)

        elif "->" in line:
            # end node
            if not "{" == line[-1]:
                Node(line[line.index("->")+1].strip(), line[0].strip(), group, parent)
            # inner node
            else:
                parent = Node(line[line.index("->")+1].strip(), line[0].strip(), group, parent)

    graph = Graph(parent)
    return graph
