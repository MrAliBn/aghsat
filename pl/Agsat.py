from tkinter import messagebox, ttk
from tkinter import *
import time
import jdatetime
from dal.repository import Repository
from time import strftime
from persiantools.jdatetime import JalaliDate

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
        self.mnu.add_command(label="Login Dr", foreground="white")
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

            self.txtendgest = Entry(self.frmsabtaghsat)
            self.txtendgest.configure(bg="white", fg="black", bd=3, justify="center")
            self.txtendgest.place(x=830, y=290)

            self.lblendgest = Label(self.frmsabtaghsat)
            self.lblendgest.configure(text="End gest", fg="black")
            self.lblendgest.place(x=700, y=290)

            self.txtmablaghgest = Entry(self.frmsabtaghsat)
            self.txtmablaghgest.configure(bg="white", fg="black", bd=3, justify="center")
            self.txtmablaghgest.place(x=830, y=340)

            self.lblmablaghgest = Label(self.frmsabtaghsat)
            self.lblmablaghgest.configure(text="mablagh aghsat", fg="black")
            self.lblmablaghgest.place(x=700, y=340)

            self.txtmablaghesmi = Entry(self.frmsabtaghsat)
            self.txtmablaghesmi.configure(bg="white", fg="black", bd=3, justify="center")
            self.txtmablaghesmi.place(x=480, y=340)

            self.lblmablaghesmi = Label(self.frmsabtaghsat)
            self.lblmablaghesmi.configure(text="mablagh esmi", fg="black")
            self.lblmablaghesmi.place(x=350, y=340)

            self.txtmablaghkamel = Entry(self.frmsabtaghsat)
            self.txtmablaghkamel.configure(bg="white", fg="black", bd=3, justify="center")
            self.txtmablaghkamel.place(x=480, y=390)

            self.lblmablaghkamel = Label(self.frmsabtaghsat)
            self.lblmablaghkamel.configure(text="mablagh kamel", fg="black")
            self.lblmablaghkamel.place(x=350, y=390)

            self.txtkarmozd = Entry(self.frmsabtaghsat)
            self.txtkarmozd.configure(bg="white", fg="black", bd=3, justify="center")
            self.txtkarmozd.place(x=830, y=390)

            self.lbltxtkarmozd = Label(self.frmsabtaghsat)
            self.lbltxtkarmozd.configure(text="karmozd", fg="black")
            self.lbltxtkarmozd.place(x=700, y=390)

            self.txtgest = ttk.Combobox(self.frmsabtaghsat, background="white", foreground="black", justify="center",
                                        state="readonly", width=19)
            self.txtgest.set(0)
            self.txtgest['values'] = self.aghsat()
            self.txtgest.place(x=650, y=460)

            self.lblaghsat = Label(self.frmsabtaghsat)
            self.lblaghsat.configure(text="aghsat", fg="black")
            self.lblaghsat.place(x=580, y=460)

            self.btnadd = Button(self.frmsabtaghsat)
            self.btnadd.configure(text="Register", bg="green", fg="black", bd=5, command=self.Onclicksabtaghsat)
            self.btnadd.place(x=680, y=500)

            self.lbldatee = Label(self.frmsabtaghsat, font="arial 12 bold")
            self.update_timee()
            self.lbldatee.place(x=630, y=10)

            self.frmsabtaghsat.place(x=0, y=0)

            self.start_date_button = Button(self.frmsabtaghsat, text=">",
                                            command=self.open_start_date_calendar, bg="#4CAF50", fg="white")
            self.start_date_button.place(x=658, y=290)

            self.end_date_button = Button(self.frmsabtaghsat, text="<",
                                          command=self.open_end_date_calendar, bg="#FF5722", fg="white")
            self.end_date_button.place(x=1010, y=290)

            # Initialize calendar window as None
            self.calendar_window = None

    def Onclicksabtaghsat(self):
        if not self.txtserial.get().isdigit() or self.txtserial.get() == '':
            messagebox.showerror("Error", "Fill in the serial part with a number")
            self.txtserial.focus()
        elif self.txtmodel.get() == '':
            messagebox.showerror("Error", "Fill in the model section")
            self.txtmodel.focus()
        elif self.txtstartgest.get() == '':
            messagebox.showerror("Error", "Fill in the startgest section")
            self.txtstartgest.focus()
        elif self.txtendgest.get() == '':
            messagebox.showerror("Error", "Fill in the endgest section")
        elif self.txtkarmozd.get() == '' or not self.txtkarmozd.get().isdigit():
            messagebox.showerror("Error", "Fill in the karmozd part with a number")
            self.txtkarmozd.focus()
        elif self.txtmablaghesmi.get() == '' or not self.txtmablaghesmi.get().isdigit():
            messagebox.showerror("Error", "Fill in the mablaghesmi part with a number")
            self.txtmablaghesmi.focus()
        elif self.txtmablaghgest.get() == '' or not self.txtmablaghgest.get().isdigit():
            messagebox.showerror("Error", "Fill in the mablaghgesat part with a number")
            self.txtmablaghgest.focus()
        elif self.txtmablaghkamel.get() == '' or not self.txtmablaghkamel.get().isdigit():
            messagebox.showerror("Error", "Fill in the mablaghkamel part with a number")
            self.txtmablaghkamel.focus()
        else:
            self.sabtaghsatt()

    def sabtaghsatt(self):
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
            obj = self.txtname.get(), self.Phone.get(), self.txtmablaghgest.get(), installment_date_shamsi_str, 'not paid'
            aghsat.addghest("aghsat", obj)

    # -------------------------------------------- taghvim ---------------------------------------

    def open_start_date_calendar(self):
        """Open calendar window for selecting start date"""
        self.open_calendar_window(self.txtstartgest)

    def open_end_date_calendar(self):
        """Open calendar window for selecting end date"""
        self.open_calendar_window(self.txtendgest)

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

        # -------------------------------------------- Clock ---------------------------------------

            # self.canvas_size = 200
            # self.center_x = self.canvas_size // 2
            # self.center_y = self.canvas_size // 2
            # self.radius = 80  # شعاع ساعت کوچکتر شده است
            #
            # self.canvas_size = 250
            # self.center_x = self.canvas_size // 2
            # self.center_y = self.canvas_size // 2
            # self.radius = 100
            #
            # # ساخت بوم
            # self.canvas = Canvas(self.frmsabtaghsat, width=self.canvas_size, height=self.canvas_size, bg="black",
            #                         highlightthickness=0)
            # self.canvas.place(x=1020, y=10)
            #
            # # رسم قاب و نشانه‌ها
            # self.setup_canvas()
            # self.update_clock()

    def update_timee(self):
        current_time = time.strftime("%H:%M:%S")
        self.lbldatee.config(text=f"{date} - {current_time}")
        self.frmsabtaghsat.after(1000, self.update_timee)

    # def draw_numbers(self):
    #     """رسم اعداد خاص (3، 6، 9، و 12)"""
    #     positions = {3: 90, 6: 180, 9: 270, 12: 0}  # اعداد و زوایای آنها
    #     for num, angle_deg in positions.items():
    #         angle = math.radians(angle_deg)
    #         x = self.center_x + (self.radius - 30) * math.sin(angle)
    #         y = self.center_y - (self.radius - 30) * math.cos(angle)
    #         self.canvas.create_text(x, y, text=str(num), font=("Helvetica", 14, "bold"), fill="gray")
    #
    # def draw_marks(self):
    #     """رسم نشانه‌های ساعت (خطوط کوتاه)"""
    #     for i in range(60):
    #         angle = math.radians(i * 6)  # هر نشانه 6 درجه
    #         length = 10 if i % 5 == 0 else 5  # نشانه‌های 5 تایی بلندتر هستند
    #         x_start = self.center_x + (self.radius - length) * math.sin(angle)
    #         y_start = self.center_y - (self.radius - length) * math.cos(angle)
    #         x_end = self.center_x + self.radius * math.sin(angle)
    #         y_end = self.center_y - self.radius * math.cos(angle)
    #         color = "#d7ad03" if i % 5 == 0 else "gray"
    #         width = 2 if i % 5 == 0 else 1
    #         self.canvas.create_line(x_start, y_start, x_end, y_end, fill=color, width=width)
    #
    # def draw_hand(self, angle, length, width, color):
    #     """رسم عقربه‌ها"""
    #     x_end = self.center_x + length * math.sin(angle)
    #     y_end = self.center_y - length * math.cos(angle)
    #     self.canvas.create_line(
    #         self.center_x, self.center_y, x_end, y_end, width=width, fill=color, capstyle=ROUND, tags="hand"
    #     )
    #
    # def update_clock(self):
    #     """به‌روزرسانی عقربه‌ها با حرکت روان"""
    #     # زمان فعلی
    #     current_time = time.localtime()
    #     hour = current_time.tm_hour % 12
    #     minute = current_time.tm_min
    #     second = current_time.tm_sec
    #     millis = int(round(time.time() * 1000)) % 1000  # میلی‌ثانیه فعلی
    #
    #     # محاسبه زوایا
    #     second_angle = math.radians((second + millis / 1000) * 6)  # حرکت روان ثانیه
    #     minute_angle = math.radians((minute + second / 60) * 6)  # حرکت روان دقیقه
    #     hour_angle = math.radians((hour + minute / 60) * 30)  # حرکت روان ساعت
    #
    #     # پاک کردن عقربه‌های قبلی
    #     self.canvas.delete("hand")
    #
    #     # رسم عقربه‌ها
    #     self.draw_hand(second_angle, self.radius - 20, 2, "red")  # عقربه ثانیه
    #     self.draw_hand(minute_angle, self.radius - 40, 4, "white")  # عقربه دقیقه
    #     self.draw_hand(hour_angle, self.radius - 60, 6, "gold")  # عقربه ساعت
    #
    #     # به‌روزرسانی سریع‌تر برای حرکت روان
    #     self.canvas.after(50, self.update_clock)
    #
    # def setup_canvas(self):
    #     """تنظیمات اولیه بوم"""
    #     # رسم قاب ساعت
    #     self.canvas.create_oval(
    #         10, 10, self.canvas_size - 10, self.canvas_size - 10, outline="gray", width=4
    #     )
    #
    #     # رسم اعداد و نشانه‌ها
    #     self.draw_numbers()
    #     self.draw_marks()

    # -------------------------------------------- Menu right ---------------------------------------

    def clicksabtaghsat(self, e):
        self.sabtaghsat()

    def clickinfoaghsat(self, e):
        self.infoaghsat()

    # -------------------------------------------- info aghsat---------------------------------------

    def infoaghsat(self):
        user = Repository()
        result = user.Exist("users", self.Phone.get())
        for item in result:

            self.frminfoaghsat = Frame(self.frmscreenuser, width=1300, height=800)

            self.lbldate = Label(self.frminfoaghsat, font="arial 12 bold")
            self.update_time()
            self.lbldate.place(x=20, y=20)

            lblid = Label(self.frminfoaghsat, text=f"Number : {item[0]}", font="arial 12 bold")
            lblid.place(x=20, y=100)

            lblname = Label(self.frminfoaghsat, text=f"Name : {item[1]}", font="arial 12 bold")
            lblname.place(x=20, y=180)

            lblfamily = Label(self.frminfoaghsat, text=f"Family : {item[2]}", font="arial 12 bold")
            lblfamily.place(x=20, y=260)

            lblphone = Label(self.frminfoaghsat, text=f"Phone : {item[3]}", font="arial 12 bold")
            lblphone.place(x=20, y=340)

            lbldateregister = Label(self.frminfoaghsat, text=f"Date-Start : {item[4]}", font="arial 12 bold")
            lbldateregister.place(x=20, y=420)

            lbltimeregister = Label(self.frminfoaghsat, text=f"Time-Start : {item[5]}", font="arial 12 bold")
            lbltimeregister.place(x=20, y=500)

            self.frminfoaghsat.place(x=0, y=0)

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


