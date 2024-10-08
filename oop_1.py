#You must make a program that read a float-point number and print a message saying in which of following intervals the number belongs: [0,25] (25,50], (50,75], (75,100]. If the read number is less than zero or greather than 100, the program must print the message “Fora de intervalo” that means "Out of Interval".
#The symbol '(' represents greather than. For example:
#[0,25] indicates numbers between 0 and 25.0000, including both.
#(25,50] indicates numbers greather than 25 (25.00001) up to 50.0000000.


def check_interval(A):
    if 0 <= A <= 25:
        print("[0,25]")
    elif 25 < A <=50:
        print("(25,50]")
    elif 50 < A <= 75:
        print("(50,75")
    elif 75 < A <= 100:
        print("(75,100]")
    else:
        print("Fora de intervalo")


a = float(input())

check_interval(a)