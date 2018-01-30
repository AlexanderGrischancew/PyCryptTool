# Zweck:   RSA Crypt Tool
# Autor:   Alexander Grischancew
# Version: 1.1
# Datum:   23.10.2015
# Lizenz:  GNU


# Imports-----------------------
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import sys

# from Decrypt import *
# from Encrypt import *
# ------------------------------


# Erstellen des GUI: fenster
fenster = Tk()
fenster.title("ACryptTool")
fenster.geometry("800x800")

headLabel = Label(fenster, text="PYCRYPTOOL: RSA EN- AND DE-CRYPTER", fg="black", bg="red",
                  font="Verdana 16 bold").place(x=20, y=20)


# Funktionen fenster (root)

def Encrypt(TextType, Entry_Text, Entry_Ergebnis, e, N, d, TextType_Ergebnis, Schlüssel, action):
    Text = Entry_Text.get("1.0", END)
    TextType = TextType.get()

    if N == "" and d == "" and e == "":
        messagebox.showinfo("INFO", "Kein Schlüssel gewählt")
        return

    if N == "":
        messagebox.showinfo("INFO", "Kein N gewählt")
        return

    if e == "" and d == "":
        messagebox.showinfo("INFO", "Kein e und d gewählt")
        return

    Key = Schlüssel.get()

    if Key == 2:
        if d == "":
            messagebox.showinfo("INFO", "Kein d gewählt, keine Verschlüsselung mit Privatem Schlüssel möglich!")
            return
        e = d

    if Key == 1 and e == "":
        messagebox.showinfo("INFO", "Kein e gewählt, keine Verschlüsselung mit Öffentlichem Schlüssel möglich!")
        return

    Entry_Ergebnis.configure(state="normal")
    Entry_Ergebnis.delete("1.0", END)

    if TextType == 1:
        TextList = list(Text)
        while "\n" in TextList:
            TextList.remove("\n")
        decTextList = list()
        for char in TextList:
            decChar = ord(char)
            decTextList.append(decChar)

    elif TextType == 3:
        decTextList = list()
        TextList = Text.split(" ")
        for char in TextList:
            decChar = int(char, 16)
            decTextList.append(decChar)


    elif TextType == 2:
        decTextList = Text.split()

    newDecCharsList = list()
    for decChars in decTextList:
        newDecChar = int(decChars) ** int(e) % int(N)
        newDecCharsList.append(newDecChar)

    TextTypeErgebnis = TextType_Ergebnis.get()

    # if action == "D":
    # sep = ""
    # else:
    # sep = " "

    if TextTypeErgebnis == 1:
        newCharList = list()
        for decChar in newDecCharsList:
            char = chr(decChar)
            # if char == "\x8d":
            # char = "#?"
            newCharList.append(char)
        # print(newCharList)
        newText = "".join(str(newChars) for newChars in newCharList)
        Entry_Ergebnis.insert(END, newText)
        Entry_Ergebnis.configure(state="disabled")

    elif TextTypeErgebnis == 2:
        newDecText = " ".join(str(newDecChars) for newDecChars in newDecCharsList)
        Entry_Ergebnis.insert(END, newDecText)
        Entry_Ergebnis.configure(state="disabled")

    elif TextTypeErgebnis == 3:
        newHexCharList = list()
        for decChar in newDecCharsList:
            hexChar = hex(decChar)
            newHexCharList.append(hexChar)
        newHexText = " ".join(str(newHexChars) for newHexChars in newHexCharList)
        Entry_Ergebnis.insert(END, newHexText)
        Entry_Ergebnis.configure(state="disabled")


def Decrypt():
    pass


def close(fenster):
    fenster.destroy()
    sys.exit()


