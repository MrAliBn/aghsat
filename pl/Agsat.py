from tkinter import messagebox, ttk
from tkinter import *
import tkinter as tk
import time
import jdatetime
import math
from dal.repository import Repository
from time import strftime
from persiantools.jdatetime import JalaliDate
import random
import webbrowser
import os
import urllib.parse



jalali_date_now = JalaliDate.today()
date = str(jalali_date_now).replace("-", "/")
Time = strftime("%X")


class App(Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.Register()
        self.Menu()
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#444444", foreground="#FFFFFF", fieldbackground="#2e2e2e",
                        font=("Arial", 10))
        style.map("Custom.Treeview", background=[('selected', '#4CAF50')])  # Highlight selected rows

    # -------------------------------------------- Menu Top ---------------------------------------

    def Menu(self):
        # ایجاد منوی اصلی
        self.Setting = Menu(self.screen, bg="#2C3E50", fg="white", font=("Arial", 12, "bold"))

        # ایجاد منوی تنظیمات فرعی
        self.mnu = Menu(self.Setting, tearoff=0, background="#34495E", fg="white")

        # جداکننده‌ها
        self.mnu.add_separator()

        # ورودی و عملکرد منوها
        self.mnu.add_command(label="ورود کاربر", command=self.Login, foreground="white", background="#2980B9",
                             activebackground="#1ABC9C")
        self.mnu.add_separator()
        self.mnu.add_command(label="ثبت نام", command=self.Register, foreground="white", background="#2980B9",
                             activebackground="#1ABC9C")
        self.mnu.add_separator()
        self.mnu.add_command(label="مدیریت", command=self.LoginDr, foreground="white", background="#2980B9",
                             activebackground="#1ABC9C")
        self.mnu.add_separator()
        self.mnu.add_separator()
        self.mnu.add_command(label="خروج", command=self.Close, foreground="white", background="#E74C3C",
                             activebackground="#C0392B")

        # اضافه کردن منو به نوار منوی اصلی
        self.Setting.add_cascade(label="تنظیمات", menu=self.mnu)

        # تنظیمات نوار منو
        self.screen.config(menu=self.Setting)

    def Close(self):
        # پیامی که هنگام بستن صفحه نمایش داده می‌شود
        result = messagebox.askquestion("خروج", "آیا مطمئن هستید که می‌خواهید از برنامه خارج شوید؟", icon='warning')
        if result == 'yes':
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
            # تنظیم فریم اصلی
            self.frmsabtaghsat = Frame(self.frmscreenuser, width=1300, height=800, bg="#F4F4F4")
            self.frmsabtaghsat.place(x=0, y=0)

            # عنوان فرم
            self.mtnuser = Label(self.frmsabtaghsat, text="کاربر", fg="#333", font=("Arial", 24, "bold"), bg="#F4F4F4")
            self.mtnuser.place(x=700, y=40)

            # نام کاربری
            Name = StringVar()
            self.txtname = Entry(
                self.frmsabtaghsat,
                bg="#FFFFFF",
                fg="#333",
                bd=2,
                justify="center",
                textvariable=Name,
                font=("Arial", 14),
                state=DISABLED,
            )
            self.txtname.place(x=480, y=90, width=200, height=30)
            Name.set(f"{item[1]} {item[2]}")

            self.lblname = Label(self.frmsabtaghsat, text="نام کاربری:", fg="#555", font=("Arial", 12), bg="#F4F4F4")
            self.lblname.place(x=400, y=90)

            # شماره
            Phone = StringVar()
            self.txtPhone = Entry(
                self.frmsabtaghsat,
                bg="#FFFFFF",
                fg="#333",
                bd=2,
                justify="center",
                textvariable=Phone,
                font=("Arial", 14),
                state=DISABLED,
            )
            Phone.set(item[3])
            self.txtPhone.place(x=830, y=90, width=200, height=30)

            self.lblPhone = Label(self.frmsabtaghsat, text="شماره:", fg="#555", font=("Arial", 12), bg="#F4F4F4")
            self.lblPhone.place(x=750, y=90)

            # سریال
            self.txtserial = Entry(
                self.frmsabtaghsat,
                bg="#FFFFFF",
                fg="#333",
                bd=2,
                justify="center",
                font=("Arial", 14),
            )
            self.txtserial.place(x=480, y=140, width=200, height=30)

            self.lblserial = Label(self.frmsabtaghsat, text="سریال:", fg="#555", font=("Arial", 12), bg="#F4F4F4")
            self.lblserial.place(x=400, y=140)

            # مدل
            self.txtmodel = Entry(
                self.frmsabtaghsat,
                bg="#FFFFFF",
                fg="#333",
                bd=2,
                justify="center",
                font=("Arial", 14),
            )
            self.txtmodel.place(x=830, y=140, width=200, height=30)

            self.lblmodel = Label(self.frmsabtaghsat, text="مدل:", fg="#555", font=("Arial", 12), bg="#F4F4F4")
            self.lblmodel.place(x=750, y=140)

            # عنوان اقساط
            self.mtnaghsat = Label(
                self.frmsabtaghsat, text="اقساط", fg="#333", font=("Arial", 20, "bold"), bg="#F4F4F4"
            )
            self.mtnaghsat.place(x=700, y=240)

            # تاریخ اولین قسط
            self.txtstartgest = Entry(
                self.frmsabtaghsat, bg="#FFFFFF", fg="#333", bd=2, justify="center", font=("Arial", 14)
            )
            self.txtstartgest.place(x=480, y=290, width=200, height=30)

            self.lblstartgest = Label(
                self.frmsabtaghsat, text="تاریخ اولین قسط:", fg="#555", font=("Arial", 12), bg="#F4F4F4"
            )
            self.lblstartgest.place(x=350, y=290)

            # مبلغ اسمی
            self.txtmablaghesmi = Entry(
                self.frmsabtaghsat,
                bg="#FFFFFF",
                fg="#333",
                bd=2,
                justify="center",
                font=("Arial", 14),
            )
            self.txtmablaghesmi.bind("<KeyRelease>", self.format_txtmablaghesmi)
            self.txtmablaghesmi.place(x=830, y=290, width=200, height=30)

            self.lblmablaghesmi = Label(
                self.frmsabtaghsat, text="مبلغ اسمی:", fg="#555", font=("Arial", 12), bg="#F4F4F4"
            )
            self.lblmablaghesmi.place(x=750, y=290)

            # درصد اقساط
            self.darsad = ttk.Combobox(
                self.frmsabtaghsat, background="white", foreground="black", justify="center", state="readonly", width=19
            )
            self.darsad['values'] = self.aghsat()
            self.darsad.set(4)
            self.darsad.place(x=650, y=350)

            # انتخاب تعداد اقساط
            self.txtgest = ttk.Combobox(
                self.frmsabtaghsat, background="white", foreground="black", justify="center", state="readonly", width=19
            )
            self.txtgest.set(1)
            self.txtgest['values'] = self.aghsat()
            self.txtgest.place(x=650, y=410)

            self.lblaghsat = Label(self.frmsabtaghsat, text="اقساط:", fg="#555", font=("Arial", 12), bg="#F4F4F4")
            self.lblaghsat.place(x=580, y=410)

            # روش پرداخت
            self.talachek = IntVar()
            self.tala = ttk.Radiobutton(self.frmsabtaghsat, text='طلا', variable=self.talachek, value=1)
            self.tala.bind("<Button-1>", self.talaentry)
            self.tala.place(x=770, y=450)

            self.chek = ttk.Radiobutton(self.frmsabtaghsat, text='چک', variable=self.talachek, value=2)
            self.chek.bind("<Button-1>", self.chekentry)
            self.chek.place(x=650, y=450)

            # دکمه ثبت
            self.btnadd = Button(
                self.frmsabtaghsat,
                text="ثبت",
                bg="#4CAF50",
                fg="white",
                font=("Arial", 14, "bold"),
                bd=2,
                command=self.Onclicksabtaghsat,
            )
            self.btnadd.place(x=690, y=600, width=100, height=40)

            # تاریخ و زمان
            self.lbldatee = Label(self.frmsabtaghsat, font=("Arial", 12, "bold"), bg="#F4F4F4", fg="#555")
            self.update_timee()
            self.lbldatee.place(x=630, y=10)

            # دکمه تاریخ انتخاب
            self.start_date_button = Button(
                self.frmsabtaghsat, text=">", command=self.open_start_date_calendar, bg="#4CAF50", fg="white"
            )
            self.start_date_button.place(x=658, y=290, width=30, height=30)

            # تقویم (در حالت اولیه None)
            self.calendar_window = None

    # -------------------------------------------- chek or tala ---------------------------------------

    def chekentry(self, e):
        try:
            # برچسب سریال چک
            self.lblserialchek = Label(
                self.frmsabtaghsat,
                text="سریال چک:",
                fg="#555",
                font=("Arial", 12),
                bg="#F4F4F4",
            )
            self.lblserialchek.place(x=550, y=500)

            # برچسب مبلغ چک
            self.lblmablaghlchek = Label(
                self.frmsabtaghsat,
                text="مبلغ چک:",
                fg="#555",
                font=("Arial", 12),
                bg="#F4F4F4",
            )
            self.lblmablaghlchek.place(x=550, y=550)

            # ورودی سریال چک
            self.serialchek = Entry(
                self.frmsabtaghsat,
                justify="center",
                bg="#FFFFFF",
                fg="#333",
                font=("Arial", 14),
                bd=2,
            )
            self.serialchek.place(x=650, y=500, width=200, height=30)

            # ورودی مبلغ چک
            self.mablaghchek = Entry(
                self.frmsabtaghsat,
                justify="center",
                bg="#FFFFFF",
                fg="#333",
                font=("Arial", 14),
                bd=2,
            )
            self.mablaghchek.bind("<KeyRelease>", self.format_mablaghchek)
            self.mablaghchek.place(x=650, y=550, width=200, height=30)

            # مخفی‌سازی فیلدهای طلا
            self.typegold.place_forget()
            self.grams.place_forget()
            self.lblgrams.place_forget()
            self.lbltypetala.place_forget()

        except AttributeError:
            pass

    # -------------------------------------------- tala entry ---------------------------------------

    def talaentry(self, e):
        try:
            # برچسب نوع طلا
            self.lbltypetala = Label(
                self.frmsabtaghsat,
                text="نوع طلا:",
                fg="#555",
                font=("Arial", 12),
                bg="#F4F4F4",
            )
            self.lbltypetala.place(x=550, y=500)

            # برچسب گرم
            self.lblgrams = Label(
                self.frmsabtaghsat,
                text="گرم:",
                fg="#555",
                font=("Arial", 12),
                bg="#F4F4F4",
            )
            self.lblgrams.place(x=550, y=550)

            # ورودی نوع طلا
            self.typegold = Entry(
                self.frmsabtaghsat,
                justify="center",
                bg="#FFFFFF",
                fg="#333",
                font=("Arial", 14),
                bd=2,
            )
            self.typegold.place(x=650, y=500, width=200, height=30)

            # ورودی گرم
            self.grams = Entry(
                self.frmsabtaghsat,
                justify="center",
                bg="#FFFFFF",
                fg="#333",
                font=("Arial", 14),
                bd=2,
            )
            self.grams.place(x=650, y=550, width=200, height=30)

            # مخفی‌سازی فیلدهای چک
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
            messagebox.showerror("خطا", "فیلد سریال را با عدد 15 رقمی پر کنید")
            self.txtserial.focus()
        elif self.txtmodel.get() == '':
            messagebox.showerror("خطا", "فیلد مدل خالی است")
            self.txtmodel.focus()
        elif self.txtstartgest.get() == '':
            messagebox.showerror("خطا", "فیلد تاریخ اولین قسط خالی است")
            self.txtstartgest.focus()
        elif self.txtmablaghesmi.get() == '' or not self.esmi.isdigit():
            messagebox.showerror("خطا", "فیلد مبلغ اسمی را با عدد پر کنید")
            self.txtmablaghesmi.focus()
        elif self.talachek.get() == 0:
            messagebox.showerror("خطا", "لطفا نوعضمانت را انتخاب کنید (طلا یا چک)")
        elif self.talachek.get() == 1 and self.grams.get() == '':
            messagebox.showerror("خطا", "لطفا انتخاب کنید طلا چند گرم است")
        elif self.talachek.get() == 1 and self.typegold.get() == '':
            messagebox.showerror("خطا", "لطفا نوع طلا را انتخاب کنید")
            self.typegold.focus()
        elif self.talachek.get() == 2 and self.serialchek.get() == '':
            messagebox.showerror("خطا", "لطفا فیلد سریال چک را با عدد پر کنید")
            self.serialchek.focus()
        elif self.talachek.get() == 2 and self.mablaghchek.get() == '':
            messagebox.showerror("خطا", "لطفا فیلد مبلغ چک را پر کنید")
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
        """باز کردن پنجره تقویم برای انتخاب تاریخ شروع"""
        self.open_calendar_window(self.txtstartgest)

    def open_calendar_window(self, entry_widget):
        """باز کردن پنجره تقویم برای انتخاب سال، ماه و روز"""
        if self.calendar_window is not None and self.calendar_window.winfo_exists():
            return

        # ایجاد پنجره جدید برای تقویم
        self.calendar_window = Toplevel(self.frmsabtaghsat)
        self.calendar_window.resizable(False, False)
        self.calendar_window.title("انتخاب تاریخ")
        self.calendar_window.geometry("%dx%d+%d+%d" % (400, 300, 700, 350))
        self.calendar_window.config(bg='#f2f2f2')

        # ایجاد برچسب و کادر انتخاب سال
        self.year_label = Label(self.calendar_window, text="سال", bg='#f2f2f2', font="Arial 8")
        self.year_label.grid(row=0, column=0)
        self.year_combobox = ttk.Combobox(self.calendar_window, state="readonly", width=15, font="Arial 8")
        self.year_combobox.grid(row=0, column=1)
        self.year_combobox['values'] = [str(year) for year in range(1400, 1501)]
        self.year_combobox.set(JalaliDate.today().year)

        # ایجاد برچسب و کادر انتخاب ماه
        self.month_label = Label(self.calendar_window, text="ماه", bg='#f2f2f2', font="Arial 8")
        self.month_label.grid(row=1, column=0)
        self.month_combobox = ttk.Combobox(self.calendar_window, state="readonly", width=15, font="Arial 8")
        self.month_combobox.grid(row=1, column=1)

        # ترکیب شماره و نام ماه‌ها
        self.month_mapping = {
            1: "فروردین", 2: "اردیبهشت", 3: "خرداد",
            4: "تیر", 5: "مرداد", 6: "شهریور",
            7: "مهر", 8: "آبان", 9: "آذر",
            10: "دی", 11: "بهمن", 12: "اسفند"
        }
        self.month_combobox['values'] = [f"{num} {name}" for num, name in self.month_mapping.items()]
        self.month_combobox.set(f"{JalaliDate.today().month} {self.month_mapping[JalaliDate.today().month]}")

        # ایجاد برچسب و کادر ورود روز
        self.day_label = Label(self.calendar_window, text="روز", bg='#f2f2f2', font="Arial 7")
        self.day_label.grid(row=2, column=0)
        self.day_entry = Entry(self.calendar_window, width=5, font="Arial 10")
        self.day_entry.grid(row=2, column=1)

        # ایجاد دکمه انتخاب تاریخ
        self.select_button = Button(self.calendar_window, text="انتخاب", command=lambda: self.select_date(entry_widget),
                                    bg="#4CAF50", fg="white", font="Arial 10", bd=1)
        self.select_button.grid(row=3, column=0, columnspan=2, pady=5)

        # نمایش تقویم جلالی
        self.show_jalali_calendar()

        # ایجاد رویداد برای بروزرسانی روزها هنگام تغییر سال یا ماه
        self.year_combobox.bind("<<ComboboxSelected>>", lambda event: self.show_jalali_calendar())
        self.month_combobox.bind("<<ComboboxSelected>>", lambda event: self.show_jalali_calendar())

    def show_jalali_calendar(self):
        """نمایش تقویم جلالی و انتخاب تاریخ"""
        selected_year = int(self.year_combobox.get())
        selected_month = int(self.month_combobox.get().split()[0])

        # حذف تنها دکمه‌های روز تقویم
        for widget in self.calendar_window.grid_slaves():
            if widget.grid_info()["row"] >= 4:
                widget.grid_forget()

        # ایجاد فریم برای روزهای تقویم
        calendar_frame = Frame(self.calendar_window, bg='#f2f2f2')
        calendar_frame.grid(row=4, column=0, columnspan=2)

        # نمایش نام روزهای هفته
        days_of_week = ["یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه"]
        for i, day_name in enumerate(days_of_week):
            day_button = Button(calendar_frame, text=day_name, width=5, font="Arial 7", bg="#555555", fg="white")
            day_button.grid(row=0, column=i)

        # نمایش روزهای ماه انتخابی
        self.show_dates(calendar_frame, selected_year, selected_month)

    def show_dates(self, calendar_frame, year, month):
        """نمایش روزهای ماه انتخابی در تقویم"""
        month_days = JalaliDate(year, month, 1).days_in_month(month, year)
        first_day_of_month = JalaliDate(year, month, 1).weekday()

        for i in range(month_days):
            row = (i + first_day_of_month) // 7 + 1
            col = (i + first_day_of_month) % 7
            day_button = Button(calendar_frame, text=str(i + 1), width=5, font="Arial 7",
                                command=lambda day=i + 1: self.select_day(day), bg="white", fg="#4c4c4c")
            day_button.grid(row=row, column=col, padx=2, pady=2)

    def select_day(self, day):
        """انتخاب روز و بروزرسانی فیلد روز در پنجره تقویم"""
        self.day_entry.delete(0, END)
        self.day_entry.insert(0, str(day))

    def select_date(self, entry_widget):
        """ذخیره تاریخ انتخاب شده در فیلد ورودی و بستن پنجره تقویم"""
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
            print("تاریخ وارد شده معتبر نیست.")

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
        """اطلاعات اقساط را نمایش می‌دهد"""
        user = Repository()
        result = user.Exist("users", self.Phone.get())

        self.frminfoaghsat = Frame(self.frmscreenuser, width=1300, height=800)

        # کادر متنی برای نمایش اطلاعات
        self.textbox = tk.Text(self.frminfoaghsat, width=45, height=38, state="disabled",
                               bg="#EAEAEA", fg="#333", font=("Arial", 12), bd=2, relief="solid")
        self.textbox.place(x=10, y=50)
        self.test()

        for item in result:
            self.textbox.config(state=NORMAL)

            # نمایش تاریخ ثبت‌نام و ساعت
            self.lbldate = Label(self.frminfoaghsat, font="arial 12 bold")
            self.update_time()
            self.lbldate.place(x=20, y=20)

            self.textbox.insert(tk.END, f"\nتاریخ ثبت نام : {item[4]} - ساعت ثبت نام {item[5]}")
            self.textbox.config(state=DISABLED)

        self.frminfoaghsat.place(x=0, y=0)

        # ورودی‌های مختلف برای اطلاعات اقساط
        self.id = StringVar()
        self.txtid = Entry(self.frminfoaghsat, textvariable=self.id)
        self.txtid.place_forget()

        self.code = StringVar()
        self.txtcode = Entry(self.frminfoaghsat, textvariable=self.code)
        self.txtcode.place_forget()

        self.paid = StringVar()
        self.txtpaid = Entry(self.frminfoaghsat, textvariable=self.paid)
        self.txtpaid.place_forget()

        # دکمه‌ها با استایل مدرن
        self.btntasfie = Button(self.frminfoaghsat, text="پرداخت", background="#28a745", command=self.oneclickpymuont,
                                font=("Arial", 12, "bold"), relief="flat", fg="white", width=10)
        self.btntasfie.place_forget()

        self.btndelete = Button(self.frminfoaghsat, text="حذف", background="#dc3545", command=self.oneclickdelete,
                                font=("Arial", 12, "bold"), relief="flat", fg="white", width=10)
        self.btndelete.place_forget()

        self.btncancel = Button(self.frminfoaghsat, text="کنسل", command=self.onclickcancel,
                                font=("Arial", 12, "bold"), relief="flat", fg="black", width=10)
        self.btncancel.place_forget()

        self.btnnotasfie = Button(self.frminfoaghsat, text="لغو پرداخت", background="#dc3545",
                                  command=self.oneclickcpymuont,
                                  font=("Arial", 12, "bold"), relief="flat", fg="white", width=10)
        self.btnnotasfie.place_forget()

        # تعریف ستون‌ها برای جداول اقساط
        s = ['row', 'code', 'name', 'phone', 'price', 'karmozd', 'kamel', 'time', 'status', 'num']

        # جدول اقساط پرنشده
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

        # عنوان ستون‌ها برای جدول اقساط
        self.tableprnashode.heading('code', text='کد', anchor='center')
        self.tableprnashode.heading('name', text='نام', anchor='center')
        self.tableprnashode.heading('phone', text='شماره', anchor='center')
        self.tableprnashode.heading('price', text='مبلغ قسط', anchor='center')
        self.tableprnashode.heading('time', text='تاریخ', anchor='center')
        self.tableprnashode.heading('status', text='وضعیت', anchor='center')

        self.tableprnashode.bind('<Button-1>', self.selectprnashode)

        self.tableprnashode.place(x=480, y=49)
        self.cleartabaleprnashode()
        self.inserttableprnashode()

        # جدول اقساط پرداخت شده
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

        # عنوان ستون‌ها برای جدول اقساط پرداخت شده
        self.tableprshode.heading('code', text='کد', anchor='center')
        self.tableprshode.heading('name', text='نام', anchor='center')
        self.tableprshode.heading('phone', text='شماره', anchor='center')
        self.tableprshode.heading('price', text='مبلغ قسط', anchor='center')
        self.tableprshode.heading('time', text='تاریخ', anchor='center')
        self.tableprshode.heading('status', text='وضعیت', anchor='center')
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
                self.textbox.insert(tk.END, f"کد موبایل: {code}\n")

                # ابتدا اطلاعات دستگاه‌ها را نمایش می‌دهیم (سریال و مدل)

                for device in data['devices']:
                    self.textbox.insert(tk.END, f"سریال: {device[4]}\n")
                    self.textbox.insert(tk.END, f"مدل: {device[6]}\n")

                # سپس اطلاعات اقساط را نمایش می‌دهیم
                for item2 in data['units']:
                    self.textbox.insert(tk.END, f"مبلغ کامل: {item2[2]}\n")
                    self.textbox.insert(tk.END, f"کل کارمزد: {int(item2[1].replace(',', '')) * int(item2[3]):,}\n")
                    self.textbox.insert(tk.END, f"کارمزد هر ماه: {item2[1]}\n")

                code_count_1 = code_count.get(code, 0)
                prshode_count = prshode.get(code, 0)
                prnashode_count = prnashode.get(code, 0)

                self.textbox.insert(tk.END, f"تعداد اقساط: {code_count_1}\n")
                self.textbox.insert(tk.END, f"اقساط پرداخت شده: {prshode_count}\n")
                self.textbox.insert(tk.END, f"اقساط پرداخت نشده: {prnashode_count}\n")

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
        result = messagebox.askyesno('هشدار', 'ایا میخاهید این قسط پرداخت شود؟')
        if result:
            user = Repository()
            obj = self.paid.get(), self.id.get()
            user.Update("aghsat", obj)
            self.infoaghsat()

    def oneclickdelete(self):
        user = Repository()
        message = messagebox.askyesno('هشدار', 'مطمعن به حذف این کد هستید؟ (همه ثبت هایی که با این کد هستند حذف خواهند شد)')
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
        result = messagebox.askyesno('هشدار', 'ایا میخاهید این پرداخت را کنسل کنید؟')
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

        # استایل برای منو و برچسب‌ها
        label_style = {
            "font": ("Arial", 16, "bold"),
            "fg": "#ecf0f1",
            "bg": "#34495e",
            "width": 25,
            "height": 2,
            "bd": 0,
            "anchor": "w",
            "padx": 20,
            "pady": 10
        }

        self.frmmenu = Frame(self.frmscreenuser, width=200, height=800, bg="#2c3e50")

        self.lblsabtaghsat = Label(self.frmmenu, text=" اطلاعات اقساط ")
        self.lblsabtaghsat.configure(**label_style)
        self.lblsabtaghsat.bind("<Button-1>", self.clickinfoaghsat)
        self.lblsabtaghsat.place(x=0, y=50)

        self.lblinfoaghsat = Label(self.frmmenu, text="ثبت اقساط")
        self.lblinfoaghsat.configure(**label_style)
        self.lblinfoaghsat.bind("<Button-1>", self.clicksabtaghsat)
        self.lblinfoaghsat.place(x=0, y=120)

        self.lblprint = Label(self.frmmenu, text="پرینت")
        self.lblprint.configure(**label_style)
        self.lblprint.bind("<Button-1>", self.clickprint)
        self.lblprint.place(x=0, y=190)

        self.frmscreenuser.place(x=0, y=0)

        for label in [self.lblsabtaghsat, self.lblinfoaghsat, self.lblprint]:
            label.bind("<Enter>", lambda e: self.change_color_on_hover(e, "#16a085"))
            label.bind("<Leave>", lambda e: self.change_color_on_hover(e, "#34495e"))

        self.frmmenu.place(x=1300, y=0)

    def clickprint(self, e):
        # فریم پرینت
        self.frmmenuprint = Frame(self.frmscreenuser, width=1300, height=800, bg="white")
        self.frmmenuprint.place(x=0, y=0)

        result = self.insertvaluecombomodel()
        # افزودن کامبوباکس
        self.listmodel = []

        self.listmodel.append(result)

        self.combomodel = ttk.Combobox(self.frmmenuprint, state='readonly', justify='center')
        self.combomodel.place(x=1000, y=20)
        try:
            self.combomodel['values'] = self.listmodel
            self.combomodel.set(self.listmodel[0])
        except Exception as e:
            print(e)


        # دکمه پرینت
        self.btnprint = Button(self.frmmenuprint, text="پرینت", command=self.print_dialog)
        self.btnprint.place(x=600, y=500)

    def print_dialog(self):
        try:
            # مسیر فایل HTML
            html_file_path = os.path.join(os.getcwd(), 'html/index.html')
            # خواندن محتوای HTML از فایل
            with open(html_file_path, 'r', encoding='utf-8') as html_file:
                html_content = html_file.read()

            user = Repository()
            result = user.alldevice("device", self.Phone.get(), self.combomodel.get())
            result1 = user.Existaghsatcode('aghsat', result[0][1])
            table_rows = ""
            num = 0
            for row in result1:
                num += 1
                table_rows += f"""
                            <tr>
                                <td>{row[1]}</td>
                                <td>{row[7]}</td>
                                <td>{row[4]}</td>
                                <td>{num}</td>
                            </tr>
                        """
            html_content = html_content.replace("<!-- داده‌ها اینجا داینامیک اضافه می‌شوند -->", table_rows)

            # جایگزینی مقدار متغیر در HTML

            html_content = html_content.replace("{{model}}", result[0][6])
            html_content = html_content.replace("{{serial}}", result[0][4])
            html_content = html_content.replace("{{username}}", result[0][2])
            html_content = html_content.replace("{{phone}}", result[0][3])
            html_content = html_content.replace("{{kol}}", result[0][5])
            # تبدیل محتوای HTML به فرمت URL-safe برای استفاده در مرورگر
            encoded_html = urllib.parse.quote(html_content)


            # باز کردن محتوای HTML در مرورگر پیش‌فرض
            webbrowser.open(f"data:text/html;charset=utf-8,{encoded_html}")

        except Exception as e:
            print(f"Error: {e}")

    def insertvaluecombomodel(self):
        user = Repository()
        result = user.Exist('device', self.Phone.get())
        for item in result:
            return item[6]


    # -------------------------------------------- Register User ---------------------------------------

    def bindregister(self):
        self.Register()

    def oneclickRegister(self, e):
        self.frmlogin.place_forget()
        self.Register()

    def OnclickRegister(self):
        if self.txtrname.get() == '' or not self.txtrname.get().isalpha():
            messagebox.showerror("خطا", "فیلد نام را فقط با حروف پر کنید")
        elif self.txtrfamily.get() == '' or not self.txtrfamily.get().isalpha():
            messagebox.showerror("خطا", "فیلد فامیلی را فقط با حروف پر کنید")
        elif self.txtrPhone.get() == '' or not self.txtrPhone.get().isdigit():
            messagebox.showerror("خطا", "فیلد شماره را فقط با اعداد پر کنید")
        elif len(self.Phone.get()) < 11:
            messagebox.showerror("خطا", "شماره اشتباه است")
            self.cleanphone()
        else:
            user = Repository()
            obj = self.txtrname.get(), self.txtrfamily.get(), self.Phone.get(), date, Time
            result = user.Exist("users", self.Phone.get())
            if result:
                messagebox.showerror("خطا", "این کاربر قبلا ثبت نام شده است")
            else:
                user.adduser("users", obj)
                self.ScreenUser()

    def Register(self):
        # فریم اصلی ثبت‌نام
        self.frmregister = Frame(self.screen, width=1500, height=800, bg="#1B1F38")
        self.frmregister.place(x=0, y=0)
        # عنوان فرم
        self.mtnregister = Label(
            self.frmregister,
            text="ثبت نام کاربر",
            fg="white",
            font=("Arial", 25, "bold"),
            bg="#1B1F38",
        )
        self.mtnregister.place(x=660, y=180)

        # فیلد ورودی نام کاربر
        self.namee = StringVar()
        self.txtrname = Entry(
            self.frmregister,
            bg="#FFFFFF",
            fg="#000",
            bd=0,
            justify="center",
            textvariable=self.namee,
            font=("Arial", 14),
        )
        self.namee.set("نام کاربر")
        self.txtrname.bind("<Button-1>", self.clearname)
        self.txtrname.place(x=585, y=250, width=300, height=40)

        # حاشیه برای فیلد
        Frame(self.frmregister, bg="#FF6B6B", width=310, height=2).place(x=580, y=292)

        # فیلد ورودی نام خانوادگی
        self.familyy = StringVar()
        self.txtrfamily = Entry(
            self.frmregister,
            bg="#FFFFFF",
            fg="#000",
            bd=0,
            justify="center",
            textvariable=self.familyy,
            font=("Arial", 14),
        )
        self.familyy.set("نام خانوادگی")
        self.txtrfamily.bind("<Button-1>", self.clearfamily)
        self.txtrfamily.place(x=585, y=310, width=300, height=40)
        Frame(self.frmregister, bg="#FF6B6B", width=310, height=2).place(x=580, y=352)

        # فیلد ورودی شماره تلفن
        self.Phone = StringVar()
        self.txtrPhone = Entry(
            self.frmregister,
            bg="#FFFFFF",
            fg="#000",
            bd=0,
            justify="center",
            textvariable=self.Phone,
            font=("Arial", 14),
        )
        self.Phone.set("09171112222")
        self.txtrPhone.bind("<Button-1>", self.clearphone)
        self.txtrPhone.place(x=585, y=370, width=300, height=40)
        Frame(self.frmregister, bg="#FF6B6B", width=310, height=2).place(x=580, y=412)

        # دکمه ورود کاربر
        self.lbllogin = Label(
            self.frmregister,
            text="ورود کاربر",
            fg="#4ACFAC",
            font=("Arial", 15, "bold"),
            bg="#1B1F38",
            cursor="hand2",
        )
        self.lbllogin.bind("<Button-1>", self.oneclickLogin)
        self.lbllogin.place(x=700, y=430)

        # دکمه ثبت‌نام
        self.btnregister = Button(
            self.frmregister,
            text="ثبت نام",
            command=self.OnclickRegister,
            bg="#4ACFAC",
            fg="white",
            font=("Arial", 14, "bold"),
            activebackground="#3BAF9E",
            activeforeground="white",
            bd=0,
        )
        self.btnregister.place(x=640, y=480, width=200, height=40)

    def clearphone(self, e):
        if self.Phone.get() == '09171112222':
            self.Phone.set('')

    def clearname(self, e):
        if self.namee.get() == 'نام کاربر':
            self.namee.set('')

    def clearfamily(self, e):
        if self.familyy.get() == 'نام خانوادگی':
            self.familyy.set('')

    # -------------------------------------------- Login User ---------------------------------------

    def cleanphone(self):
        self.Phone.set('')

    def oneclickLogin(self, e):
        self.Login()
        self.cleanphone()

    def oneclicklogin(self):
        user = Repository()
        if len(self.Phone.get()) < 11:
            messagebox.showerror("خطا", "شماره اشتباه است")
            self.cleanphone()
        else:
            result = user.Exist("users", self.Phone.get())
            if not result:
                messagebox.showerror("خطا", "کاربر پیدا نشد")
            else:
                self.ScreenUser()

    def Login(self):
        # فریم اصلی ورود
        self.frmlogin = Frame(self.screen, width=1500, height=800, bg="#1B1F38")
        self.frmlogin.place(x=0, y=0)

        # فریم برجسته برای ورود
        self.frmloginbd = Frame(self.frmlogin, width=400, height=400, bg="#FFFFFF", relief="raised", bd=10)
        self.frmloginbd.place(relx=0.5, rely=0.5, anchor="center")

        # عنوان فرم
        self.mtnregister = Label(
            self.frmloginbd,
            text="ورود کاربر",
            fg="#1B1F38",
            font=("Arial", 20, "bold"),
            bg="#FFFFFF",
        )
        self.mtnregister.place(relx=0.5, rely=0.15, anchor="center")

        # لیبل شماره تلفن
        self.lblphonee = Label(
            self.frmloginbd,
            text="شماره تلفن:",
            font=("Arial", 12),
            bg="#FFFFFF",
            fg="#6B7280",
        )
        self.lblphonee.place(relx=0.5, rely=0.35, anchor="center")

        # فیلد ورودی شماره تلفن
        self.txtlogin = Entry(
            self.frmloginbd,
            bg="#F3F4F6",
            fg="#000000",
            bd=0,
            justify="center",
            font=("Arial", 14),
            textvariable=self.Phone,
        )
        self.txtlogin.bind("<Button-1>", self.clearphone)
        self.txtlogin.place(relx=0.5, rely=0.45, anchor="center", width=250, height=30)

        # خط زیر فیلد شماره تلفن
        Frame(self.frmloginbd, bg="#1B75BB", width=260, height=2).place(relx=0.5, rely=0.51, anchor="center")

        # لینک ثبت‌نام
        self.lblregister = Label(
            self.frmloginbd,
            text="ثبت ‌نام کاربر",
            fg="#1B75BB",
            font=("Arial", 15, "bold"),
            bg="#FFFFFF",
            cursor="hand2",
        )
        self.lblregister.bind("<Button-1>", self.oneclickRegister)
        self.lblregister.place(relx=0.5, rely=0.65, anchor="center")

        # دکمه ورود
        self.btnlogin = Button(
            self.frmloginbd,
            text="ورود",
            command=self.oneclicklogin,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            bd=0,
            activebackground="#45A049",
            activeforeground="white",
        )
        self.btnlogin.place(relx=0.5, rely=0.8, anchor="center", width=200, height=40)


        # -------------------------------------------- Login Dr ---------------------------------------\

    def LoginDr(self):
        # فرم اصلی ورود
        self.frmlogindr = Frame(self.screen, width=1500, height=800, bg="#1a1a1a")
        self.frmlogindr.place(x=0, y=0)

        # فیلد ورودی رمز عبور (استایل جدید)
        self.txtlogindr = Entry(self.frmlogindr)
        self.txtlogindr.configure(bg="#333", fg="#fff", bd=2, font=("Arial", 14), relief="flat", justify="center",
                                  insertbackground='white', width=25)

        # ایجاد افکت سایه و لبه‌های گرد برای فیلد ورودی
        self.txtlogindr.config(highlightbackground="black", highlightcolor="#00b8d4", highlightthickness=2)

        # افکت روی فیلد ورودی - زمانی که روی فیلد کلیک می‌شود
        self.txtlogindr.bind("<FocusIn>", lambda event: self.txtlogindr.config(bg="#444"))
        self.txtlogindr.bind("<FocusOut>", lambda event: self.txtlogindr.config(bg="#333"))

        self.txtlogindr.place(x=650, y=290)

        # برچسب رمز عبور
        self.lbllogindr = Label(self.frmlogindr)
        self.lbllogindr.configure(text="رمز عبور", fg="white", font=("Arial", 16, "bold"), bg='#1a1a1a')
        self.lbllogindr.place(x=570, y=290)

        # دکمه ورود
        self.btnlogindr = Button(self.frmlogindr)
        self.btnlogindr.configure(text="ورود", bg="#4CAF50", fg="white", bd=2, relief="flat",
                                  font=("Arial", 14, "bold"), command=self.oneclicklogindr)
        self.btnlogindr.place(x=750, y=350)

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
        else:
            messagebox.showerror('خطا', 'رمز ورود اشتباه است')

    def MenuDr(self):
        # فرم منو
        self.menudr = Frame(self.screen, width=400, height=800, bg="#2c3e50")
        self.menudr.place(x=0, y=0)

        # استایل برای منو و برچسب‌ها
        label_style = {
            "font": ("Arial", 16, "bold"),
            "fg": "#ecf0f1",
            "bg": "#34495e",
            "width": 25,
            "height": 2,
            "bd": 0,
            "anchor": "w",
            "padx": 20,
            "pady": 10
        }

        # ایجاد اولین برچسب (امار کاربران)
        self.amar = Label(self.menudr, text="امار کاربرارن", **label_style)
        self.amar.bind("<Button-1>", self.Amar)
        self.amar.place(x=0, y=10)

        # ایجاد دومین برچسب (پرداخت شده‌ها)
        self.Pr_Shode = Label(self.menudr, text="پرداخت شده ها", **label_style)
        self.Pr_Shode.bind('<Button-1>', self.dr_prshode)
        self.Pr_Shode.place(x=0, y=80)

        # ایجاد سومین برچسب (پرداخت نشده‌ها)
        self.Pr_Nashode = Label(self.menudr, text="پرداخت نشده", **label_style)
        self.Pr_Nashode.bind('<Button-1>', self.dr_prnashode)
        self.Pr_Nashode.place(x=0, y=150)

        # ایجاد چهارمین برچسب (فعالیت‌های اخیر)
        self.searchdate = Label(self.menudr, text="فعالیت های اخیر", **label_style)
        self.searchdate.bind("<Button-1>", self.search_date)
        self.searchdate.place(x=0, y=220)

        # ایجاد پنجمین برچسب (جستجو کاربر)
        self.searchuser = Label(self.menudr, text="جستجو کاربر", **label_style)
        self.searchuser.bind("<Button-1>", self.search_user)
        self.searchuser.place(x=0, y=290)

        # افزودن انیمیشن برای تغییر رنگ دکمه‌ها هنگام هاور
        for label in [self.amar, self.Pr_Shode, self.Pr_Nashode, self.searchdate, self.searchuser]:
            label.bind("<Enter>", lambda e: self.change_color_on_hover(e, "#16a085"))
            label.bind("<Leave>", lambda e: self.change_color_on_hover(e, "#34495e"))

        # تنظیمات طراحی برای تغییر رنگ هنگام هاور
        self.menudr.place(x=0, y=0)

    def change_color_on_hover(self, event, color):
        event.widget.config(bg=color)

    def Amar(self, e):
        self.frmamar = Frame(self.screendr, width=1300, height=800, background="black")
        result = self.CountsAmar()

        # برچسب‌ها با استایل‌های جدید
        label_style = {
            "background": "#2C3E50",
            "foreground": "#ECF0F1",
            "font": ("Arial", 12),
            "padx": 10,
            "pady": 5
        }

        self.time_amar = Label(self.frmamar)
        self.time_amar.configure(**label_style)
        self.time_amar.place(x=935, y=280)
        self.update_timeee()

        self.amar_user = Label(self.frmamar)
        self.amar_user.config(text=f"تعداد کاربران : {result[0][0][0]}", fg="white", background="black", font="Arial 15 bold")
        self.amar_user.configure(**label_style)
        self.amar_user.place(x=800, y=400)

        self.total_aghsat = Label(self.frmamar)
        self.total_aghsat.configure(text=f'تعداد اقساط : {result[1][0][0]}', **label_style)
        self.total_aghsat.place(x=800, y=460)

        self.total_aghsatprshode = Label(self.frmamar)
        self.total_aghsatprshode.configure(text=f' پرداخت شده : {result[3][0][0]}', **label_style)
        self.total_aghsatprshode.place(x=800, y=520)

        self.total_aghsatprnashode = Label(self.frmamar)
        self.total_aghsatprnashode.configure(text=f'پرداخت نشده : {result[2][0][0]}', **label_style)
        self.total_aghsatprnashode.place(x=800, y=580)

        row = ['id', 'name', 'family', 'phone', 'date', 'time']
        self.tblamar = ttk.Treeview(self.frmamar, columns=row, show='headings', height=35)

        self.tblamar.heading('name', text='نام')
        self.tblamar.heading('family', text='فامیلی')
        self.tblamar.heading('phone', text='شماره')
        self.tblamar.heading('date', text='تایخ')
        self.tblamar.heading('time', text='ساعت')

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

        self.frmdr_prshode = Frame(self.screendr, width=1300, height=800, bg="#2C3E50")
        result = self.countpr_shode()

        # برچسب‌ها با استایل‌های جدید
        label_style = {
            "background": "#2C3E50",
            "foreground": "#ECF0F1",
            "font": ("Arial", 12),
            "padx": 10,
            "pady": 5
        }

        self.lblcountday = Label(self.frmdr_prshode, text=f"تعداد اقساط امروز: {result[2][0][0]}")
        self.lblcountday.config(**label_style)
        self.lblcountday.place(x=780, y=420)

        self.lblkarmozdday = Label(self.frmdr_prshode, text=f" کارمزد : {result[3]:,}")
        self.lblkarmozdday.config(**label_style)
        self.lblkarmozdday.place(x=620, y=460)

        self.lblkolday = Label(self.frmdr_prshode, text=f" پرداختی : {result[4]:,}")
        self.lblkolday.config(**label_style)
        self.lblkolday.place(x=950, y=460)

        self.lblcountmonth = Label(self.frmdr_prshode, text=f"تعداد اقساط این ماه: {result[0][0][0]}")
        self.lblcountmonth.config(**label_style)
        self.lblcountmonth.place(x=780, y=500)

        self.lblkarmozdmonth = Label(self.frmdr_prshode, text=f" کارمزد : {result[5]:,}")
        self.lblkarmozdmonth.config(**label_style)
        self.lblkarmozdmonth.place(x=620, y=540)

        self.lblkolmonth = Label(self.frmdr_prshode, text=f" پرداختی ها: {result[6]:,}")
        self.lblkolmonth.config(**label_style)
        self.lblkolmonth.place(x=950, y=540)

        self.lblcountall = Label(self.frmdr_prshode, text=f"کل اقساط: {result[1][0][0]}")
        self.lblcountall.config(**label_style)
        self.lblcountall.place(x=780, y=580)

        self.lblkarmozdall = Label(self.frmdr_prshode, text=f" کارمزد : {result[7]:,}")
        self.lblkarmozdall.config(**label_style)
        self.lblkarmozdall.place(x=620, y=620)

        self.lblkolall = Label(self.frmdr_prshode, text=f" پرداختی ها: {result[8]:,}")
        self.lblkolall.config(**label_style)
        self.lblkolall.place(x=950, y=620)

        self.lblkol = Label(self.frmdr_prshode, text=f" مبلغ کلی: {result[9]:,}")
        self.lblkol.config(**label_style)
        self.lblkol.place(x=780, y=660)
        baghimande = result[9] - result[8]

        self.lblpardakhti = Label(self.frmdr_prshode, text=f"پرداختی ها: {result[8]:,}")
        self.lblpardakhti.config(**label_style)
        self.lblpardakhti.place(x=620, y=700)

        self.lblbaghimande = Label(self.frmdr_prshode, text=f" باقیمانده: {baghimande:,}")
        self.lblbaghimande.config(**label_style)
        self.lblbaghimande.place(x=950, y=700)

        self.lbltblemroz = Label(self.frmdr_prshode, text=" اقساط امروز")
        self.lbltblemroz.configure(**label_style)
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

        self.tblprshodeemroz.heading("code", text='کد')
        self.tblprshodeemroz.heading("name", text='نام')
        self.tblprshodeemroz.heading("phone", text='شماره')
        self.tblprshodeemroz.heading("price", text='مبلغ قسط')
        self.tblprshodeemroz.heading("time", text='تاریخ')
        self.tblprshodeemroz.heading("status", text='وضعیت')
        self.tblprshodeemroz.place(x=10, y=40)

        self.inserttblprshodeemroz()

        self.lbltblmonth = Label(self.frmdr_prshode, text="اقساط این ماه")
        self.lbltblmonth.configure(**label_style)
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

        self.tblprshodemah.heading("code", text='کد')
        self.tblprshodemah.heading("name", text='نام')
        self.tblprshodemah.heading("phone", text='شماره')
        self.tblprshodemah.heading("price", text='مبلغ قسط')
        self.tblprshodemah.heading("time", text='تاریخ')
        self.tblprshodemah.heading("status", text='وضعیت')
        self.tblprshodemah.place(x=650, y=40)

        self.lbltblmonth = Label(self.frmdr_prshode, text="همه قسط ها")
        self.lbltblmonth.configure(**label_style)
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

        self.tblprshodekol.heading("code", text='کد')
        self.tblprshodekol.heading("name", text='نام')
        self.tblprshodekol.heading("phone", text='شماره')
        self.tblprshodekol.heading("price", text='مبلغ قسط')
        self.tblprshodekol.heading("time", text='تاریخ')
        self.tblprshodekol.heading("status", text='وضعیت')
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
        # فرم اصلی برای پرداخت نشده ها
        self.frmprnashode = Frame(self.screendr, width=1300, height=800, bg="#2C3E50")

        # گرفتن نتایج از تابع countpr_nashode()
        result = self.countpr_nashode()

        # برچسب‌ها با استایل‌های جدید
        label_style = {
            "background": "#2C3E50",
            "foreground": "#ECF0F1",
            "font": ("Arial", 12),
            "padx": 10,
            "pady": 5
        }

        # برچسب "امروز"
        lbltblemroz = Label(self.frmprnashode, text="امروز", **label_style)
        lbltblemroz.place(x=300, y=12)

        # تعداد پرداخت نشده‌های امروز
        lblcountday = Label(self.frmprnashode, text=f"تعداد پرداخت نشده های امروز: {result[2][0][0]}", **label_style)
        lblcountday.place(x=780, y=420)

        # کارمزد امروز
        lblkarmozdday = Label(self.frmprnashode, text=f"کارمزد: {result[1]:,}", **label_style)
        lblkarmozdday.place(x=620, y=460)

        # مبلغ قسط امروز
        lblkolday = Label(self.frmprnashode, text=f"مبلغ قسط: {result[0]:,}", **label_style)
        lblkolday.place(x=950, y=460)

        # تعداد پرداخت نشده‌های این ماه
        lblcountmonth = Label(self.frmprnashode, text=f"تعداد پرداخت نشده های این ماه: {result[5][0][0]}", **label_style)
        lblcountmonth.place(x=780, y=500)

        # کارمزد این ماه
        lblkarmozdmonth = Label(self.frmprnashode, text=f"کارمزد: {result[4]:,}", fg="white", bg="black", **label_style)
        lblkarmozdmonth.place(x=620, y=540)

        # مبلغ قسط این ماه
        lblkolmonth = Label(self.frmprnashode, text=f"مبلغ قسط: {result[3]:,}", fg="white", bg="black", **label_style)
        lblkolmonth.place(x=950, y=540)

        # تعداد پرداخت نشده‌های کل
        lblcountall = Label(self.frmprnashode, text=f"کل پرداخت نشده ها: {result[8][0][0]}", **label_style)
        lblcountall.place(x=780, y=580)

        # کارمزد کل
        lblkarmozdall = Label(self.frmprnashode, text=f"کارمزد: {result[7]:,}", fg="white", bg="black", **label_style)
        lblkarmozdall.place(x=620, y=620)

        # مبلغ قسط کل
        lblkolall = Label(self.frmprnashode, text=f"مبلغ قسط: {result[6]:,}", fg="white", bg="black", **label_style)
        lblkolall.place(x=950, y=620)

        # نمایش فرم
        self.frmprnashode.place(x=0, y=0)

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

        self.tblprnashodeemroz.heading("code", text='کد')
        self.tblprnashodeemroz.heading("name", text='نام')
        self.tblprnashodeemroz.heading("phone", text='شماره')
        self.tblprnashodeemroz.heading("price", text='مبلغ قسط')
        self.tblprnashodeemroz.heading("time", text='تاریخ')
        self.tblprnashodeemroz.heading("status", text='وضعیت')
        self.tblprnashodeemroz.place(x=10, y=40)

        self.inserttblornashodeday()

        lbltblmonth = Label(self.frmprnashode, text="این ماه")
        lbltblmonth.configure( **label_style)
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

        self.tblprnashodemah.heading("code", text='کد')
        self.tblprnashodemah.heading("name", text='نام')
        self.tblprnashodemah.heading("phone", text='شماره')
        self.tblprnashodemah.heading("price", text='مبلغ قسط')
        self.tblprnashodemah.heading("time", text='تاریخ')
        self.tblprnashodemah.heading("status", text='وضعیت')
        self.tblprnashodemah.place(x=650, y=40)
        self.inserttblprshodemonth()

        lbltblmonth = Label(self.frmprnashode, text="همه اقساط")
        lbltblmonth.configure(**label_style)
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

        self.tblprnashodekol.heading("code", text='کد')
        self.tblprnashodekol.heading("name", text='نام')
        self.tblprnashodekol.heading("phone", text='شماره')
        self.tblprnashodekol.heading("price", text='مبلغ قسط')
        self.tblprnashodekol.heading("time", text='تاریخ')
        self.tblprnashodekol.heading("status", text='وضعیت')
        self.tblprnashodekol.place(x=10, y=440)
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
        self.frmsearchdate = Frame(self.screendr, width=1300, height=800, bg="#2C3E50")

        year = jalali_date_now.year

        # استایل برای ورودی سال
        self.txtyear = StringVar()
        self.year = Entry(self.frmsearchdate, textvariable=self.txtyear, justify='center', font=("Arial", 14),
                          bg="#34495E", fg="white", bd=2, relief="solid", highlightthickness=2,
                          highlightcolor="#16A085")
        self.txtyear.set(f"{jalali_date_now.year}")
        self.year.bind("<Button-1>", self.clearyear)
        self.year.place(x=500, y=10)

        # استایل برای ورودی ماه
        self.txtmonth = StringVar()
        self.month = Entry(self.frmsearchdate, textvariable=self.txtmonth, justify='center', font=("Arial", 14),
                           bg="#34495E", fg="white", bd=2, relief="solid", highlightthickness=2,
                           highlightcolor="#16A085")
        self.txtmonth.set("Month")
        self.month.bind("<Button-1>", self.clearmonth)
        self.month.place(x=700, y=10)

        # رادیو باتن‌ها (پرداخت شده، پرداخت نشده، همه)
        self.radiovalues = IntVar()

        # تغییر استایل رادیو باتن‌ها با پر شدن رنگ مشکی در حالت پیش‌فرض
        radiopaid = Radiobutton(self.frmsearchdate, text="پرداخت شده", value=1, bg="black",
                                font=("Arial", 12, "bold"), fg="red", variable=self.radiovalues,
                                indicatoron=False)  # indicatoron=False باعث می‌شود که رادیو باتن پر شود.
        radionotpaid = Radiobutton(self.frmsearchdate, text="پرداخت نشده", value=2, bg="black",
                                   font=("Arial", 12, "bold"), fg="red", variable=self.radiovalues,
                                   indicatoron=False)
        radioall = Radiobutton(self.frmsearchdate, text="همه", value=3, bg="black",
                               font=("Arial", 12, "bold"), fg="red", variable=self.radiovalues,
                               indicatoron=False)

        # قرار دادن رادیو باتن‌ها در مکان‌های مشخص شده
        radiopaid.place(x=550, y=50)
        radionotpaid.place(x=650, y=50)
        radioall.place(x=770, y=50)

        self.btnoksearchdate = Button(self.frmsearchdate, text="جستجو", bg="#16A085", fg="white",
                                      font=("Arial", 14, "bold"), bd=0, relief="flat", command=self.oneclicksearchdate)
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

        self.tblsearchdate.heading("code", text='کد')
        self.tblsearchdate.heading("name", text='نام')
        self.tblsearchdate.heading("phone", text='شماره')
        self.tblsearchdate.heading("price", text='مبلغ قسط')
        self.tblsearchdate.heading("time", text='تاریخ')
        self.tblsearchdate.heading("status", text='وضعیت')
        self.tblsearchdate.place(x=370, y=150)

        # برچسب‌های نتیجه جستجو
        self.lblcountsearch = Label(self.frmsearchdate, fg="white", bg="#34495E", font=("Helvetica", 14, "bold"),
                                    pady=5, padx=10, relief="solid", bd=2)
        self.lblcountsearch.place_forget()

        self.lblkarmozdsearchshode = Label(self.frmsearchdate, fg="white", bg="#34495E", font=("Helvetica", 14, "bold"),
                                           pady=5, padx=10, relief="solid", bd=2)
        self.lblkarmozdsearchshode.place_forget()

        self.lblallpricesearchshode = Label(self.frmsearchdate, fg="white", bg="#34495E",
                                            font=("Helvetica", 14, "bold"), pady=5, padx=10, relief="solid", bd=2)
        self.lblallpricesearchshode.place_forget()

        self.lblkarmozdsearchnashode = Label(self.frmsearchdate, fg="white", bg="#34495E",
                                             font=("Helvetica", 14, "bold"), pady=5, padx=10, relief="solid", bd=2)
        self.lblkarmozdsearchnashode.place_forget()

        self.lblallpricesearchnashode = Label(self.frmsearchdate, fg="white", bg="#34495E",
                                              font=("Helvetica", 14, "bold"), pady=5, padx=10, relief="solid", bd=2)
        self.lblallpricesearchnashode.place_forget()

        # قرار دادن فرم در صفحه
        self.frmsearchdate.place(x=0, y=0)

        # اعمال تنظیمات اضافی
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
            self.lblcountsearch.config(text=f"تعداد اقساط پرداخت شده این ماه : {countmount[0][0]}")
            self.lblcountsearch.place(x=550, y=690)
            pricemonth = user.allusersmonth("aghsat", self.year.get(), self.month.get(), "paid")
            karmozd = 0
            all1 = 0
            for item in pricemonth:
                a = item[5].replace(',', '')
                b = item[4].replace(',', '')
                karmozd += int(a)
                all1 += int(b)
            self.lblkarmozdsearchshode.place(x=350, y=730)
            self.lblkarmozdsearchshode.config(text=f"کارمزد : {karmozd:,}")
            self.lblallpricesearchshode.place(x=800, y=730)
            self.lblallpricesearchshode.config(text=f"مبلغ کل : {all1:,}")
            self.lblkarmozdsearchnashode.place_forget()
            self.lblallpricesearchnashode.place_forget()
        elif self.radiovalues.get() == 2:
            countmount = user.CountaghsatMonth(self.year.get(), self.month.get(), "not paid")
            self.lblcountsearch.place(x=550, y=690)
            self.lblcountsearch.config(text=f"تعداد پرداخت نشده های این ماه : {countmount[0][0]}")
            pricemonth = user.allusersmonth("aghsat", self.year.get(), self.month.get(), "not paid")
            karmozd = 0
            all1 = 0
            for item in pricemonth:
                a = item[5].replace(',', '')
                b = item[4].replace(',', '')
                karmozd += int(a)
                all1 += int(b)
            self.lblkarmozdsearchshode.place(x=350, y=730)
            self.lblkarmozdsearchshode.config(text=f"کارمزد : {karmozd:,}")
            self.lblallpricesearchshode.place(x=800, y=730)
            self.lblallpricesearchshode.config(text=f"مبلغ کل : {all1:,}")
            self.lblkarmozdsearchnashode.place_forget()
            self.lblallpricesearchnashode.place_forget()
        elif self.radiovalues.get() == 3:
            self.cleartblsearchdata()
            countmount = user.CountaghsatMonth2(self.year.get(), self.month.get())
            self.lblcountsearch.place(x=550, y=690)
            self.lblcountsearch.config(text=f"تعداد پرداخت شده و نشده های این ماه : {countmount[0][0]}")
            pricemonth = user.allusersmonth2("aghsat", self.year.get(), self.month.get())
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
            self.lblkarmozdsearchshode.config(text=f"کارمزد پرداخت شده : {karmozdprshode:,}")
            self.lblallpricesearchshode.place(x=800, y=730)
            self.lblallpricesearchshode.config(text=f"اقساط پرداخت شده : {allprshode:,}")
            self.lblkarmozdsearchnashode.place(x=350, y=770)
            self.lblkarmozdsearchnashode.config(text=f"کارمزد پرداخت نشده : {karmozdprnashode:,}")
            self.lblallpricesearchnashode.place(x=800, y=770)
            self.lblallpricesearchnashode.config(text=f"اقساط پرداخت نشده : {allprnashode:,}")

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
        self.lblkarmozdsearchshode.config(text=f"کارمزد پرداخت شده : {karmozdprshode:,}")
        self.lblallpricesearchshode.place(x=800, y=730)
        self.lblallpricesearchshode.config(text=f"اقساط پرداخت شده : {allprshode:,}")
        self.lblkarmozdsearchnashode.place(x=350, y=770)
        self.lblkarmozdsearchnashode.config(text=f"کارمزد پرداخت نشده : {karmozdprnashode:,}")
        self.lblallpricesearchnashode.place(x=800, y=770)
        self.lblallpricesearchnashode.config(text=f"اقساط پرداخت نشده : {allprnashode:,}")

    def search_user(self, e):
        # فرم جستجو
        self.frmsearchuser = Frame(self.screendr, bg="#2C3E50", width=1300, height=800)

        # استایل برای کادر جستجو
        self.txtsearchuser = Entry(self.frmsearchuser, justify="center", font=("Arial", 14), bg="#34495E", fg="white",
                                   bd=2, relief="solid", highlightthickness=2, highlightcolor="#16A085")
        self.txtsearchuser.place(x=1050, y=10)

        # دکمه جستجو
        self.btnsearchuser = Button(self.frmsearchuser, text="جستجو", command=self.oneclicksearch,
                                    font=("Arial", 12, "bold"), bg="#16A085", fg="white", bd=0, relief="flat", padx=15,
                                    pady=10)
        self.btnsearchuser.place(x=970, y=10)

        # برچسب‌ها با استایل‌های جدید
        label_style = {
            "background": "#2C3E50",
            "foreground": "#ECF0F1",
            "font": ("Arial", 12),
            "padx": 10,
            "pady": 5
        }

        # نام
        self.lblname = Label(self.frmsearchuser, text="نام:", **label_style)
        self.lblname.place(x=1000, y=100)

        # تلفن
        self.lblphone = Label(self.frmsearchuser, text="تلفن:", **label_style)
        self.lblphone.place(x=1000, y=140)

        # پرداخت شده‌ها
        self.lblprshode = Label(self.frmsearchuser, text="پرداخت شده:", **label_style)
        self.lblprshode.place(x=650, y=380)

        # کارمزد پرداخت شده‌ها
        self.lblkarmozdprshode = Label(self.frmsearchuser, text="کارمزد:", **label_style)
        self.lblkarmozdprshode.place(x=500, y=440)

        # مبلغ کل پرداخت شده‌ها
        self.lblallprshode = Label(self.frmsearchuser, text="مبلغ کل:", **label_style)
        self.lblallprshode.place(x=850, y=440)

        # پرداخت نشده‌ها
        self.lblprnashode = Label(self.frmsearchuser, text="پرداخت نشده:", **label_style)
        self.lblprnashode.place(x=650, y=500)

        # کارمزد پرداخت نشده‌ها
        self.lblkarmozdprnashode = Label(self.frmsearchuser, text="کارمزد:", **label_style)
        self.lblkarmozdprnashode.place(x=500, y=560)

        # مبلغ کل پرداخت نشده‌ها
        self.lblallprnashode = Label(self.frmsearchuser, text="مبلغ کل:", **label_style)
        self.lblallprnashode.place(x=850, y=560)

        # اضافه کردن افکت hover برای دکمه
        self.btnsearchuser.bind("<Enter>", lambda e: e.widget.config(bg="#1ABC9C"))
        self.btnsearchuser.bind("<Leave>", lambda e: e.widget.config(bg="#16A085"))

        # اضافه کردن افکت hover برای فیلد جستجو
        self.txtsearchuser.bind("<Enter>", lambda e: e.widget.config(bg="#16A085"))
        self.txtsearchuser.bind("<Leave>", lambda e: e.widget.config(bg="#34495E"))

        # اضافه کردن سایه به برچسب‌ها برای تاثیر عمق
        for label in [self.lblname, self.lblphone, self.lblprshode, self.lblkarmozdprshode, self.lblallprshode,
                      self.lblprnashode, self.lblkarmozdprnashode, self.lblallprnashode]:
            label.config(highlightthickness=1, highlightbackground="#16A085")

        lblaghsat = Label(self.frmsearchuser, text='اقساط')
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

        self.tblsearchuserghest.heading("code", text='کد')
        self.tblsearchuserghest.heading("price", text='مبلغ قسط')
        self.tblsearchuserghest.heading("time", text='تاریخ')
        self.tblsearchuserghest.heading("status", text='وضعیت')
        self.tblsearchuserghest.place(x=10, y=40)

        lbldevice = Label(self.frmsearchuser, text='دستگاها')
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

        self.tblsearchuserdevice.heading('code', text='کد')
        self.tblsearchuserdevice.heading('serial', text='سریال')
        self.tblsearchuserdevice.heading('price', text='مبلغ')
        self.tblsearchuserdevice.heading('model', text='مدل')
        self.tblsearchuserdevice.place(x=10, y=400)

        lbltype = Label(self.frmsearchuser, text='چک و طلا')
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

        self.tblsearchusertype.heading('code', text='کد')
        self.tblsearchusertype.heading('type', text='نوع')
        self.tblsearchusertype.heading('type / serial', text='نوع / سریال')
        self.tblsearchusertype.heading('g / m', text='گرم / مبلغ')
        self.tblsearchusertype.place(x=500, y=40)

        self.frmsearchuser.place(x=0, y=0)

    def oneclicksearch(self):
        if self.txtsearchuser.get() == '':
            messagebox.showwarning(title='خطا', message='فید جستجو خالی است')
        elif not self.txtsearchuser.get().isdigit():
            messagebox.showwarning(title='Warning', message='فیلد جسنجو را با عدد پر کنید')
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
                self.lblname.configure(text=f"نام : {item[2]}")
                self.lblphone.configure(text=f"شماره : {item[3]}")
                self.tblsearchuserghest.insert('', 'end', values=item)
        else:
            messagebox.showwarning(title='خطا', message='کاربر پیدا نشد')

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

        self.lblprshode.configure(text=f"پرداخت شده ها : {result[0][0]}")
        self.lblprnashode.configure(text=f"پرداخت نشده ها : {result1[0][0]}")
        self.lblkarmozdprshode.configure(text=f"کارمزد : {karmozdprshode:,}")
        self.lblkarmozdprnashode.configure(text=f"کارمزد : {karmozdprnashode:,}")
        self.lblallprshode.configure(text=f"مبلغ کل : {allpriceprshode:,}")
        self.lblallprnashode.configure(text=f"مبلغ کل : {allkarmozdprnashode:,}")






