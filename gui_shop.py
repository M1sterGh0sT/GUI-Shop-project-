from tkinter import *
from tkinter import font
import tkinter as tk

from tkinter import messagebox as mb

import customtkinter as customtkinter

import products





string_result_to_file = ''
root = tk.Tk()

style1 = font.Font(family='Snell Roundhand',size=15)
style2 = font.Font(family='URW Chancery L',size=10)



# All products and prices
result = ''


# Frames to pages
page1 = tk.Frame(root, bg='grey')
page2 = tk.Frame(root, bg='grey')
page3 = tk.Frame(root, bg='grey')
page4 = tk.Frame(root, bg='grey')
page5 = tk.Frame(root, bg='grey')
page6 = tk.Frame(root, bg='grey')

page7 = tk.Frame(root, bg='grey')
page8 = tk.Frame(root, bg='grey')
page9 = tk.Frame(root, bg='grey')
page10 = tk.Frame(root, bg='grey')
result_page = tk.Frame(root, bg='grey')


# Grid pages
page1.grid(row=0, column=0, sticky='nsew')
page2.grid(row=0, column=0, sticky='nsew')
page3.grid(row=0, column=0, sticky='nsew')
page4.grid(row=0, column=0, sticky='nsew')
page5.grid(row=0, column=0, sticky='nsew')
page6.grid(row=0, column=0, sticky='nsew')

page7.grid(row=0, column=0, sticky='nsew')
page8.grid(row=0, column=0, sticky='nsew')
page9.grid(row=0, column=0, sticky='nsew')
page10.grid(row=0, column=0, sticky='nsew')

result_page.grid(row=0, column=0, sticky='nsew')



# Main Page
lb1 = Label(page1, text='Main Page', font=style1, bg='grey', fg='white', pady=20)
lb1.grid(row=0, column=4, padx=30,)


fruits_btn = Button(page1, text='Fruits', command= lambda : page2.tkraise(), font=style2, padx=30, bg='white', fg='blue')
fruits_btn.grid(row=1, column=2, pady= 35, padx= 30)

vegetables_btn = Button(page1, text='Vegetables', command= lambda : page3.tkraise(), font=style2, padx=30, bg='white', fg='orange')
vegetables_btn.grid(row=1, column=3, pady= 15, padx= 30)

snacks_btn = Button(page1, text='Snacks', command= lambda : page4.tkraise(), font=style2, padx=30, bg='white', fg='purple')
snacks_btn.grid(row=1, column=4, pady= 15, padx= 30)

ice_cream_btn = Button(page1, text='Ice-Cream', command= lambda : page5.tkraise(), font=style2, padx=30, bg='white', fg='green')
ice_cream_btn.grid(row=1, column=5, pady= 15, padx= 30)

bill_page = Button(page1, text='Bill', command= lambda : page6.tkraise(), font=style2, padx=30, bg='white', fg='blue')
bill_page.grid(row=1, column=6, pady= 15, padx= 20)


# Finish shopping
finish_btn = Button(page1, text='Finish Shopping', command= lambda : print_bill(), bg='grey', fg='white')
finish_btn.grid(row=2, column=4)


import datetime
def print_bill():
    time = datetime.datetime.now()
    full_time = time.strftime('%d %b/%X/%G')
    time_for_name_of_bill = time.strftime('%H_%M_%S')

    root.quit()


    try:
        with open(time_for_name_of_bill, 'a') as file:
            file.write(f"{' ' * 10}Grocery Bill\n")
            file.write(f'{"-" * 35}\n{" " * 6}Time:{full_time}\n')
            file.write(f"{'-' * 35}")
            file.write(f'\n{string_result_to_file}')
            file.write(f"{'-' * 35}")

            file.write(f'\nTotal: {round(total_value, 2)}$')
    except FileExistsError:
        print('File not exist')



# ------------
# Bill Page
# ------------

text_box = Text(page6, height=30, width=50)
text_box.tag_configure("center", justify='center')
text_box.insert("1.0", f"Bill\n\n")
text_box.tag_add("center", "1.0", "end")
text_box.pack(padx=50, pady=50)

len_text_box = str(text_box)



# def finish_shopping():
#     return start_total_bill


# Back button
back_btn_fruits = Button(page6, text='Back', command= lambda : page1.tkraise(), font=style2, padx=15, pady=10)
back_btn_fruits.pack()


print_btn = Button(page6)


