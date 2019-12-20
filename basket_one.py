from tkinter import *
from functools import partial

def main():

    master = Tk()
    a = 0
    column_list = []
    a_list = []
    temp_list = []
    #name_list = create_name_list()
    #item_list = create_item_list()
    name_list = [Person("Jonathan", 0), Person("Samuel", 0), Person("Anthony", 0)]
    item_list = [Item("Pears", 50), Item("Meat", 100)]
    for i in range(len(item_list)):
        Label(master, text=item_list[i].name).grid(row=i + 1, stick=W)
        for j in range(len(name_list)):
           var = IntVar()
           Checkbutton(master, text=a, variable=var).grid(row=i+1, column=j+1)
           a_list.append(var)
           a+=1
    for k in range(len(name_list)):
    	Label(master, text=name_list[k].name).grid(row=0, column=k+1)

    b1 = Button(master, text="Calculate", command= lambda : calculate_list(a_list, name_list, item_list)).grid(row=len(item_list)+1, column=len(name_list)+1)
    b2 = Button(master, text="Reset Amounts", command = lambda : reset_all(name_list, item_list)).grid(row=len(item_list), column=len(name_list)+1)
    b3 = Button(master, text="Print Name List", command = lambda : print_name_list(name_list)).grid(row=len(item_list) - 1, column=len(name_list)+1)
    b4 = Button(master, text="Print Item List", command = lambda : print_item_list(item_list)).grid(row=len(item_list) - 2, column=len(name_list)+1)
    b5 = Button(master, text="Test final_list", command = lambda : final_list(name_list, item_list)).grid(row=len(item_list) +2, column=len(name_list)+1)

    mainloop()


def reset_all(name_list, item_list):
    for i in name_list:
        i.amount = 0
        i.selected_items = []
    for j in item_list:
        j.count = 0

def print_name_list(name_list):
    #root = Tk()
    for i in name_list:
        #Label(root, text=i).pack()
        print(i)
    #mainloop()

def print_item_list(item_list):
    #root = Tk()
    for i in item_list:
        #Label(root, text=i).pack()
        print(i)
    #mainloop()


def calculate_list(a_list, name_list, item_list):

    for i in range(len(a_list)):
        #print(a_list[i].get())
        if a_list[i].get() == 1:
            r_num = i // len(name_list)
            c_num = i % len(name_list)
            print("For Checkbox %d Row: %d Column: %d" % (i, r_num, c_num))
            item_list[r_num].count += 1
            name_list[c_num].selected_items.append(item_list[r_num].name)
    print("\n")



    #name_list = [Person("Jonathan", 0), Person("Samuel", 0), Person("Anthony", 0)]
    #item_list = [Item("Pears", 100), Item("Meat", 200)]

def final_list(name_list, item_list):
    for i in name_list:
        for j in i.selected_items:
            for k in item_list:         #Checking if the item in selected_list if its equal to item in item_list	
                if k.name == j:
                    print("MATCH")
                    cost = k.price / k.count
                    i.amount += cost



class Person:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.selected_items = []

    def __repr__(self):
    	return "Person: {0} Amount Owed: {1} Items: {2}".format(self.name, self.amount, self.selected_items)



def create_name_list():
    name_list = []
    numOfPeople = input("Amount of People?\n")
    for i in range(int(numOfPeople)):
        temp_Name = input("Enter the %d person's name: " % (i))
        name_list.append(Person(temp_Name, 0))
    return name_list


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.count = 0

    def __repr__(self):
        return "Item: {0} Price: {1} Count: {2}".format(self.name, self.price, self.count)


def create_item_list():
    item_list = []
    numOfItems = input("Amount of Items?\n")
    for i in range(int(numOfItems)):
        name = input("Enter item #%d: " % (i))
        price = input("Enter cost: ")
        item_list.append(Item(name, price))
    return (item_list)

def print_a_list(a_list):
	for i in a_list:
		print(i.get(), " ")
	print("____________")

def print_list_2(a_list):
    for i in a_list:
        print(i[0].get())
        print("____________")

def check(var):
    if var.get() == 0:
        return True
    else:
        return False

main()


'''
for i in range(len(item_list)):
        Label(master, text=item_list[i].name).grid(row=i + 1, stick=W)
    for j in range(len(name_list)):
        Label(master, text=name_list[j].name).grid(row=0, column=j + 1)
        for k in range(len(item_list)):
            var = IntVar()
            Checkbutton(master, text=k, variable=var).grid(row=k + 1, column=j + 1)
            if k is not 0 and j is not 0:
                temp_list.append(var)
        a_list.append(temp_list)

'''



'''

    for i in range(len(item_list) + 1):
        Label(master, text=name_list[i].name).grid(row=0, column=i + 1)
        for j in range(len(name_list) + 1):
            Label(master, text=item_list[i].name).grid(row=i + 1)
            var1 = IntVar()
            Checkbutton(master, text="", variable=var1).grid(row=i + 1, column=j)
            intVar_List.append(var1)
    for k in intVar_List:
        if check(k):
            print(k.get())
'''