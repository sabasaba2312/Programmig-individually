#dollars_to_float - ფუნქციამ უნდა მიიღოს str ტიპის მნიშვნელობა როგორც არგუმენტი და ფორმატირებული ამ მაგალითის მიხედვით $##.## სადაც ყოველი # ნიშანი რიცხვს წარმოადგენს. უნდა წაუშალოს დოლარის ნიშანი $ და დააბრუნოს მნიშნველობა როგორც float რიცხვი. ასე მაგალითად - თუ გადავეცით $50.00, ფუნქციამ უნდა დააბრუნოს 50.0
#percent_to_float - ფუნქციამ უნდა მიიღოს str ტიპის მნიშვნელობა როგორც არგუმენტი და ფორმატირებული ამ მაგალითის მიხედვით ##% სადაც ყოველი # ნიშანი რიცხვს წარმოადგენს. უნდა წაუშალოს პროცენტის ნიშანი % და დააბრუნოს მნიშნველობა როგორც float რიცხვი. ასე მაგალითად - თუ გადავეცით 15%, ფუნქციამ უნდა პროცენტული მაჩვენებელის float ვერსია - ანუ 0.15.


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")




def dollars_to_float(to):
    number = to.replace("$", "")
    number = float(number)
    return number



def percent_to_float(saba):
    number1 = saba.replace("%", "")
    number1 = float(number1)
    return number1


main()







