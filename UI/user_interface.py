import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox
import joblib

# create window for UI
window = tk.Tk()
window.title("Used Car Price Prediction")
window.geometry("500x600+10+20")

# default data
price_buckets = {'acura': 2, 'alfa-romeo': 5, 'audi': 2, 'bmw': 2, 'buick': 2, 'cadillac': 2, 'chevrolet': 2, 'chrysler': 1, 'dodge': 2, 'fiat': 1, 'ford': 3, 'gmc': 3, 'honda': 2, 'hyundai': 2, 'infiniti': 2, 'jaguar': 2, 'jeep': 3, 'kia': 2, 'land rover': 2, 'lexus': 2, 'lincoln': 2, 'mazda': 1, 'mercedes-benz': 3, 'mercury': 0, 'mini': 1, 'mitsubishi': 1, 'nissan': 2, 'null': 3, 'pontiac': 1, 'ram': 4, 'rover': 3, 'saturn': 0, 'subaru': 2, 'tesla': 7, 'toyota': 2, 'volkswagen': 2, 'volvo': 1}

# initial input format
# input_dict = {'manufacturer': {0: 0}, 'cylinders': {0: 0}, 'odometer': {0: 0}, 'year_count': {0: 0}, 'condition_excellent': {0: 0}, 'condition_fair': {0: 0}, 'condition_good': {0: 0}, 'condition_like new': {0: 0}, 'condition_new': {0: 0}, 'condition_null': {0: 0}, 'condition_salvage': {0: 0}, 'fuel_diesel': {0: 0}, 'fuel_electric': {0: 0}, 'fuel_gas': {0: 0}, 'fuel_hybrid': {0: 0}, 'fuel_other': {0: 0}, 'transmission_automatic': {0: 0}, 'transmission_manual': {0: 0}, 'transmission_other': {0: 0}, 'drive_4wd': {0: 0}, 'drive_fwd': {0: 0}, 'drive_rwd': {0: 0}, 'type_SUV': {0: 0}, 'type_bus': {0: 0}, 'type_convertible': {0: 0}, 'type_coupe': {0: 0}, 'type_hatchback': {0: 0}, 'type_mini-van': {0: 0}, 'type_offroad': {0: 0}, 'type_other': {0: 0}, 'type_pickup': {0: 0}, 'type_sedan': {0: 0}, 'type_truck': {0: 0}, 'type_van': {0: 0}, 'type_wagon': {0: 0}}
input_dict = {'cylinders': {0: 0}, 'odometer': {0: 0}, 'year_count': {0: 0}, 'manufacturer_acura': {0: 0}, 'manufacturer_alfa-romeo': {0: 0}, 'manufacturer_audi': {0: 0}, 'manufacturer_bmw': {0: 0}, 'manufacturer_buick': {0: 0}, 'manufacturer_cadillac': {0: 0}, 'manufacturer_chevrolet': {0: 0}, 'manufacturer_chrysler': {0: 0}, 'manufacturer_dodge': {0: 0}, 'manufacturer_fiat': {0: 0}, 'manufacturer_ford': {0: 0}, 'manufacturer_gmc': {0: 0}, 'manufacturer_honda': {0: 0}, 'manufacturer_hyundai': {0: 0}, 'manufacturer_infiniti': {0: 0}, 'manufacturer_jaguar': {0: 0}, 'manufacturer_jeep': {0: 0}, 'manufacturer_kia': {0: 0}, 'manufacturer_land rover': {0: 0}, 'manufacturer_lexus': {0: 0}, 'manufacturer_lincoln': {0: 0}, 'manufacturer_mazda': {0: 0}, 'manufacturer_mercedes-benz': {0: 0}, 'manufacturer_mercury': {0: 0}, 'manufacturer_mini': {0: 0}, 'manufacturer_mitsubishi': {0: 0}, 'manufacturer_nissan': {0: 0}, 'manufacturer_null': {0: 0}, 'manufacturer_pontiac': {0: 0}, 'manufacturer_ram': {0: 0}, 'manufacturer_rover': {0: 0}, 'manufacturer_saturn': {0: 0}, 'manufacturer_subaru': {0: 0}, 'manufacturer_tesla': {0: 0}, 'manufacturer_toyota': {0: 0}, 'manufacturer_volkswagen': {0: 0}, 'manufacturer_volvo': {0: 0}, 'condition_excellent': {0: 0}, 'condition_fair': {0: 0}, 'condition_good': {0: 0}, 'condition_like new': {0: 0}, 'condition_new': {0: 0}, 'condition_null': {0: 0}, 'condition_salvage': {0: 0}, 'fuel_diesel': {0: 0}, 'fuel_electric': {0: 0}, 'fuel_gas': {0: 0}, 'fuel_hybrid': {0: 0}, 'fuel_other': {0: 0}, 'transmission_automatic': {0: 0}, 'transmission_manual': {0: 0}, 'transmission_other': {0: 0}, 'drive_4wd': {0: 0}, 'drive_fwd': {0: 0}, 'drive_rwd': {0: 0}, 'type_SUV': {0: 0}, 'type_bus': {0: 0}, 'type_convertible': {0: 0}, 'type_coupe': {0: 0}, 'type_hatchback': {0: 0}, 'type_mini-van': {0: 0}, 'type_offroad': {0: 0}, 'type_other': {0: 0}, 'type_pickup': {0: 0}, 'type_sedan': {0: 0}, 'type_truck': {0: 0}, 'type_van': {0: 0}, 'type_wagon': {0: 0}}
input_df = pd.DataFrame(input_dict)

