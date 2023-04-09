#Write a Python program to search a specific item in a given WSU linked list 
#Then return true if the item is found otherwise return false.

#Class Node wich will generate Node for Linked List 
class Node(object):
    # Singly linked node which make you to step forward and step backward
    # Thus you need to link of data 
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
#Class for 
class WSU_linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    #pre: Node object which has data
    #Method: add data in the linked List
    #Output: None
    def append_item(self, data):
        # Append an item
        new_node = Node(data,None,None)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count +=1
        #disconnect Link and setup new_item
        #check linked list if there are value that is looked by object   
    def iter(self):
        current = self.head
        while current:
            itemval = current.data
            current = current.next
            yield itemval
       
        
       
#print each elements
    def print_foward(self):
        for node in self.iter():
          print(node)
#search by end of linked list        
    def search_item(self, val):
        for node in self.iter():
            if val == node:
                return True
        return False
    
    def delete_item(self,data):
        if data == self.head:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next != None:
                if data == node.next.data:
                    tmp = node.next
                    node.next = node.next.next
                    del tmp
                    return
                else:
                    node = node.next
 



        
#set Program Language Linked List for set Node
items = WSU_linked_list() #Instance linked List of Node Object
items.append_item('PHP')  #input program language
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')
items.append_item('SQL')

print("Original list:")
items.print_foward()
print("\n")

if items.search_item('SQL'):
    print("True")
else:
    print("False")

if items.search_item('C+'):
    print("True")
else:
    print("False")

items.delete_item('Java')
items.print_foward()

