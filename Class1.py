class Group():
    def __init__(self, group_name, number, year):
        self.group_name = group_name
        self.number = number
        self.year = year
    def __year(self):
        return self.year
class Student (Group):
    def __init__(self, name, surname, middle_name, number_group):
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.number_group = number_group
    def __repr__(self):
        return 'Student({!r},{!r},{!r},{!r})'.format(self.surname,self.name,self.middle_name,self.year)
    def __str__(self):
        return "{} {} {}".format(self.surname,self.name,self.middle_name)