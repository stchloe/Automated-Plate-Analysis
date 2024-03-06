import tkinter as tk
from tkinter import Entry, Label, Button
from picamera2 import Picamera2, Preview
from time import strftime
import csv
import os

class DataCollectionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Collection App")
        
        self.label_concentration = Label(master, text="Concentration:")
        self.label_concentration.grid(row=0, column=0, padx=10, pady=10)
        self.entry_concentration = Entry(master)
        self.entry_concentration.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_result = Label(master, text="Result:")
        self.label_result.grid(row=1, column=0, padx=10, pady=10)
        self.entry_result = Entry(master)
        self.entry_result.grid(row=1, column=1, padx=10, pady=10)
        
        self.button_capture = Button(master, text="Capture Image", command=self.capture_image)
        self.button_capture.grid(row=2, column=0, columnspan=2, pady=20)
        
        self.camera = Picamera2()
        
        # Specify folder
        self.image_folder = "PlateImages"
        
        # Open a CSV file for recording details
        self.csv_file = open("training_data.csv", mode="w", newline="")
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(["Image Name", "Concentration", "Result"])
        
    def capture_image(self):
        concentration = self.entry_concentration.get()
        result = self.entry_result.get()
        
        # Create unique image name based on concentration & result
        image_name = f"{concentration}_{result}.jpg"
        
        # Combine with sub folder path
        image_path = os.path.join(self.image_folder, image_name)
        
        # Capture & save image
        self.camera.start_and_capture_file(image_path)
        
        # Neatly shut down camera
        self.camera.stop_preview()
        self.camera.stop
        
        # Record details in CSV file
        self.csv_writer.writerow([image_name, concentration, result])
        self.csv_file.flush()
        
        # Clear entry fields
        self.entry_concentration.delete(0, 'end')
        self.entry_result.delete(0, 'end')
        
if __name__ == "__main__":
    root = tk.Tk()
    app = DataCollectionApp(root)
    root.mainloop()