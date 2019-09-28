import Class1
def test():
    gr1 = Class1.Group("ASU","2","19")
    st1 = Class1.Student("Орлова", "Екатерина", "Дмитриевна","2")
    st2 = Class1.Student("Фоминых", "Полина", "Юрьевна","2")
    st2.year = "19"
    st1.year = "19"
    list_students = {1: st1, 2: st2}
    for key in list_students.keys():
        print(list_students[key].__repr__())
if __name__ == '__main__':
    test()