# Imports
from random import randrange
import matplotlib.pyplot as plt

# Sorting function
def gnomeSort(array):
    index = 0
    
    while index < len(array):
        if index == 0 or array[index - 1] <= array[index]:
            index += 1
        else:
            array[index], array[index - 1] = array[index - 1], array[index]
            index -= 1

# Display function
def show(array):
  for i in array:
    print(i, end=' ')
  
  print()

# Creating an Array with Random Numbers
nums = [randrange(200) for x in range(100)]

# Messy array
print ("Numbers:")
show(nums)

# Graphic
plt.title('Messy Numbers')
plt.grid(True)
plt.ylabel('Numbers')
plt.plot(nums)
plt.show()
plt.clf()

# Calling the sorting function
gnomeSort(nums)
print()

# Ordered array
print ("Sorted numbers:")
show(nums)

# Graphic
plt.title('Ordered Numbers')
plt.grid(True)
plt.ylabel('Numbers')
plt.plot(nums)
plt.show()