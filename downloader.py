import tkinter as tk
from pytube import YouTube

def download(link, opt):
    try:
        w1.destroy()
        yt = YouTube(link)
        yt.streams.filter(res= opt).first().download()
        lb2.config(text= "Download Successfull")
    except:
        lb2.config(text= "Something went wrong :?")
    return

def videodownloader():
    global w1
    f1080 = False
    f720 = False
    f480 = False
    opt = ["Please select video format"]
    link = ent1.get()
    ent1.delete(0, tk.END)
    try:
        yt = YouTube(link)
        videos = yt.streams.filter(only_video= True)
        for i in videos:
            if i.resolution == "1080p":
                f1080 = True
            if i.resolution == "720p":
                f720 = True
            if i.resolution == "480p":
                f480 = True
        if f1080 == True:
            opt.append("1080p")
        if f720 == True:
            opt.append("720p")
        if f480 == True:
            opt.append("480p")
        lb2.config(text= f"Downloading '{yt.title}' please wait...")
        w1 = tk.Toplevel(root)
        w1.title("Choose Format")
        w1.config(background="#ff5a36")
        w1.geometry("250x120")
        clicked = tk.StringVar()
        clicked.set(opt[0])
        drop = tk.OptionMenu(w1, clicked, *opt)
        drop.pack(pady= 15, padx= 20)
        bt1 = tk.Button(w1, text= "Download", command= lambda: download(link, clicked.get()))
        bt1.pack(pady=10)
    except:
        lb2.config(text= "Link is incorrect or not from youtube")
    
    return

def audiodownloader():
    link = ent1.get()
    ent1.delete(0, tk.END)
    try:
        yt = YouTube(link)
        videos = yt.streams.filter(only_audio= True, file_extension="mp4").first()
        lb2.config(text= f"Downloading {videos.title} please wait...")
        videos.download()
        lb2.config(text= "Download Successfull")
    except:
        lb2.config(text="Link is incorrect or not from youtube")
    return


root = tk.Tk()
root.title("Downloader")

color1 = "#09387f"
root.config(background=color1)

frame1 = tk.Frame(root, background=color1)
frame1.pack()

frame2 = tk.Frame(root, background=color1)
frame2.pack()

frame3 = tk.Frame(root, background=color1)
frame3.pack()

lb1 = tk.Label(frame1, text = "URL : ", background=color1, foreground="whitesmoke")
lb1.grid(row = 0, column = 0, padx = 10, pady= 20)

ent1 = tk.Entry(frame1, width= 50)
ent1.grid(row = 0, column = 1, padx= 10, pady= 30)

btn1 = tk.Button(frame2, text= "Video", width= 15, command=videodownloader)
btn1.grid(row = 0, column= 0, padx= 10, pady= 10)

btn2 = tk.Button(frame2, text= "Audio", width= 15, command=audiodownloader)
btn2.grid(row = 0, column= 1, padx= 10, pady= 10)


lb2 = tk.Label(frame3, text="Paste the url of the video/audio you want to download", foreground="whitesmoke", background= color1)
lb2.pack(pady=10)

root.mainloop()