total_value = 0
bill_lbl1 = Label(page1, text=f'Total price: {round(total_value, 2)}$', font=style1, pady=100, bg='grey')
bill_lbl1.grid(row=11, column=4, pady=50)

bill_lbl2 = Label(page2, text=f'Total price: {round(total_value, 2)}$', font=style1, pady=100, bg='grey')
bill_lbl2.grid(row=5, column=2)

bill_lbl3 = Label(page3, text=f'Total price: {round(total_value, 2)}$', font=style1, pady=100, bg='grey')
bill_lbl3.grid(row=11, column=4)

bill_lbl4 = Label(page4, text=f'Total price: {round(total_value, 2)}$', font=style1, pady=100, bg='grey')
bill_lbl4.grid(row=11, column=2)

bill_lbl5 = Label(page5, text=f'Total price: {round(total_value, 2)}$', font=style1, pady=100, bg='grey')
bill_lbl5.grid(row=6, column=2)




# Create multiple function
# def sequence(*functions):
#     def func(*args, **kwargs):
#         return_value = None
#         for function in functions:
#             return_value = function(*args, **kwargs)
#         return_value()
#     return func







# Fruits Frame
lb2 = Label(page2, text='Fruits', font=style1, bg='grey', fg='white')
lb2.grid(row=0, column=2)

grams_lbl = Label(page7, text='Write Grams of this product', font=style1, pady=20, bg='grey')
grams_lbl.pack()

entry = Entry(page7, bd=10)
entry.pack()


get_value_btn = Button(page7, text='Get', command=lambda : [all.compute(), page2.tkraise()], padx=15, pady=10)
get_value_btn.pack(padx=15, pady=15)

back = Button(page7, text='Back', command=lambda : page2.tkraise(), padx=15, pady=10)
back.pack()


class Main:

    def values(self, name, price):
        self.name = name
        self.price = price

    def compute(self):

        # make global variables
        global total_value
        global string_result_to_file

        self.values(self.name, self.price)


        try:
            self.grams = entry.get()
            self.price /= 1000
            self.price *= int(self.grams)
        except ValueError:
            mb.showinfo(title='Error', message='Please Write Just Digits!')

        # total price
        total_value += self.price

        # update total price text
        bill_lbl1.config(text=f'Total price: {round(total_value, 2)}$')
        bill_lbl2.config(text=f'Total price: {round(total_value, 2)}$')
        bill_lbl3.config(text=f'Total price: {round(total_value, 2)}$')
        bill_lbl4.config(text=f'Total price: {round(total_value, 2)}$')
        bill_lbl5.config(text=f'Total price: {round(total_value, 2)}$')

        string_result_to_file += f'{self.name}: {round(self.price, 2)}$\n'
        text_box.insert('2.0', f'{self.name}: {round(self.price, 2)}$\n')
        entry.delete(0, "end")


all = Main()


back_btn_fruits = Button(page2, text='Apple',
                         command= lambda : [page7.tkraise(), all.values(products.nums_of_fruits[0], products.fruits["apple"])], padx=25, bg='white', fg='blue')

back_btn_fruits.grid(row=1, column=0, pady= 15, padx= 40)

back_btn_fruits = Button(page2, text='Banana',
                         command= lambda : [page7.tkraise(), all.values(products.nums_of_fruits[1], products.fruits["banana"])], padx=25, bg='white', fg='blue')

back_btn_fruits.grid(row=1, column=1, pady= 15, padx= 40)

back_btn_fruits = Button(page2, text='Coco',
                         command= lambda : [page7.tkraise(), all.values(products.nums_of_fruits[2], products.fruits["coco"])], padx=25, bg='white', fg='blue')

back_btn_fruits.grid(row=1, column=2, pady= 15, padx= 40)

back_btn_fruits = Button(page2, text='Peach',
                         command= lambda : [page7.tkraise(), all.values(products.nums_of_fruits[3], products.fruits["peach"])], padx=25, bg='white', fg='blue')

back_btn_fruits.grid(row=1, column=3, pady= 15, padx= 40)

back_btn_fruits = Button(page2, text='Melon',
                         command= lambda : [page7.tkraise(), all.values(products.nums_of_fruits[4], products.fruits["melon"])],padx=25, bg='white', fg='blue')

back_btn_fruits.grid(row=1, column=4, pady= 15, padx= 40)

back_btn_fruits = Button(page2, text='Watermelon',
                         command= lambda : [page7.tkraise(), all.values(products.nums_of_fruits[5], products.fruits["watermelon"])], padx=25, bg='white', fg='blue')

