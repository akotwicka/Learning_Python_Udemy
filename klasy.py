import pickle
import glob

class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        kind_list = []
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if (kind == 'cake') or (text == ''):
            self.__text = text
        else:
            self.__text = ''
            print('Text can be set only for cake!')

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind: {}".format(self.kind))
        print("Taste: {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling: {}".format(self.filling))
        print("Gluten free - {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text: {}".format(self.__text))
        print('-' * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text

    Text = property(__get_text, __set_text, None)

    def save_to_file(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)
        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(catalog):
        return glob.glob(catalog+'/*bakery')


cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', False, 'Happy Birthday')
cake_02 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'], 'cream', False, '100 lat')
cake_03 = Cake('Super Sweet Meringue', 'meringue', 'very sweet', [], 'sugar', True, '')
cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, "It's a boy!")

cake_02.set_filling("vanilla cream")
cake_03.add_additives(['cocoa powder', 'coconut'])

print("Today in our offer:")

cake_01.Text = '18$$$'
cake_04.Text = 'Hello'

for cake in Cake.bakery_offer:
    cake.show_info()

for cake in Cake.bakery_offer:
    print("Is {} the object of Class Cake? - {}, {}".format(cake.name, isinstance(cake, Cake), type(cake) is Cake))

print(vars(cake_01))
print(dir(cake_01))

cake_01.save_to_file("c:/temp/cake_01.bakery")
cake_02.save_to_file('c:/temp/cake_02.bakery')

cake_05 = Cake.read_from_file('c:/temp/cake_01.bakery')
cake_05.show_info()

print(Cake.get_bakery_files('c:/temp'))