def putInKey(Entry_e_Main, Entry_d_Main, Entry_N_Main):
    # Erstellen Popup3
    popup3 = Tk()
    popup3.title("Schlüssel Wählen")
    popup3.geometry("270x100")

    def EnterPKey(Entry_e, Entry_d, Entry_N):
        # Erstellen Popup4
        popup3.destroy()
        popup4 = Tk()
        popup4.title("Privaten Schlüssel Eingeben")
        popup4.geometry("200x250")
        popup4.attributes('-topmost', 1)

        def Finish(e, d, N, Entry_e_Main, Entry_d_Main, Entry_N_Main):  # fügt alles in root-fenster ein

            e = e.get()
            d = d.get()
            N = N.get()

            try:
                int(N)
                int(d)
            except:
                messagebox.showerror("ERROR", "Kein gültiges N oder d gewählt")
                return

            Entry_e_Main.configure(state="normal")
            Entry_e_Main.delete("0", END)
            Entry_e_Main.insert(0, str(e))
            Entry_e.configure(state="disabled")

            Entry_d_Main.configure(state="normal")
            Entry_d_Main.delete("0", END)
            Entry_d_Main.insert(0, str(d))
            Entry_d.configure(state="disabled")

            Entry_N_Main.configure(state="normal")
            Entry_N_Main.delete("0", END)
            Entry_N_Main.insert(0, str(N))
            Entry_N.configure(state="disabled")

            popup4.destroy()

        # Labels + buttons poup4
        Label_e_4_op = Label(popup4, text="e ist optional")
        Label_e_4_op.place(x=60, y=20)
        Label_e_4 = Label(popup4, text="e:")
        Label_e_4.place(x=40, y=40)
        Entry_e_4 = Entry(popup4, width=15)
        Entry_e_4.place(x=60, y=40)

        Label_d_4 = Label(popup4, text="d:")
        Label_d_4.place(x=40, y=60)
        Entry_d_4 = Entry(popup4, width=15)
        Entry_d_4.place(x=60, y=60)

        Label_N_4 = Label(popup4, text="N:")
        Label_N_4.place(x=40, y=80)
        Entry_N_4 = Entry(popup4, width=15)
        Entry_N_4.place(x=60, y=80)

        knopfFinish = Button(popup4, text="Finish", width=10,
                             command=lambda: Finish(Entry_e_4, Entry_d_4, Entry_N_4, Entry_e_Main, Entry_d_Main,
                                                    Entry_N_Main))
        knopfFinish.place(x=60, y=120)

        knopfCancel = Button(popup4, text="Abbrechen", width=10, height=1, command=popup4.destroy)
        knopfCancel.place(x=60, y=150)

    def EnterPuKey(Entry_e_Main, Entry_d_Main, Entry_N_Main):
        # Erstellen Popup5
        popup3.destroy()
        popup5 = Tk()
        popup5.title("Öffentlichen Schlüssel Eingeben")
        popup5.geometry("200x250")
        popup5.attributes('-topmost', 1)

        def Finish(e, N, Entry_e_Main, Entry_N_Main):  # fügt alles in root-fenster ein

            e = e.get()
            N = N.get()

            try:
                int(e)
                int(N)
            except:
                messagebox.showerror("ERROR", "Kein gültiges e oder kein gültiges N gewählt")
                return

            if int(N) <= 256:
                messagebox.showeinfo("INFO", "N muss größer als 256 sein")
                return

            Entry_e_Main.configure(state="normal")
            Entry_e_Main.delete("0", END)
            Entry_e_Main.insert(0, str(e))
            Entry_e.configure(state="disabled")

            Entry_N_Main.configure(state="normal")
            Entry_N_Main.delete("0", END)
            Entry_N_Main.insert(0, str(N))
            Entry_N.configure(state="disabled")

            popup5.destroy()

        Label_e_5 = Label(popup5, text="e:")
        Label_e_5.place(x=40, y=40)
        Entry_e_5 = Entry(popup5, width=15)
        Entry_e_5.place(x=60, y=40)

        Label_d_5 = Label(popup5, text="d:", state="disable")
        Label_d_5.place(x=40, y=60)
        Entry_d_5 = Entry(popup5, width=15, state="disable")
        Entry_d_5.place(x=60, y=60)

        Label_N_5 = Label(popup5, text="N:")
        Label_N_5.place(x=40, y=80)
        Entry_N_5 = Entry(popup5, width=15)
        Entry_N_5.place(x=60, y=80)

        # Buttons popup5
        knopfFinish = Button(popup5, text="Finish", width=10,
                             command=lambda: Finish(Entry_e_5, Entry_N_5, Entry_e_Main, Entry_N_Main))
        knopfFinish.place(x=60, y=120)

        knopfCancel = Button(popup5, text="Abbrechen", width=10, height=1, command=popup5.destroy)
        knopfCancel.place(x=60, y=150)

    # Buttons Popup3
    knopfNewPKey = Button(popup3, text="Privater Schlüssel",
                          command=lambda: EnterPKey(Entry_e_Main, Entry_d_Main, Entry_N_Main))
    knopfNewPKey.place(x=20, y=20)

    knopfNewPuKey = Button(popup3, text="Öffentlicher Schlüssel",
                           command=lambda: EnterPuKey(Entry_e_Main, Entry_d_Main, Entry_N_Main))
    knopfNewPuKey.place(x=135, y=20)

    knopfCancel = Button(popup3, text="Abbrechen", width=10, height=1, command=popup3.destroy)
    knopfCancel.place(x=90, y=60)


