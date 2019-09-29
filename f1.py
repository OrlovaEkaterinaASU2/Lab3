import Class1
def test():
    pr1 = Class1.Lesson
    pr1.name_subject = "Высокоинтеллектуальные платформы"
    pr1.time = 144
    pr1.teacher = "Мартин Кютц"
    pr1.pages = "8-9"
    print(Class1.Journal.__str__(pr1))
if __name__ == '__main__':
    test()