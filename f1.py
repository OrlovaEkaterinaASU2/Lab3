import Class1
def test():
    pr1 = Class1.Lesson("Высокоинтеллектуальные платформы", 144, "Мартин Кютц", "7-8")
    pr3 = Class1.Lesson("Алгоритмические ЯП", 180, "Курушин", "9-10")
    pr2 = Class1.Titul("Пермский национальный исследовательский политехнический университет", "Электортехнический факультет", "2019/2020", "АСУ2-19-1м")
    pr4 = Class1.Students(1, "Фоминых", "Полина", "Юрьевна")
    pr5 = Class1.Students(2, "Орлова", "Екатерина", "Дмитриевна")
    Class1.Titul.__enter__(pr2)
    Class1.Students.__enter__(pr4)
    Class1.Students.__enter__(pr5)
    Class1.Lesson.__enter__(pr1)
    Class1.Lesson.__enter__(pr3)
    print("-------------------------")
    print(Class1.Journal.__str__(pr1))
    print(Class1.Journal.__str__(pr3),"\n")
    print(Class1.Journal.__repr__(pr4))
    print(Class1.Journal.__repr__(pr5),"\n")
if __name__ == '__main__':
    test()