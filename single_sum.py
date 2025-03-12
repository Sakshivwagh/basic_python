"""
Write a program that repeatedly adds the digits of a number until the sum is a single digit.

Algorithm
-----------------------
1. Start
2. Accept a number
3. if the number has only one digit then return the number
4. Extract the digits and calaculate the sume of these digits
5. Verify if the sum of digits is a single digit number
6. If yes print the sum
7. If no repeat step 4
8. Stop

Example
  Input: 9875
  Step 1: 9 + 8 + 7 + 5 = 29
  Step 2: 2 + 9 = 11
  Step 3: 1 + 1 = 2
  Output: 2

"""
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Implementation in Python

def digital_root(n):
    while n > 9:
        temp = 0
        while n > 0:
            temp += n % 10
            n //= 10
        n = temp
    return n

num = int(input("Enter a number: "))
print("Single digit sum:", digital_root(num))

Output-
Enter a number: 987
Single digit sum: 6
