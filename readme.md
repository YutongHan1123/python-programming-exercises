# Python Programming Exercises
Record how I get my hands free with python.
### DAY1

#### [DAY1-1](https://github.com/YutongHan1123/python-programming-exercises/blob/main/day1-1.py)
I need to write a program which will find numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). In this case, I used for loop to solve it and exported results in list. After solving it, I read the online solutions and one inspired me:

    print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")

I googled the explanation of print, and it says:

    print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

Parameter:
Name 	    Description 	                                                              Required /Optional
objects 	Object to the printed. * indicates that there may be more than one object 	Optional
sep 	    Objects are separated by sep. Default value: ' ' 	                          Optional
end 	    Specify what to print at the end. Default is line feed ('\n').              Optional
file 	    An object with write(string) method. Default: sys.stdout, which prints objects on the screen. 	Optional
flush 	The stream is forcibly flushed If flush is True. Default value: False 	Optional

| Name   | Description                                                                                   | Required /Optional |
| ------ |:---------------------------------------------------------------------------------------------:| ------------------:|
| objects| Object to the printed. * indicates that there may be more than one object                     | Optional           |
| sep    | Objects are separated by sep. Default value: ' '                                              | Optional           |
| end    | Specify what to print at the end. Default is line feed ('\n').                                | Optional           |
| file   | An object with write(string) method. Default: sys.stdout, which prints objects on the screen. | Optional           |
| flush  | The stream is forcibly flushed If flush is True. Default value: False                         | Optional           |
