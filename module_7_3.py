import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self): # подготовительный метод, который возвращает словарь
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()  #приводим к нижнему регистру
                    #избавляемся от пунктуации
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(punct, '')
                    words = content.split()  #разбиваем на слова
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []  #если файл не найден, добавляем пустой список
        return all_words

    def find(self, word): #ищет слово в каждом файле если не найдено то ноне
        word = word.lower()
        word_positions = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            try:
                position = words.index(word) + 1  #ищем позицию слова
                word_positions[file_name] = position
            except ValueError:
                word_positions[file_name] = None  #если слово не найдено

        return word_positions

    def count(self, word): #подсчет количества вхождений слова в тексте
        word = word.lower()
        word_count = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word)  #считаем количество вхождений слова
            word_count[file_name] = count

        return word_count


# Пример использования
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # Все слова
print(finder.find('text'))  # Найти слово 'text'
print(finder.count('text'))  # Подсчитать количество слова 'text'
