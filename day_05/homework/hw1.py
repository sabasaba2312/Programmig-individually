#შექმენით ფაილი სახელად playback.py და დაწერეთ პროგრამა რომელიც მომხმარებელს ჰკითხავს რაიმე ტექსტის შეყვანას, პასუხად კი დაუბრუნებს ამ ტექსტის გადაკეთებულ ვერსიას სადაც ყოველი ცარიელი ადგილი ჩანაცვლებული იქნება ... სამი წერტილით.


def replaced(to):
    to = to.replace(" ","...")
    return to

user_text = input("enter your text: ")

shedegi = replaced(user_text)

print(shedegi)

