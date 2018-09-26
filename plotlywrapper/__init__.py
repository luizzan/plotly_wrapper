import plotly.plotly as py
import plotly.offline as po
import plotly.graph_objs as go
po.init_notebook_mode(connected=True)
import networkx as nx

import numpy as np
import requests
from PIL import Image

__version__ = '0.1.3'

# Import plotly settings from file
USERNAME, API_KEY, COLORS, COLORSCALE = '', '', [], []
FOOTER, FOOTER_LEFT, FOOTER_RIGHT = '', '', ''
try:
    from settings.plotlywrapper import *
except:
    pass


def py_sign_in(username, api_key):
    try:
        py.sign_in(username, api_key)
    except:
        print('Plotly sign in error. Saving plots to png is not available.')


# Try to sign in automatically
if USERNAME and API_KEY:
    py_sign_in(USERNAME, API_KEY)
else:
    print('Sign in to Plotly to save high-resolution plots locally.')
    print('plotlywrapper.py_sign_in(username, api_key)')


# Plot types
def bar(x, y, **kwargs):
    kwargs['plot_type'] = 'bar'
    kwargs['orientation'] = 'v'
    _all_plots(x, y, **kwargs)


def barh(x, y, **kwargs):
    kwargs['plot_type'] = 'bar'
    kwargs['orientation'] = 'h'
    kwargs['y_autorange'] = kwargs.pop('y_autorange', 'reversed')
    _all_plots(x, y, **kwargs)


def scatter(x, y, **kwargs):
    kwargs['plot_type'] = 'scatter'
    _all_plots(x, y, **kwargs)


def line(x, y, **kwargs):
    kwargs['plot_type'] = 'line'
    _all_plots(x, y, **kwargs)


def pie(x, **kwargs):
    kwargs['plot_type'] = 'pie'
    kwargs['hole'] = kwargs.pop('hole', 0)
    y = x
    _all_plots(x, y, **kwargs)


def network(x, **kwargs):
    kwargs['plot_type'] = 'network'
    y = x
    _all_plots(x, y, **kwargs)


def heatmap(x, y, z, **kwargs):
    kwargs['plot_type'] = 'heatmap'
    kwargs['z'] = z
    _all_plots(x, y, **kwargs)


# Plot aggregator
def _all_plots(x, y, **kwargs):

    if kwargs['plot_type'] in ['network', 'heatmap']:
        x = [x]
        y = [y]
    else:
        if type(x[0]) != list:
            x = [x]
            y = [y]
        

    names = kwargs.pop('names', ['']*len(x))
    text = kwargs.pop('text', ['']*len(x))
    textposition = kwargs.pop('textposition', 'auto')
    if kwargs['plot_type'] not in ['pie', 'network']:
        colors = kwargs.pop('colors', COLORS)
        colors = colors + (len(x)-len(colors))*['#000000']
        colorscale = kwargs.pop('colorscale', COLORSCALE)
        colorscale = colorscale if colorscale else 'RdBu'
    
    data = []
    for i, (_x, _y, _text, _name) in enumerate(zip(x, y, text, names)):

        if kwargs['plot_type'] == 'bar':
            data.append(go.Bar(
                x=_x,
                y=_y,
                text=_text,
                textposition=textposition,
                name=_name,
                orientation=kwargs['orientation'],
                marker=dict(color=colors[i]),
            ))

        elif kwargs['plot_type'] == 'scatter':
            data.append(go.Scatter(
                x=_x,
                y=_y,
                text=_text,
                name=_name,
                mode='markers',
                marker=dict(color=colors[i]),
            ))

        elif kwargs['plot_type'] == 'line':
            data.append(go.Scatter(
                x=_x,
                y=_y,
                text=_text,
                name=_name,
                mode='lines',
                marker=dict(color=colors[i]),
            ))

        elif kwargs['plot_type'] == 'pie':

            colors = kwargs.pop('colors', COLORS)
            colors = colors + (len(_x)-len(colors))*['#000000']
            colors = colors[:len(_x)]  # Seed only the required colors

            data.append(go.Pie(
                values=_x,
                labels=kwargs.pop('labels', ['']*len(_x)),
                textinfo='none',
                marker=dict(colors=colors),
                hole=kwargs['hole'],
                direction='clockwise',
                sort=False,
            ))

        elif kwargs['plot_type'] == 'network':

            colors = kwargs.pop('colors', [COLORS[0], COLORS[2]])

            G = nx.Graph()
            # Add nodes
            for key, vals in _x.items():
                G.add_node(key)
                for val in vals:
                    G.add_node(val)

            # Add edges
            for key, vals in _x.items():
                for val in vals:
                    G.add_edge(key, val)

            # Get node positions
            pos = nx.spring_layout(G)

            # Prepare go
            node_trace_l = go.Scatter(
                x=[], y=[], text=[], mode='text',
                textfont=dict(color=colors[0], size=20))
            node_trace_s = go.Scatter(
                x=[], y=[], text=[], mode='text',
                textfont=dict(color=colors[1], size=15))
            edge_trace = go.Scatter(
                x=[], y=[], mode='lines', opacity=0.3,
                line=dict(width=3, color=colors[1]))

            # Trace nodes
            for key, vals in pos.items():
                xx, yy = pos[key]
                
                if key in _x.keys():
                    node_trace_l['x'] += tuple([xx])
                    node_trace_l['y'] += tuple([yy])
                    node_trace_l['text'] += tuple([key])
                else:
                    node_trace_s['x'] += tuple([xx])
                    node_trace_s['y'] += tuple([yy])
                    node_trace_s['text'] += tuple([key])
                    
            # Trace edges
            for key, vals in _x.items():
                for val in vals:
                    x0, y0 = pos[key]
                    x1, y1 = pos[val]
                    edge_trace['x'] += tuple([x0, x1, None])
                    edge_trace['y'] += tuple([y0, y1, None])

            data += [edge_trace, node_trace_l, node_trace_s]

        elif kwargs['plot_type'] == 'heatmap':
            data.append(go.Heatmap(
                x=_x,
                y=_y,
                z=kwargs['z'],
                colorscale=colorscale,
            ))

    _plot_or_save(data, kwargs)


