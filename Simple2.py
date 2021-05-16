book_list = [{'title': 'Война и мир', 'author': 'Толстой Л.Н.'},
             {'title': 'Идиот', 'author': 'Достоевский Ф.М.'},
             {'title': 'Капитанская дочка', 'author': 'Пушкин А.С.'}]

books = []
authors = []

for book in book_list:
    title = book['title']
    author = book['author']
    books.append(title)
    authors.append(author)


print(f'Список книг: {books}')
print(f'Список авторов: {authors}')