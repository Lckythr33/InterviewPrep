#  Target Practice - Linked List
#
#  Using the LinkedList class from your homework, add the
#                following methods to your LinkedList.
#


# DO NOT EDIT
# Node class for a linked list node
from re import A


class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None


# DO NOT EDIT
# Generate a linked list from an array
def generate_list(lst):
    if len(lst) == 0:
        return None
    head = ListNode(lst[0])
    current = head
    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next
    return head


# 1a. Create a method which prints the value of each node until the tail
#
# Input: node {ListNode}
# Output: {None}
#
# Example: (1) --> (5) --> (7) --> (10)
#
#          1
#          5
#          7
#          10
#

# Time Complexity:
# Auxiliary Space Complexity:
def print_forward(node):
    cur=node
    while cur is not None:
        print(cur.value)
        cur=cur.next

# 1b. Prints the value of each node backwards from the tail to the input node
# using recursion.
#
# Input: node {ListNode}
# Output: {None}
#
# Example: (1) --> (5) --> (7) --> (10)
#
#          10
#          7
#          5
#          1
#

# Time Complexity:
# Auxiliary Space Complexity:
def print_backward(node):
    if node is None:
        return
    print_backward(node.next)       #populate the stack
    print(node.value)                #on the way back print

# 1c. Given a node in a linked list, reverse the order of the nodes in that
# list.
#
# Input: node {ListNode}
# Output: {ListNode}
#
# Example: (1) --> (5) --> (7) --> (10)
#
#          (10) --> (7) --> (5) --> (1)
#

# Time Complexity:
# Auxiliary Space Complexity:
def reverse(node):
    prev=None
    cur=node

    while cur is not None:
        temp=cur.next
        cur.next = prev
        prev = cur
        cur=temp
    
    return prev

# 1d. Create a method which swaps the first occurance of the locations of two
#     nodes in the linked list.
#
# Input: head {ListNode}
# Input: a {Integer}
# Input: b {Integer}
# Output: {ListNode}
#
# Example:
# head = generate_list([1, 5, 7, 10])
# head = swap(head, 5, 10)
#
#          (1) --> (5) --> (7) --> (10)
#          Head
#
#          (1) --> (10) --> (7) --> (5)
#          Head
#

# Time Complexity:
# Auxiliary Space Complexity:
def swap(head, int_a, int_b):
    place_holder = ListNode(None)
    place_holder.next = head

    #locate
    prev_a = None
    prev_b = None
    a = None
    b = None

    prev=place_holder
    cur = head
    
    while cur is not None:
        if cur.value == int_a and a == None:
            prev_a = prev
            a = cur

        if cur.value == int_b and b == None:
            prev_b = prev
            b = cur

        prev = prev.next
        cur = cur.next

    if a is None or b is None:
        return head

    #swap
    prev_a.next = b
    prev_b.next = a
    a.next, b.next = b.next , a.next

    return place_holder.next
#
# Extra Credit 1:
#
# Given a ListNode, returns true if the ListNode is in a circular linked list,
# and false if the ListNode is in a linked list that terminates.
#
def is_circular(node):
    slow = node
    fast = node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False



# ############################################################
# ###############  DO NOT TOUCH TEST BELOW!!!  ###############
# ############################################################


from io import StringIO
import sys
from random import randint


# custom assert function to handle tests
# input: count {List} - keeps track out how many tests pass and how many total
#        in the form of a two item array i.e., [0, 0]
# input: name {String} - describes the test
# input: test {Function} - performs a set of operations and returns a boolean
#        indicating if test passed
# output: {None}
def expect(count, name, test):
    if (count is None or not isinstance(count, list) or len(count) != 2):
        count = [0, 0]
    else:
        count[1] += 1

    result = 'false'
    error_msg = None
    try:
        if test():
            result = ' true'
            count[0] += 1
    except Exception as err:
        error_msg = str(err)

    print('  ' + (str(count[1]) + ')   ') + result + ' : ' + name)
    if error_msg is not None:
        print('       ' + error_msg + '\n')


# code for capturing print output
#
# directions: capture_print function returns a list of all elements that were
#             printed using print with the function that it is given. Note that
#             the function given to capture_print must be fed using lambda.
#             Example cis provided below
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


def capture_print(to_run):
    with Capturing() as output:
        pass
    with Capturing(output) as output:  # note the constructor argument
        to_run()
    return output


print('linked_list instantiation tests')
test_count = [0, 0]


def test():
    test = generate_list([1, 5, 7, 10])
    return test is not None and test.value == 1 and \
        test.next.next.next.value == 10


