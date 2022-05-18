class Employee():      #ClassName, Boolean(True , False, None)
    hike=1.1
    def __init__(self,first_name, last_name, pay):   #constructor #self collect the object
        self.fname=first_name
        self.lname=last_name
        self.salary=pay
        self.email=self.fname+'.'+self.lname+'@ericcson.com'

    def fullname(self):
        return "{} {}".format(self.fname,self.lname)

    def appraisal(self):
        #self.hike=hike
        self.salary=int(self.salary*self.hike)

    @classmethod
    def create_object(cls,str):
        fn, ln, sal = str.split('-')
        return cls(fn,ln,int(sal))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "HOLIDAY"
        return "WORKING DAY"

    # def __str__(self):
    #     return "The object created for the Employee Class"

    def __add__(self,other):
        return self.salary+other.salary

    def __len__(self):
        return len(self.fullname())

    def __gt__(self,other):
        return self.salary > other.salary

str1='Raghul-Ramesh-100000'
str2='Malini-Sekar-200000'

emp_1=Employee.create_object(str1)
emp_2=Employee.create_object(str2)
# import datetime
# td=datetime.date(2022,5,22)
# print(Employee.is_workday(td))


print(emp_2 > emp_1)

# print(emp_1.salary)
# emp_1.appraisal()
# print(emp_1.salary)
#
# print(emp_2.salary)
# emp_2.appraisal()
# print(emp_2.salary)