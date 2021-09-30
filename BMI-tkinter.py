from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('300x200')
window.title('BMI Calculator')

#Entry Height
label1 = Label(window, text='Height(m):',font='Times 15')
label1.place(x=7, y=70)
height_input = Entry(window)
height_input.place(x=100, y=70)
height_input.get()

#Entry Weight
label2 = Label(window, text='Weight(kg):',font='Times 15')
label2.place(x=0, y=40)
weight_input = Entry(window)
weight_input.place(x=100, y=40)
weight_input.get()

#Hàm xử lý dữ liệu lấy được
def cal_BMI():
    BMI = round(float(weight_input.get())/(float(height_input.get())**2),1)

    if BMI > 40:
        return f'{BMI} Béo phì cấp độ III'
    elif BMI >= 35:
        return f'{BMI} Béo phì cấp độ II'
    elif BMI >= 30:
        return f'{BMI} Béo phì cấp độ I'
    elif BMI >= 25:
        return f'{BMI} Thừa cân'
    elif BMI >= 18.5:
        return f'{BMI} Bình thường'
    elif BMI >= 17:
        return f'{BMI} Gầy cấp độ I'
    elif BMI >= 16:
        return f'{BMI} Gầy cấp độ II'
    else:
        return f'{BMI} Gầy cấp độ III'

#Hàm Xử lý in ra màn hình
def print_result():
    condition_check = False
    try:
        float(height_input.get())
        float(weight_input.get())
        condition_check =True
    except:
        msb=messagebox.showwarning(title='', message='Error Data!')

    if condition_check:
        result['text'] = f'Result: {cal_BMI()}'
        msb=messagebox.showinfo(title='Thông báo', message=f'{cal_BMI()}')

#Button Calc BMI
frame_button = Frame(window) 
frame_button.place(x=100, y=100)
button1 = Button(frame_button, text= 'BMI Calculate', background = 'teal', foreground='white', command=print_result).pack()

#Result
result = Label(window,text='Result: 0 ',font='Times 15')
result.place(x=0, y=130)

window.mainloop()