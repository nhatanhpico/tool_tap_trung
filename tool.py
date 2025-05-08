print("Tool tap trung v1.0")
import tkinter as tk
from PIL import ImageTk, Image

hour, minute, second = int(input("Nhập giờ: ")), int(input("Nhập phút: ")), int(input("Nhập giây: "))
t = (second+minute*60+hour*60*60)*1000

root = tk.Tk()
root.attributes("-fullscreen", True)

tk.Label(root, text="Bạn sẽ không thể sử dụng máy tính trong thời gian này.", font="Helvetica 25 bold", bg="green").pack(anchor = 'w')
tk.Label(root, text="Hãy tập trung làm việc của bạn!", font="Helvetica 25 bold", bg="green").pack(anchor = 'w')

text = tk.Label(root, text="Tập trung học", font="Helvetica 25 bold", bg="red")
text.pack(anchor = 'w')

img = ImageTk.PhotoImage(Image.open("dog.png"))
panel = tk.Label(root, image = img).pack(side = "right")
windll.user32.BlockInput(True)


def unblock():
	text.configure(text = "Tắt")
	windll.user32.BlockInput(False)
	tk.Button(root, text ="Triển thôi =))", command = root.destroy, font="Helvetica 15 bold").pack(anchor = 'w')

root.after(t, unblock)

root.mainloop()
