# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
def make_list(num1, num2):
    result = []
    for i in range(num1, num2):
        if i % 7 == 0 and i % 5 != 0:
            result.append(i)
    return result


my_list = make_list(2000, 3201)
print(my_list)


# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# # online answer using generators and list comprehension
# print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")
