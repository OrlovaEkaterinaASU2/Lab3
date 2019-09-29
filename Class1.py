'''class Group():
    def __init__(self, group_name, number, year):
        self.group_name = group_name
        self.number = number
        self.year = year
    #def __year(self):
       # return self.year
class Student (Group):
    def __init__(self, name, surname, middle_name, number_group):
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.number_group = number_group
    def __repr__(self):
        return 'Student({!r},{!r},{!r},{!r})'.format(self.surname,self.name,self.middle_name,self.year)
    def __str__(self):
        return "{} {} {}".format(self.surname,self.name,self.middle_name) '''


class Titul:
    def __init__(self, university, faculty, years, group):
        self.university = university
        self.faculty = faculty
        self.years = years
        self.group = group

    def __enter__(self):
        print("{!r}\n{!r}\n{!r}\n{!r})\n \n ".format(self.university, self.faculty, self.years, self.group))

class Students:
    def __init__(self, number, surname, name, middle_name):
        self.number = number
        self.surname = surname
        self.name = name
        self.middle_name = middle_name


class Lesson:
    def __init__(self, name_subject, time, teacher, pages):
        self.name_subject = name_subject
        self.time = time
        self.teacher = teacher
        self.pages = pages


class Journal(Lesson, Titul):
    def __init__(self, university, faculty, years, group, name_subject, time, teacher, pages, number, surname, name, middle_name):
        Titul.__init__(self, university, faculty, years, group)
        Lesson.__init__(self, name_subject, time, teacher, pages)
        Students.__init__(self, number, surname, name, middle_name)

    def __repr__(self):
        return "{} {} {} {}".format(self.number, self.surname, self.name, self.middle_name)

    def __str__(self):
        return "{} {} {} {}".format( self.name_subject, self.time, self.teacher, self.pages)

