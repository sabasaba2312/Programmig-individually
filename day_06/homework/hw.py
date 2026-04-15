#შექმენით კალკულატორი, მომხმარებელს შეეკითხეთ ორი რიცხვი, შემდეგ შეეკითხეთ რა მოქმედების შესრულება სურს ამ ორ რიცხვზე და მისი პასუხიდან გამომდინარე შეასრულეთ მოქმედება და დაბეჭდეთ მაგალითად თუ მომხმარებელი შემოიტანს რიცხვებს 5 და 7 , და შემოიტანს მოქმედებას მაგალითად დამატებას თქვენ უნდა დაუბეჭდოთ 5 + 7 = 12

number1 = int(input("sheiyvane sheni pirveli ricxvi: "))
number2 = int(input("sheiyvane sheni moere ricxvi: "))


choose = input("sheiyvane sheni matematikuri operatori: (+) , (-) , (//) , (*) : ")

if choose != "+" and "-" and "//" and "*":
    print("shen sheiyvane araswori operatori")

if choose == "+":
    print(number1 + number2)

if choose == "-":
    print(number1 - number2)

if choose == "//":
    print(number1 // number2)

if choose == "*":
    print(number1 * number2)


