class GeeksPeople:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
        
        
    def __str__(self):
        return f'Имя:{self.name}. Почта:{self.email}. Телефон:{self.phone}.'
    
    
class Student(GeeksPeople):
    def __init__(self, name, email, phone,student_id,group_where_study):
        GeeksPeople.__init__(self,name, email, phone)
        self.student_id=student_id
        self.group_where_study=group_where_study
        
        
    def Study(self):
        print(f'ID:{self.student_id}, Группа:{self.group_where_study}')
        
        
class Teacher(GeeksPeople):
    def __init__(self, name, email, phone,teacher_id,group_where_teach):
        GeeksPeople.__init__(self,name, email, phone)
        self.teacher_id=teacher_id
        self.group_where_teach=group_where_teach
        
        
    def Teach(self):
        print(f'id:{self.teacher_id}, Преподает в:{self.group_where_teach}.')
        
        
class Admin(GeeksPeople):
    def __init__(self, name, email, phone,admin_id):
        GeeksPeople.__init__(self,name, email, phone)
        self.admin_id=admin_id
        
        
    def create_group(self):
        print(f'id Админа:{self.admin_id} создает группу.')
        
class Mentor(Student,Teacher):
    def __init__(self, name, email, phone, student_id, group_where_study,teacher_id,group_where_teach):
        Student.__init__(self,name, email, phone, student_id, group_where_study)
        Teacher.__init__(self,name, email, phone,teacher_id,group_where_teach)
        
        
    def __str__(self):
        return super().__str__()
    

People1=Student('Islam','student@gmail.com',707007041,1011,13_1)
print(People1)
People1.Study()


People2=Teacher('Сыймык Абдыкадыров','teacher@gmail.com',777777777,1101,13_2)
print(People2)
People2.Teach()


People3=Admin('Admin','admin@gmail.com',770567123,1111)
print(People3)
People3.create_group()


People4=Mentor('Kuti','kuti@gmail.com',755345789,1234,13_2,1245,11_1)
print(People4)
People4.Study()
People4.Teach()