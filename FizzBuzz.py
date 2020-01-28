#import timeit 

#defining variables
length_of_round = 00

#replace values divideable by +
fizz = 0  
buzz = 0
fizzbuzz = 0

length_of_round = int(input("\nEnter length of round desired: "))
print("\nNote: FizzBuzz = Fizz * Buzz")
fizz = int(input("Enter divider to replace with 'Fizz': "))
buzz = int(input("Enter divider to replace with 'Buzz': "))
fizzbuzz = fizz * buzz

def run_round(i):
    global fizz
    global buzz
    global fizzbuzz

    if (i % fizzbuzz) == 0:
        print("FizzBuzz")
    elif (i % fizz ) == 0:
        print("Fizz")
    elif (i % buzz ) == 0:
        print("Buzz")
    else:
        print(i)

for i in range(length_of_round):
    run_round(i+1)