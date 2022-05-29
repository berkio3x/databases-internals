
m = 3
class Node:
    """A node is an ordered list of keys"""
    def __init__(self, keys=None, order=3):
        self.keys = []
        self.children = []
        self.order = order
       
    def is_full(self):
        return len(self.keys) < self.order - 1

    def __repr__(self):
        return '@{ '+','.join([str(x) for x  in self.keys])+' }'


def search(root, v):
    print(f"print({root}, {v})")
    # using linear scan
    child_idx = 0
    while child_idx < len(root.keys):
        if root.keys[child_idx] < v:
            child_idx += 1
        elif v == root.keys[child_idx]:
            # print(f"Got -> {v}",root)
            return root
    child_node = root.children[child_idx]
    return search(child_node, v)


def split(node, v):
    print(f"split({node},{v})")
    node_keys = node.keys
    idx = 0
    while idx < len(node_keys) and node_keys[idx] < v:
        idx += 1

    c = Node()
    n1 = Node()
    n2 = Node()
    n1.keys = node_keys[:idx+1]
    n2.keys = node_keys[idx+1:]
    # c.keys = [v]
    c.children = [n1 , n2]
    
    return c
    # return [n1, n2return c]
    # insert seperator to parent <>
    

def insert(node, v, parent=None):
    print(f"insert({node} , {v}, {parent})")
    # insertion will happen at leaf node always.

    node_keys = node.keys

    if len(node_keys) == 0:
        node.keys[0] = v 
    else:
        idx = 0
        # find leaf node where insertion needs to be done.
        # 1 2 3 4 6 5
        while idx < len(node_keys) and node_keys[idx] < v:
            idx += 1

    if len(node_keys) < m-1 and len(node.children) == 0:
        node_keys[idx] = v

    # we want to insert only to leaf node.
    # if we find children , we need to 
    # look into it.
    if node.children:
        insert(node.children[idx], v, parent=node)
    else:
        # there is no space left to insert.
        # do splitting here.
        # find median seperator. 
        # add logic to find correct seperator

        seperator = node_keys[idx - 1]
        print(f"Node split required")
        N = split(node, seperator)

        N.keys = [v]
        print( seperator, N)
        print(f"new sub root after split -> {N}")
        print(f"{N.children}")
        insert(parent, v)
        parent.children = N.children

        # seperator = node_keys[idx - 1]
        # n1, n2 = split(node, seperator)
        # print(f"Node split required")
        # print( seperator, n1, n2)
        # insert(parent, seperator)



n = Node()
n.keys = [4]

n1 = Node()
n1.keys = [2]
n1.children = []
n1.is_leaf = True


n2 = Node()
n2.keys = [5,9]
n2.children= []
n2.is_leaf = True

n.children = [n1 , n2]


if __name__ == '__main__':
    # assert (search(n, 5) == n2)
    insert(n, 8)
