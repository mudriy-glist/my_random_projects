#taken for learning and testing purposes from https://stackabuse.com/python-linked-lists/
#thanks a lot to a creator of this website;D

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

#creating nodes
node1 = ListNode(15)
node2 = ListNode(8.5)
node3 = ListNode("Berlin")
node4 = ListNode(35)

track = SingleLinkedList()
print("track length: %i" % track.list_length())

for current_item in [node1, node2, node3, node4]:
    track.add_list_item(current_item)
    print("track length: %i" % track.list_length())
    track.output_list()