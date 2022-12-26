# Initialize the list
list = []

# Read in the value of n
n = int(input())

# Process n commands
for i in range(n):
  # Read in the command and the value (if applicable)
  command, *values = input().split()

  # Perform the appropriate action for each command
  if command == 'insert':
    # Convert the values to integers
    i, e = map(int, values)
    # Insert the element at the specified position
    list.insert(i, e)
  elif command == 'print':
    # Print the list
    print(list)
  elif command == 'remove':
    # Convert the value to an integer
    e = int(values[0])
    # Remove the first occurrence of the element
    list.remove(e)
  elif command == 'append':
    # Convert the value to an integer
    e = int(values[0])
    # Append the element to the end of the list
    list.append(e)
  elif command == 'sort':
    # Sort the list
    list.sort()
  elif command == 'pop':
    # Pop the last element from the list
    list.pop()
  elif command == 'reverse':
    # Reverse the list
    list.reverse()
