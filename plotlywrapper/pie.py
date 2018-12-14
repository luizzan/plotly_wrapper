def pie(self, values, kwargs):

	kwargs['colors'] = kwargs.get('colors', self.colors)
	kwargs['colors'] = kwargs['colors'] + (len(values)-len(kwargs['colors']))*[None]

	data = dict(
		type = 'pie',
		values = values,
		labels = kwargs.get('labels', ['']*len(values)),
		textinfo = kwargs.get('textinfo', 'none'),
		marker = dict(colors=kwargs['colors']),
		hole = kwargs.get('hole', 0),
		direction =kwargs.get('direction', 'clockwise'),
		sort = kwargs.get('sort', False),
	)
	self.data.append(data)

	kwargs['width'] = kwargs.get('width', 500)
	kwargs['margin_l'] = kwargs.get('margin_l', 10)
	kwargs['margin_r'] = kwargs.get('margin_r', 10)

	self.kwargs.update(kwargs)
