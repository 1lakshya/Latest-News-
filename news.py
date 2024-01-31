import io
from tkinter import *
import requests
from urllib.request import urlopen
from PIL import ImageTk, Image
import webbrowser

class NewsApp:
    def __init__(self):
        # fetch data
        self.data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=2cf83045f50c4214aa075d3086e33686").json()
        # initial Gui load
        self.load_gui()
        # load the 1st new item
        self.load_news_item(2)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry("350x650")
        self.root.resizable(0, 0)
        self.root.title("Lakshya News App")
        self.root.configure(background="black")

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):
        self.clear()

        try:
            img_url = self.data["articles"][index]["urlToImage"]
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQIAAADECAMAAABDV99/AAAA1VBMVEX/////qwD/pgD/qQD/5sj/wGX/1Jv/7Nb/+vjf4ub5+vuyuMLY2+D/rQD8/P3r7O/z9PWdpbPDyM//Uyz/6sC0usWAipzl5uiNmKhsdIZteY6HkaL/SRlndImXobBETGL/oY+nqbH/8tj/2aD/3qj/v0j/04H/uDT/05T/vD//57b/si//thb/rx3/8NL/+u//wlv/2JD/y2z/3rT/xVP/vLD/zsWBhpL/5N3/eF7/7en/hm//bk7/tKX/ZEBQXXZjanv/nYgqNlIhNFX/Qwr/WzQ+T2yUKLpWAAAC+UlEQVR4nO3Xa1fTMBzH8WxBXdvQS0qbtR2MclOBeQdEBbzh+39JJi244Z55jquz38+DrUm3neTXf9JOCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8B/Z23/80MGo6yGt2N6hHMpFw8FR12NasY3h4Ddys+sxrZiLwF56uZhB12NaMRfB02cHz2WfI5CzY7slbMo+R3Bi30anvY5g9kKIl72ugsHg1fHxkUtAyt5GIDebGpCbz9v3rse0YvPnAjnbEvsD2dcI7BJwCQjxuq8RyNnT4clx07abQh8jkIcbe2/aBMSTYR8jkId783Y/I5gdPJl728sIBsNFPd0OH/5ZHnQ9phV7cSp/M3zX9ZhWbevNo4eOXnY9JAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGA1zs5/Harq4iIL3ZGfqTCI5x/Saul7UbDcpeOlvjXwPr38cH8cVMaLmqMwiv3taP6ppJmvWpy1t730W6qKlvr+faOPl5927xtB4l6NiUIR+y4C3xhfiNhETQRhkBt7qZs+G0Hpzpj4/jU0Ro3XMYLz9Pzq+v1do4nAbBc3KtzRNoI4KYrEj6oiL10EpphWsS6KonYZ2AhMXhT2wifF59IuneKizNcwgg8fJ1dfJl/uWtnNRaUi30WR2AjibMcuAc9VQN4sAb0jolyJuHI7g1eGSd0sEU+IMlJVLHS+hnvBWZp+uk7TuzLIKk/Fopx+HTcRRMnX6fSbzu0UgzaCsVDjWPiJFi6CeGyj0IlQN9NvRieh8NZwIYyu08nZVZpets1mIZSesFe/iSDLXG+lF6ug8mwEbRU0UejMbQqlp8f+WlbB7vd0cns7mUzaG2NgCz+sal2ORbMXRGWgdajzILtp7wi5jutK1ztupvaOoPIgGHtmWwc/vMh+ryrXrwqudu+0EXju6po6sE8ByoTaF15dZ3aJ15ny3PlQB36o6/aBIbYloOranrDn7QNBFNRK+d3N5Q+Nful6JAAAAAAAAAAAAAAAAACAv+0nquUzh/a6OQoAAAAASUVORK5CYII="
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root, image=photo)
        label.pack()

        heading = Label(self.root, text=self.data["articles"][index]["title"], bg="black", fg="white", wraplength=350, justify="center")
        heading.pack(pady=(10, 20))
        heading.config(font=("Vardana", 15))

        details = Label(self.root, text=self.data["articles"][index]["description"], bg="black", fg="white", wraplength=350, justify="center")
        details.pack(pady=(2, 20))
        details.config(font=("Vardana", 12))

        frame = Frame(self.root, bg="black")
        frame.pack(expand=True, fill=BOTH)

        if index != 0:
            prev = Button(frame, text="prev", width=16, height=3, command=lambda: self.load_news_item(index - 1))
            prev.pack(side=LEFT)

        read = Button(frame, text="Read More", width=16, height=3, command=lambda: self.open_link(self.data["articles"][index]["url"]))
        read.pack(side=LEFT)

        if index != len(self.data["articles"]) - 1:
            next_btn = Button(frame, text="Next", width=16, height=3, command=lambda: self.load_news_item(index + 1))
            next_btn.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self, url):
        webbrowser.open(url)


obj = NewsApp()
