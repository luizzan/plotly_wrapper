def heatmap(self, x, y, z, kwargs):

	data = dict(
		type = 'heatmap',
		x = x,
		y = y,
		z = z,
		colorscale = kwargs.get('colorscale', self.colorscale),
	)
	self.data.append(data)