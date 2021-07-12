class Node:
    def __init__(self, data= None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '==>'
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next: # if itr.next has some values it means I'm not at the end. I will keep iterating.
            itr = itr.next # if itr.next becomes NULL, it means I'm at the last element.
        itr.next = Node(data, None) # And I want to point that last element to the new Node

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data) # takes advantage of the 'insert_at_end' method

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index. Your index should not be smaller than 0 or equal and larger than the length of the Linked List")

        if index == 0 :
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1: # You have to stop at the element which is prior to the element that you are trying to remove
                itr.next = itr.next.next # for example, a list that has 4 items (index= 0,1,2,3)
                # and we want to remove index of 2 so the 'itr' will iterate until the 'count' = index - 1; then the value of index 3 will replace the value of index 2
                break # we will break out of the loop once we meet the condition which is 'count == index - 1'
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index. Your index should not be smaller than 0 or equal and larger than the length of the Linked List")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1: # we want to modify the next pointer of the previous element so we have to stop at the previous element 'index - 1'
                node = Node(data, itr.next) # assign a Node into a variable to connect to the next item in the list
                itr.next = node # link node variable into the itr.next which is after the 'index - 1' value of the loop
                break # then break the loop
            itr = itr.next # keeps iterating until the 'count == index -1'
            count += 1 # incrementing the value of 'count' in order to meet the if clause.

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['banana','mango','grapes', 'orange'])
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(8)
    ll.insert_at_end(79)
    ll.insert_at_end(68)
    ll.print()
    print("length before remove: ", ll.get_length())
    # ll.remove_at(20) - check this one to see an exception is raised when you input invalid value for index
    ll.remove_at(2) # we remove the value that has index = 2 which is 'banana'
    print("length after remove: ", ll.get_length())
    ll.print()
    ll.insert_at(3, 'strawberry')
    print("after adding 'strawberry' to the list")
    ll.print()