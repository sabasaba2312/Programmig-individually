# მომხმარებელს შეეკითხეთ სახელი, გვარი, ასაკი, საცხოვრებელი,ჰობი შემდეგ კი დაბეჭდეთ გრძელი წინადადება მაგ. შენი სახელია "სახელი და გვარი" შენი ასაკია "ასაკი" და ასე შემდეგ

name = input("enter your name: ").strip().capitalize()
surname = input("enter your surname: ").strip().capitalize()
age = int(input("enter your age: "))
live = input("enter your live: ").strip().capitalize()
hobby = input("enter your hobby: ").strip().capitalize()

print(f"hello your name and surname is {name} {surname}, your age is {age}, you live in {live}, and your hobby is {hobby}")