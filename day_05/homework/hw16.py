#შეამოწმე, არის თუ არა მომხმარებლის შემოტანილი ორი რიცხვი ერთმანეთზე მეტი და 10-ის ჯერადი.


def matematika(to,to1):
    if to > to1 and to % 10 == 0:
        return "aris"
    elif to1 > to and to1 % 10 == 0:
        return "araris"
    else:
        return "araris"



number1 = int(input("enter your number:"))
number2 = int(input("enter your second number: "))


result = matematika(number1,number2)

print(result)