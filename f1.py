import Class1
def test():
    pr1 = Class1.Lesson("Высокоинтеллектуальные платформы", 144, "Мартин Кютц", "7-8")
    pr3 = Class1.Lesson("Алгоритмические ЯП", 180, "Курушин", "9-10")
    pr2 = Class1.Titul("Пермский национальный исследовательский политехнический университет", "Электортехнический факультет", "2019/2020", "АСУ2-19-1м")
    pr4 = Class1.Students(1, "Фоминых", "Полина", "Юрьевна")
    pr5 = Class1.Students(2, "Орлова", "Екатерина", "Дмитриевна")
    print(Class1.Journal.__enter__(pr2))
    print(Class1.Journal.__str__(pr1))
    print(Class1.Journal.__str__(pr3))
    print(Class1.Journal.__repr__(pr4))
    print(Class1.Journal.__repr__(pr5))
if __name__ == '__main__':
    test()