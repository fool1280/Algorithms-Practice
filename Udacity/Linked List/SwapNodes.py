def swap_nodes(head, left_index, right_index):
    count = 0
    one_current, one_previous = None, None
    two_current, two_previous = None, None
    dummy_previous = Node(0)
    dummy_current = head
    dummy_previous.next = dummy_current
    while not(one_current) or not(two_current):
        if count == left_index:
            one_current = dummy_current
            one_previous = dummy_previous 
        elif count == right_index:
            two_current= dummy_current
            two_previous = dummy_previous
        dummy_previous = dummy_current
        dummy_current = dummy_current.next
        count += 1
    
    one_previous.next = two_current
    temp = one_current.next
    one_current.next = two_current.next
    two_current.next = temp
    temp.next = one_current
    if left_index == 0:
        head = two_current
    return head
    pass

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
        print(head.data, end=" ")
        head = head.next
    print()
    
arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 0
right_index = 1

head = swap_nodes(head, left_index, right_index)
print_linked_list(head)