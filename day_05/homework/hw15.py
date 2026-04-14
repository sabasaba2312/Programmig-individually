#შემოატანინეთ მომხმარებელს რიცხვი და შეამოწმეთ , არის თუ არა რიცხვი 1-ის ან 0-ის ტოლი.


def matematika(to):
    if to == 1:
        return "1 is tolia"
    elif to == 0:
        return "0 is tolia"
    else:
        return "arcertis toli ar aris"



number= int(input("enter your number: "))

result = matematika(number)

print(result)