import plotly.plotly as py
import plotly.offline as po
import plotly.graph_objs as go
po.init_notebook_mode(connected=True)

from ._add_footer import _add_footer
from ._bar import _bar
from ._barh import _barh
from ._heatmap import _heatmap
from ._layout_basic import _layout_basic
from ._line import _line
from ._network import _network
from ._pie import _pie
from ._scatter import _scatter
from ._scattermapbox import _scattermapbox
from ._table import _table
from .load_settings import load_settings


__version__ = '0.2.1'


# Plot types
class PlotlyWrapper():
    """
    Plotly wrapper.
    Parameters valid for all plots:
    - height
    - width
    - margin_t
    - margin_b
    - margin_l
    - margin_r
    - pad
    - title
    - showlegend
    - leg_orientation
    - leg_traceorder
    - leg_x
    - leg_y

    All parameters below can also be used for the y axis
    - x_title
    - x_tickangle
    - x_autorange
    - x_range
    - x_showgrid
    - x_showticklabels
    - x_zeroline
    - x_type
    """

    def __init__(self):
        self.data = []
        self.layout = {}


    def load_settings(self, settings_file):
        """
        Load settings from JSON file.
        File format example:
        {
            "username" : "",
            "api_key" : "",
            "mapbox_token" : "",
            "colors" : ["#FFFFFF", "#000000"],
            "colorscale" : [[0.0, "#FFFFFF"], [0.5, "#FF0000"], [1, "#000000"]],
            "footer" : "https://raw.githubusercontent.com/luizzan/images/master/pyw_footer.png",
            "footer_left" : "https://raw.githubusercontent.com/luizzan/images/master/pyw_footer_left.png",
            "footer_right" : "https://raw.githubusercontent.com/luizzan/images/master/pyw_footer_right.png",
        }
        """

        load_settings(self, settings_file)


    def line(self, x, y, **kwargs):
        """
        Plot line chart.
        Parameters:
        - x
        - y
        - names
        - text
        """

        kwargs['x'] = x
        kwargs['y'] = y
        self._all_plots(_line(self, kwargs))


    def scatter(self, x, y, **kwargs):
        """
        Plot scatter chart.
        Parameters:
        - x
        - y
        - names
        - text
        """

        kwargs['x'] = x
        kwargs['y'] = y
        self._all_plots(_scatter(self, kwargs))


    def bar(self, x, y, **kwargs):
        """
        Plot vertical bar chart.
        Parameters:
        - x
        - y
        - names
        - text
        - barmode
        - bargap
        - bargroupgap
        """

        kwargs['x'] = x
        kwargs['y'] = y
        self._all_plots(_bar(self, kwargs))


    def barh(self, x, y, **kwargs):
        """
        Plot horizontal bar chart.
        Parameters:
        - x
        - y
        - names
        - text
        - barmode
        - bargap
        - bargroupgap
        """

        kwargs['x'] = x
        kwargs['y'] = y
        self._all_plots(_barh(self, kwargs))


    def pie(self, values, **kwargs):
        """
        Plot pie chart.
        Parameters:
        - values
        - labels
        - textinfo
        - hole
        - direction
        - sort
        """

        kwargs['values'] = values
        self._all_plots(_pie(self, kwargs))


    def network(self, data, **kwargs):
        """
        Plot network.
        Parameters:
        - data
        - edge_width
        - edge_opacity
        """

        kwargs['data'] = data
        self._all_plots(_network(self, kwargs))


    def heatmap(self, x, y, z, **kwargs):
        """
        Plot heatmap.
        Parameters:
        - x
        - y
        - z
        - colorscale
        """

        kwargs['x'] = x
        kwargs['y'] = y
        kwargs['z'] = z
        self._all_plots(_heatmap(self, kwargs))


    def table(self, header, cells, **kwargs):
        """
        Plot table.
        Parameters:
        - header
        - cells
        - header_height
        - cell_height
        """

        kwargs['header'] = header
        kwargs['cells'] = cells
        self._all_plots(_table(self, kwargs))


    def scattermapbox(self, location, values, **kwargs):
        """
        Plot map.
        Parameters:
        - location
        - values (dict or dataframe)
        - colorscale
        - range
        - showscale
        - bearing
        - lat
        - lon
        - pitch
        - zoom
        - style
        - autocolorscale
        - colorbar_thickness
        - colorbar_titleside
        - colorbar_outlinecolor
        - colorbar_ticks
        - colorbar_ticklen
        - colorbar_ticksuffix
        - colorbar_dtick
        """

        self._all_plots(_scattermapbox(self, location, values, kwargs))


    def _all_plots(self, kwargs):
        _layout_basic(self, **kwargs)


    def layout(self, **kwargs):
        """
        Add parameters to layout.
        """
        self.layout.update(kwargs)


    def plot(self):
        """
        Plot chart.
        """

        po.plot(dict(data=self.data, layout=self.layout))
        self.__init__()  # Remove previous plot and layout data


    def save(self, filename='', scale=5, footer_height=48):
        """
        Save plot locally.
        Parameters:
        - filename
        - scale
        - footer_height
        """

        try:
            py.sign_in(self.username, self.api_key)
            py.image.save_as(
                dict(data=self.data, layout=self.layout),
                filename=filename,
                scale=scale,
            )
            _add_footer(self, filename=filename, scale=scale, footer_height=footer_height)
        except Exception as e:
            print(e)
            print('\n\nImage export error. Check Plotly username and API key.')

        self.__init__()  # Remove previous plot and layout data
