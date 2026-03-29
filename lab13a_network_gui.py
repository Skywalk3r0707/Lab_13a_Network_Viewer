import json
import tkinter as tk


with open("network_devices.json", "r") as file:
    devices = json.load(file)
    print(devices[0])

window = tk.Tk()
window.title("Network Device Viewer")
window.geometry("400x300")

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

button = tk.Button(window, text="Show Device", command=show_device)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()