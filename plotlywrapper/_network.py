import networkx as nx

def _network(self, kwargs):

    kwargs['colors'] = kwargs.get('colors', self.colors)
    data = kwargs['data']

    G = nx.Graph()
    # Add nodes
    for key, vals in data.items():
        G.add_node(key)
        for val in vals:
            G.add_node(val)

    # Add edges
    for key, vals in data.items():
        for val in vals:
            G.add_edge(key, val)

    # Get node positions
    pos = nx.spring_layout(G)

    # Prepare go
    node_trace_l = dict(
        type='scatter', x=[], y=[], text=[], mode='text',
        textfont=dict(color=kwargs['colors'][0], size=20)
    )
    node_trace_s = dict(
        type='scatter', x=[], y=[], text=[], mode='text',
        textfont=dict(color=kwargs['colors'][1], size=15)
    )
    edge_trace = dict(
        type='scatter', x=[], y=[], mode='lines', opacity=kwargs.get('edge_opacity', 0.3),
        line=dict(width=kwargs.get('edge_width', 3), color=kwargs['colors'][1])
    )

    # Trace nodes
    for key, vals in pos.items():
        xx, yy = pos[key]
        
        if key in data.keys():
            node_trace_l['x'] += tuple([xx])
            node_trace_l['y'] += tuple([yy])
            node_trace_l['text'] += tuple([key])
        else:
            node_trace_s['x'] += tuple([xx])
            node_trace_s['y'] += tuple([yy])
            node_trace_s['text'] += tuple([key])
            
    # Trace edges
    for key, vals in data.items():
        for val in vals:
            x0, y0 = pos[key]
            x1, y1 = pos[val]
            edge_trace['x'] += tuple([x0, x1, None])
            edge_trace['y'] += tuple([y0, y1, None])

    self.data += edge_trace, node_trace_l, node_trace_s

    kwargs['x_showticklabels'] = kwargs.get('x_showticklabels', False)
    kwargs['y_showticklabels'] = kwargs.get('y_showticklabels', False)
    kwargs['x_zeroline'] = kwargs.get('x_zeroline', False)
    kwargs['y_zeroline'] = kwargs.get('y_zeroline', False)
    kwargs['showlegend'] = kwargs.get('showlegend', False)
    #self.layout.update(dict())

    return kwargs
