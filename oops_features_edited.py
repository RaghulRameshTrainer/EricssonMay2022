'''
Inheritance
Abstraction
Encapsulation
Polymorphism
'''

class Employee():      #ClassName, Boolean(True , False, None) 20
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

class Company():   #15 10 are common name in both Employee and Company(9, 1 from Company)
    def __init__(self):
        self.name="ERICCSON"

    def fullname(self):
        return " {} {} FROM ERICCSON ".format(self.fname, self.lname)
    def company_name(self):
        return "ERICSSON"

class Developer(Employee,Company):
    def __init__(self,fn,ln,pay,tech):
        super().__init__(fn,ln,pay)
        self.tech=tech

    def appraisal(self):
        self.salary=self.salary+50000

    def fullname(self):
        #return super(Employee,self).fullname()
        return Company.fullname(self)

dev_1=Developer('Bala','Murugan',20000,'Spark')
dev_2=Developer('Ramya','Saravanan',30000,'Mainframe')
print(dev_1.fullname())

# print(dev_1.salary)
# dev_1.appraisal()
# print(dev_1.salary)
