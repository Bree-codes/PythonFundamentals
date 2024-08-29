import random

#returns random float between 0.0 and 1.0
print(random.random())

#random int between a and b
print(random.randint(10,20))

#random choice from a sequence
list1 = [12,99,23,567,8999,1010]
list2 = [10,20,30,40,50,60]
print(random.choice(list1))

#shuffling the list
random.shuffle(list1)
print(f"The shuffled list is: {list1}")


