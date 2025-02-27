class PC: # Создание класса компьютера (системного блока)

    def __init__(self, motherboard, cpu, psu): # Конструктор класса
        self.__motherboard = motherboard # Инициализация поля материнской платы
        self.__cpu = cpu # Инициализация поля процессора
        self.__psu = psu # Инициализация поля блока питания

    # Для материнской платы
    def set_motherboard(self, motherboard): # set
        self.__motherboard = motherboard # Присвоение нового значения поля
    
    def get_motherboard(self): # get
        return self.__motherboard # Возврат значения поля материнской платы
    
    # Для процессора
    def set_cpu(self, cpu): # set
        self.__cpu = cpu # Присвоение нового значения поля
    
    def get_cpu(self): # get
        return self.__cpu # Возврат значения поля процессора
    
    # Для блока питания
    def set_psu(self, psu): # set
        self.__psu = psu # Присвоение нового значения поля
    
    def get_psu(self): # get
        return self.__psu # Возврат значения поля блока питания

# Создание объектов

# Системный блок 1
pc1 = PC("ASUS Z790", "AMD Threadripper 9999X", "KCAS 1500W Bomb Edition")
# Системный блок 2
pc2 = PC("GIGABYTE B550", "Intel i5-10400F", "Thermaltake 600W")

# Вывод значений свойств объектов
for pc in [pc1, pc2]: # Перебор компьютеров
    # Вывод свойств
    print(f"Материнская плата: {pc.get_motherboard()}\n" +\
    f"Процессор: {pc.get_cpu()}\n" +\
    f"Блок питания: {pc.get_psu()}")