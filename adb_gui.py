#test commit
import tkinter as tk
from tkinter import *
from tinydb import TinyDB, Query

#Creates and names a tkinter window
r=tk.Tk()
r.title('Address Book')

#creates and names main frame
main_frame = Frame(r, width=500, height=100)
main_frame.pack()


database = TinyDB('adb_db.json')    #Initializes database as the address book database (filename: adb_db.json)

#This function creates the drop down menu with buttons to exit, add new contact, or search for a contact. Eventually there will be a remove contact button too.
def create_menu():
    menu = Menu(r)         #Initialize menu
    r.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='Add/Search', menu=filemenu)                                     #Creates label for whole menu
    filemenu.add_command(label='Add new contact', command=lambda: add_contact_form())       #Creates add contact menu option
    filemenu.add_command(label='Remove contact', command=lambda: remove_contact_form())     #Creates remove contact menu option
    filemenu.add_separator()                                                                #Creates seperator
    filemenu.add_command(label='Search', command=search_form)                               #Creates search button menu option
    pass

#This function builds a table on the main page, which displays all addresses in the order they were placed in the table
def print_table():
    DBSize = len(database)

    #This for loop iterates over the entire database, gets the name, addy, and phone number of each item, and constructs them into a label with a white or back background
    for item in range(DBSize):
        docinfo = (database.all()[item])
        name = docinfo.get('name')
        address = docinfo.get('address')
        phone_number = docinfo.get('phone_number')
        labelstring = ""

        if name != "":
            labelstring = labelstring + name

        if phone_number != "":
            labelstring = labelstring + f": {phone_number}"

        if address != "":
            labelstring = labelstring + f" - {address}"

        #This if/else statement decides if the background is grey or white and then constructs the label for the document
        if (item % 2) == 0:
            T = Label(main_frame, text=f"{labelstring}\n", width = 50)
            T.grid(row = item, column = 0)
        else:
            T = Label(main_frame, text=f"{labelstring}\n", bg = '#bfbfbf', width = 50)
            T.grid(row = item, column = 0)
    pass

#This function iterates over each widget in a frame and destroys them all
def erase_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    pass

#This function adds a new contact to the database and updates the main display
#It is passed the name, phone number, and address from the contact entry form
def add_contact(name, phone_number, address, window):
    add_frame = Frame(window)

    database.insert({"name": name, "phone_number": phone_number, "address": address})           #Inserts the info into the adb_db.json as a document
    add_frame.grid(row=4, column=1)
    labelstring = ""
    if name != "":
        labelstring = labelstring + name
    if phone_number != "":
        labelstring = labelstring + f": {phone_number}"
    if address != "":
        labelstring = labelstring + f" - {address}"
    T = Label(add_frame, text=f"{labelstring} added!\n", bg="white", width=50)
    T.grid(row=4, column=1)
    print_table()

#This function creates an "add contact form" in a new window
def add_contact_form():
    r2 = tk.Tk()                                                #Initialize new window
    r2.title('Add contact form')                                #Title the window

    #This button erases the main frame, executes the add_contact function, and destroys the add contact form window
    button = tk.Button(r2, text='Add entry', width=25, command=lambda: [erase_frame(main_frame), add_contact(e1.get(), e2.get(), e3.get(), r2)])

    Label(r2, text='Name').grid(row=0)                          #Name button
    Label(r2, text='Phone number').grid(row=1)                  #Phone number button
    Label(r2, text='Address').grid(row=2)                       #Address button
    e1 = Entry(r2, width=40)                                    #
    e2 = Entry(r2, width=40)                                    #Initializes an entries for each button as e1, e2, and e2
    e3 = Entry(r2, width=40)                                    #
    e1.grid(row=0, column=1)                                    #
    e2.grid(row=1, column=1)                                    #Assigns e1, e2, and e3 to their respective buttons
    e3.grid(row=2, column=1)                                    #
    button.grid(row=3, column = 1)                              #Creates a button to click that adds the entry to the database
    r2.mainloop()

