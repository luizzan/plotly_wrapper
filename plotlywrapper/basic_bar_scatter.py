def basic_bar_scatter(self, x, y, kwargs):

    """Basic parameters for bar, barh, line and scatter plots"""

    data = dict(
        type = kwargs['plot_type'],
        x = x,
        y = y,
        text = kwargs.get('text', ''),
        name = kwargs.get('name', ''),
        orientation = kwargs.get('orientation', 'v'),
        marker = dict(
            color=kwargs.get('color', self.colors[len(self.data)] if self.colors else None),
            ),
    )

    if kwargs['plot_type'] == 'bar':
        data.update(
            textposition = kwargs.get('textposition', 'auto'),
        )
        self.layout.update(dict(
            barmode = kwargs.get('barmode', 'group'),
            bargap = kwargs.get('bargap', 0.1),
            bargroupgap = kwargs.get('bargroupgap', 0),
        ))

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
    
    kwargs['showlegend'] = kwargs.get('showlegend', len(self.data) > 1)
    # Prioritize bg image over footer
    kwargs['bg_image'] = kwargs.get('bg_image', self.kwargs.get('bg_image', not not self.bg_image))
    kwargs['footer'] = kwargs.get('footer', not kwargs['bg_image'] and not not self.footer)

    self.kwargs.update(kwargs)
