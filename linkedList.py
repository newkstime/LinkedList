class Node():
    """
    Simple class to hold the node of the linked list
    This is public for simplicity
    """
    
    def __init__(self, data):
        """
        Constructor:
        Set the data instance variable to the parameter
        Set the next instance variable to None
        """
        self.data = data
        self.next = None

    #def __str__(self):
    #    """
    #    Return the data instance variable as a string
    #    """
    #    return str(self.data)
        
class LinkedList:
    """
    This is an implementation of the Singly LinkedList ADT
    where both a head pointer and a tail pointer are used.  
    The number of Nodes in the list is kept and updated 
    as Nodes are added and removed. 
    Protected instance variables are used, 
    so that the child classes can get direct access.    
    """
    
    def __init__(self):
        """
        Constructor:
        Use protected instance variables
        Set the head instance variable to None
        Set the tail instance variable to None
        Set the linked list size to 0
        """
        
        self._head = None
        self._tail = None
        self._size = 0
    
    def get_size(self):
        """
        Return the linked list size
        """
        
        return self._size
        
    def is_empty(self):
        """
        Return True, if linked list is empty
        Return False, otherwise
        """
        
        if self._size == 0:
            return True
        else:
            return False

    def add_first(self, data):
        """
        Create a new Node with the given data
        Add the Node as the first element of the linked list
        Make sure both the head and tail pointers are updated properly
        Make sure you increment the size of the linked list
        """
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node
        if self.is_empty():
            self._tail = new_node
        self._size += 1

    def add_last(self, data):
        """
        Create a new Node with the given data
        Add the Node as the last element of the linked list
        Call add_first, if thre list is empty
        Make sure both the head and tail pointers are updated properly
        Make sure you increment the size of the linked list
        """

        if self.is_empty():
            self.add_first(data)
        else:
            new_node = Node(data)
            previous_node = self._tail
            self._tail = new_node
            previous_node.next = new_node
            self._size += 1
                
    def remove_first(self):
        """
        Remove the first Node of the linked list and return it
        Return None, if linked list is empty 
        Make sure both the head and tail pointers are updated properly
        Make sure you decrement the size of the linked list
        """
        
        if self.is_empty():
            return None
        else:
            this_node = self._head

            if this_node.next == None:
                self._head = None
                self._tail = None
            else:
                self._head = this_node.next
                this_node.next = None
            self._size -= 1
            return this_node.data


                
    def __str__(self):
        """
        Return the contents of the Linked List as a string
        with each Node's data on a separate line
        Remember to start each traversal of a Linked List 
        with the head pointer 
        """
        print_nodes = ""
        current_node = self._head
        for x in range(self._size):
            print_nodes += str(current_node.data) + "\n"
            current_node = current_node.next
        return print_nodes
