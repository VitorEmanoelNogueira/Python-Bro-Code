class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"
        

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch, and the Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 255)

print(book3) # Antes só retornaria o endereço na memória, mas depois da implementação do método __str__ mostra o livro e o autor

print(book1 == book4) # Mesmo se todos os atributos fossem iguais, antes da implementação do __eq__ ainda daria falso.

print(book2 < book3) # Antes da implementação do __lt__ só dava erro

print(book2 > book3) # Antes da implementação do __gt__ também dava erro

print(book1 + book3) # Antes da implementação do __add__ também dava erro

print("C.S." in book3) # Erro por não ser iterável antes da implementação do __contains__

print(book3['author']) # Erro de book objet is not subscriptable antes da implementação do __getitem___