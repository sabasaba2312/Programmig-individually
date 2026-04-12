# split() - split() ფუნქცია პროგრამირებაში გამოიყენება ტექსტის (სტრინგის) დასაყოფად პატარა ნაწილებად. split() იღებს ერთ დიდ სტრინგს და ყოფს მას სიად (list).

fullname = input("enter your fullname: ").capitalize().strip()

name,surname = fullname.split()

print(f"hello {name}")


# int - int/integer არის მთელი რიცხვი 

# მათემატიკური ოპერაციებია  + მიმატება, - გამოკლება, * გამრავლება, // მთელი გაყოფა, / გაყოფა, ** ხარისხში აყვანა, % ნაშთის დაბრუნება. Python-ში მათემატიკური ოპერაციები ძალიან მნიშვნელოვანია, რადგან ისინი საშუალებას გვაძლევს მონაცემებზე სხვადასხვა გამოთვლები და ლოგიკა შევასრულოთ.

number1 = 10 # 10 არის მთელი რიცხვი ანუ int/integer
number2 = 5 # 5 არის მთელი რიცხვი ანუ int/integer

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 ** number2)
print(number1 / number2)
print(number1 // number2)
print(number1 % number2)