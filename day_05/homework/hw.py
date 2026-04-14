#შექმენით ფაილი სახელად indoor.py და დაწერეთ პროგრამა რომელიც მომხმარებელს სთხოვს რაიმე ტექსტის შეყვანას, პასუხად კი დაუბრუნებს ამ ტექსტის lowercase(პატარა ასოებით შედგენილ) ვერსიას.


def lower_case(text):
    text = text.lower()
    return text

user_text = input("enter your text: ")

shedegi = lower_case(user_text)

print(shedegi)