back_btn_fruits.grid(row=2, column=0, pady= 15, padx= 40)



back_btn_fruits = Button(page2, text='Chery',
                         command= lambda : [page7.tkraise(), all.values(products.nums_of_fruits[6], products.fruits["chery"])], padx=25, bg='white', fg='blue')

back_btn_fruits.grid(row=2, column=1, pady= 15, padx= 40)

back_btn_fruits = Button(page2, text='Blueberry',
                         command= lambda : [page7.tkraise(), all.values(products.nums_of_fruits[7], products.fruits["blueberry"])], padx=25, bg='white', fg='blue')

back_btn_fruits.grid(row=2, column=2, pady= 15, padx= 40)

back_btn_fruits = Button(page2, text='Lemon',
                         command= lambda : [page7.tkraise(), all.values(products.nums_of_fruits[8], products.fruits["lemon"])], padx=25, bg='white', fg='blue')

back_btn_fruits.grid(row=2, column=3, pady= 15, padx= 40)

back_btn_fruits = Button(page2, text='Lime',
                         command= lambda : [page7.tkraise(), all.values(products.nums_of_fruits[9], products.fruits["lime"])], padx=25, bg='white', fg='blue')

back_btn_fruits.grid(row=2, column=4, pady= 15, padx= 40)

back_btn_fruits = Button(page2, text='Mango',
                         command= lambda : [page7.tkraise(), all.values(products.nums_of_fruits[10], products.fruits["mango"])], padx=25, bg='white', fg='blue')

back_btn_fruits.grid(row=3, column=0, pady= 15, padx= 40)

back_btn_fruits = Button(page2, text='Kiwi',
                         command= lambda : [page7.tkraise(), all.values(products.nums_of_fruits[11] , products.fruits["kiwi"])], padx=25, bg='white', fg='blue')

back_btn_fruits.grid(row=3, column=4, pady= 15, padx= 40)


# Back button
back_btn_fruits = Button(page2, text='Back', command= lambda : page1.tkraise(), font=style2, padx=15, pady=10, bg='white', fg='blue')
back_btn_fruits.grid(row=5, column=0, pady= 15, padx= 20)







class Main2:

    def values(self, name, price):
        self.name = name
        self.price = price

    def compute(self):
        # make global variables
        global total_value
        global string_result_to_file

        self.values(self.name, self.price)

        try:
            self.grams = entry2.get()
            self.price /= 1000
            self.price *= int(self.grams)
        except ValueError:
            mb.showinfo(title='Error', message='Please Write Just Digits!')

        # total price
        total_value += self.price

        # update total price text
        bill_lbl1.config(text=f'Total price: {round(total_value, 2)}$')
        bill_lbl2.config(text=f'Total price: {round(total_value, 2)}$')
        bill_lbl3.config(text=f'Total price: {round(total_value, 2)}$')
        bill_lbl4.config(text=f'Total price: {round(total_value, 2)}$')
        bill_lbl5.config(text=f'Total price: {round(total_value, 2)}$')

        string_result_to_file += f'{self.name}: {round(self.price, 2)}$\n'
        text_box.insert('2.0', f'{self.name}: {round(self.price, 2)}$\n')
        entry2.delete(0, "end")



all2 = Main2()





# Vegetables Frame
lb3 = Label(page3, text='Vegetables', font=style1, bg='grey', pady=45)
lb3.grid(row=0, column=2)

grams_lbl2 = Label(page8, text='Write Grams of this product', font=style1, pady=20, bg='grey')
grams_lbl2.pack()

entry2 = Entry(page8, bd=10)
entry2.pack()


get_value_btn2 = Button(page8, text='Get', command=lambda : [all2.compute(), page3.tkraise()], padx=15, pady=10)
get_value_btn2.pack(padx=15, pady=15)

back2 = Button(page8, text='Back', command=lambda : page3.tkraise(), padx=15, pady=10)
back2.pack()




back_btn_fruits = Button(page3, text='Potato',
                         command=lambda : [page8.tkraise(), all2.values(products.nums_of_vegetables[0], products.vegetables["potato"])], padx=15, pady=8, bg='white', fg='orange')

back_btn_fruits.grid(row=1, column=0, pady= 15, padx=40)

back_btn_fruits = Button(page3, text='Tomatoes',
                         command= lambda : [page8.tkraise(), all2.values(products.nums_of_vegetables[1], products.vegetables["tomatoes"])], padx=15, pady=8, bg='white', fg='orange')

