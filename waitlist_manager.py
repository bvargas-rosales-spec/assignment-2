# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None
   
# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None
    
    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        

    def add_end(self, name):
        new_node = Node(name)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        print(f"Added {name} to the end of the waitlist.")

    def remove(self, name):
            current = self.head
            previous = None
            while current is not None:
                if current.name == name:
                    if previous is None:
                        self.head = current.next
                    else:
                        previous.next = current.next
                    return f"Removed {name} from the waitlist."
                previous = current
                current = current.next
            return f"{name} not found in the waitlist."

    def print_list(self):
        if self.head is None: 
            print("Waitlist is empty.")
            return
        print("Current Waitlist:")
        current = self.head
        while current is not None:
            print(f" - {current.name}")
            current = current.next

def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()

    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)


        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            waitlist.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()

            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''
#The linked list does actually contain all data in one place, it holds pieces of data in Node objects. Each node contains a customer's name and a next pointer that is pointing to the next node in the list. The linked list is keeping track of the head which is the first node. The next pointers need to be followed in order to move on from the head to another node. The head is the start and follows the next pointer node until a node where next is none meaning that is the end of the list. This chain structure allows for add_fron, add_end, and remove to function. Add front is creating a new node and pointing to the next current head, and updating the head to point to the new node. When someone is added to the line in the waitlist not every node needs to move just a few updates. 
#The head is the starting point for the code. Without this then nothing will function as it should. Because nodes aren’t stored in one specific place it's only possible to reach any node at the head and continue to follow the next pointers. If the head wasn’t set correctly then the list would not be reached even if the rest of the list was set up entirely correctly.  
#A real engineer might need a custom list like this when things need to be added or removed from the front or middle. Rather than using an array list where you would be moving different elements over and taking longer to make changes, a linked list would allow for the engineer to save time and be more efficient. Instead of moving elements when adding or removing a node you would need to ensure you update next pointers. An engineer might have to use a custom list like this to build other kinds of data structures such as stacks, queues that would need to be fast when inserting or removing data. For a waitlist such as in the assignment customers can be added to the front of the line or be removed without interfering with the rest of the customers placement. 