def generateKey(Entry_e, Entry_d, Entry_N):  # Öffnet Auswahlfenster
    # Erstellen Popup1
    popup1 = Tk()
    popup1.title("Schlüssel Generieren")
    popup1.geometry("270x100")

    # Funktionen popup1
    def GenerateNewKey(Entry_e_Main, Entry_d_Main, Entry_N_Main):  # Öfnet dialog um neuen Schlüssel zu erstellen
        popup1.destroy()

        # ---------------------------------------------------------------------------------------POPUP2-------------------------------------------------------------------------------
        # Erstellen Popup2
        popup2 = Tk()
        popup2.title("Schlüssel Generieren")
        popup2.geometry("350x400")
        popup2.attributes('-topmost', 1)

        # -------------------Primzahlen--------------------------------------------------------------------------------------------
        primZ = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
                 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
                 227,
                 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
                 349,
                 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
                 467,
                 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
                 613,
                 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
                 751,
                 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883,
                 887,
                 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013]

        # -------------------------------------------------------------------------------------------------------------------------

        # Funktionen Popup2
        def GenerateN(Entry_N, Entry_phiN, popup2, knopfGenerateD):  # Errechnet N und phiN aus q und p
            varQ = variableq.get()
            varP = variablep.get()

            if varQ == "" or varP == "":
                messagebox.showerror("ERROR", "Kein q oder kein p gewählt")
                return
            elif varQ == varP:
                messagebox.showinfo("INFO", "p und q dürfen nicht gleich sein")
                return

            varQ = int(varQ)
            varP = int(varP)
            N = varQ * varP
            global phiN
            phiN = (varQ - 1) * (varP - 1)

            Entry_N.configure(state="normal")
            Entry_N.delete("0", END)
            Entry_N.insert(0, str(N))
            # Entry_N.update_idletasks()

            Entry_phiN.configure(state="normal")
            Entry_phiN.delete("0", END)
            Entry_phiN.insert(0, str(phiN))

            knopfGenerateD.config(state="normal")

            getGGTs(phiN, popup2)

        def getGGTs(phiN, popup2):  # errechnet alle e
            ggts = list()
            for e in range(0, phiN):
                save_e = e
                phiNtemp = phiN
                while phiNtemp > 0:
                    Rest = e % phiNtemp
                    e = phiNtemp
                    phiNtemp = Rest

                if e == 1 and save_e != 1:
                    ggts.append(save_e)

            global variablee
            variablee = StringVar(popup2)
            variablee.set("")  # default value

            global Menu_e
            Menu_e.destroy()
            Menu_e = OptionMenu(popup2, variablee, *ggts)
            Menu_e.place(x=60, y=130)

        def extendedGcd(a, b, Entry_d, N, knopfFinish, knopfSave, Label_PRK2, Label_PK2):  # errechnet d
            if a == "":
                messagebox.showerror("ERROR", "Kein e gewählt")
                # tkinter.Toplevel(popup2)
                return
            a = int(a)
            a_save = a

            c = b
            u = 1
            s = 0
            while b > 0:
                q = a // b
                a, b = b, a - q * b
                u, s = s, u - q * s
            if u < 0:
                u = u + c

            Entry_d.configure(state="normal")
            Entry_d.delete("0", END)
            Entry_d.insert(0, str(u))

            Label_PK2.configure(text="(" + str(a_save) + "," + str(N) + ")")

            Label_PRK2.configure(text="(" + str(u) + "," + str(N) + ")")

            knopfFinish.config(state="normal")
            knopfSave.config(state="normal")

        def Finish(e, d, N, Entry_e, Entry_d, Entry_N):  # fügt alles in root-fenster ein

            Entry_e.configure(state="normal")
            Entry_e_Main.delete("0", END)
            Entry_e.insert(0, str(e))
            Entry_e.configure(state="disabled")

            Entry_d.configure(state="normal")
            Entry_d_Main.delete("0", END)
            Entry_d.insert(0, str(d))
            Entry_d.configure(state="disabled")

            Entry_N.configure(state="normal")
            Entry_N_Main.delete("0", END)
            Entry_N.insert(0, str(N))
            Entry_N.configure(state="disabled")

            popup2.destroy()

        def save(e, d, N):
            saveString = str(e) + "," + str(d) + "," + str(N)
            SaveFile = filedialog.asksaveasfilename(filetypes=[('text files', '.txt'), ('all files', '.*')],
                                                    defaultextension='.txt')
            File = open(SaveFile, "w")
            File.write(str(saveString))
            File.close()

        # Entrys + Labels Popup2
        variablep = StringVar(popup2)
        variablep.set("")  # default value

        variableq = StringVar(popup2)
        variableq.set("")  # default value

        variablee1 = StringVar(popup2)
        variablee1.set("")  # default value

        Label_p = Label(popup2, text="p:")
        Label_p.place(x=40, y=25)
        Entry_p = OptionMenu(popup2, variablep, *primZ)
        Entry_p.place(x=60, y=20)

        Label_p = Label(popup2, text="q:")
        Label_p.place(x=140, y=25)
        Entry_q = OptionMenu(popup2, variableq, *primZ)
        Entry_q.place(x=160, y=20)

        Label_N = Label(popup2, text="N:")
        Label_N.place(x=40, y=67)
        Entry_N = Entry(popup2, state="disable", width=10)
        Entry_N.place(x=60, y=70)

        Label_phiN = Label(popup2, text="phi(N):")
        Label_phiN.place(x=140, y=67)
        Entry_phiN = Entry(popup2, state="disable", width=10)
        Entry_phiN.place(x=185, y=70)

        global Menu_e
        Label_e = Label(popup2, text="e:")
        Label_e.place(x=40, y=135)
        Menu_e = OptionMenu(popup2, variablee1, "")
        Menu_e.place(x=60, y=130)

        Label_d = Label(popup2, text="d:")
        Label_d.place(x=40, y=188)
        Entry_d = Entry(popup2, state="disable", width=10)
        Entry_d.place(x=60, y=190)

        Label_PK = Label(popup2, text="Öffentlicher Schlüssel:")
        Label_PK.place(x=40, y=310)

        Label_PRK = Label(popup2, text="Privater Schlüssel:")
        Label_PRK.place(x=40, y=330)

        Label_PK2 = Label(popup2, text="")
        Label_PK2.place(x=160, y=310)

        Label_PRK2 = Label(popup2, text="")
        Label_PRK2.place(x=160, y=330)

        # Buttons Popup2
        knopfGenerateN = Button(popup2, text="Berechnen",
                                command=lambda: GenerateN(Entry_N, Entry_phiN, popup2, knopfGenerateD))
        knopfGenerateN.place(x=260, y=66)

        knopfGenerateD = Button(popup2, text="Berechnen", state="disabled",
                                command=lambda: extendedGcd(variablee.get(), phiN, Entry_d, Entry_N.get(), knopfFinish,
                                                            knopfSave, Label_PRK2, Label_PK2))
        knopfGenerateD.place(x=260, y=183)

        knopfFinish = Button(popup2, text="Finish", width=10, state="disabled",
                             command=lambda: Finish(variablee.get(), Entry_d.get(), Entry_N.get(), Entry_e_Main,
                                                    Entry_d_Main, Entry_N_Main))
        knopfFinish.place(x=40, y=270)

        knopfSave = Button(popup2, text="Save", width=10, state="disabled",
                           command=lambda: save(variablee.get(), Entry_d.get(), Entry_N.get()))
        knopfSave.place(x=140, y=270)

        knopfCancel = Button(popup2, text="Abbrechen", width=10, height=1, command=popup2.destroy)
        knopfCancel.place(x=240, y=270)

        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Funktionen Popup1
    def LoadKey(Entry_e, Entry_d, Entry_N):
        LoadFile = filedialog.askopenfilename(filetypes=[('text files', '.txt'), ('all files', '.*')])
        File = open(LoadFile, "r")
        Line = File.readline()
        KeysList = Line.split(",")
        e = KeysList[0]
        d = KeysList[1]
        N = KeysList[2]

        Entry_e.configure(state="normal")
        Entry_e.delete("0", END)
        Entry_e.insert(0, str(e))
        Entry_e.configure(state="disabled")

        Entry_d.configure(state="normal")
        Entry_d.delete("0", END)
        Entry_d.insert(0, str(d))
        Entry_d.configure(state="disabled")

        Entry_N.configure(state="normal")
        Entry_N.delete("0", END)
        Entry_N.insert(0, str(N))
        Entry_N.configure(state="disabled")

        popup1.destroy()

    # Buttons Popup1
    knopfNewKey = Button(popup1, text="Neuer Schlüssel", command=lambda: GenerateNewKey(Entry_e, Entry_d, Entry_N))
    knopfNewKey.place(x=20, y=20)

    knopfNewKey = Button(popup1, text="Bestehender Schlüssel", command=lambda: LoadKey(Entry_e, Entry_d, Entry_N))
    knopfNewKey.place(x=120, y=20)

    knopfCancel = Button(popup1, text="Abbrechen", width=10, height=1, command=popup1.destroy)
    knopfCancel.place(x=90, y=60)


