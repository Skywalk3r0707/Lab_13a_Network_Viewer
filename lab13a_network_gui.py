import json
import tkinter as tk

with open("network_devices.json", "r") as file:
    devices = json.load(file)

window = tk.Tk()
window.title("Network Device Viewer")
window.geometry("400x500")

def show_device():
    device = devices[0]

    output = f"""
Name: {device['Name']}
IP: {device['IP']}
MAC: {device['MAC']}
RAM: {device['RAM']}
SSD: {device['SSD_Size']}
Free Space: {device['Free_Space']}
"""

    label.config(text=output)

def show_all_devices():
    output = ""

    for device in devices:
        output += f"{device['Name']} - {device['IP']}\n"

    label.config(text=output)

def save_data():
    with open("network_devices.json", "w") as file:
        json.dump(devices, file, indent=4)

def add_device():
    new_device = {
        "Name": name_entry.get(),
        "IP": ip_entry.get(),
        "MAC": mac_entry.get(),
        "RAM": ram_entry.get(),
        "SSD_Size": ssd_entry.get(),
        "Free_Space": free_entry.get()
    }

    devices.append(new_device)
    save_data()

def update_device():
    target_name = name_entry.get()
    found = False

    for device in devices:
        if device["Name"] == target_name:
            device["IP"] = ip_entry.get()
            device["MAC"] = mac_entry.get()
            device["RAM"] = ram_entry.get()
            device["SSD_Size"] = ssd_entry.get()
            device["Free_Space"] = free_entry.get()
            found = True

    save_data()

    if found:
        label.config(text="Device updated successfully")
    else:
        label.config(text="Device not found")

button = tk.Button(window, text="Show Device", command=show_device)
button.pack()

view_button = tk.Button(window, text="View All Devices", command=show_all_devices)
view_button.pack()

label = tk.Label(window, text="", justify="left")
label.pack()

tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="IP Address").pack()
ip_entry = tk.Entry(window)
ip_entry.pack()

tk.Label(window, text="MAC Address").pack()
mac_entry = tk.Entry(window)
mac_entry.pack()

tk.Label(window, text="RAM").pack()
ram_entry = tk.Entry(window)
ram_entry.pack()

tk.Label(window, text="SSD Size").pack()
ssd_entry = tk.Entry(window)
ssd_entry.pack()

tk.Label(window, text="Free Space").pack()
free_entry = tk.Entry(window)
free_entry.pack()

add_button = tk.Button(window, text="Add Device", command=add_device)
add_button.pack()

update_button = tk.Button(window, text="Update Device", command=update_device)
update_button.pack()

def delete_device():
    target_name = name_entry.get()

    global devices
    devices = [d for d in devices if d["Name"] != target_name]

    save_data()

delete_button = tk.Button(window, text="Delete Device", command=delete_device)
delete_button.pack()


window.mainloop()