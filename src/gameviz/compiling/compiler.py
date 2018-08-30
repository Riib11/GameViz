def compile(graph):

    ids = {} # id => node
    levels = {} # level => [node]
    groups = {} # group => [node]

    def add_to_dictlist(d, k, v):
        if not k in d: d[k] = []
        d[k].append(v)

    def to_id(node, prevs):
        if len(prevs) == 0: return "1"
        return "".join([ p.arrow for p in prevs if p.arrow ] + ([node.arrow] if node.arrow else []))

    def get_id(node):
        for l, n in ids.items():
            if node == n: return l
        return "MISSING"
    
    def helper(x, prevs):
        # id
        id = to_id(x, prevs)
        ids[id] = x
        # level
        add_to_dictlist(levels, x.level, x)
        # group
        add_to_dictlist(groups, x.group, x) if x.group else None
        # recurse
        for y in x.children:
            helper(y, prevs+[x])

    helper(graph.root, [])
    # print(ids.keys())

    ##############################
    s = "digraph {\n"        

    for id, node in ids.items():
        s += "\n"
        # nodes
        s += f"\"{id}\" [label=\"{node.name}\"]\n"
        # edges
        for child in node.children:
            child_id = get_id(child)
            if child.arrow:
                s += f"\"{id}\" -> \"{child_id}\" [label=\"{child.arrow}\"]\n"

    # levels
    s += "\n// ranks\n"
    for lvl, ns in levels.items():
        lbs = list(map(get_id,ns))
        x = "\"" + "\"; \"".join(lbs) + "\";"
        s += "{rank=same; " + x + "}\n"
    
    # groups
    for g, ns in groups.items():
        s += f"\n// group {g}\n"
        for i in range(len(ns)-1):
            l1 = get_id(ns[i])
            l2 = get_id(ns[i+1])
            s += f"{l1} -> {l2} [style=\"dashed\", arrowhead=\"none\"]\n"

    s += "}"
    ##############################

    # print("="*20)
    # print(s)
    return s

