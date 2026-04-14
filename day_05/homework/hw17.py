#დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი უარყოფითი ან  ლუწი.

def matematika(to):
    if to < 0 or to % 2 == 0:
        return "aris"
    else:
        return "araris"



number = int(input("enter your number: "))

result = matematika(number)
print(result)