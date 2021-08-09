from operator import le
from tokenize import Double


import matplotlib.pyplot as plt
import numpy as np
import os
from csv_import import *
from matplotlib.animation import FuncAnimation
import argparse


def update(frame, x_data, y_data, ln, axs):
    """function called for each frame
    Parameters
    ----------
    frame   :   int
                number of frame.

    x_data  :   [...]
                time value.

    y_data  :   [[...], [...], ...] 
                vertical value.

    ln      :   plot

    axs     :   [] of axes
    """
    #define plot grid for y axis 
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


def parse_commandline_args():
    parser = argparse.ArgumentParser(description="animated graph plotter")
    parser.add_argument("data_path", help = "path to csv table")
    parser.add_argument("-o", help = "output filename", default= "o.mp4")
    parser.add_argument("-p", default= "vids",  help="path to video")
    parser.add_argument("--dpi", default=100, help ="dpi for video", type=float )
    parser.add_argument("--update", default=8.072,  help="time of showing each frame", type= float )
    parser.add_argument("--time_col",  default=0, help = "number of column with time", type = int)
    parser.add_argument("--nogrid", help="render without grid" ,action="store_false")
    parser.add_argument("--figx", help="horizontal figure size in inches", default=16, type= float)
    parser.add_argument("--figy", help="vertical figure size in inches", default=9, type= float)
    parser.add_argument("--pcx", help ="horizontal plots count", default=-1, type = int)
    parser.add_argument("--pcy", help = "vertical plots count", default=-1, type= int)
    args  = parser.parse_args()
    return args

xdata, ydata = [], []
def main():
    args = parse_commandline_args()
    # vars
    dataPath = args.data_path
    if args.pcx != -1:
        hor_plot_count =args.pcx
    else:
        hor_plot_count = 3
    if args.pcy !=-1:
        ver_plot_count =  args.pcy
    else:
        ver_plot_count = 2
    output_filename = args.o
    video_path = args.p
    dpi = args.dpi
    interval = args.update
    time_col_num = args.time_col
    withGrid = args.nogrid
    figsize = (args.figx, args.figy)

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

    ani.save("{}/{}".format(video_path, output_filename), dpi=dpi)


main()