# Entry Fenster
# ---------Schlüssel Block---------------
keyimage = tkinter.PhotoImage(file="key.gif")

Label_e_main = Label(fenster, text="e:")
Label_e_main.place(x=80, y=70)
Entry_e = Entry(fenster, state="disable")
Entry_e.place(x=100, y=70)
Label_d_main = Label(fenster, text="d:")
Label_d_main.place(x=230, y=70)
Entry_d = Entry(fenster, state="disable")
Entry_d.place(x=250, y=70)
Label_N_main = Label(fenster, text="N:")
Label_N_main.place(x=380, y=70)
Entry_N = Entry(fenster, state="disable")
Entry_N.place(x=400, y=70)

knopfGenerateKey = Button(fenster, text="Schlüssel generieren", image=keyimage, compound="right", borderwidth=3,
                          command=lambda: generateKey(Entry_e, Entry_d, Entry_N))
knopfGenerateKey.place(x=550, y=50)

knopfGenerateKey = Button(fenster, text="Schlüssel eingeben  ", image=keyimage, compound="right", borderwidth=3,
                          command=lambda: putInKey(Entry_e, Entry_d, Entry_N))
knopfGenerateKey.place(x=550, y=80)
# ---------------------------------------


# ----------I/O Block---------------------
# -------------------------------------EINGABE--------------------------------------------------------------------------------------------
TextType = IntVar()
Entry_Text_Frame = Frame(fenster)

