import tkinter as tk
from tkinter import *
from tinydb import TinyDB, Query

# Creates and names a tkinter window
r = tk.Tk()
r.title('Address Book')

# creates and names main frame
main_frame = Frame(r, width=500, height=100)
main_frame.pack()

# Initializes database as the address book database (filename: adb_db.json)
database = TinyDB('adb_db.json')


# This function creates the drop-down menu with buttons
def create_menu():
    # Initialize menu
    menu = Menu(r)
    r.config(menu=menu)
    file_menu = Menu(menu)
    # Creates label for whole menu
    menu.add_cascade(label='Add/Search', menu=file_menu)
    # Creates add/remove contact and a separate search button
    file_menu.add_command(
        label='Add new contact', command=lambda: add_contact_form())
    file_menu.add_command(
        label='Remove contact', command=lambda: remove_contact_form())
    file_menu.add_separator()
    file_menu.add_command(
        label='Search', command=search_form)
    pass


# This function displays all addresses in the order they were created
def print_table():
    db_size = len(database)

    # This loop iterates over the database and constructs labels for each item
    for item in range(db_size):
        doc_info = (database.all()[item])
        name = doc_info.get('name')
        address = doc_info.get('address')
        phone_number = doc_info.get('phone_number')
        label_string = ""

        if name != "":
            label_string = label_string + name

        if phone_number != "":
            label_string = label_string + f": {phone_number}"

        if address != "":
            label_string = label_string + f" - {address}"

        # This if/else statement decides if the background is grey or white
        if (item % 2) == 0:
            T = Label(main_frame, text=f"{label_string}\n", width=50)
            T.grid(row=item, column=0)
        else:
            T = Label(
                main_frame, text=f"{label_string}\n",
                bg='#bfbfbf', width=50)
            T.grid(row=item, column=0)
    pass


# This function iterates over each widget in a frame and destroys them all
def erase_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    pass


# This function adds a new contact to the database and updates the main display
def add_contact(name, phone_number, address, window):
    add_frame = Frame(window)

    # Inserts the info into the adb_db.json as a document
    database.insert(
        {"name": name, "phone_number": phone_number, "address": address})
    add_frame.grid(row=4, column=1)
    label_string = ""
    if name != "":
        label_string = label_string + name
    if phone_number != "":
        label_string = label_string + f": {phone_number}"
    if address != "":
        label_string = label_string + f" - {address}"
    T = Label(add_frame, text=f"{label_string} added!\n", bg="white", width=50)
    T.grid(row=4, column=1)
    print_table()


# This function creates an "add contact form" in a new window
def add_contact_form():
    r2 = tk.Tk()
    r2.title('Add contact form')

    # This button executes the add_contact function
    button = tk.Button(
        r2, text='Add entry', width=25,
        command=lambda: [erase_frame(main_frame),
                         add_contact(e1.get(), e2.get(), e3.get(), r2)]
    )

    # Name, phone number, and address buttons
    Label(r2, text='Name').grid(row=0)
    Label(r2, text='Phone number').grid(row=1)
    Label(r2, text='Address').grid(row=2)
    e1 = Entry(r2, width=40)
    e2 = Entry(r2, width=40)
    e3 = Entry(r2, width=40)
    # Assigns e1, e2, and e3 to their respective buttons
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    # Creates a button to click that adds the entry to the database
    button.grid(row=3, column=1)
    r2.mainloop()


def remove_contact(name, phone_number, address, window):
    remove = Query()  # Initializes remove so we can use the query function
    remove_frame = Frame(window)

    if not search_db(name, phone_number, address):
        remove_frame.grid(row=4, column=1)
        T = Label(
            remove_frame, text="No contact matched your entry. Try Again.\n",
            bg="white", width=50)
        T.grid(row=4, column=1)

    elif name != "":
        database.remove(remove.name == name)
        remove_frame.grid(row=4, column=1)
        T = Label(
            remove_frame, text=f"{name} deleted.\n", bg="white", width=50)
        T.grid(row=4, column=1)

    elif phone_number != "":
        database.remove(remove.phone_number == phone_number)
        remove_frame.grid(row=4, column=1)
        T = Label(
            remove_frame, text=f"{phone_number} deleted.\n",
            bg="white", width=50)
        T.grid(row=4, column=1)

    elif address != "":
        database.remove(remove.address == address)
        remove_frame.grid(row=4, column=1)
        T = Label(
            remove_frame, text=f"{address} deleted.\n", bg="white", width=50)
        T.grid(row=4, column=1)

    print_table()


def remove_contact_form():
    r3 = tk.Tk()  # Initialize new window
    r3.title('Remove contact form')  # Title the window

    # This button executes the remove_contact function
    button = tk.Button(
        r3, text='Remove contact', width=25,
        command=lambda: [
            erase_frame(main_frame),
            remove_contact(e1.get(), e2.get(), e3.get(), r3)]
    )

    # Name, phone number, and address buttons
    Label(r3, text='Name').grid(row=0)
    Label(r3, text='Phone number').grid(row=1)
    Label(r3, text='Address').grid(row=2)
    # Initializes an entries for each button as e1, e2, and e2
    e1 = Entry(r3, width=40)
    e2 = Entry(r3, width=40)
    e3 = Entry(r3, width=40)
    # Assigns e1, e2, and e3 to their respective buttons
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    # Creates a button to click that adds the entry to the database
    button.grid(row=3, column=1)
    r3.mainloop()
    pass


# This function searches the database and returns the requested document
def search_db(name, phone_number, address):
    search_query = Query()

    if name != "":
        doc_info = database.search(search_query.name == name)

    elif phone_number != "":
        doc_info = database.search(search_query.phone_number == phone_number)

    elif address != "":
        doc_info = database.search(search_query.address == address)

    return doc_info


# This function formats the document returned by search_db and makes it pretty
def search_result(doc_info, search_frame):
    if not doc_info:
        T = Label(
            search_frame, text="No contact matched your entry. Try Again.\n",
            bg="white", width=50)
        T.grid(row=4, column=1)

    else:
        doc_info_size = len(doc_info)
        for item in range(doc_info_size):
            name = doc_info[item].get('name')
            address = doc_info[item].get('address')
            phone_number = doc_info[item].get('phone_number')
            # This if/else statement decides if the background is grey or white
            if (item % 2) == 0:
                T = Label(
                    search_frame, text=f"{name}: {phone_number} - {address}\n",
                    bg="white", width=50)
                T.grid(row=4 + item, column=1)
            else:
                T = Label(
                    search_frame, text=f"{name}: {phone_number} - {address}\n",
                    bg='#d9d9d9', width=50)
                T.grid(row=4 + item, column=1)


def search_form():
    r4 = tk.Tk()
    r4.title('Search form')

    search_frame = Frame(r4)
    search_frame.grid(row=4, column=1)

    # This button executes the add_contact function
    button = tk.Button(
        r4, text='Search', width=25, command=lambda: [
            erase_frame(search_frame),
            search_result(search_db(e1.get(), e2.get(), e3.get()),
                          search_frame)
        ]
    )

    # Name, phone number, and address buttons
    Label(r4, text='Name').grid(row=0)
    Label(r4, text='Phone number').grid(row=1)
    Label(r4, text='Address').grid(row=2)
    e1 = Entry(r4, width=40)
    e2 = Entry(r4, width=40)
    e3 = Entry(r4, width=40)
    # Assigns e1, e2, and e3 to their respective buttons
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    # Creates a button to click that adds the entry to the database
    button.grid(row=3, column=1)
    r4.mainloop()


# Calling the functions to create the menu and the main table
print_table()
create_menu()
r.mainloop()
