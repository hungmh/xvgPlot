#!/usr/bin/env python

import matplotlib.pyplot as plt 
import sys 
import argparse 
#parse command-line arguments 
parser = argparse.ArgumentParser() 
parser.add_argument('filenames', nargs='+', help='.xvg files to be plotted') 
parser.add_argument('-xlabel', default=None, help='x-axis label') 
parser.add_argument('-ylabel', default=None, help='y-axis label') 
args = parser.parse_args() 
#parse .xvg files and store the data 
data = [] 
for filename in args.filenames: 
    x, y = [], [] 
    with open(filename, 'r') as f: 
        for line in f: 
            if line[0] in ('#', '@'): 
                continue 
            fields = line.split() 
            x.append(float(fields[0])) 
            y.append(float(fields[1])) 
    data.append((x, y)) 
#plot the data 
for (x, y) in data: 
    plt.plot(x, y) 
#set axis labels 
if args.xlabel: 
    plt.xlabel(args.xlabel) 
if args.ylabel: 
    plt.ylabel(args.ylabel) 
#save the figure in high resolution 
plt.savefig('figure.png', dpi=300)