Entry_Text_Scrollbar = Scrollbar(Entry_Text_Frame)
Entry_Text = Text(Entry_Text_Frame, height=4, width=50)
Entry_Text.pack(side=LEFT)
Entry_Text_Scrollbar.pack(side=RIGHT, fill=Y)
Entry_Text_Scrollbar.config(command=Entry_Text.yview)
Entry_Text.configure(yscrollcommand=Entry_Text_Scrollbar.set)
Entry_Text_Frame.place(x=100, y=120)

Label_N_main = Label(fenster, text="Plaintext:")
Label_N_main.place(x=40, y=140)

Radiobutton_Char = Radiobutton(fenster, text="Char", variable=TextType, value=1, indicatoron=0, width=7)
Radiobutton_Char.select()
Radiobutton_Char.place(x=550, y=115)

Radiobutton_Dec = Radiobutton(fenster, text="Dec", variable=TextType, value=2, indicatoron=0, width=7).place(x=550,
                                                                                                             y=141)
Radiobutton_Hex = Radiobutton(fenster, text="Hex", variable=TextType, value=3, indicatoron=0, width=7).place(x=550,
                                                                                                             y=167)

# ------------------------------------AUSGABE-----------------------------------------------------------------------------------------
# Ergebiss = Ergebnis (copy-pase fehler) lol
Entry_Ergebniss_Frame = Frame(fenster)
Entry_Ergebniss_Scrollbar = Scrollbar(Entry_Ergebniss_Frame)
Entry_Ergebniss = Text(Entry_Ergebniss_Frame, height=4, width=50, state="disabled")
Entry_Ergebniss.pack(side=LEFT)
Entry_Ergebniss_Scrollbar.pack(side=RIGHT, fill=Y)
Entry_Ergebniss_Scrollbar.config(command=Entry_Ergebniss.yview)
Entry_Ergebniss.configure(yscrollcommand=Entry_Ergebniss_Scrollbar.set)
Entry_Ergebniss_Frame.place(x=100, y=220)

