import tkinter as tk
from tkinter import ttk
from henryDAO import HenryDAO


class HenrySBA:

    def __init__(self, frame, dao):

        self.frame = frame
        self.dao = dao
        self.authors = self.dao.getAuthorData()

        self.price, self.combo1, self.combo2, self.tree = tab_layout(self.frame, "Author Selection")

    def populate_tab(self):

        # grab ID number of 1st author in the list
        author1_id = self.authors[0].num
        books = self.dao.getAuthorBooks(author1_id)
        book1_price = books[0].price
        book1_id = books[0].book_code
        branches, copies_available = self.dao.getBookAvailability(book1_id)

        self.combo1['values'] = self.authors
        self.combo1.current(0)

        self.combo2['values'] = books
        self.combo2.current(0)

        self.price['text'] = f"Price:       $ {book1_price}"

        for i in range(len(branches)):
            self.tree.insert("", "end", values=[branches[i], copies_available[i]])

    def author_callback(self, event):

        author_index = event.widget.current()
        author_id = self.authors[author_index].num
        books = self.dao.getAuthorBooks(author_id)

        self.combo2['values'] = books
        self.combo2.current(0)

        for i in self.tree.get_children():
            self.tree.delete(i)

        book_index = self.combo2.current()
        book_id = books[book_index].book_code
        book_price = books[book_index].price

        self.price['text'] = f"Price:     $ {book_price}"
        branches, copies_available = self.dao.getBookAvailability(book_id)

        for i in range(len(branches)):
            self.tree.insert("", "end", values=[branches[i], copies_available[i]])

    def book_callback(self, event):

        author_index = self.combo1.current()
        author_id = self.authors[author_index].num
        books = self.dao.getAuthorBooks(author_id)

        book_index = event.widget.current()
        book_id = books[book_index].book_code
        book_price = books[book_index].price

        self.price['text'] = f"Price:     $ {book_price}"
        branches, copies_available = self.dao.getBookAvailability(book_id)

        for i in self.tree.get_children():
            self.tree.delete(i)

        for j in range(len(branches)):
            self.tree.insert("", "end", values=[branches[j], copies_available[j]])


class HenrySBC:

    def __init__(self, frame, dao):

        self.frame = frame
        self.dao = dao
        self.categories = self.dao.getCategories()
        self.price, self.combo1, self.combo2, self.tree = tab_layout(self.frame, "Category Selection")

    def populate_tab(self):

        first_category = self.categories[0]
        books = self.dao.getBooksbyCategory(first_category)
        book1_price = books[0].price
        book1_id = books[0].book_code
        branches, copies_available = self.dao.getBookAvailability(book1_id)

        self.combo1['values'] = self.categories
        self.combo1.current(0)

        self.combo2['values'] = books
        self.combo2.current(0)

        self.price['text'] = f"Price:       $ {book1_price}"

        for i in range(len(branches)):
            self.tree.insert("", "end", values=[branches[i], copies_available[i]])

    def category_callback(self, event):

        category_index = event.widget.current()
        category_selection = self.categories[category_index]
        books = self.dao.getBooksbyCategory(category_selection)

        self.combo2['values'] = books
        self.combo2.current(0)

        for i in self.tree.get_children():
            self.tree.delete(i)

        book_index = self.combo2.current()
        book_id = books[book_index].book_code
        book_price = books[book_index].price

        self.price['text'] = f"Price:     $ {book_price}"
        branches, copies_available = self.dao.getBookAvailability(book_id)

        for i in range(len(branches)):
            self.tree.insert("", "end", values=[branches[i], copies_available[i]])

    def book_callback(self, event):

        category_index = self.combo1.current()
        category_selection = self.categories[category_index]
        books = self.dao.getBooksbyCategory(category_selection)

        book_index = event.widget.current()

        book_id = books[book_index].book_code
        book_price = books[book_index].price

        self.price['text'] = f"Price:     $ {book_price}"
        branches, copies_available = self.dao.getBookAvailability(book_id)

        for i in self.tree.get_children():
            self.tree.delete(i)

        for j in range(len(branches)):
            self.tree.insert("", "end", values=[branches[j], copies_available[j]])


