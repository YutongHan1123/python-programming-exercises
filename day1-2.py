# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
def factorial_num(num):
    a = 1
    for i in range(1, num+1):
        a = i*a
    return a


test_num = factorial_num(8)
print(test_num)

# Using Lambda Function
# Solution by:  harshraj22

# n = int(input())
# def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)


# print(shortFact(n))
