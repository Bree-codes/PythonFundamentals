import math

#Squareroot
print (math.sqrt(16))

#power
print(math.pow(21,5))

#factorial
print(math.factorial(10))

# Convert 45 degrees to radians
angle_in_radians = math.radians(45)

# Calculate sine of 45 degrees
sin_val = math.sin(angle_in_radians)
print(f"sin(45°): {sin_val}")

# Calculate cosine of 45 degrees
cos_val = math.cos(angle_in_radians)
print(f"cos(45°): {cos_val}")

# Calculate tangent of 45 degrees
tan_val = math.tan(angle_in_radians)
print(f"tan(45°): {tan_val}")

#log base 2
print(math.log(10,2))
print(math.log10(100))

#area of a circle
r = int(input("Enter the radius: "))
area = math.pi * pow(r,2)
print(area)
print(f"The area rounded down is: {math.floor(area)}")
print(f"The area rounded up is: {math.ceil(area)}")
print(f"The area rounded to three decimal places is: {round(area,3)}")

#finding min and max from given numbers
list1 = [10,3,6,88,1234,0.8,3455.99]
print(f"The maximum number from the list is: {max(list1)}")
print(f"The minimum number from the list is: {min(list1)}")
