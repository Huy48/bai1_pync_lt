import tkinter as tk

# Xử lý các nút bấm
def btn_click(item):
	global expression
	expression += str(item)
	input_text.set(expression)

# Xóa toàn bộ nội dung
def btn_clear():
	global expression
	expression = ""
	input_text.set("")

# tính kết quả
def btn_equal():
	global expression
	try:
		result = str(eval(expression))
		input_text.set(result)
		expression = result
	except:
		input_text.set("Lỗi")
		expression = ""

root = tk.Tk()
root.title("Máy tính")
root.geometry("300x400")

expression = ""
input_text = tk.StringVar()

input_frame = tk.Frame(root, width=300, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) 

btns_frame = tk.Frame(root, width=300, height=350, bg="grey")
btns_frame.pack()

tk.Button(btns_frame, text="C", width=32, height=3, bg="#eee", fg="black", command=btn_clear).grid(row=0, column=0, columnspan=3)
tk.Button(btns_frame, text="/", width=10, height=3, bg="grey", fg="white", command=lambda: btn_click("/")).grid(row=0, column=3)

tk.Button(btns_frame, text="7", width=10, height=3, bg="#fff", fg="black", command=lambda: btn_click(7)).grid(row=1, column=0)
tk.Button(btns_frame, text="8", width=10, height=3, bg="#fff", fg="black", command=lambda: btn_click(8)).grid(row=1, column=1)
tk.Button(btns_frame, text="9", width=10, height=3, bg="#fff", fg="black", command=lambda: btn_click(9)).grid(row=1, column=2)
tk.Button(btns_frame, text="*", width=10, height=3, bg="grey", fg="white", command=lambda: btn_click("*")).grid(row=1, column=3)

tk.Button(btns_frame, text="4", width=10, height=3, bg="#fff", fg="black", command=lambda: btn_click(4)).grid(row=2, column=0)
tk.Button(btns_frame, text="5", width=10, height=3, bg="#fff", fg="black", command=lambda: btn_click(5)).grid(row=2, column=1)
tk.Button(btns_frame, text="6", width=10, height=3, bg="#fff", fg="black", command=lambda: btn_click(6)).grid(row=2, column=2)
tk.Button(btns_frame, text="-", width=10, height=3, bg="grey", fg="white", command=lambda: btn_click("-")).grid(row=2, column=3)

tk.Button(btns_frame, text="1", width=10, height=3, bg="#fff", fg="black", command=lambda: btn_click(1)).grid(row=3, column=0)
tk.Button(btns_frame, text="2", width=10, height=3, bg="#fff", fg="black", command=lambda: btn_click(2)).grid(row=3, column=1)
tk.Button(btns_frame, text="3", width=10, height=3, bg="#fff", fg="black", command=lambda: btn_click(3)).grid(row=3, column=2)
tk.Button(btns_frame, text="+", width=10, height=3, bg="grey", fg="white", command=lambda: btn_click("+")).grid(row=3, column=3)

tk.Button(btns_frame, text="0", width=21, height=3, bg="#fff", fg="black", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2)
tk.Button(btns_frame, text=".", width=10, height=3, bg="#eee", fg="black", command=lambda: btn_click(".")).grid(row=4, column=2)
tk.Button(btns_frame, text="=", width=10, height=3, bg="#32cd32", fg="white", command=btn_equal).grid(row=4, column=3)

root.mainloop()
