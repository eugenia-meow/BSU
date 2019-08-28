# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 18:47:57 2018

@author: User
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import matplotlib.patches as patches
import pylab
import math

def newline(p1, p2):
    ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if(p2[0] == p1[0]):
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmax-p1[0])
        ymin = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmin-p1[0])

    l = mlines.Line2D([xmin,xmax], [ymin,ymax])
    ax.add_line(l)
    return l

def clip(subjectPolygon, clipPolygon):
   def inside(p):
      return(cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])
 
   def computeIntersection():
      dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ]
      dp = [ s[0] - e[0], s[1] - e[1] ]
      n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
      n2 = s[0] * e[1] - s[1] * e[0] 
      n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
      return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]
 
   outputList = subjectPolygon
   cp1 = clipPolygon[-1]
 
   for clipVertex in clipPolygon:
      cp2 = clipVertex
      inputList = outputList
      outputList = []
      s = inputList[-1]
 
      for subjectVertex in inputList:
         e = subjectVertex
         if inside(e):
            if not inside(s):
               outputList.append(computeIntersection())
            outputList.append(e)
         elif inside(s):
            outputList.append(computeIntersection())
         s = e
      cp1 = cp2
   return(outputList)

subjectPolygon =  [(50,150),(200,50),(350,150),(350,300),(250,300),(200,250),(150,350),(100,250),(100,200)]
clipPolygon = [(100,100),(300,100),(300,300),(100,300)]
outputList = clip(subjectPolygon, clipPolygon)

polygons = [subjectPolygon, clipPolygon, outputList]
colors = ['red', 'green', 'blue']
width = [7, 5, 3]

for i in range(3):
    pp = polygons[i]
#    pp.append(pp[0])
    print(pp)
    cent=(sum([p[0] for p in pp])/len(pp),sum([p[1] for p in pp])/len(pp))
    # sort by polar angle
    pp.sort(key=lambda p: math.atan2(p[1]-cent[1],p[0]-cent[0]))
    # plot points
    pylab.scatter([p[0] for p in pp],[p[1] for p in pp])
    # plot polyline
    pylab.gca().add_patch(patches.Polygon(pp,closed=True,fill=False, color=colors[i], linewidth = width[i]))
    pylab.grid()
    pylab.show()