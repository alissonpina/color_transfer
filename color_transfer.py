import numpy as np
import cv2
import os
from tkinter import filedialog


def get_sources():
    
    sources = [i for i in os.listdir('_source') if i[-4:] in ['.png', '.bmp', '.jpg']]
    
    if len(sources) == 0:
        print("There must be at least one image in the '_source' folder.")
    else:  
        return sources


def get_target():
    
    target = filedialog.askopenfilename(initialdir="_target", title="Select A Target", filetypes=[('image files', ('.png', '.bmp', '.jpg'))])
    
    if len(target) == 0:
        print("Select an image that will be used as a target.")
    else:  
        return cv2.cvtColor(cv2.imread(target), cv2.COLOR_BGR2LAB)


def get_mean_and_std(x):
    x_mean, x_std = cv2.meanStdDev(x)
    x_mean = np.hstack(np.around(x_mean,2))
    x_std = np.hstack(np.around(x_std,2))
    return x_mean, x_std


def color_transfer():

    sources = get_sources()
    
    if sources:
        
        t = get_target()
        t_mean, t_std = get_mean_and_std(t)
        
        if len(t) != 0:
        
            for n in range(len(sources)):
                print("Converting picture " + sources[n] + "...")
                
                s = cv2.imread('_target/' + sources[n])
                s = cv2.cvtColor(s, cv2.COLOR_BGR2LAB)
                s_mean, s_std = get_mean_and_std(s)

                height, width, channel = s.shape
                for i in range(0,height):
                    for j in range(0,width):
                        for k in range(0,channel):
                            x = s[i,j,k]
                            x = ((x - s_mean[k]) * (t_std[k] / s_std[k])) + t_mean[k]
                            x = round(x)
                            x = 0 if x < 0 else x
                            x = 255 if x > 255 else x
                            s[i,j,k] = x

                s = cv2.cvtColor(s, cv2.COLOR_LAB2BGR)
                cv2.imwrite('_output/' + sources[n], s)


color_transfer()