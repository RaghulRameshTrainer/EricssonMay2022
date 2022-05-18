'''
Inheritance
Abstraction
Encapsulation
Polymorphism
'''

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

class Developer(Employee):
    def __init__(self,fn,ln,pay,tech):
        super().__init__(fn,ln,pay)
        self.tech=tech
    '''
    def get_domain(self,client_name):
        self.clinet_name=client_name
        if client_name.casefold() in ['ericcson','att','verizon']:
            return 'telecom domain'
        elif client_name.casefold() in ['goldman','amex','ceditsuisse','socitiegenerale','sc']:
            return 'banking domain'
        elif client_name.casefold() in ['tezla','ford','mazda','honda']:
            return 'manufacture domain'
        else:
            return 'retail domain'
    
    def get_domain(self,client_name,location):
        if client_name.casefold() in ['ericcson','att','verizon'] and location.casefold() == 'chennai':
            return 'telecom business domain'
        elif client_name.casefold() in ['ericcson','att','verizon'] and location.casefold() == 'gurgaon':
            return 'telecom technology domain'
        else:
            return 'telecom service domain'
    '''

    def get_domain(self,*info):
        self.client_name, self.location='',''
        if len(info)==2:
            self.client_name,self.location=info[0],info[1]
        else:
            self.client_name=info[0]

        if self.location != '':
            if self.client_name.casefold() in ['ericcson', 'att', 'verizon'] and self.location.casefold() == 'chennai':
                return 'telecom business domain'
            elif self.client_name.casefold() in ['ericcson', 'att', 'verizon'] and self.location.casefold() == 'gurgaon':
                return 'telecom technology domain'
            else:
                return 'telecom service domain'
        else:
            if self.client_name.casefold() in ['ericcson', 'att', 'verizon']:
                return 'telecom domain'
            elif self.client_name.casefold() in ['goldman', 'amex', 'ceditsuisse', 'socitiegenerale', 'sc']:
                return 'banking domain'
            elif self.client_name.casefold() in ['tezla', 'ford', 'mazda', 'honda']:
                return 'manufacture domain'
            else:
                return 'retail domain'

dev_1=Developer('Bala','Murugan',20000,'Spark')
dev_2=Developer('Ramya','Saravanan',30000,'Mainframe')

print(dev_1.get_domain('Ericcson','Chennai'))