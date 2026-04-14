#დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი ერთდროულად 50-ზე ნაკლები და 10-ის ჯერადი.

def matematika(to):
    if to < 50 and to % 10 == 0:
        return "aris"
    else:
        return "araris"


number = int(input("enter your number: "))

result = matematika(number)
print(result)