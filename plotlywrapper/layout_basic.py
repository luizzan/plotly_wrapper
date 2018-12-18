def layout_basic(self):
    
    # Standard parameters
    self.layout.update(dict(
        title = self.kwargs.get('title', ''),
        width = self.kwargs.get('width', 800),
        height = self.kwargs.get('height', 400),
        margin = dict(
            t = self.kwargs.get('margin_t', 30 if self.kwargs.get('title', '') else 10),
            b = self.kwargs.get('margin_b', 50 if self.kwargs.get('x_title', '') else 30),
            l = self.kwargs.get('margin_l', 60 if self.kwargs.get('y_title', '') else 40),
            r = self.kwargs.get('margin_r', 10),
            pad = self.kwargs.get('pad', 2),
        ),
        xaxis = dict(
            title = self.kwargs.get('x_title', ''),
            tickangle = self.kwargs.get('x_tickangle', 0),
            autorange = self.kwargs.get('x_autorange', False if self.kwargs.get('x_range', '') else True),
            range = self.kwargs.get('x_range', [0, 0]),
            showgrid = self.kwargs.get('x_showgrid', False),
            showticklabels = self.kwargs.get('x_showticklabels', True),
            zeroline = self.kwargs.get('x_zeroline', True),
            type = self.kwargs.get('x_type', '-'),
            linecolor = self.kwargs.get('x_linecolor', '#000000'),
            linewidth = self.kwargs.get('x_linewidth', 0),
        ),
        yaxis = dict(
            title = self.kwargs.get('y_title', ''),
            tickangle = self.kwargs.get('y_tickangle', 0),
            autorange = self.kwargs.get('y_autorange', False if self.kwargs.get('y_range', '') else True),
            range = self.kwargs.get('y_range', [0, 0]),
            showgrid = self.kwargs.get('y_showgrid', False),
            showticklabels = self.kwargs.get('y_showticklabels', True),
            zeroline = self.kwargs.get('y_zeroline', True),
            type = self.kwargs.get('y_type', '-'),
            linecolor = self.kwargs.get('y_linecolor', '#000000'),
            linewidth = self.kwargs.get('y_linewidth', 0),
        ),
        showlegend = self.kwargs.get('showlegend', True),
        legend = dict(
            orientation = self.kwargs.get('leg_orientation', 'v'),
            traceorder = self.kwargs.get('leg_traceorder', 'normal'),
            x = self.kwargs.get('leg_x', 1.02),
            y = self.kwargs.get('leg_y', 1.00),
        ),
    ))

    self.kwargs['bg_image'] = self.kwargs.get('bg_image', False)
    if self.bg_image and self.kwargs['bg_image']:
        self.layout.update(dict(
            images= [dict(
                source = self.bg_image,
                xref = self.kwargs.get('images_xref', 'paper'),
                yref = self.kwargs.get('images_yref', 'paper'),
                x = self.kwargs.get('images_x', 0.5),
                y = self.kwargs.get('images_y', 0.5),
                xanchor = self.kwargs.get('images_xanchor', 'center'),
                yanchor = self.kwargs.get('images_yanchor', 'middle'),
                sizex = self.kwargs.get('images_sizex', 1),
                sizey = self.kwargs.get('images_sizey', 1),
                sizing = self.kwargs.get('images_sizing', 'contain'),
                opacity = self.kwargs.get('images_opacity', 0.2),
                layer = self.kwargs.get('images_layer', 'below'),
            )],
    ))
