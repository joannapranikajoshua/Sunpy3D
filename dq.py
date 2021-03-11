from astropy.coordinates import SkyCoord
import astropy.units as u
from sunpy.coordinates.utils import get_rectangle_coordinates
from astropy.visualization.wcsaxes import Quadrangle
from astropy.coordinates import Longitude, SkyCoord, UnitSphericalRepresentation
import matplotlib.pyplot as plt
from sunpy.visualization import wcsaxes_compat
from matplotlib.patches import Polygon

def convert_to_Skycoord(mas, coords):
    print(coords.xy[0:5])
    corners = SkyCoord(coords.xy[:,0]*u.deg, coords.xy[:,1]*u.deg , frame='heliographic_stonyhurst', obstime=mas.date)
    return corners

def convert_rect_to_Skycoord(mas, coords):
    x0,y0 = coords.get_bbox().x0, coords.get_bbox().y0
    x1,y1 = coords.get_bbox().x1, coords.get_bbox().y1
    corners = SkyCoord((x0,y0)*u.deg, (x1,y1)*u.deg , frame='heliographic_stonyhurst', obstime=mas.date)
    return corners

def draw_quadrangle(mas, bottom_left, *, width: u.deg = None, height: u.deg = None,
                    axes=None, top_right=None, **kwargs):
    bottom_left, top_right = get_rectangle_coordinates(
        bottom_left, top_right=top_right, width=width, height=height)

    width = Longitude(top_right.spherical.lon - bottom_left.spherical.lon)
    height = top_right.spherical.lat - bottom_left.spherical.lat
    if not axes:
        axes = plt.gca()
    kwergs = {
        "transform": axes.get_transform(bottom_left.frame.replicate_without_data()),
        "edgecolor": "white",
        "fill": False,
    }
    kwergs.update(kwargs)
    print('in quadragnle', mas._get_lon_lat(bottom_left), width, height)
    quad = Quadrangle(mas._get_lon_lat(bottom_left), width, height, **kwergs)
    corners = convert_to_Skycoord(mas, quad)
    return corners
import numpy as np




class Rect(Polygon):

    def __init__(mas, anchor, width, height, resolution=100, vertex_unit=u.degree, **kwargs):

        longitude, latitude = u.Quantity(anchor).to_value(u.deg)

        width = width.to_value(vertex_unit)
        height = height.to_value(vertex_unit)
        print(longitude, latitude, width, height)

        # print(width, height)

        
        lon_seq = longitude + np.linspace(0, width, resolution + 1)
        lat_seq = latitude + np.linspace(0, height, resolution + 1)

        
        rhs = longitude + np.linspace(0, width, resolution + 1)
        top = latitude + np.linspace(0, height, resolution + 1)
        lhs = np.flip(rhs)
        bot = np.flip(top)

        rsd = np.concatenate([[rhs, np.repeat(top[0], 101)]])
        # tsd = np.concatenate([[top, np.repeat(top[0], 101)]])

        tsd = np.concatenate([[np.repeat(rhs[-1], 101), top]])
        print(rsd.T[0:5])
        lsd = np.concatenate([[lhs, np.repeat(top[-1], 101)]])

        bsd = np.concatenate([[np.repeat(rhs[0], 101), bot]])

        fin = np.concatenate([rsd.T, tsd.T, lsd.T, bsd.T])

        # xx = np.concatenate([rhs[0:-1], ])

        # fins = np.concatenate([])
        # print(fin)

        super().__init__(fin, **kwargs)


def draw_rectangles(mas, bottom_left, *, width: u.deg = None, height: u.deg = None,
                       axes=None, top_right=None, resolution=100, **kwargs):


    bottom_left, top_right = get_rectangle_coordinates(
        bottom_left, top_right=top_right, width=width, height=height)

    width = Longitude(top_right.spherical.lon - bottom_left.spherical.lon)
    height = top_right.spherical.lat - bottom_left.spherical.lat
    if not axes:
        axes = plt.gca()
    kwergs = {
        "transform": axes.get_transform(bottom_left.frame.replicate_without_data()),
        "edgecolor": "white",
        "fill": False,
    }
    kwergs.update(kwargs)
    print('in rectangle', mas._get_lon_lat(bottom_left), width, height)
    quad = Rect(mas._get_lon_lat(bottom_left), width, height, **kwergs)    
    corners = convert_to_Skycoord(mas, quad)
    return corners

# def draw_rectangle(mas, bottom_left, *, width: u.deg = None, height: u.deg = None,
#                        axes=None, top_right=None, **kwargs):
#         bottom_left, top_right = get_rectangle_coordinates(bottom_left,
#                                                            top_right=top_right,
#                                                            width=width,
#                                                            height=height)

#         bottom_left = bottom_left.transform_to(mas.coordinate_frame)
#         top_right = top_right.transform_to(mas.coordinate_frame)

#         width = Longitude(top_right.spherical.lon - bottom_left.spherical.lon)
#         height = top_right.spherical.lat - bottom_left.spherical.lat

#         if not axes:
#             axes = plt.gca()
#         if wcsaxes_compat.is_wcsaxes(axes):
#             axes_unit = u.deg
#         else:
#             axes_unit = mas.spatial_units[0]

#         bottom_left = u.Quantity(mas._get_lon_lat(bottom_left), unit=axes_unit).value

#         width = width.to(axes_unit).value
#         height = height.to(axes_unit).value
#         kwergs = {'transform': wcsaxes_compat.get_world_transform(axes),
#                   'edgecolor': 'white',
#                   'fill': False}
#         kwergs.update(kwargs)
#         rect = plt.Rectangle(bottom_left, width, height, **kwergs)


        # print(rect.get_bbox())
        # axes.add_patch(rect)
        # return [rect]