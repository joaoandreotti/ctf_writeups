import matplotlib.pyplot as pyplot
import xml.etree.ElementTree as xml
import matplotlib.patches as mpatches
import numpy as np

def arc_patch(center, radius, theta1, theta2, ax=None, resolution=50, **kwargs):
    # make sure ax is not empty
    if ax is None:
        ax = pyplot.gca()
    # generate the points
    theta = np.linspace(np.radians(theta1), np.radians(theta2), resolution)
    points = np.vstack((radius*np.cos(theta) + center[0], 
                        radius*np.sin(theta) + center[1]))
    # build the polygon and add it to the axes
    poly = mpatches.Polygon(points.T, closed=True, **kwargs)
    ax.add_patch(poly)
    return poly

## INIT OBJECTS
def func (str):
    fig, ax = pyplot.subplots(1,2)
    tree = xml.parse ('plotMe.xml')
    root = tree.getroot ()
    for line in root.findall ('Line'):
        p0 = (float (line.find ('XStart').text), float (line.find ('YStart').text))
        p1 = (float (line.find ('XEnd').text), float (line.find ('YEnd').text))
        if (line.find ('Color') is not None) and line.find ('Color').text == str:
            ax [0].plot ((p0 [0], p1 [0]), (p0 [1], p1 [1]), '-o', color=line.find ('Color').text)
        if (line.find ('Color') is None) and (str == 'white'):
            ax [0].plot ((p0 [0], p1 [0]), (p0 [1], p1 [1]), '-o', color='black')

    for arc in root.findall ('Arc'):
        c = (float (arc.find ('XCenter').text), float (arc.find ('YCenter').text))
        r = float (arc.find ('Radius').text)
        st = float (arc.find ('ArcStart').text)
        sz = float (arc.find ('ArcExtend').text) + st
        if (arc.find ('Color') is not None) and arc.find ('Color').text == str:
            arc_patch (c, r, st, sz, ax=ax [0], fill=False, color=arc.find ('Color').text)
        if (arc.find ('Color') is None) and (str == 'white'):
            arc_patch (c, r, st, sz, ax=ax [0], fill=False, color='black')
    pyplot.show ()

func ('blue')
func ('green')
func ('red')
func ('yellow')
func ('white')
