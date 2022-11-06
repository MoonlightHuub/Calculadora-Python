from tkinter import *

#Ventana

ventana = Tk()
ventana.title("Calculadora")
ventana.config(bg = "#2B2B2B")

#Variabe Global para que solo el primer numero se posicione en el indice cero

i = 0

#input

txtin = Entry(ventana, font = ("minecraftia 20"))
txtin.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 5)


#funciones

def click_btn(valor):
    global i 
    txtin.insert(i, valor)
    i += 1

def clean():
    txtin.delete(0, END)
    i = 0

def math():
    operacion = txtin.get()
    resultado = eval(operacion)
    txtin.delete(0, END)
    txtin.insert(0, resultado)
    i = 0



#Botones

btn = Button(ventana, text = "1", width = 15, height = 5, bg = "#2C3639", fg = "white", command = lambda: click_btn(1))
btn1 = Button(ventana, text = "2", width = 15, height = 5, bg = "#2C3639", fg = "white", command = lambda: click_btn(2))
btn2 = Button(ventana, text = "3", width = 15, height = 5, bg = "#2C3639", fg = "white", command = lambda: click_btn(3))
btn3 = Button(ventana, text = "4", width = 15, height = 5, bg = "#2C3639", fg = "white", command = lambda: click_btn(4))
btn4 = Button(ventana, text = "5", width = 15, height = 5, bg = "#2C3639", fg = "white", command = lambda: click_btn(5))
btn5 = Button(ventana, text = "6", width = 15, height = 5, bg = "#2C3639", fg = "white", command = lambda: click_btn(6))
btn6 = Button(ventana, text = "7", width = 15, height = 5, bg = "#2C3639", fg = "white", command = lambda: click_btn(7))
btn7 = Button(ventana, text = "8", width = 15, height = 5, bg = "#2C3639", fg = "white", command = lambda: click_btn(8))
btn8 = Button(ventana, text = "9", width = 15, height = 5, bg = "#2C3639", fg = "white", command = lambda: click_btn(9))
btn9 = Button(ventana, text = "0", width = 30, height = 5, bg = "#2C3639", fg = "white", command = lambda: click_btn(0))

btn_cl = Button(ventana, text = "C", width = 15, height = 4, bg = "#F0FF42", command = lambda: clean())
btn_parentesis_A = Button(ventana, text = "(", width = 15, height = 4, bg = "#2C3639", fg = "white", command = lambda: click_btn("("))
btn_parentesis_B = Button(ventana, text = ")", width = 15, height = 4, bg = "#2C3639", fg = "white", command = lambda: click_btn(")"))
btn_punto = Button(ventana, text = ".", width = 15, height = 4, bg = "#2C3639", fg = "white", command = lambda: click_btn("."))
btn_result = Button(ventana, text = "=", width = 15, height = 4, bg = "#54B435", command = lambda: math())

btn_suma = Button(ventana, text = "+", width = 15, height = 4, bg = "#2C3639", fg = "white", command = lambda: click_btn("+"))
btn_resta = Button(ventana, text = "-", width = 15, height = 4, bg = "#2C3639", fg = "white", command = lambda: click_btn("-"))
btn_mult = Button(ventana, text = "*", width = 15, height = 4, bg = "#2C3639", fg = "white", command = lambda: click_btn("*"))
btn_div = Button(ventana, text = "/", width = 15, height = 4, bg = "#2C3639", fg = "white", command = lambda: click_btn("/"))


#Grid 

btn_cl.grid(row = 1, column = 0)
btn_parentesis_A.grid(row = 1, column = 1)
btn_parentesis_B.grid(row = 1, column = 2)
btn_div.grid(row = 1, column = 3, pady = 10)
btn_mult.grid(row = 2, column = 3, pady = 5)
btn_suma.grid(row = 3, column = 3)
btn_resta.grid(row = 4, column = 3, pady = 5) 
btn_result.grid(row = 5, column = 3, pady = 5)

btn.grid(row = 2, column = 0, padx = 5, pady = 5)
btn1.grid(row = 2, column = 1, padx = 5, pady = 5)
btn2.grid(row = 2, column = 2, padx = 5, pady = 5)
btn3.grid(row = 3, column = 0, padx = 5, pady = 5)
btn4.grid(row = 3, column = 1, padx = 5, pady = 5)
btn5.grid(row = 3, column = 2, padx = 5, pady = 5)
btn6.grid(row = 4, column = 0, padx = 5, pady = 5)
btn7.grid(row = 4, column = 1, padx = 5, pady = 5)
btn8.grid(row = 4, column = 2, padx = 5, pady = 5)
btn9.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)

btn_punto.grid(row = 5, column = 2)



ventana.mainloop()