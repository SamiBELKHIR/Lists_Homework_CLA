#LISTS
#Create a list that contains all the even numbers between 1 and 299.
#first method
even_numbers=[]
for i in range(300):
    if i%2==1:
        even_numbers.append(i)
print(even_numbers)
#second method
Even_numbers=[i for i in range(300) if i%2==1]
print(Even_numbers)
#Iterate through the previously created list 
#print first length of the list 
#then all the squared values of the list.
print(len(Even_numbers))
Squared_even_numbers=[i**2 for i in Even_numbers ]
print('the values are', Squared_even_numbers)
#In one line check if 57 is in the list using one line of python.
print(57 in Even_numbers)
#the previous line would return true if 57 is indeed in Even_numbers