# load model
model_etr = joblib.load('./ECE-143-Group14/model_etr.model')

# create combobox class for selecting options
class Combobox():
    def __init__(self, options):
        # create a combobox
        self.cmb = ttk.Combobox(window)
        self.cmb.pack()
        # set the values in combobox
        self.cmb['value'] = options
        # set the permission to read only
        self.cmb['state'] = 'readonly'
        # set default value to idx 0
        self.cmb.current(0)

# default manufacturers
options_manufacturer = ('ford', 'chevrolet', 'ram', 'buick', 'nissan', 'hyundai', 'dodge',
       'subaru', 'toyota', 'lexus', 'volvo', 'chrysler', 'jeep', 'acura',
       'gmc', 'kia', 'honda', 'volkswagen', 'bmw', 'null', 'pontiac',
       'cadillac', 'mazda', 'lincoln', 'saturn', 'fiat', 'audi',
       'mercury', 'mercedes-benz', 'mini', 'mitsubishi', 'jaguar',
       'infiniti', 'rover', 'tesla', 'land rover', 'alfa-romeo')

# create combobox for Manufacturer, Cylinders, Condition, Fuel, Transmission, Drive and Type
tk.Label(window, text="Manufacturer").pack()
cmb_manufacturer = Combobox(options_manufacturer)

tk.Label(window, text="Cylinders").pack()
options_cylinders = ("3", "4", "5", "6", "8", "10","12")
cmb_cylinders = Combobox(options_cylinders)

tk.Label(window, text="Condition").pack()
options_condition = ('excellent', 'fair', 'good', 'like new', 'new', 'null', 'salvage')
cmb_condition = Combobox(options_condition)

tk.Label(window, text="Fuel").pack()
options_fuel = ('diesel', 'electric', 'gas', 'hybrid', 'other')
cmb_fuel = Combobox(options_fuel)

tk.Label(window, text="Transmission").pack()
options_transmission = ('automatic', 'manual', 'other')
cmb_transmission = Combobox(options_transmission)

tk.Label(window, text="Drive").pack()
options_drive = ('4wd', 'fwd', 'rwd')
cmb_drive = Combobox(options_drive)

tk.Label(window, text="Type").pack()
options_type = ('SUV', 'bus', 'convertible', 'coupe', 'hatchback', 'mini-van', 'offroad', 'other', 'pickup', 'sedan', 'truck', 'van', 'wagon')
cmb_type = Combobox(options_type)

# Create entries for Odometer and Year
tk.Label(window, text="Odometer").pack()
entry_odometer = tk.Entry(window, bd = 5)
entry_odometer.pack()

tk.Label(window, text="Year").pack()
entry_year = tk.Entry(window, bd = 5)
entry_year.pack()

# executing function for generating predicted price after hitting the submit button
def exec():
    # input_df['manufacturer'] = cmb_manufacturer.cmb.get()
    # input_df['manufacturer'].replace(price_buckets, inplace=True)
    # manufacturer
    manufacturer = cmb_manufacturer.cmb.get()
    prefix_manufacturer = 'manufacturer_'
    idx_manufacturer = options_manufacturer.index(manufacturer)
    set_dummy(idx_manufacturer, prefix_manufacturer, options_manufacturer)

    input_df['cylinders'] = float(cmb_cylinders.cmb.get())
    input_df['odometer'] = float(entry_odometer.get())
    input_df['year_count'] = float(entry_year.get())-1900
    # condition
    condition = cmb_condition.cmb.get()
    prefix_condition = 'condition_'
    idx_condition = options_condition.index(condition)
    set_dummy(idx_condition, prefix_condition, options_condition)
    # fuel
    fuel = cmb_fuel.cmb.get()
    prefix_fuel = 'fuel_'
    idx_fuel = options_fuel.index(fuel)
    set_dummy(idx_fuel, prefix_fuel, options_fuel)
    # transmission
    transmission = cmb_transmission.cmb.get()
    prefix_transmission = 'transmission_'
    idx_transmission = options_transmission.index(transmission)
    set_dummy(idx_transmission, prefix_transmission, options_transmission)
    # drive
    drive = cmb_drive.cmb.get()
    prefix_drive = 'drive_'
    idx_drive = options_drive.index(drive)
    set_dummy(idx_drive, prefix_drive, options_drive)
    # type
    car_type = cmb_type.cmb.get()
    prefix_type = 'type_'
    idx_type = options_type.index(car_type)
    set_dummy(idx_type, prefix_type, options_type)

    price = model_etr.predict(input_df)
    messagebox.showinfo("Price", str(int(price)))

def set_dummy(idx, prefix, options):
    for i, val in enumerate(options):
        if i == idx:
            input_df[prefix+val] = 1
        else:
            input_df[prefix+val] = 0

# submit button
button = tk.Button(window, width=20, height=2, text ="Submit", command = exec)
button.pack()

# set mainloop for the ui in incase it exits
window.mainloop()