def _get_params(kwargs):
    
    params = {}
    params['title'] = kwargs.pop('title', '')
    params['x_title'] = kwargs.pop('x_title', '')
    params['y_title'] = kwargs.pop('y_title', '')
    params['fig_width'] = kwargs.pop('fig_width', 800)
    params['fig_height'] = kwargs.pop('fig_height', 400)
    if params['title']:
        params['t_margin'] = kwargs.pop('t_margin', 30)
    else:
        params['t_margin'] = kwargs.pop('t_margin', 0)
    params['b_margin'] = kwargs.pop('b_margin', 40)
    params['r_margin'] = kwargs.pop('r_margin', 0)
    params['l_margin'] = kwargs.pop('l_margin', 60)
    params['pad'] = kwargs.pop('pad', 5)
    params['filename'] = kwargs.pop('filename', '')
    params['x_tickangle'] = kwargs.pop('x_tickangle', 0)
    params['y_tickangle'] = kwargs.pop('y_tickangle', 0)
    
    params['x_range'] = kwargs.pop('x_range', [0, 0])
    if params['x_range'] == [0, 0]:
        params['x_autorange'] = kwargs.pop('x_autorange', True)
    else:
        params['x_autorange'] = kwargs.pop('x_autorange', False)
    params['y_range'] = kwargs.pop('y_range', [0, 0])
    if params['y_range'] == [0, 0]:
        params['y_autorange'] = kwargs.pop('y_autorange', True)
    else:
        params['y_autorange'] = kwargs.pop('y_autorange', False)

    if kwargs['plot_type'] == 'network':
        params['x_showticklabels'] = kwargs.pop('x_showticklabels', False)
        params['y_showticklabels'] = kwargs.pop('y_showticklabels', False)
        params['x_zeroline'] = kwargs.pop('x_zeroline', False)
        params['y_zeroline'] = kwargs.pop('y_zeroline', False)
    else:
        params['x_showticklabels'] = kwargs.pop('x_showticklabels', True)
        params['y_showticklabels'] = kwargs.pop('y_showticklabels', True)
        params['x_zeroline'] = kwargs.pop('x_zeroline', True)
        params['y_zeroline'] = kwargs.pop('y_zeroline', True)

    params['x_showgrid'] = kwargs.pop('x_showgrid', False)
    params['y_showgrid'] = kwargs.pop('y_showgrid', False)
    params['x_type'] = kwargs.pop('x_type', '-')
    params['y_type'] = kwargs.pop('y_type', '-')

    params['leg_orientation'] = kwargs.pop('leg_orientation', 'v')
    params['leg_traceorder'] = kwargs.pop('leg_traceorder', 'normal')
    params['leg_x'] = kwargs.pop('leg_x', 1.02)
    params['leg_y'] = kwargs.pop('leg_y', 1.00)


    if kwargs['plot_type'] == 'network':
        params['showlegend'] = kwargs.pop('showlegend', False)
    else:
        params['showlegend'] = kwargs.pop('showlegend', True)

    params['barmode'] = kwargs.pop('barmode', 'group')
    params['bargap'] = kwargs.pop('bargap', 0)
    params['bargroupgap'] = kwargs.pop('bargroupgap', 0)
    
