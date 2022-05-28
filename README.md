# database-internals

### storage

#### Day 1 (Btree search)

```python
class Node:
    def __init__(self, keys=None, order=3):
        self.keys = []
        self.children = []
        self.order = order
       
    def is_full(self):
        return len(self.keys) < self.order - 1

    def __repr__(self):
        return '@{ '+','.join([str(x) for x  in self.keys])+' }' # <- to debug


def search(root, v):
    # use linear scan to find key in node is ok for now.
    
    child_idx = 0
    while child_idx < len(root.keys):
        if root.keys[child_idx] < v:
            child_idx += 1
        elif v == root.keys[child_idx]:
            return root
    child_node = root.children[child_idx]
    return search(child_node, v)
    
if __name__ == '__main__':

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


    assert (search(n, 5) == n2)
```
