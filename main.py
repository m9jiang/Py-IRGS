
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from skimage import io
import numpy as np
import os



root = tk.Tk()
root.withdraw()
# if cancel 
img_path = filedialog.askopenfilenames(title='Please select the image(s) need to be segmented')
root.destroy()
dir = os.path.dirname(img_path[0])
landmask_path = os.path.join(dir,'landmask.bmp')
try:
    landmask = io.imread(landmask_path)
except FileNotFoundError:
    landmask = None
else:
    root = tk.Tk()
    messagebox.showinfo(title='land mask has been loaded', message='land mask ({}) has been loaded'.format('landmask.bmp'))
    root.destroy()


if img_path == '':
    print("No file selected!!!")
    exit()

num_band = len(img_path)
img_0 = io.imread(img_path[0])
row, col = img_0.shape[0], img_0.shape[1]
img = np.zeros((row, col, num_band), dtype=float)
img[:,:,0] = img_0

for i in range(1, num_band):
    img_temp = io.imread(img_path[0])
    if row != img_temp.shape[0] or col != img_temp.shape[1]:
        print("ERROR: Selected images have different dimensions")
        exit()
    img[:,:,i] = img_temp


print('Done!')