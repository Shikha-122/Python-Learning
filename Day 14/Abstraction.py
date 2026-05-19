#abc - Abstract Base Class
# Abstraction : Giving the access on functionality but hiding implementation

#Example:


from abc import ABC,abstractmethod
#Abstract Class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

#Concrete class (implemented abstract methods from abstract class)
class Car(Vehicle):
    def start(self):
        print('Car engine started')

    def stop(self):
        print('Car engine stopped')

# Usage
# v=Vehicle() -- cannot create object for the abstract class

c1=Car()
c1.start()
c1.stop()