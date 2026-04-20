def get_books (filename: str) -> list:
    '''Задание 1Необходимо реализовать функцию, которая выбирает данные из указанного файла и возвращает список списков'''
    def prs_ln (line: str) -> list:
        words = line.strip().split('|')
        return [words[0], words[1],words[2], int (words[3]), float (words[4])]
    with open (filename, 'r', encoding='utf-8') as file:
        next (file)
        return list(map(prs_ln, file))

result = get_books('books.csv')
print ('Задание 1')
print(result[1]) # В квадратные скобочки можем написать номер книги, который хотим узнать

def filtered_books (books: list, book_search: str) -> list:
    '''Задание 2Необходимо реализовать функцию, которая получает список созданный в предыдущем задании,
выбирает книги с указанным параметром в названии и возвращает список списков'''
    book_search = book_search.lower()
    def match (book: list) -> list:
        return book_search in book[1].lower()

    def filter (book: list) -> list:
        return [book [0], ','.join ((book [1], book[2])),book[3], book [4]]
    return list(map(filter, books))

print ('Задание 2')
books = get_books('books.csv')
res = filtered_books(books,'python') # Указываем любое название книги, исходя из списка
print (res)

def get_book_sum(books: list) -> list:
    '''Напишите функцию, которая должна принять в качестве параметра список
    (результат функции из предыдущего задания) и вернуть список кортежей'''
    return list(map(lambda b: (b[0], b[2] * b[3]), books))

final_sum = get_book_sum(res)
print ('Задание 3')
print(final_sum) # Здесь так же можно указать конкретно интересующую книгу из исходного списка