back_btn_fruits.grid(row=1, column=1, pady= 15, padx= 40)

back_btn_fruits = Button(page3, text='Cherry',
                         command= lambda : [page8.tkraise(), all2.values(products.nums_of_vegetables[2], products.vegetables["cherry"])], padx=15, pady=8, bg='white', fg='orange')

back_btn_fruits.grid(row=2, column=4, pady= 15, padx= 40)

back_btn_fruits = Button(page3, text='Cucumber',
                         command= lambda : [page8.tkraise(), all2.values(products.nums_of_vegetables[3] , products.vegetables["cucumber"])], padx=15, pady=8, bg='white', fg='orange')

back_btn_fruits.grid(row=1, column=2, pady= 15, padx= 40)

back_btn_fruits = Button(page3, text='Paper',
                         command= lambda : [page8.tkraise(), all2.values(products.nums_of_vegetables[4] , products.vegetables["paper"])], padx=15, pady=8, bg='white', fg='orange')

back_btn_fruits.grid(row=1, column=3, pady= 15, padx= 40)


back_btn_fruits = Button(page3, text='Cabbage',
                         command= lambda : [page8.tkraise(), all2.values(products.nums_of_vegetables[5] , products.vegetables["cabbage"])], padx=15, pady=8, bg='white', fg='orange')

back_btn_fruits.grid(row=1, column=4, pady= 15, padx= 40)

back_btn_fruits = Button(page3, text='Lettuce',
                         command= lambda : [page8.tkraise(), all2.values(products.nums_of_vegetables[6] , products.vegetables["lettuce"])], padx=15, pady=8, bg='white', fg='orange')

back_btn_fruits.grid(row=2, column=0, pady= 15, padx=40)

back_btn_fruits = Button(page3, text='Onion',
                         command= lambda : [page8.tkraise(), all2.values(products.nums_of_vegetables[7] , products.vegetables["onion"])], padx=15, pady=8, bg='white', fg='orange')

back_btn_fruits.grid(row=2, column=1, pady= 15, padx= 40)

back_btn_fruits = Button(page3, text='Garlic',
                         command= lambda : [page8.tkraise(), all2.values(products.nums_of_vegetables[8] , products.vegetables["garlic"])], padx=15, pady=8, bg='white', fg='orange')

back_btn_fruits.grid(row=2, column=3, pady= 15, padx= 40)


# Back button
back_btn_vegetables = Button(page3, text='Back', command= lambda : page1.tkraise(), font=style2, padx=15, pady=10, bg='white', fg='orange')
back_btn_vegetables.grid(row=6, column=0, pady= 15, padx= 20)





# Snacks Frame
lb4 = Label(page4, text='Snacks', font=style1, bg='grey', pady=45)
lb4.grid(row=0, column=2, padx=45)


def compute(name, price):
    global total_value
    global string_result_to_file

    total_value += price
    bill_lbl1.config(text=f'Total price: {round(total_value, 2)}$')
    bill_lbl2.config(text=f'Total price: {round(total_value, 2)}$')
    bill_lbl3.config(text=f'Total price: {round(total_value, 2)}$')
    bill_lbl4.config(text=f'Total price: {round(total_value, 2)}$')
    bill_lbl5.config(text=f'Total price: {round(total_value, 2)}$')

    string_result_to_file += f'{name}: {round(price, 2)}$\n'

    text_box.insert('2.0', f'{name}: {round(price, 2)}$\n')



back_btn_fruits = Button(page4, text='Solt Lays',
                         command= lambda : [compute(products.nums_of_snacks[0] , products.snacks["Solt Lays"])], padx=20, bg='white', fg='purple')

back_btn_fruits.grid(row=1, column=0, padx= 70)

back_btn_fruits = Button(page4, text='Paper Lays',
                         command= lambda : [compute(products.nums_of_snacks[1] , products.snacks["Paper Lays"])], padx=20, bg='white', fg='purple')

back_btn_fruits.grid(row=1, column=1, pady= 15, padx= 10)



back_btn_fruits = Button(page4, text='Cheese Lays',
                         command= lambda : [compute(products.nums_of_snacks[2] , products.snacks["Cheese Lays"])], padx=20, bg='white', fg='purple')

back_btn_fruits.grid(row=1, column=2, pady= 15, padx= 10)

