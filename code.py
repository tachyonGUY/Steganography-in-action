import cv2
import os
import sys
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# global variables to store the encoded password and message
encode_pass = ""
msg = ""


def decrypt_msg(password_entry, decode_window):
    global encode_pass, msg, img
    password = password_entry.get()
    print('Password entered to decode secret message:', password)
    decode_window.destroy()
    if password == encode_pass:
        x, y, z = 0, 0, 0
        secret_msg = ""
        for i in range(len(msg)):
            n = img[x, y, z]
            secret_msg += chr(n)
            z += 1
            if z == img.shape[2]:
                z = 0
                y += 1
                if y == img.shape[1]:
                    y = 0
                    x += 1

        messagebox.showinfo("Decoded Message", f"Secret message is: {secret_msg}")
    else:
        messagebox.showerror("Error", "Incorrect password")


def decode_frame():
    decode_window = Tk()
    decode_window.title("Decode Message")
    decode_window.geometry('300x200')
    decode_window.eval('tk::PlaceWindow . center')

    frame = Frame(decode_window, bg='white', width=300, borderwidth=3, relief='sunken')
    frame.pack(fill='both')

    l = Label(frame, text="Enter your password to decode message")
    l.pack(pady=10)

    password_entry = Entry(frame, show='*', relief='sunken', width=30)
    password_entry.pack(pady=10)

    b = Button(decode_window, fg='black', text='Decode', command=lambda: decrypt_msg(password_entry, decode_window))
    b.pack(side=BOTTOM, pady=10)


def encode_msg():
    global encode_pass, msg, img
    msg = inputtxt1.get(1.0, "end-1c")
    if len(msg) > img.shape[0] * img.shape[1] * img.shape[2]:
        messagebox.showerror("Error", "Message is too long")
        sys.exit("Exiting program due to error: Message is too long")
    else:
        encode_pass = inputtxt2.get(1.0, "end-1c")
        print('password to encode secret message:', encode_pass)
        x, y, z = 0, 0, 0
        '''height--->img.shape[0]
           width--->img.shape[1]
           channel--->img.shape[2]'''
        for i in range(len(msg)):
            img[x, y, z] = ord(msg[i])
            z += 1
            if z == img.shape[2]:  # Reset z and move to the next pixel
                z = 0
                y += 1
                if y == img.shape[1]:  # Reset y and move to the next row
                    y = 0
                    x += 1
        cv2.imwrite('encoded.jpg', img)
        os.startfile('encoded.jpg')  # Use os.startfile on Windows to open the image
        encode_window.destroy()
        decode_frame()
encode_window = Tk()
encode_window.title("Encode Message")
#ADJUSTING AND CENTERING ENCRYPT_WINDOW
win_width = 500
win_height = 550
screen_width = encode_window.winfo_screenwidth()
screen_height = encode_window.winfo_screenheight()
x = screen_width / 2 - win_width / 2
y = screen_height / 2 - win_height / 2
encode_window.geometry(f"{win_width}x{win_height}+{int(x)}+{int(y)}")
encode_window.maxsize(500, 550)
#frame-1....PROJECT TITLE
frame1 = Frame(encode_window, borderwidth=8, bg="white", relief=SUNKEN)
frame1.pack(side=TOP, fill="x")
l1 = Label(frame1, text="Steganography in Action", font="Helvetica 16 bold", fg="black", pady=22)
l1.pack()
#frame-2....TO PROJECT SELECTED IMAGE FILE
frame2 = Frame(encode_window, bg='Turquoise', height=300, width=500, borderwidth=3, relief='sunken')
frame2.pack(fill='both')
#frame-3....TO ENTER SECRET MESSAGE
frame3 = Frame(encode_window, bg='white', width=500, borderwidth=3, relief='sunken')
frame3.pack(fill='both')
inputtxt1 = Text(frame3, height=2, width=500, relief='sunken')
inputtxt1.pack()
l2 = Label(frame3, text="Enter your message here")
l2.pack()
#frame-4....TO ENTER PASSWORD
frame4 = Frame(encode_window, bg='white', width=500, borderwidth=3, relief='sunken')
frame4.pack(fill='both')
inputtxt2 = Text(frame4, height=2, width=500, relief='sunken')
inputtxt2.pack()
l3 = Label(frame4, text="Enter your password here")
l3.pack()
b1 = Button(encode_window, fg='black', text='Encode', command=encode_msg)
b1.pack(side=BOTTOM)

'''OPENING IMAGE
ASSIGN UR CHOSEN FILE PATH TO 'filepath' VARIABLE'''
filepath = 'test.png'
img = cv2.imread(filepath)
blue, green, red = cv2.split(img)

'''here i done resizing of image to fit in Frame-2 
so i took a separate img_for_display so that img variable RGB matrix wouldn't get affected'''
img_for_display = cv2.merge((red, green, blue))
imgResize = cv2.resize(img_for_display, (500, 300))
im = Image.fromarray(imgResize)
imgtk = ImageTk.PhotoImage(image=im)
Label(frame2, image=imgtk).pack()

encode_window.mainloop()
