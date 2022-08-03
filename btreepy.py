
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
    print(f"split(node to be split={node},value to be inserted={v})")

    keys = []

    for i in node.keys:
        if i < v:
            keys.append(i)
    
    keys.append(v)

    for k in node.keys:
        if k > v:
            keys.append(k)

    seperator_idx = len(keys)//2 
    # for idx, i  in enumerate(keys):
    #     if i < v:

    print(keys, seperator_idx,"+++")


    c = Node()
    n1 = Node()
    n2 = Node()
    n1.keys = keys[:seperator_idx]
    n2.keys = keys[seperator_idx+1:]
    c.children = [n1 , n2]
    
    return {
        'new_root':c, 
        'seperator_key':keys[seperator_idx]
    }
    # return [n1, n2return c]
    # insert seperator to parent <>

def print_tree(root):
    print(root)
    if root.children:
        cc = ""
        for  index,c in enumerate(root.children):
            cc +=  str(c)
        print(cc)

def insert(node, v, parent=None, after_split=False):
    """
    Accept the node to which we want to insert, 
    We keep track of parent in recursive calls in
    order to track back, 
    `after_split` parameter indicates if this is a 
    insert request after a node split has occured.
    """
    print(f"insert(root={node} , {v}, parent={parent})")
    # insertion will happen at leaf node always.


    node_keys = node.keys

    # if insert request has bubbled up to root , 
    # root node gets split up.

    if parent == None and after_split and len(node_keys) == m-1:
        '''
        If the splitting goes all the way up to the root,
        it creates a new root with a single separator 
        value and two children,
        '''
        pass
        print(f'[-] splitting root node')
        splitted_root = split(node, v)
        print(f'[+] splitted root={splitted_root}')
        N = splitted_root['new_root']
        seperator_key= splitted_root['seperator_key']

        nn = Node()
        root = nn

        # del parent.children[idx]
        nn.children.extend(N.children)

        # seperator_key = keys[seperator]
        N.keys = [seperator_key]
        print( f"[+] seperator ={seperator_key}")
        print(f"[+] children of subroot {N}={N.children}")
        print(f"[+] new sub root after split -> {N}")
        return


    if len(node_keys) < m-1 and after_split:
        node.keys.append(v)
        return
    else:
        idx = 0
        # find leaf node where insertion needs to be done.
        while idx < len(node_keys) and node_keys[idx] < v:
            idx += 1

    if len(node_keys) < m-1 and len(node.children) == 0:
        print(node_keys, idx,"-->")
        node_keys.append(v)
        return

    # we want to insert only to leaf node.
    # if we find children , we need to 
    # look into it.
    if node.children:
        print(f"Look into children")
        print(f"children of={node} childidx={idx} children={node.children}")
        insert(node.children[idx], v, parent=node)
    else:
        # there is no space left to insert.
        # do splitting here.
        # find median seperator.
    

        # To find the proper seperator & process further
        # we need to create actual node in sorted order & 
        # then perform split
        
        print(f'new keys before split={node}')
        # node.keys = keys

        # seperator = node_keys[idx - 1]

        print(node)
        print(f"[+] Node split required")
        # node.keys.append(v)
        splitted_node = split(node, v)
        print(f'[+] splitted_node={splitted_node}')
        N = splitted_node['new_root']
        seperator_key= splitted_node['seperator_key']

        del parent.children[idx]
        parent.children.extend(N.children)

        # seperator_key = keys[seperator]
        N.keys = [seperator_key]
        print( f"[+] seperator ={seperator_key}")
        print(f"[+] children of subroot {N}={N.children}")
        print(f"[+] new sub root after split -> {N}")
        insert(parent, seperator_key, after_split=True)

       
        print(f"[+] new children={parent.children}")
        
        


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
root = n

if __name__ == '__main__':
    # assert (search(n, 5) == n2)
    for i in range(10000):
        insert(n,i)
    print(10)
    # print_tree(root)
    # insert(n, 8)
    # print_tree(n)
    # print("\n#########\n")
    # insert(n, 10)
    # print("\n#-----##\n")
    # print_tree(n)
    # nn = insert(n, 11)
    # print_tree(n)

    # print(nn,"==>")


    # search(n, 11)

