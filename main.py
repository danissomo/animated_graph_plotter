from operator import le
from tokenize import Double
from PIL import Image, ImageDraw

import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.ticker as ticker
from decimal import Decimal
from csv_import import *
from matplotlib.animation import FuncAnimation


xdata, ydata = [], []


def update(frame, x_data, y_data, ln, axs):

    if frame == 0:
        for i in range(len(axs)):
            for j in range(len(axs[i])):
                axs[i][j].set_ylim(np.min(y_data[i*len(axs[i])+j]),
                                   np.max(y_data[i*len(axs[i])+j]))
    start_scale = 150
    if(frame > start_scale):
        xdata.append(x_data[frame])
        for i in range(len(axs)):
            for j in range(len(axs[i])):
                ydata[i*len(axs[i])+j].append(y_data[i*len(axs[i])+j][frame])
                axs[i, j].set_xlim(
                    xdata[len(xdata)-1-start_scale], xdata[len(xdata)-1])
                axs[i][j].plot(xdata, ydata[i*len(axs[i])+j],
                               color="red", label="joint{}".format(i*len(axs[i])+j))
        return ln,

    xdata.append(x_data[frame])
    for i in range(len(axs)):

        for j in range(len(axs[i])):
            axs[i, j].set_xlim(x_data[0], x_data[start_scale])
            ydata[i*len(axs[i])+j].append(y_data[i*len(axs[i])+j][frame])
            axs[i][j].plot(xdata, ydata[i*len(axs[i])+j], color="red")

    return ln,


def main():
    # vars
    dataPath = "data_ex/2021_08_06_09_39_21.csv"
    hor_plot_count, ver_plot_count = 3, 2
    output_filename = dataPath.split("/")[-1]
    video_path = "vids"
    dpi = 100
    interval = 8.072
    time_col_num = 0
    withGrid = True
    figsize = (16, 9)

    #import csv as array
    table = get_csv(dataPath)

    # ploting
    fig, axs = plt.subplots(ver_plot_count, hor_plot_count,
                            sharex=True, sharey=False, figsize=figsize)
    ln, = plt.plot([], [], 'r')

    x_data = get_column(table, time_col_num)
    y_data = []
    for i in range(len(table[0])):
        if i == time_col_num:
            continue
        y_data.append(get_column(table, i))
        ydata.append([])

    # setup plots
    for row in axs:
        for elem in row:
            elem.grid(withGrid)
    for i in range(len(axs)):
        for j in range(len(axs[i])):
            axs[i][j].set_title("joint {}".format(i*len(axs[i])+j))

    ani = FuncAnimation(fig, update, frames=range(len(x_data)),
                        blit=True, fargs=[x_data, y_data, ln, axs], interval=interval)

    if not os.path.exists(video_path):
        os.mkdir(video_path)

    ani.save("{}/{}.mp4".format(video_path, output_filename), dpi=dpi)


main()
