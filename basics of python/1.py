'''program to add the even number from the list of nuumber'''

def even_adder(num_list):
    sum = 0
    for num in num_list:
        if num%2==0:
            sum += num
 
    return sum
    
num_list = [1, 2, 3, 4, 5, 5, 6, 7]

print(f"The total sum of even in the list is: {even_adder(num_list)}")