# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

simple_dict = {}


def make_dict(key):
    for i in range(1, key+1):
        simple_dict[i] = i * i
    return simple_dict


test_dict = make_dict(10)
print(test_dict)


# online solutions:

'''Solution by: yurbika
   Corrected by: developer-47
'''

# num = int(input("Number: "))
# print(dict(enumerate([i*i for i in range(1, num+1)], 1)))


# Using dictionary comprehension

# n = int(input())
# ans={i : i*i for i in range(1,n+1)}
# print(ans)
