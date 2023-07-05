# Given two numbers m and n, such that 0 ≤ m ≤ n :

# convert all numbers from m to n (inclusive) to binary
# sum them as if they were in base 10
# convert the result to binary
# return as a string

def binary_pyramid(m, n):
    total = 0
    for i in range(m, n+1):
        total += int(bin(i)[2:])
        print(total)
    return str(bin(total)[2:])


print(binary_pyramid(1, 4))
