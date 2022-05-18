from abc import ABC , abstractmethod
class Car(ABC):
    @abstractmethod
    def breaks(self):
        pass
    @abstractmethod
    def seats(self):
        pass
    @abstractmethod
    def mirror(self):
        pass
    @abstractmethod
    def engine(self):
        pass
    def price(self,name):
        if name.casefold()=='ecosport':
            return 1600000
        elif name.casefold()=='aspire':
            return 1200000
        else:
            return 'Please check with the showroom'
class NewCar(Car):
    def __init__(self):
        self.make='FORD'
    def breaks(self):
        print('Breaks are applied')
    def engine(self):
        self.type='petrol'
    def mirror(self):
        self.status='fitted'
    def seats(self):
        print('5 seater car')

nc1=NewCar()
print("The price of the EcoSport car is : ",nc1.price('EcoSport'))
print("The price of the Aspire car is : ",nc1.price('ASPIRE'))
print("The price of the FIGO car is : ",nc1.price('FIGO'))