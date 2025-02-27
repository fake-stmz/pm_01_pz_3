import re # Импорт RegEx для проверки ограничений

class PC: # Создание класса компьютера (системного блока)

    def __init__(self, motherboard, cpu, psu): # Конструктор класса
        self.set_motherboard(motherboard) # Инициализация поля материнской платы
        self.set_cpu(cpu) # Инициализация поля процессора
        self.set_psu(psu) # Инициализация поля блока питания

    # Для материнской платы
    def set_motherboard(self, motherboard): # set
        if len(motherboard) < 20 or len(motherboard) > 150: # Проверка ограничения
            # Вывод ошибки
            print("[!] Название материнской платы должно быть не менее 20 символов и не более 150 символов")
            return # Досрочное завершение функции
        self.__motherboard = motherboard # Присвоение нового значения поля
    
    def get_motherboard(self): # get
        return self.__motherboard # Возврат значения поля материнской платы
    
    # Для процессора
    def set_cpu(self, cpu): # set
        if not re.fullmatch(r"[A-Za-z0-9 .;-]+", cpu): # Проверка ограничения
            # Вывод ошибки
            print("[!] Процессор должен содержать только буквы, цифры, тире, точки и/или точки с запятой")
            return # Досрочное завершение функции
        self.__cpu = cpu # Присвоение нового значения поля
    
    def get_cpu(self): # get
        return self.__cpu # Возврат значения поля процессора
    
    # Для блока питания
    def set_psu(self, psu): # set
        if not re.fullmatch(r".*\d{3,4}W.*", psu): # Проверка ограничения
            # Вывод ошибки
            print("[!] Блок питания должен содержать значение напряжение в формате \"<Число>W\"")
            return # Досрочное завершение функции
        self.__psu = psu # Присвоение нового значения поля
    
    def get_psu(self): # get
        return self.__psu # Возврат значения поля блока питания

# Создание объектов

# Системный блок 1
pc1 = PC("ASUSSSSSSSSSSSSSSSSSSS Z790", "AMD Threadripper 9999X", "KCAS 1500W Bomb Edition")
# Системный блок 2
pc2 = PC("GIGABYTEEEEEEEEEEEE B550", "Intel i5-10400F", "Thermaltake 600W")

# Вывод значений свойств объектов
for pc in [pc1, pc2]: # Перебор компьютеров
    # Вывод свойств
    print(f"Материнская плата: {pc.get_motherboard()}\n" +\
    f"Процессор: {pc.get_cpu()}\n" +\
    f"Блок питания: {pc.get_psu()}")

# Проверка работы ограничений
pc1.set_motherboard("0") # Материнская плата
pc1.set_cpu("##@##@##@#") # Процессор 
pc1.set_psu("No w no digits :(") # Блок питания

# Замена данными, подходящими под ограничения
pc2.set_motherboard("1" * 30) # Материнская плата
pc2.set_cpu("Qualcomm 850-1X") # Процессор 
pc2.set_psu("Omega 200W") # Блок питания
print(pc2.get_motherboard(), pc2.get_cpu(), pc2.get_psu()) # Вывод свойств