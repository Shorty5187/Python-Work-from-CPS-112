class Course:

    def __init__(self, crs_id, title, hours):
        self.crs_id = crs_id
        self.title = title
        self.hours = hours

    def __str__(self):
        return '{}:{}, {} hrs'.format(self.crs_id, self.title, self.hours)

class Schedule:

    def __init__(self, name):
        self.name = name
        self.courses = []

    def __str__(self):
        tmp = self.name
        for i in range(len(self.courses)):
            tmp += '\n{}: {}'.format(i+1, self.courses[i])
        tmp += '\nTotal hours: {}'.format(self.hours())

        return tmp

    def add_course(self, course):
        self.courses.append(course)

    def hours(self):
        total = 0
        for crs in self.courses:
            total += crs.hours
        return total

    def tuition(self):
        hours = self.hours()

        if hours < 12:
            return hours * 1263
        elif hours <= 17:
            return 15156
        elif hours <=20:
            return 15156 + (hours-17)* 892
        else:
            return 15156 + (hours-17)* 892 + (hours-20)*1263


crs1 = Course('2017-2U CPS112-01', 'OOP', 3)
crs2 = Course('2017-2U MAT133-01', 'Calc II', 5)

print(crs1)
print(crs2)
print()

sch = Schedule('J Denny Beaver')
print(sch)

# sch.courses.append(crs1)
# sch.courses.append(crs2)
sch.add_course(crs1)
sch.add_course(crs2)
sch.add_course( Course('2017-U2 SWK141-01', 'Und Soc Welfare', 3) )
sch.add_course( Course('2017-U2 ECN142-01' 'Prin Micro Econ', 3) )
print( sch )
print('Tuition: ${0:,.2f}'.format(sch.tuition()))
#print(sch.hours())
