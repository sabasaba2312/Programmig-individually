#დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი ლუწი ან 3-ის ჯერადი.


def matematika(to):
    if to % 2 == 0:
        return "ricxvi luwia"
    if to % 3 == 0:
        return "ricxvi 3-is jeradia"
    else:
        return "arcerti arari"


number = int(input("enter your number: "))

result = matematika(number)

print(result)