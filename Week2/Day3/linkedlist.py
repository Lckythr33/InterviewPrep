from contextlib import nullcontext
# #recursive approach
# def print_forward(node):
#     if node is None:
#         return
#     print(node.data)
#     print_forward(node.next)

#iterative approach is better
def print_forward(node):
    cur=node
    while cur is not None:
        print(cur.data)
        cur=cur.next

def print_backward(node):
    if node is None:
        return
    print_backward(node.next)       #populate the stack
    print(node.data)                #on the way back print

def reverse_linkedlist(node):
    prev=None
    cur=node

    while cur is not None:
        temp=cur.next
        cur.next = prev
        prev = cur
        cur=temp
    
    return prev

def swap_nodes(head,int_a,int_b):
    place_holder = SinglyLinkedListNode(None)
    place_holder.next = head

    #locate
    prev_a = None
    prev_b = None
    a = None
    b = None

    prev=place_holder
    cur = head
    while cur is not None:
        if cur.data == int_a and a == None:
            prev_a = prev
            a = cur

        if cur.data == int_b and b == None:
            prev_b = prev
            b = cur

        prev=prev.next
        cur = cur.next

    if a is None or b is None:
        return head

    #swap
    prev_a.next = a
    prev_b.next = b

    ref_a = a.next
    ref_b = b.next
    
    a.next = ref_b
    b.next = ref_a


def is_circular(node):
    slow = node
    fast = node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False



