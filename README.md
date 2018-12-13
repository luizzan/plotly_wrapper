# Install

`pip install git+https://github.com/luizzan/plotlywrapper.git`

If running the command from within a virtualenv, be sure to have `wheel` installed in global python.<br>
Run `pip3 install wheel` outside the virtualenv.

# Notes

Saving images as PNG files is only available if signed in to Plotly.<br>
Plotting maps requires a mapbox token.<br><br>

A settings file can be used to store usernames, passwords and a few other parameters in JSON format. Example:

```
{
	"username" : "",
	"api_key" : "",
	"mapbox_token" : "",
	"colors" : ["#FFFFFF", "#000000"],
	"colorscale" : [[0.0, "#FFFFFF"], [0.5, "#FF0000"], [1, "#000000"]],
	"footer" : "https://raw.githubusercontent.com/luizzan/images/master/pyw_footer.png",
	"footer_left" : "https://raw.githubusercontent.com/luizzan/images/master/pyw_footer_left.png",
	"footer_right" : "https://raw.githubusercontent.com/luizzan/images/master/pyw_footer_right.png",
    "plot_inline" : true
}
```

Note that none of these parameters is mandatory.

# Usage example

See more details in `examples.ipynb`

```
from plotlywrapper import PlotlyWrapper
pyw = PlotlyWrapper()
pyw.load_settings('path/to/json/file.json')

pyw.line(
    [
        ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    ],
    [
        [1.5, 4, 3, 6, 5, 8, 7],
        [0.5, 3, 2, 5, 4, 7, 6],
    ],
    names = ['A', 'B'],
)
pyw.plot()

pyw.scatter(
    ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    [0.5, 3, 2, 5, 4, 7, 6],
)
pyw.save(filename='my_fig.png')

```

# Footer

A footer can be added to the image. The `fig_height` and `fig_width` parameters do not take into account the footer dimensions. Footer height can be set using the `footer_height` parameter. Footer width will be the same as the original image.

Three-part footers can be configured in the settings file:<br>
1. `footer`: Can be a completer footer or a background image, mandatory if using any of the other footers below;
2. `footer_left`: An image to be attached to the left side of the footer;
3. `footer_right`: Attached to the right side of the footer.

For a usage example, try these:
```
footer = 'https://raw.githubusercontent.com/luizzan/images/master/pyw_footer.png'
footer_left = 'https://raw.githubusercontent.com/luizzan/images/master/pyw_footer_left.png'
footer_right = 'https://raw.githubusercontent.com/luizzan/images/master/pyw_footer_right.png'
```

# Configurable parameters (kwargs):

Use `help(pyw)` for general parameters or, for instance, `help(pyw.line)` for parameters specific to a plot type.
