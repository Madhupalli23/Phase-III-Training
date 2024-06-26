class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
def copyRandomList(head):
        if head == None:
            return None 

        currNode = head 
        while currNode:
            currDeepCopy = Node(currNode.val)
            currDeepCopy.next = currNode.next 
            currNode.next = currDeepCopy 
            currNode = currNode.next.next 

        currNode = head 
        while currNode:
            currDeepCopy = currNode.next 
            if currNode.random:
                currDeepCopy.random = currNode.random.next 

            currNode = currNode.next.next
        
        currNode = head 
        dummyNode = Node(-1)
        tail = dummyNode
        while currNode:
            currDeepCopy = currNode.next 
            tail.next = currDeepCopy 
            tail = tail.next 
            currNode.next = currDeepCopy.next 
            currNode = currNode.next 
        return dummyNode.next
head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
print(copyRandomList(head))