back_btn_fruits = Button(page4, text='Barbecue Lays',
                         command= lambda : [compute(products.nums_of_snacks[3] , products.snacks["Barbecue Lays"])], padx=20, bg='white', fg='purple')

back_btn_fruits.grid(row=1, column=3, pady= 15, padx= 10)

back_btn_fruits = Button(page4, text='Solt Sticks',
                         command= lambda : [compute(products.nums_of_snacks[4] , products.snacks["Solt Sticks"])], padx=25, bg='white', fg='purple')

back_btn_fruits.grid(row=1, column=4, pady= 15, padx= 10)

back_btn_fruits = Button(page4, text='Sticks',
                         command= lambda : [compute(products.nums_of_snacks[5] , products.snacks["Sticks"])], padx=25, bg='white', fg='purple')

back_btn_fruits.grid(row=2, column=0, pady= 15, padx= 10)

back_btn_fruits = Button(page4, text='Cheese Popcorn',
                         command= lambda : [compute(products.nums_of_snacks[6] , products.snacks["Cheese Popcorn"])], padx=25, bg='white', fg='purple')

back_btn_fruits.grid(row=2, column=1, pady= 15, padx= 10)

back_btn_fruits = Button(page4, text='Solt Popcorn',
                         command= lambda : [compute(products.nums_of_snacks[7] , products.snacks["Solt Lays"])], padx=25, bg='white', fg='purple')

back_btn_fruits.grid(row=2, column=3, pady= 15, padx= 10)

back_btn_fruits = Button(page4, text='Bacon Popcorn',
                         command= lambda : [compute(products.nums_of_snacks[8] , products.snacks["Bacon Popcorn"])], padx=25, bg='white', fg='purple')

back_btn_fruits.grid(row=2, column=4, pady= 15, padx= 10)



back_btn_ice_cream = Button(page4, text='Back', command= lambda : page1.tkraise(), font=style2, padx=15, pady=10, bg='white', fg='purple')
back_btn_ice_cream.grid(row=6, column=0, pady= 15, padx= 15)





# Ice-Cream Frame
lb5 = Label(page5, text='Ice-Cream', font=style1, bg='grey', pady=45)
lb5.grid(row=0, column=2, padx=45)




back_btn_fruits = Button(page5, text='Vanilla ice-cream',
                         command= lambda : [compute(products.nums_of_ice_cream[0] , products.ice_cream["vanilla ice-cream"])], padx=25, bg='white', fg='green')

back_btn_fruits.grid(row=1, column=1, pady= 15, padx= 20)


back_btn_fruits = Button(page5, text='Chocolate Ice-Cream',
                         command= lambda : [compute(products.nums_of_ice_cream[1] , products.ice_cream["chocolate ice-cream"])], padx=25, bg='white', fg='green')

back_btn_fruits.grid(row=1, column=2, pady= 15, padx= 20)

back_btn_fruits = Button(page5, text='Lemon Ice-Cream',
                         command= lambda : [compute(products.nums_of_ice_cream[2] , products.ice_cream["lemon ice-cream"])], padx=25, bg='white', fg='green')

back_btn_fruits.grid(row=1, column=3, pady= 15, padx= 20)


back_btn_fruits = Button(page5, text='Caramel Ice-Cream',
                         command= lambda : [compute(products.nums_of_ice_cream[3] , products.ice_cream["caramel ice-cream"])], padx=25, bg='white', fg='green')

back_btn_fruits.grid(row=2, column=1, pady= 15, padx= 20)


back_btn_fruits = Button(page5, text='Tropic Ice-Cream',
                         command= lambda : [compute(products.nums_of_ice_cream[4] , products.ice_cream["tropic ice-cream"])], padx=25, bg='white', fg='green')

back_btn_fruits.grid(row=2, column=2, pady= 15, padx= 20)


back_btn_fruits = Button(page5, text='Fruits Mix Ice-Cream',
                         command= lambda : [compute(products.nums_of_ice_cream[5] , products.ice_cream["fruits mix ice-cream"])], padx=25, bg='white', fg='green')

back_btn_fruits.grid(row=2, column=3, pady= 15, padx= 20)



# Back button
back_btn_vegetables = Button(page5, text='Back', command= lambda : page1.tkraise(), font=style2, padx=15, pady=10, bg='white', fg='green')
back_btn_vegetables.grid(row=6, column=0, pady= 15, padx= 20)







page1.tkraise()
root.geometry('925x670')
root.title('Multiply Shop')
root.resizable(False, False)
root.mainloop()