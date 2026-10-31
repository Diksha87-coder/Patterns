#1.Function to find the sum of all elements in a list

def sum(lst):
    total = 0
    for i in lst:
        total +=i
    return total
numbers = [10,20,30,40,50]
print("sum=", sum(numbers))
    

#2.Function to find the largest and smallest elements

def largest_smallest(lst):
    largest=lst[0]
    smallest=lst[0]
    
    for i in lst:
        if i>largest:
            largest=i
        if i<smallest:
            smallest=i 
    print("largest=", largest)
    print("smallest=", smallest)
numbers=[12,5,25,8,2]
largest_smallest(numbers)

#3. Function to count even and odd numbers

def count_even_odd(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    print("even numbers =", even)
    print("odd numbers = ", odd)
numbers=[1,2,3,4,5,6]
count_even_odd(numbers)

#4. funcition to remove duplicate elements from the list

def remove_duplicates(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result
numbers = [1, 2, 2, 3, 4, 4, 5]
print("After remove dulicate values=", remove_duplicates(numbers))