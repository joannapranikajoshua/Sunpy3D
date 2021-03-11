import functools

import numpy as np
import pyvista as pv

from astropy.constants import R_sun

from sunpy.coordinates import HeliocentricInertial
from sunpy.map.maputils import all_corner_coords_from_map
from dq import draw_quadrangle, draw_rectangles


__all__ = ['PyVistaPlotter']


class PyVistaPlotter:
    """
    A plotter for 3D data.
    Since pyvista is not coordinate aware, all coordinates are converted to
    a specific frame (`~sunpy.coordinates.HeliocentricInertial` by default),
    and distance units are such that :math:`R_{sun} = 1`.
    Parameters
    ----------
    coordinate_frame : astropy.coordinates.BaseFrame
        Coordinate frame of the plot. The x, y, z axes of the pyvista plotter
        will be the x, y, z axes in this coordinate system.
    """
    def __init__(self, coordinate_frame=None):
        if coordinate_frame is None:
            coordinate_frame = HeliocentricInertial()
        self._coordinate_frame = coordinate_frame
        self._plotter = pv.Plotter()

    @property
    def coordinate_frame(self):
        """
        Coordinate frame of the plot.
        """
        return self._coordinate_frame

    @property
    def plotter(self):
        """
        `pyvista.Plotter`.
        """
        return self._plotter

    @functools.wraps(pv.Plotter.show)
    def show(self, *args, **kwargs):
        """
        Show the plot.
        """
        self.plotter.show(*args, **kwargs)

    def _coords_to_xyz(self, coords):
        coords = coords.transform_to(self.coordinate_frame)
        coords.representation_type = 'cartesian'
        return np.column_stack((coords.x.to_value(R_sun),
                                coords.y.to_value(R_sun),
                                coords.z.to_value(R_sun)))

    def _pyvista_mesh(self, m):
        """
        Create a mesh from a map.
        Parameters
        ----------
        m : sunpy.map.Map
        Returns
        -------
        pyvista.StructuredGrid
        """
        corner_coords = all_corner_coords_from_map(m)
        nodes = self._coords_to_xyz(corner_coords.ravel())
        grid = pv.StructuredGrid()
        grid.points = nodes
        grid.dimensions = [m.data.shape[0] + 1,
                           m.data.shape[1] + 1,
                           1]
        data = m.data.T.reshape(-1)
        grid['data'] = m.plot_settings['norm'](data)
        return grid

    def plot_map(self, m, **kwargs):
        """
        Plot a map.
        Parameters
        ----------
        m : sunpy.map.Map
            Map to be plotted.
        **kwargs :
            Keyword arguments are handed to `pyvista.Plotter.add_mesh`.
        """
        cmap = kwargs.pop('cmap', m.cmap)
        mesh = self._pyvista_mesh(m)
        self.plotter.add_mesh(mesh, cmap=cmap, **kwargs)
    
    def plot_rectangle(self, m, **kwargs):
        """
        Plot a quadrangle on the map from the given map
        """
        # bottom_left = SkyCoord(40*u.deg, -45*u.deg, frame='heliographic_stonyhurst', obstime=m.date)
        # coords = draw_rectangles(m, bottom_left, width=80*u.deg, height=90*u.deg)

        bottom_left = SkyCoord(40*u.deg, -45*u.deg, frame='heliographic_stonyhurst', obstime=m.date)
        coords = draw_rectangles(m, bottom_left, width=80*u.deg, height=90*u.deg)
        # print(coords)
        coords = self._coords_to_xyz(coords)
        coords -= 0.001
        mesh = pv.StructuredGrid(coords[:, 0], coords[:, 1], coords[:, 2])
        self.plotter.add_mesh(mesh, color='lightblue', line_width=2.0)
        

    def plot_quadrangle(self, m, **kwargs):
        """
        Plot a quadrangle on the map from the given map
        """
        bottom_left = SkyCoord(40*u.deg, -45*u.deg, frame='heliographic_stonyhurst', obstime=m.date)
        coords = draw_quadrangle(m, bottom_left, width=10*u.deg, height=90*u.deg)
        coords = self._coords_to_xyz(coords)
        coords -= 0.001
        mesh = pv.StructuredGrid(coords[:, 0], coords[:, 1], coords[:, 2])
        self.plotter.add_mesh(mesh, color='lightblue', line_width=2.0)

    def plot_line(self, coords, **kwargs):
        """
        Plot a line from a set of coordinates.
        Parameters
        ----------
        coords : astropy.coordinates.SkyCoord
        **kwargs :
            Keyword arguments are handed to `pyvista.Plotter.add_mesh`.
        Notes
        -----
        This plots a `pyvista.Spline` object.
        """
        points = self._coords_to_xyz(coords)
        spline = pv.Spline(points)
        self.plotter.add_mesh(spline, **kwargs)

    def plot_solar_axis(self, length=2.5, arrow_kwargs={}, **kwargs):
        """
        Plot the solar rotation axis as an arrow.
        Parameters
        ----------
        length : float
            Length of the arrow in multiples of solar radii.
        arrow_kwargs : dict
            Keyword arguments to be handed to `pyvista.Arrow`.
            ``start``, ``direction``, and ``scale`` cannot be manually
            specified, as they are automatically set.
        **kwargs :
            Keyword arguments are handed to `pyvista.Plotter.add_mesh`.
        """
        defaults = {'shaft_radius': 0.01,
                    'tip_length': 0.05,
                    'tip_radius': 0.02}
        defaults.update(arrow_kwargs)
        arrow = pv.Arrow(start=(0, 0, -length / 2),
                         direction=(0, 0, length),
                         scale='auto',
                         **defaults)
        self.plotter.add_mesh(arrow, **kwargs)
        
        
"""
=======================
Three dimensional plots
=======================
sunpy can interface with the `pyvista` package to produce interactive 3D plots.
"""
###############################################################################
# Start by importing the required modules
import astropy.constants as const
import astropy.units as u
from astropy.coordinates import SkyCoord

from sunpy.data.sample import AIA_193_IMAGE
from sunpy.map import Map
# from sunpy.visualization.pyvista import PyVistaPlotter

###############################################################################
# Import some sample data
m = Map(AIA_193_IMAGE)
m.plot()

###############################################################################
# 3D plots are done on "plotter" objects, which are similar to matplotlib axes.
# sunpy has a built in `PyVistaPlotter` class that can be used to plot maps
# and coordinate aware objects.

# Start by creating a plotter
plotter = PyVistaPlotter()
# Plot a map
plotter.plot_map(m)
plotter.plot_quadrangle(m)
# plotter.plot_rectangle(m)
# Add an arrow to show the solar rotation axis
plotter.plot_solar_axis()
# Plot an arbitrary line
line = SkyCoord(lon=[180, 190, 200] * u.deg,
                lat=[0, 10, 20] * u.deg,
                distance=[1, 2, 3] * const.R_sun,
                frame='heliocentricinertial')
plotter.plot_line(line)

# Uncomment this line to show the plot when running locally
plotter.show(cpos=(-100,0,0), screenshot="quad.png")
