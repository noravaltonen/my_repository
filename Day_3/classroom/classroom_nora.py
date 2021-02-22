class Person(object):
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def getFirstname(self):
        return self.firstname
    def getLastname(self):
        return self.lastname
    def __str__(self):
        return "First name is %s and last name is %s" % (self.firstname, self.lastname)

class Student(Person):
    def __init__(self, firstname,lastname,subject_area):
        Person.__init__(self, firstname,lastname)
        self.subject_area = subject_area
    def SubjectArea(self):
        return self.subject_area

    @property
    def printNameSubject(self):
        return print('%s %s, %s' % (self.firstname, self.lastname, self.subject_area))

class Teacher(Person):

    def __init__(self,firstname,lastname,course):
        Person.__init__(self,firstname,lastname)
        self.course = course

    def Course(self):
        return self.course

    @property
    def printNameCourse(self):
        return print('%s %s, %s' % (self.firstname, self.lastname, self.course))
