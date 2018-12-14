def _basic_bar_scatter(self, kwargs):

    """Basic parameters for bar, barh, line and scatter plots"""

    if type(kwargs['x'][0]) != list:
        kwargs['x'] = [kwargs['x']]
        kwargs['y'] = [kwargs['y']]
        kwargs['showlegend'] = kwargs.get('showlegend', False)
    else:
        kwargs['showlegend'] = kwargs.get('showlegend', True)
        
    kwargs['names'] = kwargs.get('names', ['']*len(kwargs['x']))
    kwargs['text'] = kwargs.get('text', ['']*len(kwargs['x']))
    kwargs['colors'] = kwargs.get('colors', self.colors)
    kwargs['bg_image'] = kwargs.get('bg_image', True)  # shows a provided background image

    for i, (x, y, text, name) in enumerate(zip(
                                                kwargs['x'],
                                                kwargs['y'],
                                                kwargs['text'],
                                                kwargs['names'],
                                            )):
        data = dict(
            type = kwargs['plot_type'],
            x = x,
            y = y,
            text = text,
            name = name,
            orientation = kwargs.get('orientation', 'v'),
            marker = dict(
                color=kwargs['colors'][i] if kwargs['colors'] and i < len(kwargs['colors']) else None
                ),
        )
        if kwargs['plot_type'] == 'bar':
            data.update(
                textposition = kwargs.get('textposition', 'auto'),
            )
        elif kwargs['plot_type'] == 'line':
            data.update(
                line = dict(
                    dash = kwargs.get('dash', 'solid'),
                ),
            )
        else:
            data.update(
                mode = kwargs['mode'],
            )
        self.data.append(data)
    
    self.layout.update(dict(
        barmode = kwargs.get('barmode', 'group'),
        bargap = kwargs.get('bargap', 0.1),
        bargroupgap = kwargs.get('bargroupgap', 0),
    ))

    return kwargs