# Install

`pip install git+https://github.com/luizzan/plotly_wrapper.git`

If running the command from within a virtualenv, be sure to have `wheel` installed in global python.<br>
Run `pip3 install wheel` outside the virtualenv.

# Requirements

To automatically sign in to Plotly (to save png files) and/or configure colors:
Somewhere in PYTHONPATH<br>
Create a "settings" folder<br>
In this folder create the following files:

plotly_wrapper.py
```
USERNAME = ''
API_KEY = ''
COLORS = ['']  # e.g.: ['#FFFFFF', '#000000']
FOOTER = ''  # See Footer section below for a detailed description
FOOTER_LEFT = ''
FOOTER_RIGHT = ''
```

# Usage example

See more details in `examples.ipynb`

```
import plotly_wrapper as pyw

# pyw.line(x, y, kwargs)
pyw.bar(['A', 'B', 'C'], [4, 6, 5])
pyw.bar([['A', 'B', 'C'], ['A', 'B', 'C']], [[1,3,2], [2,1,5]])

# pyw.bar(x, y, kwargs)
pyw.bar(['A', 'B', 'C'], [4, 6, 5])

# pyw.barh(x, y, kwargs)
pyw.barh([4, 6, 5], ['A', 'B', 'C'])

# pyw.scatter(x, y, kwargs)
pyw.scatter(['A', 'B', 'C'], [4, 6, 5])

# pyw.pie(x, kwargs)
pyw.pie([1, 3, 2], labels=['A', 'B', 'C'])
```

To save the plot to a png file:

```
pyw.bar(['A', 'B', 'C'], [4, 6, 5],
        filename='bar_plot.png',
)
```

# Footer

A footer can be added to the image. The `fig_height` and `fig_width` parameters do not take into account the footer dimensions. Footer height can be set using the `footer_height` parameter. Footer width will be the same as the original image.

Three-part footers can be configured in `settings.plotly_wrapper.py`:<br>
1. `FOOTER`: Can be a completer footer or a background image;
2. `FOOTER_LEFT`: An image to be attached to the left side of the footer;
3. `FOOTER_RIGHT`: Attached to the right side of the footer.

For a usage example, try these:
```
FOOTER = 'https://raw.githubusercontent.com/luizzan/images/master/pyw_footer.png'
FOOTER_LEFT = 'https://raw.githubusercontent.com/luizzan/images/master/pyw_footer_left.png'
FOOTER_RIGHT = 'https://raw.githubusercontent.com/luizzan/images/master/pyw_footer_right.png'
```

# Configurable parameters (kwargs):

```
title  # Main title
x_title  # x axis title
y_title  # y axis title
fig_width
fig_height
t_margin
b_margin
r_margin
l_margin
pad
filename  # if provided, the file is saved to <filename> instead of plotted
x_tickangle
y_tickangle
x_range
x_autorange
y_range
y_autorange
x_showticklabels
y_showticklabels
x_showgrid
y_showgrid
leg_orientation  # legend orientation
leg_traceorder
leg_x  # legend x position
leg_y  # legend y position
barmode  # for bar plots, 'grouped', 'stacked', etc.
bargap
bargroupgap
scale  # Figure scale, for higher resolutions. Default is 5
footer_height  # In pixels, calculated before scaling the figure
```
