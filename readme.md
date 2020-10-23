# Python Programming Exercises
Record how I get my hands free with python.
### Directory
[DAY-1](https://github.com/YutongHan1123/python-programming-exercises/blob/main/readme.md#day1)

### DAY1

#### [DAY1-1](https://github.com/YutongHan1123/python-programming-exercises/blob/main/day1-1.py)
I need to write a program which will find numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). In this case, I used for loop to solve it and exported results in list. After solving it, I read the online solutions and one inspired me:

    print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")

I googled the explanation of print, and it says:

    print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

Parameter:
| Name   | Description                                                                                   | Required /Optional |
| ------ |:---------------------------------------------------------------------------------------------:| ------------------:|
| objects| Object to the printed. * indicates that there may be more than one object                     | Optional           |
| sep    | Objects are separated by sep. Default value: ' '                                              | Optional           |
| end    | Specify what to print at the end. Default is line feed ('\n').                                | Optional           |
| file   | An object with write(string) method. Default: sys.stdout, which prints objects on the screen. | Optional           |
| flush  | The stream is forcibly flushed If flush is True. Default value: False                         | Optional           |

Here is an example.

    fp = open("file.txt","w")
    print("Append me to the file", file=fp)
    fp.close()


#### [DAY1-2](https://github.com/YutongHan1123/python-programming-exercises/blob/main/day1-2.py)
I need to write a program which can compute the factorial of a given numbers. I used for loop to solve it. And when I go through online solutions, the Lambda Function solution caught my attention. 

Using Lambda Function Solution by:  harshraj22

    n = int(input())
    def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
    
I like the way shorFact(x) ... shortFact(x-1), it like matryoshka doll, and very short, clean.

#### [DAY1-3](https://github.com/YutongHan1123/python-programming-exercises/blob/main/day1-3.py)
I need to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n. I still used for loop to solve it. And don't forget:
> when using for i in range(a, b+1), the result will be between a and b (both included).

And I learned two new solutions from website:
1. Solution by: yurbika. Corrected by: developer-47

    num = int(input("Number: "))
    print(dict(enumerate([i*i for i in range(1, num+1)], 1))) 

*Numerate* is a built-in function of Python. Its usefulness can not be summarized in a single line. Yet most of the newcomers and even some advanced programmers are unaware of it. It allows us to loop over something and have an automatic counter. Here is an example:

    my_list = ['apple', 'banana', 'grapes', 'pear']
    for counter, value in enumerate(my_list):
    print counter, value

# Output:
# 0 apple
# 1 banana
# 2 grapes
# 3 pear


2. Using dictionary comprehension

    n = int(input())
    ans={i : i*i for i in range(1,n+1)}
    print(ans)
