# Initialize a list
my_list = [10, 20, 30, 40]

# Access elements
print(my_list[0])  # Output: 10

# Append an element
my_list.append(50)

# Insert an element
my_list.insert(2, 25)  # [10, 20, 25, 30, 40, 50]

# Remove an element
my_list.remove(30)

# Slicing
print(my_list[1:4])  # Output: [20, 25, 40]
print("\n")
#--------------------------------------------------------------

### **Practice Problems**

# 1. Write a function to find the maximum and minimum values in a list.
def find_max_and_min(lst):
    if not lst: #Check if list is empty
        return None, None
    max_number = lst[0]
    min_number = lst[0]

    for num in lst:
        if num > max_number:
            max_number = num
        if num < min_number:
            min_number = num
    
    return max_number, min_number

my_list = [10, 20, 25, 40, 50]
max_val, min_val = find_max_and_min(my_list)
print("Maximum:", max_val)
print("Minimum:", min_val)
print("\n")

# 2. Implement a function to reverse a list.
# Function to reverse a list
def reverse_list(lst):
    return lst[::-1] #Using slice to reverse the list

# Reverse the list
reversed_list = reverse_list(my_list)
print("Reverse list:", reversed_list)

# Sorting the list and printing it
sorted_list = sorted(my_list)
print("Sorted list", sorted_list)
print("\n")

# 3. Create a function that checks if a list is a palindrome.

def is_palindrome(lst):
    return lst == lst[::-1] #Compare the list with its reverse

result = is_palindrome(my_list)
print("Is the lsit a palindrome", result)
print("\n")

# 4. Write a function to rotate a list k-times to the right.
# Function to rotate a list k times to the right

def rotate_list(lst, k):
    k = k % len(lst) # Handle cases where k is grater than the list length
    return lst[-k:] + lst[:-k] # Slice the list to rotate it

# Rotate the list 2 times to the right
rotated_list = rotate_list(my_list, 2)
print("List after rotating 2 times to the right:", rotated_list)

# Rotate the list 3 times to the right
rotated_list2 = rotate_list(my_list, 3)
print("List after rotating 3 times to the right:", rotated_list2)

print("\n")
#--------------------------------------------------------------

# Manages the player's inventory.
inventory = []

def add_item(item):
    inventory.append(item)

def remove_item(item):
    if item in inventory:
        inventory.remove(item)
    else:
        print(f"{item} not found in inventory!")

def view_inventory():
    print("Inventory:", inventory)

# Example usage
view_inventory()
add_item("Health Potion")
add_item("Sword")
add_item("Shield")
remove_item("Apple")
view_inventory()
remove_item("Sword")
view_inventory()