Label_N_main = Label(fenster, text="ChifreText:")
Label_N_main.place(x=36, y=240)

TextType_Ergebnis = IntVar()

Radiobutton_Char_Ergebnis = Radiobutton(fenster, text="Char", variable=TextType_Ergebnis, value=1, indicatoron=0,
                                        width=7).place(x=550, y=215)

Radiobutton_Dec_Ergebnis = Radiobutton(fenster, text="Dec", variable=TextType_Ergebnis, value=2, indicatoron=0, width=7)
Radiobutton_Dec_Ergebnis.select()
Radiobutton_Dec_Ergebnis.place(x=550, y=241)

Radiobutton_Hex_Ergebnis = Radiobutton(fenster, text="Hex", variable=TextType_Ergebnis, value=3, indicatoron=0,
                                       width=7).place(x=550, y=267)

# Label_Unicode = Label(fenster,text="Unbekannter Unicode: '#?' ")
# Label_Unicode.place(x=210,y=300)
# ------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------I/O block ENDE-----------------------------------------------------------------------------------------------------


# Select Mode

schlossimageZu = tkinter.PhotoImage(file="SchlossZu.gif")
schlossimageOffen = tkinter.PhotoImage(file="SchlossOffen.gif")

knopfEncrypt = Button(fenster, text="Verschlüsseln", compound="right", width=130, image=schlossimageZu, borderwidth=3,
                      command=lambda: Encrypt(TextType, Entry_Text, Entry_Ergebniss, Entry_e.get(), Entry_N.get(),
                                              Entry_d.get(), TextType_Ergebnis, Schlüssel, "E"))
knopfEncrypt.place(x=100, y=345)

Schlüssel = IntVar()

Radiobutton_PuKey = Radiobutton(fenster, text="Öffentlicher Schlüssel", variable=Schlüssel, value=1)
Radiobutton_PuKey.select()
Radiobutton_PuKey.place(x=100, y=375)

Radiobutton_PKey = Radiobutton(fenster, text="Privater Schlüssel", variable=Schlüssel, value=2).place(x=100, y=395)

knopfDecrypt = Button(fenster, text="Entschlüsseln", compound="right", image=schlossimageOffen, width=130,
                      borderwidth=3,
                      command=lambda: Encrypt(TextType, Entry_Text, Entry_Ergebniss, Entry_d.get(), Entry_N.get(),
                                              Entry_e.get(), TextType_Ergebnis, Schlüssel, "D"))
knopfDecrypt.place(x=370, y=345)

SchlüsselDecrypt = IntVar()

Radiobutton_PuKey_Decrypt = Radiobutton(fenster, text="Öffentlicher Schlüssel", variable=SchlüsselDecrypt,
                                        value=1).place(x=370, y=375)

Radiobutton_PKey_Decrypt = Radiobutton(fenster, text="Privater Schlüssel", variable=SchlüsselDecrypt, value=2)
Radiobutton_PKey_Decrypt.select()
Radiobutton_PKey_Decrypt.place(x=370, y=395)

# --------------------------------BOTTOM-------------------------------------------------------------------------------------------------------

knopfEnd = Button(fenster, text="Beenden", width=15, height=1, command=lambda: close(fenster))
knopfEnd.place(x=320, y=750)

bottemLabel = Label(fenster, text="© Alexander Grischancew", fg="red", font="Verdana 7 bold").place(x=10, y=780)
bottemLabelLicence = Label(fenster, text="GNU General Public License", fg="red", font="Verdana 7 bold").place(x=650,
                                                                                                              y=780)

fenster.mainloop()