expect(test_count, 'should be able to create a linked_list instance', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('print_forward tests')
test_count = [0, 0]


def test():
    record = capture_print(lambda: print_forward(generate_list([1, 5, 7, 10])))
    return (len(record) == 4 and record[0] == '1' and record[1] == '5' and
            record[2] == '7' and record[3] == '10')


expect(test_count, 'should be able to print elements of [1, 5, 7, 10] ' +
       'linked list]', test)


def test():
    record = capture_print(lambda: print_forward(generate_list([1])))
    return len(record) == 1 and record[0] == '1'


expect(test_count, 'should be able to print forward with a single element',
       test)


def test():
    record = capture_print(lambda: print_forward(generate_list([])))
    return len(record) == 0


expect(test_count, 'should print nothing for empty linked list', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('print_backward tests')
test_count = [0, 0]


def test():
    record = capture_print(lambda:
                           print_backward(generate_list([1, 5, 7, 10])))
    return (len(record) == 4 and record[0] == '10' and record[1] == '7' and
            record[2] == '5' and record[3] == '1')


expect(test_count, 'should be able to print backwards the elements of ' +
       '[1, 5, 7, 10] linked list]', test)


def test():
    record = capture_print(lambda: print_backward(generate_list([1])))
    return len(record) == 1 and record[0] == '1'


expect(test_count, 'should be able to print backwards with a single element ' +
       'linked list]', test)


def test():
    record = capture_print(lambda: print_backward(generate_list([])))
    return len(record) == 0


expect(test_count, 'should print nothing for an empty linked list]', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('reverse tests')
test_count = [0, 0]


def test():
    test = generate_list([1, 5, 7, 10])
    test = reverse(test)
    return (test is not None and test.value == 10 and test.next.value == 7 and
            test.next.next.value == 5 and test.next.next.next.value == 1)


expect(test_count, 'should be able to reverse 1 --> 5 --> 7 --> 10 to be ' +
       '10 --> 7 --> 5 --> 1', test)


def test():
    test = ListNode(1)
    test = reverse(test)
    return test is not None and test.value == 1 and test.next is None


expect(test_count, 'should be able to handle single element linked lists',
       test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('swap tests')
test_count = [0, 0]


def test():
    test = generate_list([1, 5, 7, 10])
    test = swap(test, 1, 5)
    return (test is not None and test.value == 5 and test.next.value == 1 and
            test.next.next.value == 7 and test.next.next.next.value == 10)


expect(test_count, 'should be able to swap 1 and 5 to change [1, 5, 7, 10] ' +
       'linked list to look like [5, 1, 7, 10]', test)


def test():
    test = generate_list([1, 5, 7, 10])
    test = swap(test, 1, 7)
    return (test is not None and test.value == 7 and test.next.value == 5 and
            test.next.next.value == 1 and test.next.next.next.value == 10)


expect(test_count, 'should be able to swap 1 and 7 to change [1, 5, 7, 10] ' +
       'linked list to look like [7, 5, 1, 10]', test)


def test():
    test = generate_list([1, 5, 7, 10])
    test = swap(test, 1, 10)
    return (test is not None and test.value == 10 and test.next.value == 5 and +
            test.next.next.value == 7 and test.next.next.next.value == 1)


expect(test_count, 'should be able to swap 1 and 10 to change [1, 5, 7, 10] ' +
       'linked list to look like [10, 5, 7, 1]', test)


def test():
        test = generate_list([1, 5, 7, 10])
        swap(test, 5, 10)
        return (test is not None and test.value == 1 and test.next.value == 10
                and test.next.next.value == 7 and test.next.next.next.value == 5)


expect(test_count, 'should be able to swap 5 and 10 to change [1, 5, 7, 10] ' +
       'linked list to look like [1, 10, 7, 5]', test)


def test():
        test = generate_list([1, 5, 7, 10])
        swap(test, 5, 11)
        return (test.value == 1 and test.next.value == 5 and
                test.next.next.value == 7 and test.next.next.next.value == 10)


expect(test_count, 'should not perform any swap when trying to swap value ' +
       'that does not exist', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('is_circular tests')
test_count = [0, 0]


def test():
    # setup of node in a circular linked list
    circular_node = ListNode(randint(0, 10000))
    current_node = circular_node
    circle_size = randint(0, 10000-100) + 100

    for x in range(0, circle_size):
        current_node.next = ListNode(randint(0, 10000))
        current_node = current_node.next
        if x == (circle_size-1):
            # circular ListNode circular_node is ready for use
            current_node.next = circular_node

    results = is_circular(circular_node)
    return results is True


expect(test_count, 'should return true for circular linked list', test)


def test():
    # setup of a node in a linked list that terminates
    terminal_node = ListNode(randint(0, 10000))
    current_node = terminal_node
    circle_size = randint(0, 10000-100) + 100

    for x in range(0, circle_size):
        current_node.next = ListNode(randint(0, 10000))
        # terminating linked_list terminal_node is ready for use
        current_node = current_node.next

    results = is_circular(terminal_node)
    return results is False


expect(test_count, 'should return false for terminal linked list', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')