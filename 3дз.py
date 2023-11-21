class Computer:
    def __init__(self,cpu,memory):
        self.__cpu=cpu
        self.__memory=memory
    @property
    def cpu(self):
        return self.__cpu
    
    @property
    def memory(self):
        return self.__memory
    def math(self):
        print(f'Сложение:{self.__cpu + self.__memory }')
        print(f'Вычитание:{self.__cpu - self.__memory }')
        print(f'Умножение:{self.__cpu * self.__memory }')
        print(f'Деление:{self.__cpu / self.__memory }')
class Laptor(Computer):
    def __init__(self,cpu,memory,memory_card):
        Computer.__init__(self,cpu,memory)
        self.__memory_card=memory_card
    @property
    def memory_card(self):
        return self.__memory_card
    def info(self):
        print(f'Центральный процессор:{self.cpu},Память:{self.memory}, Карта памяти:{self.memory_card}')
a=Computer(10,10)
a.math()
b=Laptor(10,500,16)
b.info()