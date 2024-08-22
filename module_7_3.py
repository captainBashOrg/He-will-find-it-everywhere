#from pprint import pprint
print( "Записать и запомнить")


class WordsFinder ():
    bad_chars = ['\\', '/' , ',' , '.', '=', '!', '?', ';', ':', ' - ']
# нецензурные слова :)

    all_words = {}  # Создаём пустой словарь

    def __init__(self,   *file_names ):         #  создаём экземпляр класса
        self.file_names = file_names

    def get_all_words (self ):
        for f in self.file_names:
            with open(f, encoding="utf-8") as file:
                key = f
                splitted_line = []
                for line in file:
                    line = ''.join((filter(lambda i: i not in self.bad_chars, line))) #Используя лямбда-функцию, функция filter может удалить все bad_chars и вернуть нужную уточненную строку.
                    line = line.lower()  # давим бит регистра

                    splitted_line += line.split()
                    self.all_words[key] = splitted_line

                file.close()
                #print(self.all_words)
        return self.all_words

    def find(self, word):
        poz  = {}
        full_words = self.get_all_words()

        for key, value in full_words.items():
            if word.lower() in value :
                poz[key] = value.index(word.lower()) + 1

        return poz

    def count(self, word):
        qtys = {}

        full_words = self.get_all_words()
        for key, value in full_words.items():
            #print(  value)
            words_count = value.count(word.lower())
            qtys[key] = words_count
        return qtys

#w1 = WordsFinder(  "file1.txt", "file2.txt") #, "file3.txt", "file4.txt" )

#w1.get_all_words()

#print(w1.find('Text'))

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
