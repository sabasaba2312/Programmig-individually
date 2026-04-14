#მომხმარებლის შემოტანილი რიცხვი შეამოწმე, არის თუ არა  20-ის ჯერადი და დადებითი.


def matematika(to):
    if to > 0 and to % 20 == 0:
        return "aris"
    else:
        return "araris"
        


number = int(input("enter your number: "))

result = matematika(number)
print(result)