def remove_contact(name, phone_number, address, window):

    remove = Query()  # Initializes remove so we can use the query function
    remove_frame = Frame(window)

    if search_db(name, phone_number, address) == []:
        remove_frame.grid(row=4, column=1)
        T = Label(remove_frame, text="No contact matched your entry. Try Again.\n", bg="white", width=50)
        T.grid(row=4, column=1)

    elif name != "":
        database.remove(remove.name == name)
        remove_frame.grid(row=4, column=1)
        T = Label(remove_frame, text=f"{name} deleted.\n", bg="white", width=50)
        T.grid(row=4, column=1)

    elif  phone_number != "":
        database.remove(remove.phone_number == phone_number)
        remove_frame.grid(row=4, column=1)
        T = Label(remove_frame, text=f"{phone_number} deleted.\n", bg="white", width=50)
        T.grid(row=4, column=1)

    elif address != "":
        database.remove(remove.address == address)
        remove_frame.grid(row=4, column=1)
        T = Label(remove_frame, text=f"{address} deleted.\n", bg="white", width=50)
        T.grid(row=4, column=1)

    print_table()

def remove_contact_form():
    r3 = tk.Tk()  # Initialize new window
    r3.title('Remove contact form')  # Title the window

    # This button erases the main frame, executes the remove_contact function, and destroys the remove contact form window
    button = tk.Button(r3, text='Remove contact', width=25,  command=lambda: [erase_frame(main_frame), remove_contact(e1.get(), e2.get(), e3.get(), r3)])

    Label(r3, text='Name').grid(row=0)  # Name button
    Label(r3, text='Phone number').grid(row=1)  # Phone number button
    Label(r3, text='Address').grid(row=2)  # Address button
    e1 = Entry(r3, width=40)  #
    e2 = Entry(r3, width=40)  # Initializes an entries for each button as e1, e2, and e2
    e3 = Entry(r3, width=40)  #
    e1.grid(row=0, column=1)  #
    e2.grid(row=1, column=1)  # Assigns e1, e2, and e3 to their respective buttons
    e3.grid(row=2, column=1)  #
    button.grid(row=3, column=1)  # Creates a button to click that adds the entry to the database
    r3.mainloop()
    pass

def search_db(name, phone_number, address):
    searchquery = Query()

    if name != "":
        docinfo = database.search(searchquery.name == name)

    elif phone_number != "":
        docinfo = database.search(searchquery.phone_number == phone_number)

    elif address != "":
        docinfo = database.search(searchquery.address == address)

    return docinfo

def search_result(docinfo, search_frame):

    if docinfo == []:
        T = Label(search_frame, text="No contact matched your entry. Try Again.\n", bg="white", width=50)
        T.grid(row=4, column=1)

    else:
        docinfo_size = len(docinfo)
        for item in range(docinfo_size):
            name = docinfo[item].get('name')
            address = docinfo[item].get('address')
            phone_number = docinfo[item].get('phone_number')
            #This if/else statement decides if the background is grey or white
            if (item % 2) == 0:
                T = Label(search_frame, text=f"{name}: {phone_number} - {address}\n", bg = "white", width = 50)
                T.grid(row = 4 + item, column = 1)
            else:
                T = Label(search_frame, text=f"{name}: {phone_number} - {address}\n", bg = '#d9d9d9', width = 50)
                T.grid(row = 4 + item, column = 1)

def search_form():
    r4 = tk.Tk()  # Initialize new window
    r4.title('Search form')  # Title the window

    search_frame = Frame(r4)
    search_frame.grid(row=4, column=1)

    # This button executes the add_contact function and destroys the add contact form window
    button = tk.Button(r4, text='Search', width=25, command=lambda: [erase_frame(search_frame), search_result(search_db(e1.get(), e2.get(), e3.get()), search_frame)])

    Label(r4, text='Name').grid(row=0)  # Name button
    Label(r4, text='Phone number').grid(row=1)  # Phone number button
    Label(r4, text='Address').grid(row=2)  # Address button
    e1 = Entry(r4, width=40)  #
    e2 = Entry(r4, width=40)  # Initializes an entries for each button as e1, e2, and e2
    e3 = Entry(r4, width=40)  #
    e1.grid(row=0, column=1)  #
    e2.grid(row=1, column=1)  # Assigns e1, e2, and e3 to their respective buttons
    e3.grid(row=2, column=1)  #
    button.grid(row=3, column=1)  # Creates a button to click that adds the entry to the database
    r4.mainloop()


#Calling the functions to create the menu and the main table
print_table()
create_menu()
r.mainloop()