#     # Calculate position of the SEMrush banner
#     params['y_banner'] = -1*params['b_margin']/(params['fig_height'] - params['b_margin'] - params['t_margin'])
#     params['x_banner'] = -1*params['l_margin']/(params['fig_width'] - params['l_margin'] - params['r_margin'])
#     params['x_sz_banner'] = params['fig_width']/(params['fig_width'] - params['l_margin'] - params['r_margin'])

    return params


def _get_layout(params):
    
    layout = go.Layout(
        title = params['title'],
        width = params['fig_width'],
        height = params['fig_height'],
#         Plotly does not support referencing for sizes
#         so the footer cannot have the same width as the
#         image if there is a legend. PIL is used instead.
#         images = [dict(
#             x = params['x_banner'],
#             y = params['y_banner'],
#             sizex = params['x_sz_banner'],
#             sizey = 1,
#             source = 'https://raw.githubusercontent.com/luizzan/images/master/pyw_footer.png',
#             xref = 'paper',
#             yref = 'paper',
#             xanchor = 'left',
#             yanchor = 'bottom',
#         )],
        margin = dict(
            t = params['t_margin'],
            b = params['b_margin'],
            r = params['r_margin'],
            l = params['l_margin'],
            pad = params['pad'],
        ),
        xaxis = dict(
            title = params['x_title'],
            tickangle = params['x_tickangle'],
            autorange = params['x_autorange'],
            range = params['x_range'],
            showgrid=params['x_showgrid'],
            showticklabels=params['x_showticklabels'],
            zeroline=params['x_zeroline'],
            type=params['x_type'],
        ),
        yaxis = dict(
            title = params['y_title'],
            tickangle = params['y_tickangle'],
            autorange = params['y_autorange'],
            range = params['y_range'],
            showgrid=params['y_showgrid'],
            showticklabels=params['y_showticklabels'],
            zeroline=params['y_zeroline'],
            type=params['y_type'],
        ),
        barmode = params['barmode'],
        bargap = params['bargap'],
        bargroupgap = params['bargroupgap'],
        showlegend = params['showlegend'],
        legend = dict(
            orientation=params['leg_orientation'],
            traceorder=params['leg_traceorder'],
            x = params['leg_x'],
            y = params['leg_y'],
        ),
    )

    return layout


def _plot_or_save(data, kwargs):

    params = _get_params(kwargs)
    layout = _get_layout(params)
    filename = params['filename']

    if filename:
        try:
            scale = kwargs.pop('scale', 5)
            py.image.save_as(dict(data=data, layout=layout),
                             filename=filename,
                             scale=scale,
            )
            
        except:
            print('Image export error. Check Plotly sign in parameters.')
            print('plotlywrapper.py_sign_in(username, api_key)')
            
        # Add footer, if any
        try:
            if FOOTER:
                footer_height = kwargs.pop('footer_height', 40)
                footer_height = footer_height*scale
                
                main_img = Image.open(filename)
                footer_img = Image.open(requests.get(FOOTER, stream=True).raw)
                footer_img = footer_img.resize((main_img.size[0], footer_height))
                if FOOTER_LEFT:
                    with Image.open(requests.get(FOOTER_LEFT, stream=True).raw) as _left:
                        _aspect_ratio = _left.size[0]/_left.size[1]
                        _width = round(_aspect_ratio*footer_height)
                        _left = _left.resize((_width, footer_height), Image.ANTIALIAS)
                        footer_img.paste(_left, (0,0))
                if FOOTER_RIGHT:
                    with Image.open(requests.get(FOOTER_RIGHT, stream=True).raw) as _right:
                        _aspect_ratio = _right.size[0]/_right.size[1]
                        _width = round(_aspect_ratio*footer_height)
                        _right = _right.resize((_width, footer_height), Image.ANTIALIAS)
                        footer_img.paste(_left, (0,0))
                        _pos = footer_img.size[0]-_right.size[0]
                        footer_img.paste(_right, (_pos,0))
                imgs = np.vstack([main_img, footer_img])
                Image.fromarray(imgs).save(filename)

        except:
            print('Image export error. Check footer images.')

    else:
        po.plot(dict(data=data, layout=layout))
