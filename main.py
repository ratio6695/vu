import tkinter as tk
from tkinter import Frame
from PIL import ImageTk, Image
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import subprocess

def sodo():
    root.destroy()
    subprocess.call(["python", "D:/python/btcuoiki/kichthuoc.py"])

def dsnhanvien():
    root.destroy()
    subprocess.call(["python", "D:/python/btcuoiki/dsnhanvien.py"])
    
def dsphongban():
    root.destroy()
    subprocess.call(["python", "D:/python/btcuoiki/dsphongban.py"])

def gioithieu():
    subprocess.call(["python", "D:/python/btcuoiki/gioithieu.py"])

def thongtin():
    subprocess.call(["python", "D:/python/btcuoiki/thongtin.py"])

def banhang():
    root.destroy()
    subprocess.call(["python", "D:/python/btcuoiki/test.py"])  

def dangnhap():
    root.destroy()
    subprocess.call(["python", "D:/python/btcuoiki/login.py"])  

def thoat():
    root.destroy()
    
def on_enter(event):
    event.widget.config(fg='silver')  # Thay đổi màu nền của label thành màu vàng khi chuột vào

def on_leave(event):
    event.widget.config(fg='black')  # Thay đổi màu nền của label thành màu trắng khi chuột rời đi

def thoigian():
    thoigianHT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    thoigian_lable.config(text=thoigianHT)
    root.after(1000, thoigian)

root = tk.Tk()

root.geometry("1000x600")

# Thiết lập tên cửa sổ
root.title("giao diện")




header_frame = tk.Frame(root, height=50, bg="DodgerBlue")
header_frame.pack(fill=tk.X, side=tk.TOP)
header_frame.bind("<Configure>", lambda event: header_frame.configure(height=50))

sidebar_frame = tk.Frame(root, height=100, bg="#fff", borderwidth=1)
sidebar_frame.pack(fill=tk.Y, side=tk.LEFT)
sidebar_frame.bind("<Configure>", lambda event: sidebar_frame.configure(width=200))

lable_logo = tk.Label(root, text="Cafe QKV xin Chào!",  font=('Times New Roman',18), bg="DodgerBlue", fg="#fff")
lable_logo.place(x=10, y=12, anchor="nw")

image_caidat = Image.open("D:/python/btcuoiki/image/exit.jpg")
image_caidat = image_caidat.resize((20,20))
photo_caidat = ImageTk.PhotoImage(image_caidat)
lable_CAIDAT = tk.Button(root, image=photo_caidat , bg="DodgerBlue", command=thoat)
lable_CAIDAT.place(relx=1, rely=0, anchor="ne", x=-20, y=17)

image_dn = Image.open("D:/python/btcuoiki/image/nguoi.png")
image_dn = image_dn.resize((20,20))
photo_dn = ImageTk.PhotoImage(image_dn)
lable_CAIDAT = tk.Button(root, image=photo_dn , bg="DodgerBlue", command=dangnhap)
lable_CAIDAT.place(relx=1, rely=0, anchor="ne", x=-50, y=17)

image = Image.open("D:/python/btcuoiki/image/cf.jpg")
image = image.resize((196,130))
photo = ImageTk.PhotoImage(image)
image_lable = tk.Label(root, image=photo)
image_lable.place(x = 0, y = 50, anchor="nw")



lable_tc =tk.Label(root, text="Trang Chủ", borderwidth=1, width=20, font=24, bg="#fff", fg="black")
lable_tc.place(x=8, y=200)

lable_tc.bind('<Enter>', on_enter)  # Gắn sự kiện khi chuột vào label
lable_tc.bind('<Leave>', on_leave)  # Gắn sự kiện khi chuột rời khỏi label


lable_gt =tk.Label(root, text="Giới Thiệu", borderwidth=1, width=20, font=24, bg="#fff", fg="black", cursor="hand2")
lable_gt.place(x=8, y=230)
lable_gt.bind("<Button-1>", lambda event: gioithieu())

lable_gt.bind('<Enter>', on_enter)  # Gắn sự kiện khi chuột vào label
lable_gt.bind('<Leave>', on_leave)  # Gắn sự kiện khi chuột rời khỏi label

lable_td =tk.Label(root, text="Thông Tin", borderwidth=1, width=20, font=24, bg="#fff", fg="black",cursor="hand2")
lable_td.place(x=8, y=260)
lable_td.bind("<Button-1>", lambda event: thongtin())

lable_td.bind('<Enter>', on_enter)  # Gắn sự kiện khi chuột vào label
lable_td.bind('<Leave>', on_leave)  # Gắn sự kiện khi chuột rời khỏi label

lable_tieude = tk.Label(root, text ="CHÀO MỪNG BẠN TRỞ LẠI!", font=('Times New Roman',24))
lable_tieude.place(x=220, y=60)
lable_tieude1 = tk.Label(root, text ="HÔM NAY NGÀY: ", font=('Times New Roman',10), fg="gray")
lable_tieude1.place(x=230, y=100)
thoigian_lable = tk.Label(root, font=('Times New Roman',10), fg="gray")
thoigian_lable.place(x=340, y=100)


framett1 = Frame(root,width=200, height=300)
image_QLNV = Image.open("D:/python/btcuoiki/image/QLNV.jpg")
image_QLNV = image_QLNV.resize((200,130))
photo_QLNV = ImageTk.PhotoImage(image_QLNV)
labelid = tk.Button(framett1, image=photo_QLNV,command=dsnhanvien)
labelid.pack(side='left')

image_QLPB = Image.open("D:/python/btcuoiki/image/QLPB.jpg")
image_QLPB = image_QLPB.resize((200,130))
photo_QLPB = ImageTk.PhotoImage(image_QLPB)
labelhoten = tk.Button(framett1, image=photo_QLPB, command=dsphongban)
labelhoten.pack(side='left', padx=100)
framett1.pack(padx=50, pady=80)


framett2 = Frame(root)
image_ip = Image.open("D:/python/btcuoiki/image/nuocuong.png")
image_ip = image_ip.resize((200,130))
photo_ip = ImageTk.PhotoImage(image_ip)
labelip = tk.Button(framett2, image=photo_ip, command=banhang)
labelip.pack(side='left')


image_sd = Image.open("D:/python/btcuoiki/image/doanhso.png")
image_sd = image_sd.resize((200,130))
photo_sd = ImageTk.PhotoImage(image_sd)
labelsd = tk.Button(framett2, image=photo_sd, command=sodo)
labelsd.pack(side='left', padx=100)

framett2.pack()
thoigian()
root.mainloop()



