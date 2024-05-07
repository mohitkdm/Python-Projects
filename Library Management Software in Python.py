class Library:
    def __init__(self):
        self.noBooks=0
        self.Books=[]

    def addbook(self,book):
        self.Books.append(book)
        self.noBooks=len(self.Books)
        
    def showInfo(self):
        print(f"The library has {self.noBooks} books. \nThe Books are :")
        for book in self.Books:
            print(book)

l1=Library()
l1.addbook("6th Bal ram Katha")
l1.addbook("6th Basant")
l1.addbook("6th Sanskirt")
l1.addbook("6th A pact with the sun")
l1.addbook("6th HoneySuckle")
l1.showInfo()