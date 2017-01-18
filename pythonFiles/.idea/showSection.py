import matplotlib.pyplot as plt
import numpy as np

def displayBoxes(boxes, color='g', lineWidth=2):
    currentAxis = plt.gca()
    for each in boxes:
        coords = (each[0], each[1]), each[2], each[3]
        currentAxis.add_patch(plt.Rectangle(*coords, fill=False, edgecolor=color, linewidth=2))

