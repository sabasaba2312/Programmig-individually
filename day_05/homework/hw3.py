#შექმენით ფაილი სახელად einstein.py
#პროგრამა რომელიც მომხმარებელს ჰკითხავს m მასას და დააბრუნებს შესაბამის რიცხვს ჯოულებში.**







def matematika():
    m_masa = int(input("enter your M masa: "))
    c = 300000000
    jouli = m_masa * c * c

    return jouli


result = matematika()
print(result)


