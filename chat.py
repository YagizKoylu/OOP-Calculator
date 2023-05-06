
class InputCollector:
    def __init__(self):
        self.numbers = []
        self.words = []
        self.sayi = []


    def collect_inputs(self):
        while True:
            user_input = input("Lütfen sayı veya kelime giriniz (Çıkmak için 'q' giriniz): ")
            
            if user_input == 'q':
                break
            try:
                number = float(user_input)
                self.numbers.append(number)
            except ValueError:
                self.words.append(user_input)
            
            
    def bilgilerigöster(self):
        print("""
              Numbers: {}
              Strings: {}
              """.format(self.numbers, self.words))
    def collect_indexs(self):
        while True:
            user_index = input("Lütfen istediğiniz indexi giriniz(Bittiğinde 'w' giriniz):")
            if user_index == 'w':
                break
            try:
                sayı = int(user_index)
                self.sayi.append(sayı)
            except IndexError:
                print("Index numarası girmediniz.")
    def indexbilgilerinigöster(self):
        print("""
              Girdiğim index numaraları: {}
              """.format(self.sayi))
    
class Calculator: 
    def __init__(self, input_collector):
        self.input_collector = input_collector
    def index_inputs(self):
        while True:
            index = input("İndex numarası giriniz:")
            
            if index == 'w':
                break
            try:
                indexnumber = int(index)
                self.num_list.append(indexnumber)
            except ValueError:
                self.gecersiz.append(index)

    def calculate(self):
        while True:
            result = 0
            numbers = self.input_collector.numbers
            operator = input("Lütfen bir işlem operatörü giriniz(+,-,*,/):")
            if operator == '+':
                for i in range(len(self.input_collector.sayi)): #[2,4]
                    result += numbers[self.input_collector.sayi[i]]
            elif operator == '-':
                result = 2*numbers[self.input_collector.sayi[0]]
                for i in range(len(self.input_collector.sayi)): #[2,4]
                    result -= numbers[self.input_collector.sayi[i]]
            elif operator == '*':
                result = 1
                for i in range(len(self.input_collector.sayi)): #[2,4]
                    result *= numbers[self.input_collector.sayi[i]]
            elif operator == '/':
                result = numbers[self.input_collector.sayi[0]]**2
                for i in range(len(self.input_collector.sayi)): #[2,4]
                    try:
                        result /= numbers[self.input_collector.sayi[i]]
                    except ZeroDivisionError:
                        result = 'Tanımsız'
                    except TypeError:
                        result = '0/0 belirsizdir.'
                
            else:

                raise ValueError("Geçersiz operatör.Programı tekrar çalıştırın.")

            print("Sonuç: ", result)
            
            next_calculation = input("Bir daha işlem yapmak istermisin?(Evetse herhangi bir tuş giriniz, Hayırsa 'H' giriniz.")
            if next_calculation == "H" or next_calculation == "h":
                break
                
        
        
        

input_collector = InputCollector()
input_collector.collect_inputs()
input_collector.bilgilerigöster()
input_collector.collect_indexs()
input_collector.indexbilgilerinigöster()

calculator = Calculator(input_collector)
calculator.calculate()
