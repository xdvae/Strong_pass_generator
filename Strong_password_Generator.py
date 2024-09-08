# Strong Password Generator Made by: Vaibhav
# Enter the desired number of alphabets and numbers you'd like in your password and the program will generate a strong password for you.

import random
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [0,1,2,3,4,5,6,7,8,9] 

# Below is the import Var's required for this.
alp_size = len(alphabets)
num_size = len(numbers)
alp_needed = ""
num_needed = ""

# Ensure the user enters a number only.
while True:
    try:
        alp_needed = int(input("How many alphabets do you want: "))
        break
    except ValueError:
        print("Enter a number.")
        
while True:
    try:
        num_needed = int(input("How many numbers do you need: "))
        break
    except ValueError:
        print("Enter a number.")
        
pass_length = alp_needed + num_needed
password = []

alp_generated = 0
num_generated = 0

# Generating the pass:
while len(password) < pass_length:
    rand_num = random.randint(1,2)

    if rand_num == 1 and alp_generated < alp_needed:
        rand_num = random.randint(0 , alp_size - 1)
        word = alphabets[rand_num]

        if rand_num % 2 == 0:
            password.append(word.capitalize())
            alp_generated+=1
            
        else:
            password.append(word)
            alp_generated+=1

    
    elif rand_num != 1 and num_generated < num_needed:
        rand_num = random.randint(0 , num_size - 1)
        password.append(numbers[rand_num])
        num_generated+=1

# Joins the (password) list into a string.
pass_str = ''.join(map(str,password))
print(pass_str)