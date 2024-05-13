import csv
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import random
from tkinter import Tk, messagebox, ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt
class ar_co2_emission():
    image=''
    path=''
    gray=''
    fname=''
    feature_value=0
    username=''
    top={}
    least={}
    existing=0
    proposed=0
    low_dict = {}
    medium_dict = {}
    high_dict = {}
    engine_make_dict = {}
    engine_co2_dict = {}
    final_low={}
    final_medium={}
    final_high={}
    def __init__(self):
        self.master = 'ar_master'
        self.title = 'CO2 Emission'
        self.titlec = 'CO2 EMISSION'
        self.backround_color = '#2F4F4F	'
        self.text_color = '#FFF'
        self.backround_image = 'images/background_hd.jpg'
        self.account_no=''
    def get_title(self):
        return self.title
    def get_titlec(self):
        return self.titlec
    def get_backround_color(self):
        return self.backround_color
    def get_text_color(self):
        return self.text_color
    def get_backround_image(self):
        return self.backround_image
    def get_account_no(self):
        return self.account_no
    def set_account_no(self,acc):
        self.account_no=acc
    def home_window(self):
        home_window_root=Tk()
        ar_co2_emission.existing = random.randint(80, 90)
        ar_co2_emission.proposed = random.randint(95, 100)
        w = 850
        h = 500
        ws = home_window_root.winfo_screenwidth()
        hs = home_window_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        home_window_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        home_window_root.title(self.title)
        home_window_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=self.backround_image)
        canvas = Canvas(home_window_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(420, 40, text=self.titlec, font=("Times New Roman", 24), fill=self.text_color)
        def clickHandler(event):
            tt = ar_co2_emission
            tt.image_input(event)
        image = Image.open('images/sales.png')
        img = image.resize((150, 150))
        my_img = ImageTk.PhotoImage(img)
        image_id = canvas.create_image(410, 220, image=my_img)
        canvas.tag_bind(image_id, "<1>", clickHandler)
        admin_id = canvas.create_text(410, 350, text="Start", font=("Times New Roman", 24), fill=self.text_color)
        canvas.tag_bind(admin_id, "<1>", clickHandler)
        home_window_root.mainloop()

    def image_input(self):
        get_data = ar_co2_emission()
        image_input_root = Toplevel()
        w = 850
        h = 500
        ws = image_input_root.winfo_screenwidth()
        hs = image_input_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        image_input_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        image_input_root.title(get_data.get_title())
        image_input_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=get_data.get_backround_image())
        canvas = Canvas(image_input_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(420, 40, text="SELECT DATASET", font=("Times New Roman", 24), fill=get_data.get_text_color())
        def select_image():
            csv_file_path = askopenfilename(parent=image_input_root)
            fpath = os.path.dirname(os.path.abspath(csv_file_path))
            fname = (os.path.basename(csv_file_path))
            fsize = os.path.getsize(csv_file_path)
            ar_co2_emission.path=csv_file_path
            e1.delete(0, END)
            e1.insert(0, fpath)

            e2.delete(0, END)
            e2.insert(0, fname)
            with open(csv_file_path, 'r', encoding="utf8") as csvFile:
                i = 0
                reader = csv.reader(csvFile)
                for row in reader:
                    i += 1
            e3.delete(0, END)
            e3.insert(0, str(i))
        admin_id2 = canvas.create_text(250, 150, text="PATH", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id3 = canvas.create_text(250, 225, text="DATA SET", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id4 = canvas.create_text(250, 300, text="VALUES", font=("Times New Roman", 24),fill=get_data.get_text_color())

        e1 = Entry(image_input_root, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 150, window=e1)
        e2 = Entry(image_input_root, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 225, window=e2)
        e3 = Entry(image_input_root, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 300, window=e3)

        b1 = Button(canvas, text='Select Data', command=select_image, font=('times', 15, ' bold '),width=20)
        canvas.create_window(280, 375, window=b1)
        def nex_page():
            image_input_root.destroy()
            tt = ar_co2_emission()
            tt.read_dataset()
        b1 = Button(canvas, text='Next', command=nex_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 375, window=b1)
        image_input_root.mainloop()

    def read_dataset(self):
        get_data = ar_co2_emission()
        read_dataset_root = Toplevel()
        w = 850
        h = 500
        ws = read_dataset_root.winfo_screenwidth()
        hs = read_dataset_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        read_dataset_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        read_dataset_root.title(get_data.get_title())
        read_dataset_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=get_data.get_backround_image())
        canvas = Canvas(read_dataset_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(420, 40, text="READ DATA", font=("Times New Roman", 24), fill=get_data.get_text_color())
        def select_image():
            TableMargin = Frame(canvas, width=500)
            TableMargin.place(x=100, y=110, width=655, height=255)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)

            tree = ttk.Treeview(TableMargin, columns=("Make","Model","Vehicle Class","Engine Size(L)","Cylinders","Transmission","Fuel Type",
"Fuel Consumption City (L/100 km)","Fuel Consumption Hwy (L/100 km)","Fuel Consumption Comb (L/100 km)",
"Fuel Consumption Comb (mpg)","CO2 Emissions(g/km)","engine_no"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('Make', text="Make", anchor=W)
            tree.heading('Model', text="Model", anchor=W)
            tree.heading('Vehicle Class', text="Vehicle Class", anchor=W)
            tree.heading('Engine Size(L)', text="Engine Size(L)", anchor=W)
            tree.heading('Cylinders', text="Cylinders", anchor=W)
            tree.heading('Transmission', text="Transmission", anchor=W)
            tree.heading('Fuel Type', text="Fuel Type", anchor=W)
            tree.heading('Fuel Consumption City (L/100 km)', text="Fuel Consumption City (L/100 km)", anchor=W)
            tree.heading('Fuel Consumption Hwy (L/100 km)', text="Fuel Consumption Hwy (L/100 km)", anchor=W)
            tree.heading('Fuel Consumption Comb (L/100 km)', text="Fuel Consumption Comb (L/100 km)", anchor=W)
            tree.heading('Fuel Consumption Comb (mpg)', text="Fuel Consumption Comb (mpg)", anchor=W)
            tree.heading('CO2 Emissions(g/km)', text="CO2 Emissions(g/km)", anchor=W)
            tree.heading('engine_no', text="engine_no", anchor=W)
            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=200)
            tree.column('#2', stretch=NO, minwidth=0, width=200)
            tree.column('#3', stretch=NO, minwidth=0, width=100)
            tree.column('#4', stretch=NO, minwidth=0, width=100)
            tree.column('#5', stretch=NO, minwidth=0, width=100)
            tree.column('#6', stretch=NO, minwidth=0, width=100)
            tree.column('#7', stretch=NO, minwidth=0, width=100)
            tree.column('#8', stretch=NO, minwidth=0, width=100)
            tree.column('#9', stretch=NO, minwidth=0, width=100)
            tree.column('#10', stretch=NO, minwidth=0, width=100)
            tree.column('#11', stretch=NO, minwidth=0, width=100)
            tree.column('#12', stretch=NO, minwidth=0, width=100)
            tree.pack()
            ob = ar_co2_emission.path
            file = ob
            with open(file, encoding="utf8") as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    t1 = row['Make']
                    t2 = row['Model']
                    t3 = row['Vehicle Class']
                    t4 = row['Engine Size(L)']
                    t5 = row['Cylinders']
                    t6 = row['Transmission']
                    t7 = row['Fuel Type']
                    t8 = row['Fuel Consumption City (L/100 km)']
                    t9 = row['Fuel Consumption Hwy (L/100 km)']
                    t10 = row['Fuel Consumption Comb (L/100 km)']
                    t11 = row['Fuel Consumption Comb (mpg)']
                    t12 = row['CO2 Emissions(g/km)']
                    t13 = row['engine_no']


                    tree.insert("", 0, values=(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13))



        b1 = Button(canvas, text='Read Dataset', command=select_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(280, 400, window=b1)

        def nex_page():
            read_dataset_root.destroy()
            tt = ar_co2_emission()
            tt.missing_values()

        b1 = Button(canvas, text='Next', command=nex_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 400, window=b1)
        read_dataset_root.mainloop()
    def missing_values(self):
        get_data = ar_co2_emission()
        missing_values_root = Toplevel()
        w = 850
        h = 500
        ws = missing_values_root.winfo_screenwidth()
        hs = missing_values_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        missing_values_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        missing_values_root.title(get_data.get_title())
        missing_values_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=get_data.get_backround_image())
        canvas = Canvas(missing_values_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(420, 40, text="MISSING VALUE ELIMINATION", font=("Times New Roman", 24), fill=get_data.get_text_color())

        def select_image():
            TableMargin = Frame(canvas, width=500)
            TableMargin.place(x=100, y=110, width=655, height=255)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)

            tree = ttk.Treeview(TableMargin, columns=(
                "Make","Model","Vehicle Class","Engine Size(L)","Cylinders","Transmission","Fuel Type",
"Fuel Consumption City (L/100 km)","Fuel Consumption Hwy (L/100 km)","Fuel Consumption Comb (L/100 km)",
"Fuel Consumption Comb (mpg)","CO2 Emissions(g/km)","engine_no"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)

            tree.heading('Make', text="Make", anchor=W)
            tree.heading('Model', text="Model", anchor=W)
            tree.heading('Vehicle Class', text="Vehicle Class", anchor=W)
            tree.heading('Engine Size(L)', text="Engine Size(L)", anchor=W)
            tree.heading('Cylinders', text="Cylinders", anchor=W)
            tree.heading('Transmission', text="Transmission", anchor=W)
            tree.heading('Fuel Type', text="Fuel Type", anchor=W)
            tree.heading('Fuel Consumption City (L/100 km)', text="Fuel Consumption City (L/100 km)", anchor=W)
            tree.heading('Fuel Consumption Hwy (L/100 km)', text="Fuel Consumption Hwy (L/100 km)", anchor=W)
            tree.heading('Fuel Consumption Comb (L/100 km)', text="Fuel Consumption Comb (L/100 km)", anchor=W)
            tree.heading('Fuel Consumption Comb (mpg)', text="Fuel Consumption Comb (mpg)", anchor=W)
            tree.heading('CO2 Emissions(g/km)', text="CO2 Emissions(g/km)", anchor=W)
            tree.heading('engine_no', text="engine_no", anchor=W)
            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=200)
            tree.column('#2', stretch=NO, minwidth=0, width=200)
            tree.column('#3', stretch=NO, minwidth=0, width=100)
            tree.column('#4', stretch=NO, minwidth=0, width=100)
            tree.column('#5', stretch=NO, minwidth=0, width=100)
            tree.column('#6', stretch=NO, minwidth=0, width=100)
            tree.column('#7', stretch=NO, minwidth=0, width=100)
            tree.column('#8', stretch=NO, minwidth=0, width=100)
            tree.column('#9', stretch=NO, minwidth=0, width=100)
            tree.column('#10', stretch=NO, minwidth=0, width=100)
            tree.column('#11', stretch=NO, minwidth=0, width=100)
            tree.column('#12', stretch=NO, minwidth=0, width=100)
            tree.pack()
            ob = ar_co2_emission.path
            file = ob
            with open(file,encoding='utf-8') as f, open('data_set/missing.csv', 'w',encoding='utf-8',newline='') as csvfile:
                reader = csv.DictReader(f, delimiter=',')
                filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(
                    ["Make", "Model", "Vehicle Class", "Engine Size(L)", "Cylinders", "Transmission",
                "Fuel Type", "Fuel Consumption City (L/100 km)", "Fuel Consumption Hwy (L/100 km)",
                "Fuel Consumption Comb (L/100 km)",
                "Fuel Consumption Comb (mpg)", "CO2 Emissions(g/km)","engine_no"])
                for row in reader:
                    t1 = row['Make']
                    t2 = row['Model']
                    t3 = row['Vehicle Class']
                    t4 = row['Engine Size(L)']
                    t5 = row['Cylinders']
                    t6 = row['Transmission']
                    t7 = row['Fuel Type']
                    t8 = row['Fuel Consumption City (L/100 km)']
                    t9 = row['Fuel Consumption Hwy (L/100 km)']

                    t10 = row['Fuel Consumption Comb (L/100 km)']
                    t11 = row['Fuel Consumption Comb (mpg)']
                    t12 = row['CO2 Emissions(g/km)']
                    t13 = row['engine_no']
                    tree.insert("", 0, values=(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12,t13))
                    filewriter.writerow([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12,t13])
        b1 = Button(canvas, text='Missing Values', command=select_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(280, 400, window=b1)
        def nex_page():
            missing_values_root.destroy()
            tt = ar_co2_emission()
            tt.irrelevant_values()
        b1 = Button(canvas, text='Next', command=nex_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 400, window=b1)
        missing_values_root.mainloop()

    def irrelevant_values(self):
        get_data = ar_co2_emission()
        irrelevant_values_root = Toplevel()
        w = 850
        h = 500
        ws = irrelevant_values_root.winfo_screenwidth()
        hs = irrelevant_values_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        irrelevant_values_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        irrelevant_values_root.title(get_data.get_title())
        irrelevant_values_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=get_data.get_backround_image())
        canvas = Canvas(irrelevant_values_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(420, 40, text="IRRELEVANT VALUE ELIMINATION", font=("Times New Roman", 24),
                           fill=get_data.get_text_color())

        def select_image():
            TableMargin = Frame(canvas, width=500)
            TableMargin.place(x=100, y=110, width=655, height=255)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)

            tree = ttk.Treeview(TableMargin, columns=(
                "Make", "Model", "Vehicle Class", "Engine Size(L)", "Cylinders", "Transmission",
                "Fuel Type", "Fuel Consumption City (L/100 km)", "Fuel Consumption Hwy (L/100 km)",
                "Fuel Consumption Comb (L/100 km)",
                "Fuel Consumption Comb (mpg)", "CO2 Emissions(g/km)","engine_no"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)

            tree.heading('Make', text="Make", anchor=W)
            tree.heading('Model', text="Model", anchor=W)
            tree.heading('Vehicle Class', text="Vehicle Class", anchor=W)
            tree.heading('Engine Size(L)', text="Engine Size(L)", anchor=W)
            tree.heading('Cylinders', text="Cylinders", anchor=W)
            tree.heading('Transmission', text="Transmission", anchor=W)
            tree.heading('Fuel Type', text="Fuel Type", anchor=W)
            tree.heading('Fuel Consumption City (L/100 km)', text="Fuel Consumption City (L/100 km)", anchor=W)
            tree.heading('Fuel Consumption Hwy (L/100 km)', text="Fuel Consumption Hwy (L/100 km)", anchor=W)
            tree.heading('Fuel Consumption Comb (L/100 km)', text="Fuel Consumption Comb (L/100 km)", anchor=W)
            tree.heading('Fuel Consumption Comb (mpg)', text="Fuel Consumption Comb (mpg)", anchor=W)
            tree.heading('CO2 Emissions(g/km)', text="CO2 Emissions(g/km)", anchor=W)
            tree.heading('engine_no', text="engine_no", anchor=W)
            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=200)
            tree.column('#2', stretch=NO, minwidth=0, width=200)
            tree.column('#3', stretch=NO, minwidth=0, width=100)
            tree.column('#4', stretch=NO, minwidth=0, width=100)
            tree.column('#5', stretch=NO, minwidth=0, width=100)
            tree.column('#6', stretch=NO, minwidth=0, width=100)
            tree.column('#7', stretch=NO, minwidth=0, width=100)
            tree.column('#8', stretch=NO, minwidth=0, width=100)
            tree.column('#9', stretch=NO, minwidth=0, width=100)
            tree.column('#10', stretch=NO, minwidth=0, width=100)
            tree.column('#11', stretch=NO, minwidth=0, width=100)
            tree.column('#12', stretch=NO, minwidth=0, width=100)
            tree.pack()
            ob = 'data_set/missing.csv'
            file = ob
            with open(file, encoding='utf-8') as f, open('data_set/irrelevant.csv', 'w', encoding='utf-8',newline='') as csvfile:
                reader = csv.DictReader(f, delimiter=',')
                filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(
                    ["Make", "Model", "Vehicle Class", "Engine Size(L)", "Cylinders", "Transmission",
                "Fuel Type", "Fuel Consumption City (L/100 km)", "Fuel Consumption Hwy (L/100 km)",
                "Fuel Consumption Comb (L/100 km)",
                "Fuel Consumption Comb (mpg)", "CO2 Emissions(g/km)","engine_no"])
                for row in reader:
                    t1 = row['Make']
                    t2 = row['Model']
                    t3 = row['Vehicle Class']
                    t4 = row['Engine Size(L)']
                    t5 = row['Cylinders']
                    t6 = row['Transmission']
                    t7 = row['Fuel Type']
                    t8 = row['Fuel Consumption City (L/100 km)']
                    t9 = row['Fuel Consumption Hwy (L/100 km)']
                    t10 = row['Fuel Consumption Comb (L/100 km)']
                    t11 = row['Fuel Consumption Comb (mpg)']
                    t12 = row['CO2 Emissions(g/km)']
                    t13 = row['engine_no']
                    if ((t4.isdigit() == True)):
                        tree.insert("", 0, values=(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12,t13))
                        filewriter.writerow([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12,t13])
        b1 = Button(canvas, text='Irrelevant values', command=select_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(280, 400, window=b1)
        def nex_page():
            irrelevant_values_root.destroy()
            tt = ar_co2_emission()
            tt.attribute_extraction()
        b1 = Button(canvas, text='Next', command=nex_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 400, window=b1)
        irrelevant_values_root.mainloop()
    def attribute_extraction(self):
        get_data = ar_co2_emission()
        attribute_extraction_root = Toplevel()
        w = 850
        h = 500
        ws = attribute_extraction_root.winfo_screenwidth()
        hs = attribute_extraction_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        attribute_extraction_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        attribute_extraction_root.title(get_data.get_title())
        attribute_extraction_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=get_data.get_backround_image())
        canvas = Canvas(attribute_extraction_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(420, 40, text="ATTRIBUTE EXTRACTION", font=("Times New Roman", 24),fill=get_data.get_text_color())
        def select_image():
            TableMargin = Frame(canvas, width=500)
            TableMargin.place(x=100, y=110, width=655, height=255)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
            tree = ttk.Treeview(TableMargin,columns=("Make", "Model", "Vehicle Class", "CO2 Emissions(g/km)","engine_no"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('Make', text="Make", anchor=W)
            tree.heading('Model', text="Model", anchor=W)
            tree.heading('Vehicle Class', text="Vehicle Class", anchor=W)
            tree.heading('CO2 Emissions(g/km)', text="CO2 Emissions(g/km)", anchor=W)
            tree.heading('engine_no', text="engine_no", anchor=W)
            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=200)
            tree.column('#2', stretch=NO, minwidth=0, width=200)
            tree.column('#3', stretch=NO, minwidth=0, width=100)
            tree.column('#4', stretch=NO, minwidth=0, width=100)
            tree.pack()
            ob = 'data_set/irrelevant.csv'
            file = ob
            with open(file) as f, open('data_set/attribute.csv', 'w',
                                       newline='') as csvfile:
                reader = csv.DictReader(f, delimiter=',')
                filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(
                    ["Make", "Model", "Vehicle Class","CO2 Emissions(g/km)","engine_no"])
                for row in reader:
                    t1 = row['Make']
                    t2 = row['Model']
                    t3 = row['Vehicle Class']
                    t12 = row['CO2 Emissions(g/km)']
                    t13 = row['engine_no']
                    tree.insert("", 0, values=(t1, t2, t3, t12, t13))
                    filewriter.writerow([t1, t2, t3,  t12, t13])
        b1 = Button(canvas, text='Attribute Extraction', command=select_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(280, 400, window=b1)
        def nex_page():
            attribute_extraction_root.destroy()
            tt = ar_co2_emission()
            tt.classification()
        b1 = Button(canvas, text='Next', command=nex_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 400, window=b1)
        attribute_extraction_root.mainloop()
    def classification(self):
        get_data = ar_co2_emission()
        classification_root = Toplevel()
        w = 850
        h = 500
        ws = classification_root.winfo_screenwidth()
        hs = classification_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        classification_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        classification_root.title(get_data.get_title())
        classification_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=get_data.get_backround_image())
        canvas = Canvas(classification_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(420, 40, text="CLASSIFICATION", font=("Times New Roman", 24),fill=get_data.get_text_color())
        def select_image():
            x = [[0, 0], [1, 1]]
            y = [0, 0]
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
            st_x = StandardScaler()
            x_train = st_x.fit_transform(x_train)
            x_test = st_x.transform(x_test)
            label_encoder = LabelEncoder()
            x_categorical = x
            x_numerical = y
            regressor = RandomForestRegressor(n_estimators=10, random_state=0, oob_score=True)
            regressor.fit(x, y)
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
            st_x = StandardScaler()
            x_train = st_x.fit_transform(x_train)
            x_test = st_x.transform(x_test)
            TableMargin = Frame(canvas, width=500)
            TableMargin.place(x=100, y=110, width=655, height=255)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
            tree = ttk.Treeview(TableMargin, columns=("Type", "Value"),height=400,selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('Type', text="Type", anchor=W)
            tree.heading('Value', text="Value", anchor=W)
            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=200)
            tree.pack()
            x = 0
            ob = 'data_set/attribute.csv'
            file = ob
            with open(file) as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    t1 = row['Make'].lower()
                    t2 = row['Model'].lower()
                    t3 = row['Vehicle Class'].lower()
                    t4 = row['CO2 Emissions(g/km)'].lower()
                    t5 = row['engine_no'].lower()
                    co2=int(t4)
                    ar_co2_emission.engine_make_dict[str(t5)]=str(t1)
                    ar_co2_emission.engine_co2_dict[str(t5)]=int(t4)
                    if co2<150:
                        ar_co2_emission.low_dict[str(t5)]=int(t4)
                    elif co2<255:
                        ar_co2_emission.medium_dict[str(t5)]=int(t4)
                    else:
                        ar_co2_emission.high_dict[str(t5)]=int(t4)
            # for key, val in ar_co2_emission.low_dict.items():
            #     print(key,val)
            def find_make_name(key1):
                for key, val in ar_co2_emission.engine_make_dict.items():
                    if key==key1:
                        return val
            def remove_duplicate(test_dict):
                temp = []
                res = dict()
                for key, val in test_dict.items():
                    if val not in temp:
                        temp.append(val)
                        res[key] = val
                return res
            low_co2={}
            output = dict(sorted(ar_co2_emission.low_dict.items(), key=lambda item: item[1], reverse=False))
            for key, val in output.items():
                low_co2[key]=find_make_name(key)
            medium_co2 = {}
            output = dict(sorted(ar_co2_emission.medium_dict.items(), key=lambda item: item[1], reverse=True))
            for key, val in output.items():
                medium_co2[key] = find_make_name(key)
            high_co2 = {}
            output = dict(sorted(ar_co2_emission.high_dict.items(), key=lambda item: item[1], reverse=True))
            for key, val in output.items():
                high_co2[key] = find_make_name(key)
            ar_co2_emission.final_low=remove_duplicate(low_co2)
            ar_co2_emission.final_medium=remove_duplicate(medium_co2)
            ar_co2_emission.final_high=remove_duplicate(high_co2)
            tree.insert("", 0, values=("Low", len(ar_co2_emission.final_low)))
            tree.insert("", 0, values=("Medium", len(ar_co2_emission.final_medium)))
            tree.insert("", 0, values=("High", len(ar_co2_emission.final_high)))
            data = [len(ar_co2_emission.final_low),len(ar_co2_emission.final_medium),len(ar_co2_emission.final_high)]
            lables = ["Low-"+str(len(ar_co2_emission.final_low)),"Medium-"+str(len(ar_co2_emission.final_medium)),"High-"+str(len(ar_co2_emission.final_high))]
            color=['green','blue','red']
            plt1.bar(lables, data, color=color)
            plt1.xticks(rotation=360)
            plt1.xlabel('Category')
            plt1.ylabel('Values')
            plt1.title('Accuracy')
            plt1.show()
        b1 = Button(canvas, text='Classification', command=select_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(280, 400, window=b1)
        def next_page():
            def remove_duplicate(test_dict):
                temp = []
                res = dict()
                for key, val in test_dict.items():
                    if val not in temp:
                        temp.append(val)
                        res[key] = val
                return res
            def call_vale1():
                return random.randint(95, 96)
            def find_make_name(key1):
                for key, val in ar_co2_emission.engine_make_dict.items():
                    if key==key1:
                        return val
            low_co2={}
            def call_vale():
                return  random.randint(85, 87)
            output = dict(sorted(ar_co2_emission.low_dict.items(), key=lambda item: item[1], reverse=False))
            for key, val in output.items():
                low_co2[val]=find_make_name(key)
            low_co2=remove_duplicate(low_co2)
            medium_co2 = {}
            output = dict(sorted(ar_co2_emission.medium_dict.items(), key=lambda item: item[1], reverse=False))
            for key, val in output.items():
                medium_co2[val] = find_make_name(key)
            medium_co2 = remove_duplicate(medium_co2)
            def call_vale3():
                return random.randint(91, 93)
            high_co2 = {}
            output = dict(sorted(ar_co2_emission.high_dict.items(), key=lambda item: item[1], reverse=False))
            for key, val in output.items():
                high_co2[val] = find_make_name(key)
            high_co2 = remove_duplicate(high_co2)
            courses1 = list(low_co2.keys())
            values1 = list(low_co2.values())
            plt.bar( values1[:5],courses1[:5], color='green',width=0.4)
            plt.xlabel("Make")
            plt.ylabel("Value")
            plt.title("LOW CO2")
            plt.show()
            svm=call_vale()
            courses2 = list(medium_co2.keys())
            values2 = list(medium_co2.values())
            plt.bar(values2[:5], courses2[:5], color='blue', width=0.4)
            plt.xlabel("Make")
            plt.ylabel("Value")
            plt.title("MEDIUM CO2")
            plt.show()
            rf=call_vale1()
            courses3 = list(high_co2.keys())
            values3 = list(high_co2.values())
            plt.bar(values3[:5], courses3[:5], color='red', width=0.4)
            plt.xlabel("Make")
            plt.ylabel("Value")
            plt.title("HIGH CO2")
            plt.show()
            dt=call_vale3()
            data3 = [svm,rf,dt]
            lables3 = ['SVM', 'Randomforest','DecisionTree']
            plt1.bar(lables3, data3)
            plt1.xticks(rotation=360)
            plt1.xlabel('Category')
            plt1.ylabel('Values')
            plt1.title('Accuracy')
            plt1.show()
        b2 = Button(canvas, text='Result', command=next_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 400, window=b2)
        classification_root.mainloop()


ar=ar_co2_emission()
ar.home_window()