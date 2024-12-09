from tkinter import messagebox, ttk
from tkinter import *
import tkinter as tk
import time
from tkinter.ttk import Treeview

import jdatetime
import math
from dal.repository import Repository
from time import strftime
from persiantools.jdatetime import JalaliDate
import random
from collections import Counter


jalali_date_now = JalaliDate.today()
date = str(jalali_date_now).replace("-", "/")
Time = strftime("%X")


class App(Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.Register()
        self.Menu()

    # -------------------------------------------- Menu Top ---------------------------------------

    def Menu(self):
        self.Setting = Menu(self.screen)

        self.mnu = Menu(self.Setting, tearoff=0, background="black")
        self.mnu.add_separator(background="black")
        self.mnu.add_command(label="User Login", command=self.Login, foreground="white")
        self.mnu.add_separator(background="black")
        self.mnu.add_command(label="User Register", command=self.Register, foreground="white")
        self.mnu.add_separator(background="black")
        self.mnu.add_command(label="Login Dr", foreground="white", command=self.LoginDr)
        self.mnu.add_separator(background="black")
        self.mnu.add_separator(background="black")
        self.mnu.add_command(label="Exit", command=self.Close, foreground="white")

        self.Setting.add_cascade(label="Setting", menu=self.mnu)

        self.screen.config(menu=self.Setting)

    def Close(self):
        self.screen.destroy()

    # -------------------------------------------- Sabt Aghsat ---------------------------------------

    def aghsat(self):
        num = []
        for i in range(1, 25):
            num.append(i)
        return num

    def sabtaghsat(self):
        self.frminfoaghsat.place_forget()
        user = Repository()
        result = user.Exist("users", self.Phone.get())
        for item in result:
            self.frmsabtaghsat = Frame(self.frmscreenuser, width=1300, height=800)

            self.mtnuser = Label(self.frmsabtaghsat)
            self.mtnuser.configure(text="User", fg="black", font="Arial 20 bold")
            self.mtnuser.place(x=680, y=40)

            Name = StringVar()
            self.txtname = Entry(self.frmsabtaghsat)
            self.txtname.configure(bg="white", fg="black", bd=3, justify="center", textvariable=Name, state=DISABLED)
            self.txtname.place(x=480, y=90)
            Name.set(f"{item[1]} {item[2]}")

            self.lblname = Label(self.frmsabtaghsat)
            self.lblname.configure(text="UserName", fg="black")
            self.lblname.place(x=400, y=90)

            Phone = StringVar()
            self.txtPhone = Entry(self.frmsabtaghsat)
            self.txtPhone.configure(bg="white", fg="black", bd=3, justify="center", textvariable=Phone, state=DISABLED)
            Phone.set(item[3])
            self.txtPhone.place(x=830, y=90)

            self.lblPhone = Label(self.frmsabtaghsat)
            self.lblPhone.configure(text="Phone", fg="black")
            self.lblPhone.place(x=750, y=90)

            self.txtserial = Entry(self.frmsabtaghsat)
            self.txtserial.configure(bg="white", fg="black", bd=3, justify="center")
            self.txtserial.place(x=480, y=140)

            self.lblserial = Label(self.frmsabtaghsat)
            self.lblserial.configure(text="serial", fg="black")
            self.lblserial.place(x=400, y=140)

            self.txtmodel = Entry(self.frmsabtaghsat)
            self.txtmodel.configure(bg="white", fg="black", bd=3, justify="center")
            self.txtmodel.place(x=830, y=140)

            self.lblmodel = Label(self.frmsabtaghsat)
            self.lblmodel.configure(text="model", fg="black")
            self.lblmodel.place(x=750, y=140)

            self.mtnaghsat = Label(self.frmsabtaghsat)
            self.mtnaghsat.configure(text="aghsat", fg="black", font="Arial 20 bold")
            self.mtnaghsat.place(x=680, y=220)

            self.txtstartgest = Entry(self.frmsabtaghsat)
            self.txtstartgest.configure(bg="white", fg="black", bd=3, justify="center")
            self.txtstartgest.place(x=480, y=290)

            self.lblstartgest = Label(self.frmsabtaghsat)
            self.lblstartgest.configure(text="Start gest", fg="black")
            self.lblstartgest.place(x=350, y=290)

            self.txtmablaghesmi = Entry(self.frmsabtaghsat)
            self.txtmablaghesmi.configure(bg="white", fg="black", bd=3, justify="center")
            self.txtmablaghesmi.bind("<KeyRelease>", self.format_txtmablaghesmi)
            self.txtmablaghesmi.place(x=830, y=290)

            self.lblmablaghesmi = Label(self.frmsabtaghsat)
            self.lblmablaghesmi.configure(text="mablagh esmi", fg="black")
            self.lblmablaghesmi.place(x=730, y=290)

            self.darsad = ttk.Combobox(self.frmsabtaghsat, background="white", foreground="black", justify="center",
                                        state="readonly", width=19)
            self.darsad['values'] = self.aghsat()
            self.darsad.set(4)
            self.darsad.place(x=650, y=350)


            self.txtgest = ttk.Combobox(self.frmsabtaghsat, background="white", foreground="black", justify="center",
                                        state="readonly", width=19)
            self.txtgest.set(1)
            self.txtgest['values'] = self.aghsat()
            self.txtgest.place(x=650, y=410)

            self.lblaghsat = Label(self.frmsabtaghsat)
            self.lblaghsat.configure(text="aghsat", fg="black")
            self.lblaghsat.place(x=580, y=410)

            self.talachek = IntVar()
            self.tala = ttk.Radiobutton(self.frmsabtaghsat, text='tala', variable=self.talachek, value=1)
            self.tala.bind("<Button-1>", self.talaentry)
            self.tala.place(x=770, y=450)

            self.chek = ttk.Radiobutton(self.frmsabtaghsat, text='chek', variable=self.talachek, value=2)
            self.chek.bind("<Button-1>", self.chekentry)
            self.chek.place(x=650, y=450)

            self.btnadd = Button(self.frmsabtaghsat)
            self.btnadd.configure(text="Register", bg="green", fg="black", bd=5, command=self.Onclicksabtaghsat)
            self.btnadd.place(x=690, y=600)

            self.lbldatee = Label(self.frmsabtaghsat, font="arial 12 bold")
            self.update_timee()
            self.lbldatee.place(x=630, y=10)

            self.frmsabtaghsat.place(x=0, y=0)

            self.start_date_button = Button(self.frmsabtaghsat, text=">",
                                            command=self.open_start_date_calendar, bg="#4CAF50", fg="white")
            self.start_date_button.place(x=658, y=290)

            # Initialize calendar window as None
            self.calendar_window = None

    def chekentry(self, e):
        try:
            self.lblserialchek = Label(self.frmsabtaghsat, text="serial chek", fg="black")
            self.lblserialchek.place(x=550, y=500)
            self.lblmablaghlchek = Label(self.frmsabtaghsat, text="mablagh chek", fg="black")
            self.lblmablaghlchek.place(x=550, y=550)
            self.serialchek = Entry(self.frmsabtaghsat, justify="center")
            self.serialchek.place(x=650, y=500)
            self.mablaghchek = Entry(self.frmsabtaghsat, justify="center")
            self.mablaghchek.bind("<KeyRelease>", self.format_mablaghchek)
            self.mablaghchek.place(x=650, y=550)
            self.typegold.place_forget()
            self.grams.place_forget()
            self.lblgrams.place_forget()
            self.lbltypetala.place_forget()
        except AttributeError:
            pass
    def talaentry(self, e):
        try:
            self.lbltypetala = Label(self.frmsabtaghsat, text="type tala", fg="black")
            self.lbltypetala.place(x=550, y=500)
            self.lblgrams = Label(self.frmsabtaghsat, text="grams", fg="black")
            self.lblgrams.place(x=550, y=550)

            self.typegold = Entry(self.frmsabtaghsat, justify="center")
            self.typegold.place(x=650, y=500)
            self.grams = Entry(self.frmsabtaghsat, justify="center")
            self.grams.place(x=650, y=550)
            self.serialchek.place_forget()
            self.mablaghchek.place_forget()
            self.lblserialchek.place_forget()
            self.lblmablaghlchek.place_forget()

        except AttributeError:
            pass
    def format_txtmablaghesmi(self, e):
        self.textmablaghesmi = self.txtmablaghesmi.get()
        if self.textmablaghesmi.strip() != "":
            try:
                number = int(self.txtmablaghesmi.get().replace(",", ""))
                formatted = f"{number:,}"
                self.txtmablaghesmi.delete(0, tk.END)
                self.txtmablaghesmi.insert(0, formatted)
            except ValueError:
                pass

    def format_mablaghchek(self, e):
        self.textmablaghchek = self.mablaghchek.get()
        if self.textmablaghchek.strip() != "":
            try:
                number = int(self.mablaghchek.get().replace(",", ""))
                formatted = f"{number:,}"
                self.mablaghchek.delete(0, tk.END)
                self.mablaghchek.insert(0, formatted)
            except ValueError:
                pass

    def Onclicksabtaghsat(self):
        self.esmi = self.txtmablaghesmi.get().replace(",", "")
        if not self.txtserial.get().isdigit() or self.txtserial.get() == '' or len(self.txtserial.get()) != 15:
            messagebox.showerror("Error", "Fill in the serial part with a number")
            self.txtserial.focus()
        elif self.txtmodel.get() == '':
            messagebox.showerror("Error", "Fill in the model section")
            self.txtmodel.focus()
        elif self.txtstartgest.get() == '':
            messagebox.showerror("Error", "Fill in the startgest section")
            self.txtstartgest.focus()
        elif self.txtmablaghesmi.get() == '' or not self.esmi.isdigit():
            messagebox.showerror("Error", "Fill in the mablaghesmi part with a number")
            self.txtmablaghesmi.focus()
        elif self.talachek.get() == 0:
            messagebox.showerror("Error", "Fill in the gram part with a number")
        elif self.talachek.get() == 1 and self.grams.get() == '':
            messagebox.showerror("Error", "Fill in the gram part with a number")
        elif self.talachek.get() == 1 and self.typegold.get() == '':
            messagebox.showerror("Error", "Fill in the type gold part with a number")
            self.typegold.focus()
        elif self.talachek.get() == 2 and self.serialchek.get() == '':
            messagebox.showerror("Error", "Fill in the serial chek part with a number")
            self.serialchek.focus()
        elif self.talachek.get() == 2 and self.mablaghchek.get() == '':
            messagebox.showerror("Error", "Fill in the mablaghchek part with a number")
            self.mablaghchek.focus()
        else:
            try:
                self.sabtaghsatt()
                self.sabtaghsat()
            except Exception as e:
                print(e)

    def sabtaghsatt(self):
        if self.esmi.isdigit():
            a = (int(self.esmi) * int(self.darsad.get())) / 100

            karmozd = a * int(self.txtgest.get())
            karmozd2 = karmozd / int(self.txtgest.get())
            kamel = int(self.esmi) + karmozd
            mathc = kamel / int(self.txtgest.get())
            number = "{:,.0f}".format(mathc)
            karmozd1 = "{:,.0f}".format(karmozd2)
            kamel1 = "{:,.0f}".format(kamel)

            code = random.randint(1, 999999)
            a = self.txtgest.get()
            for i in range(int(a)):
                # محاسبه تاریخ قسط با اضافه کردن ماه‌ها
                b = self.txtstartgest.get()
                b = b.replace("/", "-")
                start_date_shamsi = jdatetime.date.fromisoformat(b)
                year = start_date_shamsi.year
                month = start_date_shamsi.month + i  # اضافه کردن ماه‌ها
                day = start_date_shamsi.day

                # اگر ماه از 12 بیشتر شد، سال را افزایش داده و ماه را به مقدار صحیح تبدیل می‌کنیم
                while month > 12:
                    month -= 12
                    year += 1

                # ایجاد تاریخ جدید با ماه‌های افزوده شده
                installment_date_shamsi = jdatetime.date(year, month, day)

                # تبدیل تاریخ شمسی به رشته
                installment_date_shamsi_str = f"{installment_date_shamsi.year}/{installment_date_shamsi.month:02d}/{installment_date_shamsi.day:02d}"
                aghsat = Repository()
                obj = code, self.txtname.get(), self.Phone.get(), number, karmozd1, kamel1, installment_date_shamsi_str, 'not paid', self.txtgest.get()
                aghsat.addghest("aghsat", obj)
            aghsat = Repository()
            obj1 = code, self.txtname.get(), self.Phone.get(), self.txtserial.get(), kamel1, self.txtmodel.get()
            aghsat.adddevice("device", obj1)
            if self.talachek.get() == 1:
                obj = (code, self.txtname.get(), self.txtPhone.get(), 'Tala', self.typegold.get(), self.grams.get())
                aghsat.addtype(obj)
            elif self.talachek.get() == 2:
                obj = (code, self.txtname.get(), self.txtPhone.get(), 'Check', self.serialchek.get(), self.mablaghchek.get())
                aghsat.addtype(obj)
    # -------------------------------------------- taghvim ---------------------------------------

    def open_start_date_calendar(self):
        """Open calendar window for selecting start date"""
        self.open_calendar_window(self.txtstartgest)

    def open_calendar_window(self, entry_widget):
        """Open calendar window to select year, month, and day"""
        if self.calendar_window is not None and self.calendar_window.winfo_exists():
            return

        # Create new top-level window for the calendar
        self.calendar_window = Toplevel(self.frmsabtaghsat)
        self.calendar_window.resizable(False, False)
        self.calendar_window.title("Select Date")
        self.calendar_window.geometry("%dx%d+%d+%d" % (400, 300, 700, 350))
        self.calendar_window.config(bg='#f2f2f2')

        # Smaller font and size for year combobox
        self.year_label = Label(self.calendar_window, text="Year", bg='#f2f2f2', font="Arial 8")
        self.year_label.grid(row=0, column=0)
        self.year_combobox = ttk.Combobox(self.calendar_window, state="readonly", width=15, font="Arial 8")
        self.year_combobox.grid(row=0, column=1)
        self.year_combobox['values'] = [str(year) for year in range(1400, 1501)]
        self.year_combobox.set(JalaliDate.today().year)

        # Smaller font and size for month combobox
        self.month_label = Label(self.calendar_window, text="Month", bg='#f2f2f2', font="Arial 8")
        self.month_label.grid(row=1, column=0)
        self.month_combobox = ttk.Combobox(self.calendar_window, state="readonly", width=15, font="Arial 8")
        self.month_combobox.grid(row=1, column=1)

        # ترکیب شماره و نام ماه‌ها
        self.month_mapping = {
            1: "Farvardin", 2: "Ordibehesht", 3: "Khordad",
            4: "Tir", 5: "Mordad", 6: "Shahrivar",
            7: "Mehr", 8: "Aban", 9: "Azar",
            10: "Dey", 11: "Bahman", 12: "Esfand"
        }
        self.month_combobox['values'] = [f"{num} {name}" for num, name in self.month_mapping.items()]
        self.month_combobox.set(f"{JalaliDate.today().month} {self.month_mapping[JalaliDate.today().month]}")

        # Smaller day entry
        self.day_label = Label(self.calendar_window, text="Day", bg='#f2f2f2', font="Arial 7")
        self.day_label.grid(row=2, column=0)
        self.day_entry = Entry(self.calendar_window, width=5, font="Arial 10")
        self.day_entry.grid(row=2, column=1)

        # Smaller Select button
        self.select_button = Button(self.calendar_window, text="Select", command=lambda: self.select_date(entry_widget),
                                    bg="#4CAF50", fg="white", font="Arial 10", bd=1)
        self.select_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Show Jalali calendar
        self.show_jalali_calendar()

        # Bind events to update days when year or month changes
        self.year_combobox.bind("<<ComboboxSelected>>", lambda event: self.show_jalali_calendar())
        self.month_combobox.bind("<<ComboboxSelected>>", lambda event: self.show_jalali_calendar())

    def show_jalali_calendar(self):
        """Show Jalali calendar and allow for selecting a date"""
        selected_year = int(self.year_combobox.get())
        selected_month = int(self.month_combobox.get().split()[0])

        # Remove only calendar day buttons
        for widget in self.calendar_window.grid_slaves():
            if widget.grid_info()["row"] >= 4:
                widget.grid_forget()

        # Frame for calendar days
        calendar_frame = Frame(self.calendar_window, bg='#f2f2f2')
        calendar_frame.grid(row=4, column=0, columnspan=2)

        # Smaller days of the week
        days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for i, day_name in enumerate(days_of_week):
            day_button = Button(calendar_frame, text=day_name, width=5, font="Arial 7", bg="#555555", fg="white")
            day_button.grid(row=0, column=i)

        # Show dates for the selected month and year
        self.show_dates(calendar_frame, selected_year, selected_month)

    def show_dates(self, calendar_frame, year, month):
        """Show the dates of the selected month in the calendar"""
        month_days = JalaliDate(year, month, 1).days_in_month(month, year)
        first_day_of_month = JalaliDate(year, month, 1).weekday()

        for i in range(month_days):
            row = (i + first_day_of_month) // 7 + 1
            col = (i + first_day_of_month) % 7
            day_button = Button(calendar_frame, text=str(i + 1), width=5, font="Arial 7",
                                command=lambda day=i + 1: self.select_day(day), bg="white", fg="#4c4c4c")
            day_button.grid(row=row, column=col, padx=2, pady=2)

    def select_day(self, day):
        """Select a day and update the day entry in the calendar window"""
        self.day_entry.delete(0, END)
        self.day_entry.insert(0, str(day))

    def select_date(self, entry_widget):
        """Save the selected date in the entry widget and close the calendar window"""
        year = self.year_combobox.get()
        month = self.month_combobox.get().split()[0]  # فقط شماره ماه را استخراج کن
        day = self.day_entry.get()

        try:
            jalali_date = JalaliDate(int(year), int(month), int(day))
            selected_date = jalali_date.strftime('%Y/%m/%d')

            entry_widget.delete(0, END)
            entry_widget.insert(0, selected_date)

            self.calendar_window.destroy()

        except ValueError:
            print("Invalid date entered.")

    def update_timee(self):
        current_time = time.strftime("%H:%M:%S")
        self.lbldatee.config(text=f"{date} - {current_time}")
        self.frmsabtaghsat.after(1000, self.update_timee)

    # -------------------------------------------- Menu right ---------------------------------------

    def clicksabtaghsat(self, e):
        self.sabtaghsat()

    def clickinfoaghsat(self, e):
        self.infoaghsat()

    # -------------------------------------------- info aghsat---------------------------------------

    def infoaghsat(self):
        user = Repository()
        result = user.Exist("users", self.Phone.get())
        self.frminfoaghsat = Frame(self.frmscreenuser, width=1300, height=800)
        self.textbox = tk.Text(self.frminfoaghsat, width=55, height=40, state="disabled")
        self.textbox.place(x=10, y=50)
        self.test()
        for item in result:
            self.textbox.config(state=NORMAL)

            self.lbldate = Label(self.frminfoaghsat, font="arial 12 bold")
            self.update_time()
            self.lbldate.place(x=20, y=20)

            self.textbox.insert(tk.END, f"\nDate Register : {item[4]} - Time Register {item[5]}")
            self.textbox.config(state=DISABLED)

        self.frminfoaghsat.place(x=0, y=0)

        self.id = StringVar()
        self.txtid = Entry(self.frminfoaghsat, textvariable=self.id)
        self.txtid.place_forget()

        self.code = StringVar()
        self.txtcode = Entry(self.frminfoaghsat, textvariable=self.code)
        self.txtcode.place_forget()

        self.paid = StringVar()
        self.txtpaid = Entry(self.frminfoaghsat, textvariable=self.paid)
        self.txtpaid.place_forget()

        self.btntasfie = Button(self.frminfoaghsat, text="payment", background="green", command=self.oneclickpymuont)
        self.btntasfie.place_forget()
        self.btndelete = Button(self.frminfoaghsat, text="Delete", background="red", command=self.oneclickdelete)
        self.btndelete.place_forget()
        self.btncancel = Button(self.frminfoaghsat, text="Cancel", command=self.onclickcancel)
        self.btncancel.place_forget()
        self.btnnotasfie = Button(self.frminfoaghsat, text="Cpayment", background="red", command=self.oneclickcpymuont)
        self.btnnotasfie.place_forget()

        s = ['row', 'code', 'name', 'phone', 'price', 'karmozd', 'kamel', 'time', 'status', 'num']

        self.tableprnashode = ttk.Treeview(self.frminfoaghsat, columns=s, show='headings', height=15)

        self.tableprnashode.column('row', width=0, stretch=tk.NO)
        self.tableprnashode.column('code', width=100, anchor='center')
        self.tableprnashode.column('name', width=150, anchor='center')
        self.tableprnashode.column('phone', width=150, anchor='center')
        self.tableprnashode.column('price', width=200, anchor='center')
        self.tableprnashode.column('time', width=100, anchor='center')
        self.tableprnashode.column('status', width=100, anchor='center')
        self.tableprnashode.column('karmozd', width=0, stretch=tk.NO)
        self.tableprnashode.column('kamel', width=0, stretch=tk.NO)
        self.tableprnashode.column('num', width=0, stretch=tk.NO)

        self.tableprnashode.heading('code', text=s[1], anchor='center')
        self.tableprnashode.heading('name', text=s[2], anchor='center')
        self.tableprnashode.heading('phone', text=s[3], anchor='center')
        self.tableprnashode.heading('price', text=s[4], anchor='center')
        self.tableprnashode.heading('time', text=s[7], anchor='center')
        self.tableprnashode.heading('status', text=s[8], anchor='center')

        self.tableprnashode.bind('<Button-1>', self.selectprnashode)

        self.tableprnashode.place(x=480, y=49)
        self.cleartabaleprnashode()
        self.inserttableprnashode()

        self.tableprshode = ttk.Treeview(self.frminfoaghsat, columns=s, show='headings', height=15)

        self.tableprshode.column('row', width=0, stretch=tk.NO)
        self.tableprshode.column('code', width=100, anchor='center')
        self.tableprshode.column('name', width=150, anchor='center')
        self.tableprshode.column('phone', width=150, anchor='center')
        self.tableprshode.column('price', width=200, anchor='center')
        self.tableprshode.column('time', width=100, anchor='center')
        self.tableprshode.column('status', width=100, anchor='center')
        self.tableprshode.column('karmozd', width=0, stretch=tk.NO)
        self.tableprshode.column('kamel', width=0, stretch=tk.NO)
        self.tableprshode.column('num', width=0, stretch=tk.NO)

        self.tableprshode.heading('code', text=s[1], anchor='center')
        self.tableprshode.heading('name', text=s[2], anchor='center')
        self.tableprshode.heading('phone', text=s[3], anchor='center')
        self.tableprshode.heading('price', text=s[4], anchor='center')
        self.tableprshode.heading('time', text=s[7], anchor='center')
        self.tableprshode.heading('status', text=s[8], anchor='center')
        self.tableprshode.bind('<Button-1>', self.selectprshode)

        self.tableprshode.place(x=480, y=411)
        self.cleartabaleprshode()
        self.inserttableprshode()

    def test(self):
        phone = self.Phone.get()
        unit = set()

        a = Repository()
        result = a.Exist("device", phone)
        result1 = a.Exist("aghsat", phone)

        # شمارش تعداد تکرار هر کد در result1
        code_count = {}
        prshode = {}
        prnashode = {}

        if result and result1:
            self.textbox.config(state=NORMAL)

            # اضافه کردن مقادیر به set برای جلوگیری از تکرار
            for item1 in result1:
                key = item1[1]
                unit.add((key, item1[5], item1[6], item1[9]))  # فقط مقادیر مورد نظر را اضافه کنید
                # شمارش تعداد تکرار کد دستگاه
                if key in code_count:
                    code_count[key] += 1
                else:
                    code_count[key] = 1
                if item1[8] == "not paid":
                    if key in prnashode:
                        prnashode[key] += 1
                    else:
                        prnashode[key] = 1
                if item1[8] == "paid":
                    if key in prshode:
                        prshode[key] += 1
                    else:
                        prshode[key] = 1

            unit_list = list(unit)

            grouped_data = {}

            for device in result:
                device_code = device[1]  # کد دستگاه در ستون 1
                if device_code not in grouped_data:
                    grouped_data[device_code] = {
                        'devices': [],
                        'units': []
                    }
                grouped_data[device_code]['devices'].append(device)

            # افزودن اطلاعات اقساط مربوط به هر کد دستگاه
            for item2 in unit_list:
                code = item2[0]  # کد دستگاه در unit
                if code in grouped_data:
                    grouped_data[code]['units'].append(item2)

            for code, data in grouped_data.items():
                self.textbox.insert(tk.END, f"Code: {code}\n")

                # ابتدا اطلاعات دستگاه‌ها را نمایش می‌دهیم (سریال و مدل)

                for device in data['devices']:
                    self.textbox.insert(tk.END, f"Serial: {device[4]}\n")
                    self.textbox.insert(tk.END, f"Model: {device[6]}\n")

                # سپس اطلاعات اقساط را نمایش می‌دهیم
                for item2 in data['units']:
                    self.textbox.insert(tk.END, f"mablagh koli: {item2[2]}\n")
                    self.textbox.insert(tk.END, f"Karmozd koli: {int(item2[1].replace(',', '')) * int(item2[3]):,}\n")
                    self.textbox.insert(tk.END, f"Karmozd har mah: {item2[1]}\n")

                code_count_1 = code_count.get(code, 0)
                prshode_count = prshode.get(code, 0)
                prnashode_count = prnashode.get(code, 0)

                self.textbox.insert(tk.END, f"Tedad Eqsat: {code_count_1}\n")
                self.textbox.insert(tk.END, f"Tedad prshode: {prshode_count}\n")
                self.textbox.insert(tk.END, f"Tedad prnashode: {prnashode_count}\n")

                self.textbox.insert(tk.END, f"\n-----------------------------------------------\n")

            self.textbox.config(state=DISABLED)

    def inserttableprnashode(self):
        user = Repository()
        result = user.Exist("aghsat", self.Phone.get())
        for item in result:
            if item[8] == "not paid":
                self.tableprnashode.insert('', END, values=item)

    def cleartabaleprnashode(self):
        for item in self.tableprnashode.get_children():
            sel = (str(item),)
            self.tableprnashode.delete(*sel)

    def selectprnashode(self, e):
        selection = self.tableprnashode.selection()
        if selection != ():
            self.id.set(self.tableprnashode.item(selection)["values"][0])
            self.code.set(self.tableprnashode.item(selection)["values"][1])
            self.paid.set("paid")
            self.btntasfie.place(x=850, y=375)
            self.btndelete.place(x=950, y=375)
            self.btncancel.place(x=750, y=375)

    def onclickcancel(self):
        self.btntasfie.place_forget()
        self.btncancel.place_forget()
        self.btndelete.place_forget()
        self.cleartabaleprnashode()
        self.inserttableprnashode()
        self.cleartabaleprshode()
        self.inserttableprshode()
        self.btnnotasfie.place_forget()
        self.id.set('')
        self.paid.set('')

    def selectprshode(self, e):
        selection = self.tableprshode.selection()
        if selection != ():
            self.id.set(self.tableprshode.item(selection)["values"][0])
            self.paid.set("not paid")
            self.btnnotasfie.place(x=850, y=750)
            self.btncancel.place(x=750, y=750)
    def inserttableprshode(self):
        user = Repository()
        result = user.Exist("aghsat", self.Phone.get())
        for item in result:
            if item[8] == "paid":
                self.tableprshode.insert('', END, values=item)

    def cleartabaleprshode(self):
        for item in self.tableprshode.get_children():
            sel = (str(item),)
            self.tableprshode.delete(*sel)

    def oneclickpymuont(self):
        result = messagebox.askyesno('warning', 'Are you sure about the payment?')
        if result:
            user = Repository()
            obj = self.paid.get(), self.id.get()
            user.Update("aghsat", obj)
            self.infoaghsat()

    def oneclickdelete(self):
        user = Repository()
        message = messagebox.askyesno('warning', 'Are you sure about the Delete?')
        if message:
            result = user.Delete("aghsat", self.code.get())
            result1 = user.Delete("device", self.code.get())
            result3 = user.Delete("type", self.code.get())
            if result and result1 and result3:
                messagebox.showinfo('ok', 'ok')
                self.infoaghsat()
            else:
                messagebox.showinfo('cancel', 'cancel')

    def oneclickcpymuont(self):
        result = messagebox.askyesno('warning', 'Are you sure about the cancel payment?')
        if result:
            user = Repository()
            obj = self.paid.get(), self.id.get()
            user.Update("aghsat", obj)
            self.infoaghsat()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.lbldate.config(text=f"Today : {date} - {current_time}")
        self.frminfoaghsat.after(1000, self.update_time)

    def ScreenUser(self):
        self.frmscreenuser = Frame(self.screen, width=1500, height=800, bg="white")
        self.infoaghsat()

        self.frmmenu = Frame(self.frmscreenuser, width=200, height=800, bg="black")

        self.lblsabtaghsat = Label(self.frmmenu)
        self.lblsabtaghsat.configure(text="info aghsat", fg="white", font="Arial 12 bold", bg="black")
        self.lblsabtaghsat.bind("<Button-1>", self.clickinfoaghsat)
        self.lblsabtaghsat.place(x=50, y=100)

        self.lblinfoaghsat = Label(self.frmmenu)
        self.lblinfoaghsat.configure(text="sabt aghsat", fg="white", font="Arial 12 bold", bg="black")
        self.lblinfoaghsat.bind("<Button-1>", self.clicksabtaghsat)
        self.lblinfoaghsat.place(x=50, y=50)

        self.frmscreenuser.place(x=0, y=0)
        self.frmmenu.place(x=1300, y=0)

    # -------------------------------------------- Register User ---------------------------------------

    def bindregister(self):
        self.Register()

    def oneclickRegister(self, e):
        self.frmlogin.place_forget()
        self.Register()

    def OnclickRegister(self):
        if self.txtrname.get() == '' or not self.txtrname.get().isalpha():
            messagebox.showerror("Error", "Please enter your name")
        elif self.txtrfamily.get() == '' or not self.txtrfamily.get().isalpha():
            messagebox.showerror("Error", "Please enter your family name")
        elif self.txtrPhone.get() == '' or not self.txtrPhone.get().isdigit():
            messagebox.showerror("Error", "Please enter your phone number")
        elif len(self.Phone.get()) < 11:
            messagebox.showerror("Error", "The phone number is wrong")
            self.cleanphone()
        else:
            user = Repository()
            obj = self.txtrname.get(), self.txtrfamily.get(), self.Phone.get(), date, Time
            result = user.Exist("users", self.Phone.get())
            if result:
                messagebox.showerror("Error", "The user is already registered")
            else:
                user.adduser("users", obj)
                self.ScreenUser()

    def Register(self):
        self.frmregister = Frame(self.screen, width=1500, height=800)
        self.mtnregister = Label(self.frmregister)
        self.mtnregister.configure(text="Register User", fg="black", font="Arial 20 bold")
        self.mtnregister.place(x=670, y=160)

        self.txtrname = Entry(self.frmregister)
        self.txtrname.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtrname.place(x=670, y=230)

        self.lblrname = Label(self.frmregister)
        self.lblrname.configure(text="Name", fg="black")
        self.lblrname.place(x=580, y=230)

        self.txtrfamily = Entry(self.frmregister)
        self.txtrfamily.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtrfamily.place(x=670, y=280)

        self.lblrfamily = Label(self.frmregister)
        self.lblrfamily.configure(text="Family", fg="black")
        self.lblrfamily.place(x=580, y=280)

        self.Phone = StringVar()
        self.txtrPhone = Entry(self.frmregister, textvariable=self.Phone)
        self.txtrPhone.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtrPhone.place(x=670, y=330)

        self.lblrPhone = Label(self.frmregister)
        self.lblrPhone.configure(text="Phone", fg="black")
        self.lblrPhone.place(x=580, y=330)

        self.lbllogin = Label(self.frmregister)
        self.lbllogin.configure(text="User Login", fg="blue", font="Arial 12 bold")
        self.lbllogin.bind("<Button-1>", self.oneclickLogin)
        self.lbllogin.place(x=710, y=370)

        self.btnregister = Button(self.frmregister, command=self.OnclickRegister)
        self.btnregister.configure(text="Register", bg="green", fg="white", bd=3)
        self.btnregister.place(x=710, y=410)
        self.frmregister.place(x=0, y=0)

    # -------------------------------------------- Login User ---------------------------------------

    def cleanphone(self):
        self.Phone.set('')

    def oneclickLogin(self, e):
        self.Login()
        self.cleanphone()

    def oneclicklogin(self):
        user = Repository()
        if len(self.Phone.get()) < 11:
            messagebox.showerror("Error", "The phone number is wrong")
            self.cleanphone()
        else:
            result = user.Exist("users", self.Phone.get())
            if not result:
                messagebox.showerror("Error", "User not found")
            else:
                self.ScreenUser()

    def Login(self):
        self.frmlogin = Frame(self.screen, width=1500, height=800)

        self.mtnregister = Label(self.frmlogin)
        self.mtnregister.configure(text="Login User", fg="black", font="Arial 20 bold")
        self.mtnregister.place(x=660, y=220)

        self.txtlogin = Entry(self.frmlogin)
        self.txtlogin.configure(bg="white", fg="black", bd=3, justify="center", textvariable=self.Phone)
        self.txtlogin.place(x=650, y=290)

        self.lbllogin = Label(self.frmlogin)
        self.lbllogin.configure(text="Phone", fg="black")
        self.lbllogin.place(x=600, y=290)

        self.lblregister = Label(self.frmlogin)
        self.lblregister.configure(text="User Register", fg="blue", font="Arial 12 bold")
        self.lblregister.bind("<Button-1>", self.oneclickRegister)
        self.lblregister.place(x=680, y=330)

        self.btnlogin = Button(self.frmlogin)
        self.btnlogin.configure(text="Login", bg="green", fg="white", bd=3, command=self.oneclicklogin)
        self.btnlogin.place(x=700, y=370)

        self.frmlogin.place(x=0, y=0)

        # -------------------------------------------- Login Dr ---------------------------------------\
    def LoginDr(self):
        self.frmlogindr = Frame(self.screen, width=1500, height=800)

        self.txtlogindr = Entry(self.frmlogindr)
        self.txtlogindr.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtlogindr.place(x=650, y=290)

        self.lbllogindr = Label(self.frmlogindr)
        self.lbllogindr.configure(text="Password", fg="black")
        self.lbllogindr.place(x=580, y=290)

        self.btnlogindr = Button(self.frmlogindr)
        self.btnlogindr.configure(text="Login", bg="green", fg="white", bd=3, command=self.oneclicklogindr)
        self.btnlogindr.place(x=700, y=370)

        self.frmlogindr.place(x=0, y=0)


    def ScreenDr(self):
        self.screendr = Frame(self.frmlogindr, width=1300, height=800)
        self.Amar('')

        self.menudr = Frame(self.frmlogindr, width=200, height=800)
        self.MenuDr()
        self.menudr.place(x=1300, y=0)
        self.screendr.place(x=0, y=0)

    def oneclicklogindr(self):
        if self.txtlogindr.get() == "1234":
            self.ScreenDr()


    def MenuDr(self):

        self.amar = Label(self.menudr)
        self.amar.configure(text="Amar", font="Arial 15 bold")
        self.amar.bind("<Button-1>", self.Amar)
        self.amar.place(x=40, y=20)

        self.Pr_Shode = Label(self.menudr)
        self.Pr_Shode.configure(text="Pr_Shode", font="Arial 15 bold")
        self.Pr_Shode.bind('<Button-1>', self.dr_prshode)
        self.Pr_Shode.place(x=40, y=80)

        self.Pr_Nashode = Label(self.menudr)
        self.Pr_Nashode.configure(text="Pr_Nashode", font="Arial 15 bold")
        self.Pr_Nashode.bind('<Button-1>', self.dr_prnashode)
        self.Pr_Nashode.place(x=40, y=140)

        self.searchdate = Label(self.menudr)
        self.searchdate.configure(text="Search Date", font="Arial 15 bold")
        self.searchdate.bind("<Button-1>", self.search_date)
        self.searchdate.place(x=40, y=200)

        self.searchuser = Label(self.menudr)
        self.searchuser.configure(text="Search User", font="Arial 15 bold")
        self.searchuser.bind("<Button-1>", self.search_user)
        self.searchuser.place(x=40, y=260)


    def Amar(self, e):
        self.frmamar = Frame(self.screendr, width=1300, height=800, background="black")
        result = self.CountsAmar()

        self.time_amar = Label(self.frmamar)
        self.time_amar.configure(fg="white", background="black", font="Arial 15 bold")
        self.time_amar.place(x=935, y=280)
        self.update_timeee()

        self.amar_user = Label(self.frmamar)
        self.amar_user.config(text=f"Total User : {result[0][0][0]}", fg="white", background="black", font="Arial 15 bold")
        self.amar_user.configure()
        self.amar_user.place(x=800, y=400)

        self.total_aghsat = Label(self.frmamar)
        self.total_aghsat.configure(text=f'Total Aghsat : {result[1][0][0]}', fg="white", background="black", font="Arial 15 bold")
        self.total_aghsat.place(x=800, y=460)

        self.total_aghsatprshode = Label(self.frmamar)
        self.total_aghsatprshode.configure(text=f'aghsat prshode : {result[3][0][0]}', fg="white", background="black", font="Arial 15 bold")
        self.total_aghsatprshode.place(x=800, y=520)

        self.total_aghsatprnashode = Label(self.frmamar)
        self.total_aghsatprnashode.configure(text=f'aghsat prnashode : {result[2][0][0]}', fg="white", background="black", font="Arial 15 bold")
        self.total_aghsatprnashode.place(x=800, y=580)

        row = ['id', 'name', 'family', 'phone', 'date', 'time']
        self.tblamar = ttk.Treeview(self.frmamar, columns=row, show='headings', height=35)

        self.tblamar.heading('name', text='Name')
        self.tblamar.heading('family', text='Family')
        self.tblamar.heading('phone', text='Phone')
        self.tblamar.heading('date', text='Date')
        self.tblamar.heading('time', text='Time')

        self.tblamar.column('name', anchor='center', width=150)
        self.tblamar.column('family', anchor='center', width=150)
        self.tblamar.column('phone', anchor='center', width=150)
        self.tblamar.column('date', anchor='center', width=150)
        self.tblamar.column('time', anchor='center', width=150)
        self.tblamar.column('id', stretch=tk.NO, width=0)

        self.tblamar.place(x=10, y=10)

        self.inserttableamaruser()

        self.frmamar.place(x=0, y=0)

    # -------------------------------------------- Clock ---------------------------------------

        self.canvas_size = 200
        self.center_x = self.canvas_size // 2
        self.center_y = self.canvas_size // 2
        self.radius = 80  # شعاع ساعت کوچکتر شده است

        self.canvas_size = 250
        self.center_x = self.canvas_size // 2
        self.center_y = self.canvas_size // 2
        self.radius = 100

        # ساخت بوم
        self.canvas = Canvas(self.frmamar, width=self.canvas_size, height=self.canvas_size, bg="black",
                                highlightthickness=0)
        self.canvas.place(x=910, y=10)

        # رسم قاب و نشانه‌ها
        self.setup_canvas()
        self.update_clock()

    def draw_numbers(self):
        """رسم اعداد خاص (3، 6، 9، و 12)"""
        positions = {3: 90, 6: 180, 9: 270, 12: 0}  # اعداد و زوایای آنها
        for num, angle_deg in positions.items():
            angle = math.radians(angle_deg)
            x = self.center_x + (self.radius - 30) * math.sin(angle)
            y = self.center_y - (self.radius - 30) * math.cos(angle)
            self.canvas.create_text(x, y, text=str(num), font=("Helvetica", 14, "bold"), fill="gray")

    def draw_marks(self):
        """رسم نشانه‌های ساعت (خطوط کوتاه)"""
        for i in range(60):
            angle = math.radians(i * 6)  # هر نشانه 6 درجه
            length = 10 if i % 5 == 0 else 5  # نشانه‌های 5 تایی بلندتر هستند
            x_start = self.center_x + (self.radius - length) * math.sin(angle)
            y_start = self.center_y - (self.radius - length) * math.cos(angle)
            x_end = self.center_x + self.radius * math.sin(angle)
            y_end = self.center_y - self.radius * math.cos(angle)
            color = "#d7ad03" if i % 5 == 0 else "gray"
            width = 2 if i % 5 == 0 else 1
            self.canvas.create_line(x_start, y_start, x_end, y_end, fill=color, width=width)

    def draw_hand(self, angle, length, width, color):
        """رسم عقربه‌ها"""
        x_end = self.center_x + length * math.sin(angle)
        y_end = self.center_y - length * math.cos(angle)
        self.canvas.create_line(
            self.center_x, self.center_y, x_end, y_end, width=width, fill=color, capstyle=ROUND, tags="hand"
        )

    def update_clock(self):
        """به‌روزرسانی عقربه‌ها با حرکت روان"""
        # زمان فعلی
        current_time = time.localtime()
        hour = current_time.tm_hour % 12
        minute = current_time.tm_min
        second = current_time.tm_sec
        millis = int(round(time.time() * 1000)) % 1000  # میلی‌ثانیه فعلی

        # محاسبه زوایا
        second_angle = math.radians((second + millis / 1000) * 6)  # حرکت روان ثانیه
        minute_angle = math.radians((minute + second / 60) * 6)  # حرکت روان دقیقه
        hour_angle = math.radians((hour + minute / 60) * 30)  # حرکت روان ساعت

        # پاک کردن عقربه‌های قبلی
        self.canvas.delete("hand")

        # رسم عقربه‌ها
        self.draw_hand(second_angle, self.radius - 20, 2, "red")  # عقربه ثانیه
        self.draw_hand(minute_angle, self.radius - 40, 4, "white")  # عقربه دقیقه
        self.draw_hand(hour_angle, self.radius - 60, 6, "gold")  # عقربه ساعت

        # به‌روزرسانی سریع‌تر برای حرکت روان
        self.canvas.after(50, self.update_clock)

    def setup_canvas(self):
        """تنظیمات اولیه بوم"""
        # رسم قاب ساعت
        self.canvas.create_oval(
            10, 10, self.canvas_size - 10, self.canvas_size - 10, outline="gray", width=4
        )

        # رسم اعداد و نشانه‌ها
        self.draw_numbers()
        self.draw_marks()

    def update_timeee(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_amar.config(text=f"{date} - {current_time}")
        self.time_amar.after(1000, self.update_timeee)

    def inserttableamaruser(self):
        user = Repository()
        result = user.allusers('users')

        for item in result:
            self.tblamar.insert('', END, values=item)

    def CountsAmar(self):
        user = Repository()
        result = user.CountUsers("users")
        result1 = user.CountUsers("aghsat")
        result2 = user.CountUserWhere('not paid')
        result3 = user.CountUserWhere('paid')
        return result, result1, result2, result3


    def dr_prshode(self, e):

        self.frmdr_prshode = Frame(self.screendr, width=1300, height=800, bg="black")
        result = self.countpr_shode()

        self.lblcountday = Label(self.frmdr_prshode, text=f"Total Day: {result[2][0][0]}")
        self.lblcountday.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblcountday.place(x=830, y=420)

        self.lblkarmozdday = Label(self.frmdr_prshode, text=f" Karmozd day: {result[3]:,}")
        self.lblkarmozdday.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblkarmozdday.place(x=620, y=460)

        self.lblkolday = Label(self.frmdr_prshode, text=f" price day: {result[4]:,}")
        self.lblkolday.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblkolday.place(x=950, y=460)

        self.lblcountmonth = Label(self.frmdr_prshode, text=f"Total Months: {result[0][0][0]}")
        self.lblcountmonth.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblcountmonth.place(x=830, y=500)

        self.lblkarmozdmonth = Label(self.frmdr_prshode, text=f" Karmozd Month: {result[5]:,}")
        self.lblkarmozdmonth.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblkarmozdmonth.place(x=620, y=540)

        self.lblkolmonth = Label(self.frmdr_prshode, text=f" price Month: {result[6]:,}")
        self.lblkolmonth.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblkolmonth.place(x=950, y=540)

        self.lblcountall = Label(self.frmdr_prshode, text=f"Total All: {result[1][0][0]}")
        self.lblcountall.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblcountall.place(x=830, y=580)

        self.lblkarmozdall = Label(self.frmdr_prshode, text=f" Karmozd all: {result[7]:,}")
        self.lblkarmozdall.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblkarmozdall.place(x=620, y=620)

        self.lblkolall = Label(self.frmdr_prshode, text=f" price all: {result[8]:,}")
        self.lblkolall.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblkolall.place(x=950, y=620)

        self.lblkol = Label(self.frmdr_prshode, text=f" kol: {result[9]:,}")
        self.lblkol.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblkol.place(x=830, y=660)
        baghimande = result[9] - result[8]

        self.lblpardakhti = Label(self.frmdr_prshode, text=f"pardakhti: {result[8]:,}")
        self.lblpardakhti.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblpardakhti.place(x=620, y=700)

        self.lblbaghimande = Label(self.frmdr_prshode, text=f" baghimande: {baghimande:,}")
        self.lblbaghimande.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblbaghimande.place(x=950, y=700)

        self.lbltblemroz = Label(self.frmdr_prshode, text="ToDay")
        self.lbltblemroz.configure(bg="black", fg="white", font="arial 10 bold")
        self.lbltblemroz.place(x=300, y=12)
        s = ['row', 'code', 'name', 'phone', 'price', 'karmozd', 'kamel', 'time', 'status', 'num']

        self.tblprshodeemroz = ttk.Treeview(self.frmdr_prshode, columns=s, height=17, show="headings")

        self.tblprshodeemroz.column("row", stretch=tk.NO, width=0)
        self.tblprshodeemroz.column("code", width=80, anchor="s")
        self.tblprshodeemroz.column("name", width=100, anchor="s")
        self.tblprshodeemroz.column("phone", width=100, anchor="s")
        self.tblprshodeemroz.column("price", width=120, anchor="s")
        self.tblprshodeemroz.column("karmozd", stretch=tk.NO, width=0)
        self.tblprshodeemroz.column("kamel", stretch=tk.NO, width=0)
        self.tblprshodeemroz.column("time", width=100, anchor="s")
        self.tblprshodeemroz.column("status", width=100, anchor="s")
        self.tblprshodeemroz.column("num", stretch=tk.NO, width=0)

        self.tblprshodeemroz.heading("row", text=s[0])
        self.tblprshodeemroz.heading("code", text=s[1])
        self.tblprshodeemroz.heading("name", text=s[2])
        self.tblprshodeemroz.heading("phone", text=s[3])
        self.tblprshodeemroz.heading("price", text=s[4])
        self.tblprshodeemroz.heading("karmozd", text=s[5])
        self.tblprshodeemroz.heading("kamel", text=s[6])
        self.tblprshodeemroz.heading("time", text=s[7])
        self.tblprshodeemroz.heading("status", text=s[8])
        self.tblprshodeemroz.heading("num", text=s[9])
        self.tblprshodeemroz.place(x=10, y=40)

        self.inserttblprshodeemroz()

        self.lbltblmonth = Label(self.frmdr_prshode, text="this month")
        self.lbltblmonth.configure(bg="black", fg="white", font="arial 10 bold")
        self.lbltblmonth.place(x=920, y=12)

        self.tblprshodemah = ttk.Treeview(self.frmdr_prshode, columns=s, height=17, show="headings")
        self.tblprshodemah.column("row", stretch=tk.NO, width=0)
        self.tblprshodemah.column("code", width=80, anchor="s")
        self.tblprshodemah.column("name", width=100, anchor="s")
        self.tblprshodemah.column("phone", width=100, anchor="s")
        self.tblprshodemah.column("price", width=120, anchor="s")
        self.tblprshodemah.column("karmozd", stretch=tk.NO, width=0)
        self.tblprshodemah.column("kamel", stretch=tk.NO, width=0)
        self.tblprshodemah.column("time", width=100, anchor="s")
        self.tblprshodemah.column("status", width=100, anchor="s")
        self.tblprshodemah.column("num", stretch=tk.NO, width=0)

        self.tblprshodemah.heading("row", text=s[0])
        self.tblprshodemah.heading("code", text=s[1])
        self.tblprshodemah.heading("name", text=s[2])
        self.tblprshodemah.heading("phone", text=s[3])
        self.tblprshodemah.heading("price", text=s[4])
        self.tblprshodemah.heading("karmozd", text=s[5])
        self.tblprshodemah.heading("kamel", text=s[6])
        self.tblprshodemah.heading("time", text=s[7])
        self.tblprshodemah.heading("status", text=s[8])
        self.tblprshodemah.heading("num", text=s[9])
        self.tblprshodemah.place(x=650, y=40)

        self.lbltblmonth = Label(self.frmdr_prshode, text="All Ghest")
        self.lbltblmonth.configure(bg="black", fg="white", font="arial 10 bold")
        self.lbltblmonth.place(x=300, y=415)

        self.tblprshodekol = ttk.Treeview(self.frmdr_prshode, columns=s, height=15, show="headings")
        self.tblprshodekol.column("row", stretch=tk.NO, width=0)
        self.tblprshodekol.column("code", width=80, anchor="s")
        self.tblprshodekol.column("name", width=100, anchor="s")
        self.tblprshodekol.column("phone", width=100, anchor="s")
        self.tblprshodekol.column("price", width=120, anchor="s")
        self.tblprshodekol.column("karmozd", stretch=tk.NO, width=0)
        self.tblprshodekol.column("kamel", stretch=tk.NO, width=0)
        self.tblprshodekol.column("time", width=100, anchor="s")
        self.tblprshodekol.column("status", width=100, anchor="s")
        self.tblprshodekol.column("num", stretch=tk.NO, width=0)

        self.tblprshodekol.heading("row", text=s[0])
        self.tblprshodekol.heading("code", text=s[1])
        self.tblprshodekol.heading("name", text=s[2])
        self.tblprshodekol.heading("phone", text=s[3])
        self.tblprshodekol.heading("price", text=s[4])
        self.tblprshodekol.heading("karmozd", text=s[5])
        self.tblprshodekol.heading("kamel", text=s[6])
        self.tblprshodekol.heading("time", text=s[7])
        self.tblprshodekol.heading("status", text=s[8])
        self.tblprshodekol.heading("num", text=s[9])
        self.tblprshodekol.place(x=10, y=440)
        self.inserttblprshodekoll()

        self.frmdr_prshode.place(x=0, y=0)
        self.inserttblprshodemonth()

    def inserttblprshodeemroz(self):
        user = Repository()
        result = user.allusersday("aghsat", date, 'paid')

        for item in result:
            self.tblprshodeemroz.insert('', END, values=item)

    def inserttblprshodekoll(self):
        user = Repository()
        result = user.alluserswhere('aghsat', 'paid')
        for item in result:
            self.tblprshodekol.insert('', END, values=item)



    def countpr_shode(self):
        user = Repository()
        year = jalali_date_now.year
        month = jalali_date_now.month
        result = user.CountaghsatMonth(year, month, "paid")
        result1 = user.CountUserWhere("paid")
        result2 = user.CountaghsatWhere(date, 'paid')
        result3 = user.allusersday("aghsat", date, 'paid')
        result4 = user.allusersmonth("aghsat", year, month, 'paid')
        result5 = user.alluserswhere("aghsat", "paid")
        result6 = user.allusers("device")
        karmozdtoday = 0
        koltoday = 0
        karmozdmonth = 0
        kolmonth = 0
        karmozdall = 0
        kolall = 0
        kolprice = 0
        for item in result3:
            a = item[5].replace(',', '')
            b = item[4].replace(',', '')
            karmozdtoday += int(a)
            koltoday += int(b)
        for item in result4:
            c = item[5].replace(',', '')
            d = item[4].replace(',', '')
            karmozdmonth += int(c)
            kolmonth += int(d)

        for item in result5:
            i = item[5].replace(',', '')
            f = item[4].replace(',', '')
            karmozdall += int(i)
            kolall += int(f)

        for item in result6:
            a = item[5].replace(',', '')
            kolprice += int(a)

        return result, result1, result2, karmozdtoday, koltoday, karmozdmonth, kolmonth, karmozdall, kolall, kolprice


    def dr_prnashode(self, e):
        self.frmprnashode = Frame(self.screendr, width=1300, height=800, background='black')
        result = self.countpr_nashode()

        lbltblemroz = Label(self.frmprnashode, text="ToDay")
        lbltblemroz.configure(bg="black", fg="white", font="arial 10 bold")
        lbltblemroz.place(x=300, y=12)

        lblcountday = Label(self.frmprnashode, text=f"Total Day: {result[2][0][0]}")
        lblcountday.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        lblcountday.place(x=830, y=420)

        lblkarmozdday = Label(self.frmprnashode, text=f" Karmozd day: {result[1]:,}")
        lblkarmozdday.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        lblkarmozdday.place(x=620, y=460)

        lblkolday = Label(self.frmprnashode, text=f" price day: {result[0]:,}")
        lblkolday.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        lblkolday.place(x=950, y=460)

        lblcountmonth = Label(self.frmprnashode, text=f"Total Months: {result[5][0][0]}")
        lblcountmonth.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        lblcountmonth.place(x=830, y=500)

        lblkarmozdmonth = Label(self.frmprnashode, text=f" Karmozd Month: {result[4]:,}")
        lblkarmozdmonth.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        lblkarmozdmonth.place(x=620, y=540)

        lblkolmonth = Label(self.frmprnashode, text=f" price Month: {result[3]:,}")
        lblkolmonth.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        lblkolmonth.place(x=950, y=540)

        lblcountall = Label(self.frmprnashode, text=f"Total All: {result[8][0][0]}")
        lblcountall.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        lblcountall.place(x=830, y=580)

        lblkarmozdall = Label(self.frmprnashode, text=f" Karmozd all: {result[7]:,}")
        lblkarmozdall.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        lblkarmozdall.place(x=620, y=620)

        lblkolall = Label(self.frmprnashode, text=f" price all: {result[6]:,}")
        lblkolall.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        lblkolall.place(x=950, y=620)

        s = ['row', 'code', 'name', 'phone', 'price', 'karmozd', 'kamel', 'time', 'status', 'num']

        self.tblprnashodeemroz = ttk.Treeview(self.frmprnashode, columns=s, height=17, show="headings")

        self.tblprnashodeemroz.column("row", stretch=tk.NO, width=0)
        self.tblprnashodeemroz.column("code", width=80, anchor="s")
        self.tblprnashodeemroz.column("name", width=100, anchor="s")
        self.tblprnashodeemroz.column("phone", width=100, anchor="s")
        self.tblprnashodeemroz.column("price", width=120, anchor="s")
        self.tblprnashodeemroz.column("karmozd", stretch=tk.NO, width=0)
        self.tblprnashodeemroz.column("kamel", stretch=tk.NO, width=0)
        self.tblprnashodeemroz.column("time", width=100, anchor="s")
        self.tblprnashodeemroz.column("status", width=100, anchor="s")
        self.tblprnashodeemroz.column("num", stretch=tk.NO, width=0)

        self.tblprnashodeemroz.heading("row", text=s[0])
        self.tblprnashodeemroz.heading("code", text=s[1])
        self.tblprnashodeemroz.heading("name", text=s[2])
        self.tblprnashodeemroz.heading("phone", text=s[3])
        self.tblprnashodeemroz.heading("price", text=s[4])
        self.tblprnashodeemroz.heading("karmozd", text=s[5])
        self.tblprnashodeemroz.heading("kamel", text=s[6])
        self.tblprnashodeemroz.heading("time", text=s[7])
        self.tblprnashodeemroz.heading("status", text=s[8])
        self.tblprnashodeemroz.heading("num", text=s[9])
        self.tblprnashodeemroz.place(x=10, y=40)

        self.inserttblornashodeday()

        lbltblmonth = Label(self.frmprnashode, text="this month")
        lbltblmonth.configure(bg="black", fg="white", font="arial 10 bold")
        lbltblmonth.place(x=920, y=12)

        self.tblprnashodemah = ttk.Treeview(self.frmprnashode, columns=s, height=17, show="headings")
        self.tblprnashodemah.column("row", stretch=tk.NO, width=0)
        self.tblprnashodemah.column("code", width=80, anchor="s")
        self.tblprnashodemah.column("name", width=100, anchor="s")
        self.tblprnashodemah.column("phone", width=100, anchor="s")
        self.tblprnashodemah.column("price", width=120, anchor="s")
        self.tblprnashodemah.column("karmozd", stretch=tk.NO, width=0)
        self.tblprnashodemah.column("kamel", stretch=tk.NO, width=0)
        self.tblprnashodemah.column("time", width=100, anchor="s")
        self.tblprnashodemah.column("status", width=100, anchor="s")
        self.tblprnashodemah.column("num", stretch=tk.NO, width=0)

        self.tblprnashodemah.heading("row", text=s[0])
        self.tblprnashodemah.heading("code", text=s[1])
        self.tblprnashodemah.heading("name", text=s[2])
        self.tblprnashodemah.heading("phone", text=s[3])
        self.tblprnashodemah.heading("price", text=s[4])
        self.tblprnashodemah.heading("karmozd", text=s[5])
        self.tblprnashodemah.heading("kamel", text=s[6])
        self.tblprnashodemah.heading("time", text=s[7])
        self.tblprnashodemah.heading("status", text=s[8])
        self.tblprnashodemah.heading("num", text=s[9])
        self.tblprnashodemah.place(x=650, y=40)
        self.inserttblprshodemonth()

        lbltblmonth = Label(self.frmprnashode, text="All Ghest")
        lbltblmonth.configure(bg="black", fg="white", font="arial 10 bold")
        lbltblmonth.place(x=300, y=415)

        self.tblprnashodekol = ttk.Treeview(self.frmprnashode, columns=s, height=15, show="headings")
        self.tblprnashodekol.column("row", stretch=tk.NO, width=0)
        self.tblprnashodekol.column("code", width=80, anchor="s")
        self.tblprnashodekol.column("name", width=100, anchor="s")
        self.tblprnashodekol.column("phone", width=100, anchor="s")
        self.tblprnashodekol.column("price", width=120, anchor="s")
        self.tblprnashodekol.column("karmozd", stretch=tk.NO, width=0)
        self.tblprnashodekol.column("kamel", stretch=tk.NO, width=0)
        self.tblprnashodekol.column("time", width=100, anchor="s")
        self.tblprnashodekol.column("status", width=100, anchor="s")
        self.tblprnashodekol.column("num", stretch=tk.NO, width=0)

        self.tblprnashodekol.heading("row", text=s[0])
        self.tblprnashodekol.heading("code", text=s[1])
        self.tblprnashodekol.heading("name", text=s[2])
        self.tblprnashodekol.heading("phone", text=s[3])
        self.tblprnashodekol.heading("price", text=s[4])
        self.tblprnashodekol.heading("karmozd", text=s[5])
        self.tblprnashodekol.heading("kamel", text=s[6])
        self.tblprnashodekol.heading("time", text=s[7])
        self.tblprnashodekol.heading("status", text=s[8])
        self.tblprnashodekol.heading("num", text=s[9])
        self.tblprnashodekol.place(x=10, y=440)

        self.frmprnashode.place(x=0, y=0)
        self.inserttblprnashodekoll()

    def inserttblornashodeday(self):
        user = Repository()
        result = user.allusersday("aghsat", date, 'not paid')
        for item in result:
            self.tblprnashodeemroz.insert('', 'end', values=item)

    def inserttblprshodemonth(self):
        user = Repository()
        year = jalali_date_now.year
        month = jalali_date_now.month
        result = user.searchdate('aghsat', year, month)
        for item in result:
            if hasattr(self, 'tblprshodemah'):
                if item[8] == 'paid':
                    self.tblprshodemah.insert('', END, values=item)
            if hasattr(self, 'tblprnashodemah'):
                if item[8] == 'not paid':
                    self.tblprnashodemah.insert('', END, values=item)

    def inserttblprnashodekoll(self):
        user = Repository()
        result = user.alluserswhere('aghsat', 'not paid')
        for item in result:
            self.tblprnashodekol.insert('', END, values=item)

    def countpr_nashode(self):
        user = Repository()
        year = jalali_date_now.year
        month = jalali_date_now.month

        karmozdday = 0
        ghestday = 0

        karmozdmonth = 0
        ghestmount = 0

        karmozdall = 0
        ghestall = 0

        priceday = user.allusersday("aghsat", date, 'not paid')
        countday = user.CountaghsatWhere(date, 'paid')

        pricemonth = user.allusersmonth("aghsat", year, month, 'not paid')
        countmount = user.CountaghsatMonth(year, month, "not paid")

        allprice = user.alluserswhere('aghsat', 'not paid')
        allcount = user.CountUserWhere("not paid")

        for item in priceday:
            a = item[4].replace(',', '')
            b = item[5].replace(',', '')
            karmozdday += int(a)
            ghestday += int(b)

        for item in pricemonth:
            a = item[4].replace(',', '')
            b = item[5].replace(',', '')
            karmozdmonth += int(a)
            ghestmount += int(b)

        for item in allprice:
            a = item[4].replace(',', '')
            b = item[5].replace(',', '')
            karmozdall += int(a)
            ghestall += int(b)

        return karmozdday, ghestday, countday, karmozdmonth, ghestmount, countmount, karmozdall, ghestall, allcount


    def search_date(self, e):
        self.frmsearchdate = Frame(self.screendr, width=1300, height=800, background="black")

        year = jalali_date_now.year

        self.txtyear = StringVar()
        self.year = Entry(self.frmsearchdate, textvariable=self.txtyear, justify='center')
        self.txtyear.set(f"{year}")
        self.year.bind("<Button-1>", self.clearyear)
        self.year.place(x=500, y=10)

        self.txtmonth = StringVar()
        self.month = Entry(self.frmsearchdate, textvariable=self.txtmonth, justify='center')
        self.txtmonth.set("Month")
        self.month.bind("<Button-1>", self.clearmonth)
        self.month.place(x=700, y=10)

        self.radiovalues = IntVar()
        radiopaid = Radiobutton(self.frmsearchdate, text="paid",  value=1, bg="#57524c", variable=self.radiovalues)
        radionotpaid = Radiobutton(self.frmsearchdate, text="not paid",  value=2, bg="#57524c"
                                   , variable=self.radiovalues)
        radioall = Radiobutton(self.frmsearchdate, text="All",  value=3, bg="#57524c", variable=self.radiovalues)
        radiopaid.place(x=550, y=50)
        radionotpaid.place(x=650, y=50)
        radioall.place(x=770, y=50)

        self.btnoksearchdate = Button(self.frmsearchdate, text="Search", bg="#57524c", command=self.oneclicksearchdate)
        self.btnoksearchdate.place(x=650, y=100)

        s = ['row', 'code', 'name', 'phone', 'price', 'karmozd', 'kamel', 'time', 'status', 'num']

        self.tblsearchdate = ttk.Treeview(self.frmsearchdate, columns=s, height=25, show="headings")
        self.tblsearchdate.column("row", stretch=tk.NO, width=0)
        self.tblsearchdate.column("code", width=80, anchor="s")
        self.tblsearchdate.column("name", width=100, anchor="s")
        self.tblsearchdate.column("phone", width=100, anchor="s")
        self.tblsearchdate.column("price", width=120, anchor="s")
        self.tblsearchdate.column("karmozd", stretch=tk.NO, width=0)
        self.tblsearchdate.column("kamel", stretch=tk.NO, width=0)
        self.tblsearchdate.column("time", width=100, anchor="s")
        self.tblsearchdate.column("status", width=100, anchor="s")
        self.tblsearchdate.column("num", stretch=tk.NO, width=0)

        self.tblsearchdate.heading("row", text=s[0])
        self.tblsearchdate.heading("code", text=s[1])
        self.tblsearchdate.heading("name", text=s[2])
        self.tblsearchdate.heading("phone", text=s[3])
        self.tblsearchdate.heading("price", text=s[4])
        self.tblsearchdate.heading("karmozd", text=s[5])
        self.tblsearchdate.heading("kamel", text=s[6])
        self.tblsearchdate.heading("time", text=s[7])
        self.tblsearchdate.heading("status", text=s[8])
        self.tblsearchdate.heading("num", text=s[9])
        self.tblsearchdate.place(x=370, y=150)

        self.lblcountsearch = Label(self.frmsearchdate)
        self.lblcountsearch.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblcountsearch.place_forget()

        self.lblkarmozdsearchshode = Label(self.frmsearchdate)
        self.lblkarmozdsearchshode.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblkarmozdsearchshode.place_forget()

        self.lblallpricesearchshode = Label(self.frmsearchdate)
        self.lblallpricesearchshode.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblallpricesearchshode.place_forget()

        self.lblkarmozdsearchnashode = Label(self.frmsearchdate)
        self.lblkarmozdsearchnashode.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblkarmozdsearchnashode.place_forget()

        self.lblallpricesearchnashode = Label(self.frmsearchdate)
        self.lblallpricesearchnashode.config(fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.lblallpricesearchnashode.place_forget()

        self.frmsearchdate.place(x=0, y=0)
        self.cleartblsearchdata()
        self.defult()

    def clearyear(self, e):
        year = jalali_date_now.year
        if self.txtyear.get() == f"{year}":
            self.year.delete(0, END)

    def clearmonth(self, e):
        if self.txtmonth.get() == "Month":
            self.month.delete(0, END)

    def oneclicksearchdate(self):
        if self.year.get() == "":
            messagebox.showerror("Error", "Please enter a valid year")
            self.year.focus_set()

        elif self.month.get() == "" or self.month.get() == "Month":
            messagebox.showerror("Error", "Please enter a valid month")
            self.month.focus_set()
        elif self.radiovalues.get() == 0:
            messagebox.showerror("Error", "Please enter a valid Radio")
        else:
            self.cleartblsearchdata()
            self.inserttblsearchdata()
            self.counttblsearchdata()

    def cleartblsearchdata(self):
        for item in self.tblsearchdate.get_children():
            self.tblsearchdate.delete(str(item),)

    def inserttblsearchdata(self):
        user = Repository()
        if self.radiovalues.get() == 1:
            result = user.allusersmonth("aghsat", int(self.year.get()), int(self.month.get()), 'paid')
            for item in result:
                self.tblsearchdate.insert('', END, values=item)
        elif self.radiovalues.get() == 2:
            result = user.allusersmonth("aghsat", self.year.get(), self.month.get(), 'not paid')
            for item in result:
                self.tblsearchdate.insert('', END, values=item)
        elif self.radiovalues.get() == 3:
            result = user.allusersmonth2("aghsat", self.year.get(), self.month.get())
            for item in result:
                self.tblsearchdate.insert('', END, values=item)

    def counttblsearchdata(self):
        user = Repository()
        if self.radiovalues.get() == 1:
            countmount = user.CountaghsatMonth(self.year.get(), self.month.get(), "paid")
            self.lblcountsearch.config(text=f"Total : {countmount[0][0]}")
            self.lblcountsearch.place(x=630, y=690)
            pricemonth = user.allusersmonth("aghsat", self.year.get(), self.month.get(), "paid")
            karmozd = 0
            all1 = 0
            for item in pricemonth:
                a = item[5].replace(',', '')
                b = item[4].replace(',', '')
                karmozd += int(a)
                all1 += int(b)
            self.lblkarmozdsearchshode.place(x=350, y=730)
            self.lblkarmozdsearchshode.config(text=f"Karmozd : {karmozd:,}")
            self.lblallpricesearchshode.place(x=800, y=730)
            self.lblallpricesearchshode.config(text=f"all : {all1:,}")
            self.lblkarmozdsearchnashode.place_forget()
            self.lblallpricesearchnashode.place_forget()
        elif self.radiovalues.get() == 2:
            countmount = user.CountaghsatMonth(self.year.get(), self.month.get(), "not paid")
            self.lblcountsearch.place(x=630, y=690)
            self.lblcountsearch.config(text=f"Total : {countmount[0][0]}")
            pricemonth = user.allusersmonth("aghsat", self.year.get(), self.month.get(), "not paid")
            karmozd = 0
            all1 = 0
            for item in pricemonth:
                a = item[5].replace(',', '')
                b = item[4].replace(',', '')
                karmozd += int(a)
                all1 += int(b)
            self.lblkarmozdsearchshode.place(x=350, y=730)
            self.lblkarmozdsearchshode.config(text=f"Karmozd : {karmozd:,}")
            self.lblallpricesearchshode.place(x=800, y=730)
            self.lblallpricesearchshode.config(text=f"all : {all1:,}")
            self.lblkarmozdsearchnashode.place_forget()
            self.lblallpricesearchnashode.place_forget()
        elif self.radiovalues.get() == 3:
            self.cleartblsearchdata()
            countmount = user.CountaghsatMonth2(self.year.get(), self.month.get())
            self.lblcountsearch.place(x=630, y=690)
            self.lblcountsearch.config(text=f"Total : {countmount[0][0]}")
            year = jalali_date_now.year
            month = jalali_date_now.month
            pricemonth = user.allusersmonth2("aghsat", year, month)
            karmozdprshode = 0
            karmozdprnashode = 0

            allprshode = 0
            allprnashode = 0
            for item in pricemonth:
                self.tblsearchdate.insert('', END, values=item)
                if item[8] == "paid":
                    a = item[5].replace(',', '')
                    b = item[4].replace(',', '')
                    karmozdprshode += int(a)
                    allprshode += int(b)
                if item[8] == "not paid":
                    a = item[5].replace(',', '')
                    b = item[4].replace(',', '')
                    karmozdprnashode += int(a)
                    allprnashode += int(b)

            self.lblkarmozdsearchshode.place(x=350, y=730)
            self.lblkarmozdsearchshode.config(text=f"k_prshode : {karmozdprshode:,}")
            self.lblallpricesearchshode.place(x=800, y=730)
            self.lblallpricesearchshode.config(text=f"all_prshode : {allprshode:,}")
            self.lblkarmozdsearchnashode.place(x=350, y=770)
            self.lblkarmozdsearchnashode.config(text=f"k_prnashode : {karmozdprnashode:,}")
            self.lblallpricesearchnashode.place(x=800, y=770)
            self.lblallpricesearchnashode.config(text=f"all_prnashode : {allprnashode:,}")

    def defult(self):
        user = Repository()
        year = jalali_date_now.year
        month = jalali_date_now.month
        countmount = user.CountaghsatMonth2(year, month)
        self.lblcountsearch.place(x=630, y=690)
        self.lblcountsearch.config(text=f"Total : {countmount[0][0]}")
        pricemonth = user.allusersmonth2("aghsat", year, month)
        karmozdprshode = 0
        karmozdprnashode = 0

        allprshode = 0
        allprnashode= 0
        for item in pricemonth:
            self.tblsearchdate.insert('', END, values=item)
            if item[8] == "paid":
                a = item[5].replace(',', '')
                b = item[4].replace(',', '')
                karmozdprshode += int(a)
                allprshode += int(b)
            if item[8] == "not paid":
                a = item[5].replace(',', '')
                b = item[4].replace(',', '')
                karmozdprnashode += int(a)
                allprnashode += int(b)

        self.lblkarmozdsearchshode.place(x=350, y=730)
        self.lblkarmozdsearchshode.config(text=f"k_prshode : {karmozdprshode:,}")
        self.lblallpricesearchshode.place(x=800, y=730)
        self.lblallpricesearchshode.config(text=f"all_prshode : {allprshode:,}")
        self.lblkarmozdsearchnashode.place(x=350, y=770)
        self.lblkarmozdsearchnashode.config(text=f"k_prnashode : {karmozdprnashode:,}")
        self.lblallpricesearchnashode.place(x=800, y=770)
        self.lblallpricesearchnashode.config(text=f"all_prnashode : {allprnashode:,}")

    def search_user(self, e):
        self.frmsearchuser = Frame(self.screendr, bg="black", width=1300, height=800)

        self.txtsearchuser = Entry(self.frmsearchuser, justify="center")
        self.txtsearchuser.place(x=1130, y=10)
        self.btnsearchuser = Button(self.frmsearchuser, text="Search", command=self.oneclicksearch)
        self.btnsearchuser.place(x=1050, y=10)

        self.lblname = Label(self.frmsearchuser, background='black', foreground="white", font=("Arial", 12))
        self.lblname.place(x=1000, y=100)

        self.lblphone = Label(self.frmsearchuser, background='black', foreground="white", font=("Arial", 12))
        self.lblphone.place(x=1000, y=140)

        self.lblprshode = Label(self.frmsearchuser, background='black', foreground="white",
                              font=("Arial", 12))
        self.lblprshode.place(x=650, y=380)

        self.lblkarmozdprshode = Label(self.frmsearchuser, background='black', foreground="white",
                                font=("Arial", 12))
        self.lblkarmozdprshode.place(x=500, y=440)

        self.lblallprshode = Label(self.frmsearchuser, background='black', foreground="white",
                                       font=("Arial", 12))
        self.lblallprshode.place(x=850, y=440)

        self.lblprnashode = Label(self.frmsearchuser, background='black', foreground="white",
                                font=("Arial", 12))
        self.lblprnashode.place(x=650, y=500)

        self.lblkarmozdprnashode = Label(self.frmsearchuser, background='black', foreground="white",
                                       font=("Arial", 12))
        self.lblkarmozdprnashode.place(x=500, y=560)

        self.lblallprnashode = Label(self.frmsearchuser, background='black', foreground="white",
                                   font=("Arial", 12))
        self.lblallprnashode.place(x=850, y=560)

        lblaghsat = Label(self.frmsearchuser, text='Aghsat')
        lblaghsat.place(x=200, y=10)
        s = ['row', 'code', 'name', 'phone', 'price', 'karmozd', 'kamel', 'time', 'status', 'num']

        self.tblsearchuserghest = ttk.Treeview(self.frmsearchuser, columns=s, height=15, show="headings")
        self.tblsearchuserghest.column("row", stretch=tk.NO, width=0)
        self.tblsearchuserghest.column("code", width=100, anchor="s")
        self.tblsearchuserghest.column("name", stretch=tk.NO, width=0)
        self.tblsearchuserghest.column("phone", stretch=tk.NO, width=0)
        self.tblsearchuserghest.column("price", width=160, anchor="s")
        self.tblsearchuserghest.column("karmozd", stretch=tk.NO, width=0)
        self.tblsearchuserghest.column("kamel", stretch=tk.NO, width=0)
        self.tblsearchuserghest.column("time", width=100, anchor="s")
        self.tblsearchuserghest.column("status", width=110, anchor="s")
        self.tblsearchuserghest.column("num", stretch=tk.NO, width=0)

        self.tblsearchuserghest.heading("code", text=s[1])
        self.tblsearchuserghest.heading("price", text=s[4])
        self.tblsearchuserghest.heading("time", text=s[7])
        self.tblsearchuserghest.heading("status", text=s[8])
        self.tblsearchuserghest.place(x=10, y=40)

        lbldevice= Label(self.frmsearchuser, text='Device')
        lbldevice.place(x=200, y=370)

        a = ['row', 'code', 'name', 'phone', 'serial', 'price', 'model']
        self.tblsearchuserdevice = ttk.Treeview(self.frmsearchuser, columns=a, height=15, show="headings")
        self.tblsearchuserdevice.column('row', stretch=tk.NO, width=0)
        self.tblsearchuserdevice.column('code', width=80, anchor='s')
        self.tblsearchuserdevice.column('name', stretch=tk.NO, width=0)
        self.tblsearchuserdevice.column('phone', stretch=tk.NO, width=0)
        self.tblsearchuserdevice.column('serial', width=160, anchor='s')
        self.tblsearchuserdevice.column('price', width=100, anchor='s')
        self.tblsearchuserdevice.column('model', width=130, anchor='s')

        self.tblsearchuserdevice.heading('code', text=a[1])
        self.tblsearchuserdevice.heading('serial', text=a[4])
        self.tblsearchuserdevice.heading('price', text=a[5])
        self.tblsearchuserdevice.heading('model', text=a[6])
        self.tblsearchuserdevice.place(x=10, y=400)

        lbltype = Label(self.frmsearchuser, text='check or tala')
        lbltype.place(x=680, y=10)

        b = ['row', 'code', 'name', 'phone', 'type', 'type / serial', 'g / m']
        self.tblsearchusertype = ttk.Treeview(self.frmsearchuser, columns=b, height=15, show="headings")
        self.tblsearchusertype.column('row', stretch=tk.NO, width=0)
        self.tblsearchusertype.column('code', width=80, anchor='s')
        self.tblsearchusertype.column('name', stretch=tk.NO, width=0)
        self.tblsearchusertype.column('phone', stretch=tk.NO, width=0)
        self.tblsearchusertype.column('type', width=80, anchor='s')
        self.tblsearchusertype.column('type / serial', width=150, anchor='s')
        self.tblsearchusertype.column('g / m', width=130, anchor='s')

        self.tblsearchusertype.heading('code', text=b[1])
        self.tblsearchusertype.heading('type', text=b[4])
        self.tblsearchusertype.heading('type / serial', text=b[5])
        self.tblsearchusertype.heading('g / m', text=b[6])
        self.tblsearchusertype.place(x=500, y=40)

        self.frmsearchuser.place(x=0, y=0)

    def oneclicksearch(self):
        if self.txtsearchuser.get() == '':
            messagebox.showwarning(title='Warning', message='Please enter a valid number')
        elif not self.txtsearchuser.get().isdigit():
            messagebox.showwarning(title='Warning', message='Please enter a valid number')
        else:
            self.clearalltablesearch()
            self.insertdatasearchuseraghsat()
            self.insertdatatblsearchdevice()
            self.insertdatasearchtype()
            self.insetdatalblsearchuser()

    def insertdatasearchuseraghsat(self):
        user = Repository()
        result = user.Exist("aghsat", self.txtsearchuser.get())
        if result:
            for item in result:
                self.lblname.configure(text=f"name : {item[2]}")
                self.lblphone.configure(text=f"Phone : {item[3]}")
                self.tblsearchuserghest.insert('', 'end', values=item)
        else:
            messagebox.showwarning(title='Warning', message='not user')

    def insertdatatblsearchdevice(self):
        user = Repository()
        result = user.Exist("device", self.txtsearchuser.get())
        if result:
            for item in result:
                self.tblsearchuserdevice.insert('', 'end', values=item)

    def insertdatasearchtype(self):
        user = Repository()
        result = user.Exist("type", self.txtsearchuser.get())
        if result:
            for item in result:
                self.tblsearchusertype.insert('', 'end', values=item)


    def clearalltablesearch(self):
        for item in self.tblsearchuserghest.get_children():
            self.tblsearchuserghest.delete(str(item),)
        for item in self.tblsearchuserdevice.get_children():
            self.tblsearchuserdevice.delete(str(item), )
        for item in self.tblsearchusertype.get_children():
            self.tblsearchusertype.delete(str(item), )

    def insetdatalblsearchuser(self):
        user = Repository()
        result = user.CountUserWhere2(self.txtsearchuser.get(), 'paid')
        result1 = user.CountUserWhere2(self.txtsearchuser.get(), 'not paid')
        result2 = user.Exist("aghsat", self.txtsearchuser.get())
        karmozdprshode = 0
        allpriceprshode = 0

        karmozdprnashode = 0
        allkarmozdprnashode = 0
        for item in result2:
            if item[8] == "paid":
                a = item[5].replace(",", "")
                karmozdprshode += int(a)
                b = item[4].replace(",", "")
                allpriceprshode += int(b)
            else:
                a = item[5].replace(",", "")
                karmozdprnashode += int(a)
                b = item[4].replace(",", "")
                allkarmozdprnashode += int(b)

        self.lblprshode.configure(text=f"پرداخت شده ها : {result[0][0]}", justify="right")
        self.lblprnashode.configure(text=f"Total pr_nashode : {result1[0][0]}")
        self.lblkarmozdprshode.configure(text=f"karmozed : {karmozdprshode:,}")
        self.lblkarmozdprnashode.configure(text=f"karmozed : {karmozdprnashode:,}")
        self.lblallprshode.configure(text=f"all price : {allpriceprshode:,}")
        self.lblallprnashode.configure(text=f"all price : {allkarmozdprnashode:,}")






