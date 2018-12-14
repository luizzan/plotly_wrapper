def _layout_basic(self, **kwargs):
    
    # Standard parameters
    self.layout.update(dict(
        title = kwargs.get('title', ''),
        width = kwargs.get('width', 800),
        height = kwargs.get('height', 400),
        margin = dict(
            t = kwargs.get('margin_t', 30 if kwargs.get('title', '') else 10),
            b = kwargs.get('margin_b', 50 if kwargs.get('x_title', '') else 30),
            l = kwargs.get('margin_l', 60 if kwargs.get('y_title', '') else 40),
            r = kwargs.get('margin_r', 10),
            pad = kwargs.get('pad', 2),
        ),
        xaxis = dict(
            title = kwargs.get('x_title', ''),
            tickangle = kwargs.get('x_tickangle', 0),
            autorange = kwargs.get('x_autorange', False if kwargs.get('x_range', '') else True),
            range = kwargs.get('x_range', [0, 0]),
            showgrid = kwargs.get('x_showgrid', False),
            showticklabels = kwargs.get('x_showticklabels', True),
            zeroline = kwargs.get('x_zeroline', True),
            type = kwargs.get('x_type', '-'),
        ),
        yaxis = dict(
            title = kwargs.get('y_title', ''),
            tickangle = kwargs.get('y_tickangle', 0),
            autorange = kwargs.get('y_autorange', False if kwargs.get('y_range', '') else True),
            range = kwargs.get('y_range', [0, 0]),
            showgrid = kwargs.get('y_showgrid', False),
            showticklabels = kwargs.get('y_showticklabels', True),
            zeroline = kwargs.get('y_zeroline', True),
            type = kwargs.get('y_type', '-'),
        ),
        showlegend = kwargs.get('showlegend', True),
        legend = dict(
            orientation = kwargs.get('leg_orientation', 'v'),
            traceorder = kwargs.get('leg_traceorder', 'normal'),
            x = kwargs.get('leg_x', 1.02),
            y = kwargs.get('leg_y', 1.00),
        ),
    ))

    if self.bg_image and kwargs.get('bg_image', False):
        self.layout.update(dict(
            images= [dict(
                source= self.bg_image,
                xref= kwargs.get('images_xref', 'paper'),
                yref= kwargs.get('images_yref', 'paper'),
                x= kwargs.get('images_x', 0.5),
                y= kwargs.get('images_y', 0.5),
                xanchor = kwargs.get('images_xanchor', 'center'),
                yanchor = kwargs.get('images_yanchor', 'middle'),
                sizex = kwargs.get('images_sizex', 1),
                sizey = kwargs.get('images_sizey', 1),
                sizing= kwargs.get('images_sizing', 'contain'),
                opacity= kwargs.get('images_opacity', 0.2),
                layer= kwargs.get('images_layer', 'below'),
            )],
    ))
