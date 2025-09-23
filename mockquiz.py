def evod(n1): # defines a function called evod() which has one parameter
    if n1%2==0: # checks if the number is divisible by 2 using % operator
        return 'Even' # when function is called it returns a value of 'Even' if the number is divisible by 2 
    else:
        return 'Odd' # if number is not divisble by 2 functions returns a value 'Odd'

def posneg(n1): # defines a funciton called posneg() which has one parameter
    if n1==0: 
        return 'Number is Zero' # Checks if the number entered is 0 and returns a value 'Number is Zero' if it is
    elif n1>0:
        return 'Number is Positive' # Checks if the number entered is positive and returns a value 'Number is Positive' if it is
    elif n1<0:
        return 'Number is Negative' # Checks if the number entered is negative and returns a value 'Number is Negative' if it is

def sq(n1): # defines a function called sq() which has one parameter
    return n1*n1 # returns the square of the number

def cub(n1): # defines a fucntion called cub() which has one parameter
    return n1*n1*n1 # returns the cube of the number

def main(): # defines a function called main()
    n=int(input('Enter a number: ')) #  takes an integer n from the user
    print(evod(n))
    print(posneg(n))
    print('Square of the number is', sq(n))
    print('Cube of the number is', cub(n))
    # calls the 4 functions written above

main() # calling the function