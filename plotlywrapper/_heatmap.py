def _heatmap(self, kwargs):

	data = dict(
		type = 'heatmap',
		x = kwargs['x'],
		y = kwargs['y'],
		z = kwargs['z'],
		colorscale = kwargs.get('colorscale', self.colorscale),
	)
	self.data.append(data)

	#self.layout.update(dict())

	return kwargs