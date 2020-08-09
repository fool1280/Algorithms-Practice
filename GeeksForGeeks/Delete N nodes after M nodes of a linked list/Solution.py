class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    dummy = Node(0)
    dummy.next = head
    while dummy:
        for count in range(i):
            if dummy.next:
                dummy = dummy.next
                print(dummy.data)
            else: 
                return head
        current = dummy
        for count in range(j):
            if current:
                current = current.next
        if current:
            dummy.next = current.next
        else:
            dummy.next = current
    return head
    pass

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

head = create_linked_list(arr)
print_linked_list(head)

head = skip_i_delete_j(head, 2, 2)
print_linked_list(head)

