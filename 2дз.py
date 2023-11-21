class Person:
    def __init__(self,Fullname,Age,is_married):
        self.Fullname=Fullname
        self.Age=Age
        self.is_married=is_married
        pass
    def inroduce_myself(self):
        print(f'Полное имя:{self.Fullname}, Возраст:{self.Age} ,Женат(а):{self.is_married}')
class Teacher(Person):
    def __init__(self,Fullname,Age,is_married,experience,salary):
        Person.__init__(self,Fullname,Age,is_married)
        self.experience=experience
        self.salary=salary
    def salary_worth(self):
        self.salary+=3000*self.experience
    def info(self):
        print(F'Опыт:{self.experience},Зарплата:{self.salary}')
teacher=Person('Темиров Исламбек Арстанбекович',20,'No')
teacher.inroduce_myself()
experience=Teacher('Темиров Исламбек Арстанбекович',20,'No',2,20000)
experience.info()