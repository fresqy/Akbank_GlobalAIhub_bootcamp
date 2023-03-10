import csv
import datetime

#Pizza class'ı tanımlayıp daha sonra oluşturacağımız pizzalarımız için özellik tanımlayacağız
class Pizza:
    def __init__(self):
        self._description = "Pizza"
        self._cost = 0

    def get_description(self):
        return self._description

    def get_cost(self):
        return self._cost


class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Klasik Pizza: Domates, mozzarella ve feslegen"
        self._cost = 10.0


class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Margherita Pizza: Domates, mozarella, feslegen, zeytinyagı ve tuz"
        self._cost = 12.0


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Türk Pizza: Domates, kiyma, sogan ve sarimsak"
        self._cost = 15.0


class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Sade Pizza"
        self._cost = 8.0

#Daha sonra yazacağımız ek malzemeler için decorator oluşturuyoruz.
class Decorator(Pizza):
    def __init__(self, component):
        super().__init__()
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Olive(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Zeytin"
        self._cost = 2.0


class Mushroom(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Mantar"
        self._cost = 1.5


class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Keci Peyniri"
        self._cost = 3.0


class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Sucuk"
        self._cost = 4.0


class Onion(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Sogan"
        self._cost = 1.0


class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Mısır"
        self._cost = 1.5

#Müşteri isteği doğrultusunda main fonksiyonu oluşturuyoruz.
def main():
    # menu.txt dosyasını okumak ve ekrana türkçe basmak için aşağıdaki kodu yazıyoruz.
    with open('menu.txt', 'r', encoding='utf=8') as file:
        # Okunan txt içeriğini değişken türüne çeviriyoruz.
        file_contents = file.read()
        # menu içeriğini basıyoruz.
    print(file_contents)

    # Pizza seçimini kullıcıdan alıyoruz.
    pizza_choice = int(input("Pizza seçiminiz: "))
    while pizza_choice not in [1, 2, 3, 4]:
        pizza_choice = int(input("lütfen geçerli bir sayı girin: "))
    pizza = None
    if pizza_choice == 1:
        pizza = ClassicPizza()
    elif pizza_choice == 2:
        pizza = MargheritaPizza()
    elif pizza_choice == 3:
        pizza = TurkPizza()
    elif pizza_choice == 4:
        pizza = SadePizza()

    # ek malzeme seçimini kullanıcıdan alıyoruz.
    sauce_choice = int(input("Ek malzeme seçin: "))
    while sauce_choice not in [11, 12, 13, 14, 15, 16]:
        sauce_choice = int(input("lütfen geçerli bir sayı girin: "))
    sauce = None
    if sauce_choice == 11:
        sauce = Olive(pizza)
    elif sauce_choice == 12:
        sauce = Mushroom(pizza)
    elif sauce_choice == 13:
        sauce = GoatCheese(pizza)
    elif sauce_choice == 14:
        sauce = Meat(pizza)
    elif sauce_choice == 15:
        sauce = Onion(pizza)
    elif sauce_choice == 16:
        sauce = Misir(pizza)

    # Toplam fiş tutarını hesaplıyoruz.
    cost = sauce.get_cost()
    print("Total cost: ", cost)

    # Müşteriden bilgilerini alıyoruz
    isim = input("İsminiz: ")
    tc_no = input("T.C kimlik numaranızı girin: ")
    kredi_kart_no = input("Kredi kartı Numaranızı Tuşlayın: ")
    kredi_kart_sifre = input("Kart şifrenizi girin: ")
    adres = input("Adres bilgilerini giriniz: ")
    order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    order_description = sauce.get_description()

    # CSV dosyası yoksa otomatik oluşturacak kodu yazıyoruz.
    with open("Orders_Database.csv", "a", encoding='utf-8', newline="") as f:
        fieldnames = ['isim', 'T.C no', 'Adres', 'Kredi Kart Numarasi', 'Siparis Detay', 'Fiyat', 'Siparis Zamani',
                      'Kredi Karti Sifre']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if f.tell() == 0:
            writer.writeheader()

        # Csv dosyasına aldığımız bilgileri yazıyoruz.
        writer.writerow({'isim': isim, 'T.C no': tc_no, 'Kredi Kart Numarasi': kredi_kart_no, 'Adres': adres,
                         'Siparis Detay': order_description, 'Fiyat': cost, 'Siparis Zamani': order_time,
                         'Kredi Karti Sifre': kredi_kart_sifre})

    print("Siparişiniz başarıyla alındı!Bizi tercih ettiğiniz için teşekkürler!!!")


if __name__ == '__main__':
    main()