class HenrySBP:

    def __init__(self, frame, dao):

        self.frame = frame
        self.dao = dao
        self.pubs = self.dao.getPublishers()
        self.price, self.combo1, self.combo2, self.tree = tab_layout(self.frame, "Publisher Selection")

    def populate_tab(self):

        pub1_code = self.pubs[0].pub_code
        books = self.dao.getBooksbyPublisher(pub1_code)
        book1_price = books[0].price
        book1_id = books[0].book_code
        branches, copies_available = self.dao.getBookAvailability(book1_id)

        self.combo1['values'] = self.pubs
        self.combo1.current(0)

        self.combo2['values'] = books
        self.combo2.current(0)

        self.price['text'] = f"Price:       $ {book1_price}"

        for i in range(len(branches)):
            self.tree.insert("", "end", values=[branches[i], copies_available[i]])

    def pub_callback(self, event):

        pub_index = event.widget.current()
        pub_selection = self.pubs[pub_index].pub_code
        books = self.dao.getBooksbyPublisher(pub_selection)

        self.combo2['values'] = books
        self.combo2.current(0)

        for i in self.tree.get_children():
            self.tree.delete(i)

        book_index = self.combo2.current()
        book_id = books[book_index].book_code
        book_price = books[book_index].price

        self.price['text'] = f"Price:     $ {book_price}"
        branches, copies_available = self.dao.getBookAvailability(book_id)

        for i in range(len(branches)):
            self.tree.insert("", "end", values=[branches[i], copies_available[i]])

    def book_callback(self, event):

        pub_index = self.combo1.current()
        pub_selection = self.pubs[pub_index].pub_code
        books = self.dao.getBooksbyPublisher(pub_selection)

        book_index = event.widget.current()
        book_id = books[book_index].book_code
        book_price = books[book_index].price

        self.price['text'] = f"Price:     $ {book_price}"
        branches, copies_available = self.dao.getBookAvailability(book_id)

        for i in self.tree.get_children():
            self.tree.delete(i)

        for j in range(len(branches)):
            self.tree.insert("", "end", values=[branches[j], copies_available[j]])


def tab_layout(frame, search_parameter):

    category_label = ttk.Label(frame)
    category_label.grid(column=1, row=1)
    category_label['text'] = f"{search_parameter}"

    book_label = ttk.Label(frame)
    book_label.grid(column=3, row=1)
    book_label['text'] = "Book Selection:"

    price_label = ttk.Label(frame)
    price_label.grid(column=5, row=0)

    combo1 = ttk.Combobox(frame, width=20)
    combo1.grid(column=1, row=2)

    combo2 = ttk.Combobox(frame, width=30)
    combo2.grid(column=3, row=2)

    tree = ttk.Treeview(frame, columns=('Branch Name', 'Copies Available'), show='headings')
    tree.heading('Branch Name', text='Branch Name')
    tree.heading('Copies Available', text='Copies Available')
    tree.grid(column=1, row=0)

    return price_label, combo1, combo2, tree


def main():

    # instantiate data access object
    dao = HenryDAO()

    # set up GUI
    root = tk.Tk()
    root.title("Henry Bookstore")
    root.geometry('1000x500')
    tabControl = ttk.Notebook(root)
    tabControl.pack(expand=1, fill="both")

    # set up tab #1 ('Search By Author')
    sba_frame = ttk.Frame(tabControl)
    sba_tab = HenrySBA(sba_frame, dao)
    tabControl.add(sba_tab.frame, text='Search by Author')
    sba_tab.populate_tab()

    # event handler for tab #1
    sba_tab.combo1.bind("<<ComboboxSelected>>", sba_tab.author_callback)
    sba_tab.combo2.bind("<<ComboboxSelected>>", sba_tab.book_callback)

    # set up tab #2 ('Search By Category')
    sbc_frame = ttk.Frame(tabControl)
    sbc_tab = HenrySBC(sbc_frame, dao)
    tabControl.add(sbc_tab.frame, text='Search by Category')
    sbc_tab.populate_tab()

    # event handler for tab #2
    sbc_tab.combo1.bind("<<ComboboxSelected>>", sbc_tab.category_callback)
    sbc_tab.combo2.bind("<<ComboboxSelected>>", sbc_tab.book_callback)

    # set up tab number 3
    sbp_frame = ttk.Frame(tabControl)
    sbp_tab = HenrySBP(sbp_frame, dao)
    tabControl.add(sbp_frame, text='Search By Publisher')
    sbp_tab.populate_tab()

    # event handler for tab #3 ('Search By Publisher')
    sbp_tab.combo1.bind("<<ComboboxSelected>>", sbp_tab.pub_callback)
    sbp_tab.combo2.bind("<<ComboboxSelected>>", sbp_tab.book_callback)

    root.mainloop()

    dao.close()


if __name__ == '__main__':

    main()
