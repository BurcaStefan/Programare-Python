class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} a fost verificat.")
        else:
            print(f"{self.title} este deja verificat.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} a fost returnat.")
        else:
            print(f"{self.title} este deja returnat.")

    def display_info(self):
        if self.checked_out:
            status = "Verificat" 
        else:
            status = "Valabil"
        print(f"Titlu: {self.title}, Status: {status}")


class Book(LibraryItem):
    def __init__(self, title, author, num_pages):
        super().__init__(title)
        self.author = author
        self.num_pages = num_pages

    def display_info(self):
        super().display_info()
        print(f"Autor: {self.author}, Pagini: {self.num_pages}")


class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        super().__init__(title)
        self.director = director
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Producator: {self.director}, Durata: {self.duration} minute")


class Magazine(LibraryItem):
    def __init__(self, title, issue_number):
        super().__init__(title)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Numarul aparitiilor: {self.issue_number}")



book = Book("Jurnalul unui pusti 1", "Jeff Kinney", 180)
dvd = DVD("Bal", "Popescu", 148)
magazine = Magazine("Junimea", 202)

book.display_info()
book.check_out()
book.return_item()

dvd.display_info()
dvd.check_out()
dvd.return_item()

magazine.display_info()
magazine.check_out()
magazine.return_item()
