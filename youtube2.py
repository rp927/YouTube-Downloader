import youtube_dl
import tkinter as tk

class YouTube:
    def __init__(self,master):
        self.__master = master
        self.__master.title("YouTube Downloader")
        self.__master.geometry("400x200")

        '''Labels'''
        self.__label1 = tk.Label(self.__master,text="Enter YouTube URL:",font=('Arial',10))
        self.__label1.pack()
        self.__label2 = tk.Label(self.__master,text="Status: ",font=('Arial',10))

        '''Entry'''
        self.entry1 = tk.Entry(bd=5)
        self.entry1.pack(ipadx=100,ipady=5)

        '''Buttons'''
        self.__button1 = tk.Button(text="DOWNLOAD",command=self.download_vid)
        self.__button1.pack()
        self.__label2.pack()


    def download_vid(self):
        user_input = self.get_vid()
        yt_dict = {}
        with youtube_dl.YoutubeDL(yt_dict) as yt:
            yt.download([user_input])
        self.__label2 = tk.Label(self.__master, text="Complete!", font=('Arial', 10))
        self.__label2.pack()

    def get_vid(self):
        string = str(self.entry1.get())
        return string




root = tk.Tk()
my_gui = YouTube(root)
root.mainloop()