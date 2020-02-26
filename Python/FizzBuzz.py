import time

#defining variables
length_of_round = 00

#replace values divideable by +
fizz = 0  
buzz = 0
fizzbuzz = 0

# length_of_round = int(input("\nEnter length of round desired: "))
# print("\nNote: FizzBuzz = Fizz * Buzz")
# fizz = int(input("Enter divider to replace with 'Fizz': "))
# buzz = int(input("Enter divider to replace with 'Buzz': "))


length_of_round = 100
fizz = 3
buzz = 5
fizzbuzz = fizz * buzz

start = time.time()

def run_round(i):
    global fizz
    global buzz
    global fizzbuzz
    
    output = ""

    if (i % fizzbuzz) == 0:
        output = "FizzBuzz"
    elif (i % fizz ) == 0:
        output = "Fizz"
    elif (i % buzz ) == 0:
        output = "Buzz"
    else:
        output = str(i)

    return output


for i in range(length_of_round):
    print(run_round(i+1))


end = time.time()

print("\nHow long program ran(seconds):")
print(end - start)