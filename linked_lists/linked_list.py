#taken for learning and testing purposes from https://stackabuse.com/python-linked-lists/
#thanks a lot to a creator of this website;D

from doctest import OutputChecker


class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"

        #store data
        self.data = data

        #store reference (next item)
        self.next = None
        return

    def has_value(self, value):
        "method to compare the value with the ndoe data"
        if self.data == value:
            return True
        else:
            return False


class SingleLinkedList:
    def __init__(self):
        "constructor to initiate this object"

        self.head = None
        self.tail = None
        return

    def add_list_item(self, item):
        "add an item at the head of the list"

        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        
        self.tail = item

        return
    
    def list_length(self):
        "returns the number of items in the list"

        count = 0
        current_node = self.head

        while current_node is not None:
            #increase counter by one
            count += 1

            #jump to the linked node
            current_node = current_node.next

        return count

    def output_list (self):
        "outputs the list (the value of the node, actually)"

        current_node = self.head

        while current_node is not None:

            print(current_node.data)

            #jump to the linked node
            current_node = current_node.next
        
        return

    def unordered_search(self, value):
        "search the linked list for the node that has this value"

        # define current_node
        current_node = self.head
        
        # define position
        node_id = 1
        
        # define list of results
        results = []
        
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
                
            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1
        
        return results

    def remove_list_item_by_id(self, item_id):
        "remove the list item with the item id"

        current_id = 1
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_id == item_id:
                #if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    #we don't have to look any further
                    return
            
            #needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_id += 1
    
    

#creating nodes
list1 = ListNode([1,2,4])
list2 = ListNode([1,3,4])

track = SingleLinkedList()
print("List: ")
for current_item in [list1, list2]:
    track.add_list_item(current_item)

track.merge_lists(list1, list2)

