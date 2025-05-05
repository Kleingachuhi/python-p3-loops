#!/usr/bin/env python3

def happy_new_year():
     for i in range(1, 11):
         print(i)
         i -=1
         print("Happy New Year!")
     pass


def square_integers(int_list=[1, 2, 3, 4, 5] ):
   int_list =[integer ** 2 for integer in int_list]
   return(int_list)
   pass
def fizzbuzz():
    i = 1
    for i in range(1, 101):
        if i %15 ==0 :
            print("FizzBuzz")
        elif i %5 ==0 :
            print("Buzz")
        elif i % 3 ==0:
            print("Fizz") 
        else:
            print(i)
    pass
