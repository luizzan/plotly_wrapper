def _pie(self, kwargs):

	kwargs['colors'] = kwargs.get('colors', self.colors)
	kwargs['colors'] = kwargs['colors'] + (len(kwargs['values'])-len(kwargs['colors']))*['#000000']

	data = dict(
		type = 'pie',
		values = kwargs['values'],
		labels = kwargs.get('labels', ['']*len(kwargs['values'])),
		textinfo = kwargs.get('textinfo', 'none'),
		marker = dict(colors=kwargs['colors']),
		hole = kwargs.get('hole', 0),
		direction =kwargs.get('direction', 'clockwise'),
		sort = kwargs.get('sort', False),
	)
	self.data.append(data)

	kwargs['width'] = kwargs.get('width', 600)
	#self.layout.update(dict())

	return kwargs