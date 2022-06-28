import os, csv
import pandas as pd
import matplotlib.pyplot as plt
import cv2

images_path = os.path.join('..','MTSD','Images')
df = pd.read_csv(os.path.join('..','MTSD','GT.csv'))
print(df[0])
