# This program will take the numbers 1-50 and evaluate them for the following criteria:

# Number divisible by three and five:         Output = FizzBuzz
# Number divisible by three but not five:     Output = Fizz
# Number divisible by five but not three:     Output = Buzz
# Number divisible by neither three or five:  Output = number

# Programmed by Gage Wooldridge on 5/13/16

# Declare counter variable and assign initial value
i = 0

# Implement loop to evaluate and increment counter variable
while (i < 50):

    # Increment count
    i += 1
	
	# Evaluate data and display output
    if i % 3 == 0 and i % 5 == 0:
        print "FizzBuzz"
    elif i % 3 == 0:
        print "Fizz"
    elif i % 5 == 0:
        print "Buzz"
    else:
        print str(i)