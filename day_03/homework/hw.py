#მომხმარებელს input ის საშუალებით შემოატანინეთ სახელი შემდეგ კი პროგრამა მას მიესალმოს

fullname = input("enter your fullname: ").strip().capitalize()
name, surname = fullname.split()
print("hello" + " " + name)