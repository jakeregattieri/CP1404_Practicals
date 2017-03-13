"""
Write a program to calculate the average age of a group of people, of unknown size
Use a negative number as the 'sentinel' (when to stop)
"""
total_age = []
age = int(input("enter age:"))
while age > 0:
    total_age.append(age)
    age = int(input("enter age:"))
total_age = sum(total_age) / len(total_age)
print(total_age)
