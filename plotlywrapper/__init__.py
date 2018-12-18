from .bar import bar
from .barh import barh
from .heatmap import heatmap
from .layout_basic import layout_basic
from .line import line
from .network import network
from .pie import pie
from .scatter import scatter
from .scattermapbox import scattermapbox
from .table import table
from .load_settings import load_settings
from .plot import plot
from .save import save


__version__ = '0.3.2'


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
        self.kwargs = {}


    def reset(self):
        self.__init__()


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

        line(self, x, y, kwargs)
        self._all_plots()


    def scatter(self, x, y, **kwargs):
        """
        Plot scatter chart.
        Parameters:
        - x
        - y
        - names
        - text
        """

        scatter(self, x, y, kwargs)
        self._all_plots()


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

        bar(self, x, y, kwargs)
        self._all_plots()


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

        barh(self, x, y, kwargs)
        self._all_plots()


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

        pie(self, values, kwargs)
        self._all_plots()


    def network(self, data, **kwargs):
        """
        Plot network.
        Parameters:
        - data
        - edge_width
        - edge_opacity
        """

        network(self, data, kwargs)
        self._all_plots()


    def heatmap(self, x, y, z, **kwargs):
        """
        Plot heatmap.
        Parameters:
        - x
        - y
        - z
        - colorscale
        """

        heatmap(self, x, y, z, kwargs)
        self._all_plots()


    def table(self, cells, **kwargs):
        """
        Plot table.
        Parameters:
        - cells
        - header
        - cell_height
        - header_height
        """

        table(self, cells, kwargs)
        self._all_plots()


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
        
        scattermapbox(self, location, values, kwargs)
        self._all_plots()


    def _all_plots(self):
        layout_basic(self)


    def layout(self, **kwargs):
        """
        Add parameters to layout.
        """

        self.layout.update(kwargs)


    def plot(self):
        """
        Plot chart.
        """

        return plot(self)


    def save(self, filename, **kwargs):
        """
        Save plot locally.
        Parameters:
        - filename
        - scale
        - footer_height
        """

        save(self, filename, kwargs)
