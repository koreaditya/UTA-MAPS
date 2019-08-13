# This program uses a GUI to get hypotenuse of right angled triangle

from tkinter import *
import tkinter
import sqlite3
import math
import datetime

sqlite_file = 'SpatialiteDatabase.sqlite'
connection = sqlite3.connect(sqlite_file)


class UTA_MAP:
    def __init__(self):
        buildings = ["A_Meadow_Run5","A_Swift_Center","A_Meadow_Run3","A_Meadow_Run4","A_Meadow_Run2","A_Meadow_Run1","TENNIS_CENTER","MEADOW_RUN_A",
                    "MEADOW_RUN_B","MEADOW_RUN_C","MEADOW_RUN_D","ARBOR_OAKS_A",
                    "ARBOR_OAKS_B","ARBOR_OAKS_C","ARBOR_OAKS_D","ARBOR_OAKS_E",
                    "PARKING_LOT_ARBOR_OAKS",
                    "UNIVERSITY_VILLAGE_A","UNIVERSITY_VILLAGE_B",
                    "UNIVERSITY_VILLAGE_C","UNIVERSITY_VILLAGE_D",
                    "UNIVERSITY_VILLAGE_E","UNIVERSITY_VILLAGE_F",
                    "Texas hall","Davis Hall Parking","Davis Hall","Nanofab Building",
                    "Campus Center","Architecture Building","Fine Arts Building","Music Building",
                    "Smart Hospital","Trinity House","Maverick Activity Center","Carlisle Hall",
                    "Brazos House","B.A. Baker Chemistry Research",
                    "Life Science","Preston Hall","Science Hall","University Hall",
                    "Central Library","MapleSquare","BookStore","Tric","Richlynn_Apt",
                    "GardenClub,Thermal Plant","UTA Planetarium","Health Center",
                    "University Center","College Hall","Arlington Hall","University College",
                    "Vandergriff Hall at College Park","Texadelphia","Dan Dipert Welcome center",
                    "College Ministry","GeoScience Building","Science Laboratory","College Park Center",
                    "Lipscomb Hall","The Green at College Park","Woolf Hall","Engineering Research Building","Nedderman Hall"]
        buildings.sort()
        types=["Parking Lot","Housing","Commercial","Academic","Administrative","Open Area","Recreational","Athletic Field","Healthcare"]
        types.sort()

        self.main_window = tkinter.Tk()
        self.main_window.title("UTA MAP")

        canvas = Canvas(self.main_window, width=1200, height=300)
        img = PhotoImage(file="LOGO.png")
        canvas.create_image(120, 20, anchor=NW, image=img)


        # Create the five frames.
        self.Find_Building = tkinter.Frame(self.main_window)
        self.Find_Within = tkinter.Frame(self.main_window)
        self.Result = tkinter.Frame(self.main_window)

        self.button_frame = tkinter.Frame(self.main_window)

        # Finding Building on Campus
        self.Label_A_0 = tkinter.Label(self.Find_Building, text='Find a Building on Campus: ', font=("Helvetica",18,"bold"))
        self.Label_A_1 = tkinter.Label(self.Find_Building, text='Select Area ',font=("Helvetica", 16))
        self.variable = StringVar(self.main_window)
        self.variable.set("Area")
        self.Dropdown_A_1 = OptionMenu(self.Find_Building,self.variable,*buildings)
        self.Dropdown_A_1.configure(font=("Helvetica", 16))
        self.Label_A_2 = tkinter.Label(self.Find_Building, text='Enter Layer Name',font=("Helvetica", 16))
        self.Label_A_3 = tkinter.Entry(self.Find_Building,width=20,font=("Helvetica", 16))
        self.button_A_1=tkinter.Button(self.Find_Building,text='Find Building',font=("Helvetica", 14),command=self.find_Building)

        self.Label_A_0.grid(row=1, column=0, padx=15, pady=50)
        self.Label_A_1.grid(row = 1, column = 1, padx=15, pady = 50)
        self.Dropdown_A_1.grid(row=1, column=2, padx=15, pady=50)
        self.Label_A_2.grid(row = 1, column = 3, padx=15, pady = 50)
        self.Label_A_3.grid(row = 1, column = 4, padx=15, pady = 50)
        self.button_A_1.grid(row = 1, column = 5, padx=15, pady = 50)




        # Finding Building within meters of other building
        self.Label_B_0 = tkinter.Label(self.Find_Within, text='Find on Campus: ',
                                     font=("Helvetica", 18, "bold"))
        self.variable_1 = StringVar(self.main_window)
        self.variable_1.set("Type")
        self.Dropdown_B_1 = OptionMenu(self.Find_Within, self.variable_1, *types)
        self.Dropdown_B_1.configure(font=("Helvetica", 16))
        self.Label_B_1 = tkinter.Label(self.Find_Within, text='Within', font=("Helvetica", 16))
        self.Label_B_2 = tkinter.Entry(self.Find_Within, width=4, font=("Helvetica", 16))
        self.Label_B_3 = tkinter.Label(self.Find_Within, text='Meters of', font=("Helvetica", 16))
        self.variable_2 = StringVar(self.main_window)
        self.variable_2.set("Select Building")
        self.Dropdown_B_2 = OptionMenu(self.Find_Within, self.variable_2, *buildings)
        self.Dropdown_B_2.configure(font=("Helvetica", 16))
        self.Label_B_4 = tkinter.Label(self.Find_Within, text='Enter Layer Name', font=("Helvetica", 16))
        self.Label_B_5 = tkinter.Entry(self.Find_Within, width=10, font=("Helvetica", 16))
        self.button_B_1 = tkinter.Button(self.Find_Within, text='Find Building', font=("Helvetica", 14),command=self.find_within)

        self.Label_B_0.grid(row=1, column=0, padx=6, pady=50)
        self.Dropdown_B_1.grid(row=1, column=1, padx=6, pady=50)
        self.Label_B_1.grid(row=1, column=2, padx=6, pady=50)
        self.Label_B_2.grid(row=1, column=3, padx=6, pady=50)
        self.Label_B_3.grid(row=1, column=4, padx=6, pady=50)
        self.Dropdown_B_2.grid(row=1, column=5, padx=6, pady=50)
        self.Label_B_4.grid(row=1, column=6, padx=6, pady=50)
        self.Label_B_5.grid(row=1, column=7, padx=6, pady=50)
        self.button_B_1.grid(row=1, column=8, padx=6, pady=50)

        self.Result_1 = tkinter.Entry(self.Result, width=80 ,font=("Helvetica", 20))
        self.Result_1.grid(row=1, column=0, padx=6, pady=50)


        # Pack the frames.
        canvas.pack()
        self.Find_Building.pack()
        self.Find_Within.pack()
        self.Result.pack()

        # Start the main loop.
        tkinter.mainloop()

    # The calc_sideC method is the callback function for
    # the calc_button widget.

    def find_Building(self):
        building_name=self.variable.get()
        layer_name=self.Label_A_3.get()
        layer_name=layer_name.lower()
        find_building = connection.cursor()
        find_building.execute(('create view '+layer_name+' as select * from UTA_final_polygon where Name="'+building_name+'";'))
        find_building.execute('INSERT INTO geometry_columns (f_table_name, f_geometry_column, geometry_type, coord_dimension, srid, spatial_index_enabled) VALUES ("'+layer_name+'", "geometry", 3, 2, 0, 0)')
        connection.commit()
        self.Result_1.delete('0', END)
        self.Result_1.update()
        self.Result_1.insert(0," Please Check building "+building_name+" in QGIS")
    def find_within(self):
        building_name=self.variable_2.get()
        building_type=self.variable_1.get()
        distance=self.Label_B_2.get()
        distance=str(int(distance)/100000)
        layer_name=self.Label_B_5.get()
        find_within_distance=connection.cursor()
        find_within_distance.execute('create view '+layer_name+' as select n.name,n.Geometry from uta_final_polygon as n , uta_final_polygon s where s.Name ="'+building_name+'" and n.Btype="'+building_type+'" and PtDistWithin(Centroid(n.Geometry),Centroid(s.Geometry),'+distance+')')
        find_within_distance.execute('INSERT INTO geometry_columns (f_table_name, f_geometry_column, geometry_type, coord_dimension, srid, spatial_index_enabled) VALUES ("'+layer_name+'", "geometry", 3, 2, 0, 0)')
        connection.commit()
        self.Result_1.delete('0', END)
        self.Result_1.update()
        self.Result_1.insert(0, "Check Results in QGIS")

uta_map = UTA_MAP()
connection.close()
