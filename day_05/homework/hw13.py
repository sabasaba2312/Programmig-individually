#მომხმარებელს შემოატანინეთ მისი ასაკი და შეამოწმეთ არის თუ არა სრულწლოვანი 

def asaki(to):
    if to >= 18:
        return "srulwlovania"
    else:
        return "arasrulwlovania"


age = int(input("enter your age: "))

result = asaki(age)

print(result)
