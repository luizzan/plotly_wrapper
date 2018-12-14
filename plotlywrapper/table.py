def table(self, cells, kwargs):

	# Prepare plot
	if kwargs.get('header', []):
		if type(kwargs['header']) != list:
			kwargs['header'] = [kwargs['header']]
		kwargs['header'] = ['<b>{}</b>'.format(i) for i in kwargs['header']]
		kwargs['header_height'] = kwargs.get('header_height', 30)
	else:
		kwargs['header'] = ['']
		kwargs['header_height'] = 0

	if type(cells[0]) != list:
		cells = [cells]
	kwargs['cell_height'] = kwargs.get('cell_height', 20)

	self.data.append(dict(
		type = 'table',
		header = dict(values=kwargs['header'], height=kwargs['header_height']),
		cells = dict(values=cells, height=kwargs['cell_height']),
	))

	kwargs['margin_t'] = kwargs.get('margin_t', 1)
	kwargs['margin_b'] = kwargs.get('margin_b', 1)
	kwargs['margin_l'] = kwargs.get('margin_l', 1)
	kwargs['margin_r'] = kwargs.get('margin_r', 1)
	kwargs['height'] = kwargs.get('height', None)
	kwargs['width'] = kwargs.get('width', 200*len(cells))
	if not kwargs.get('height', None):
		margins = kwargs['margin_t'] + kwargs['margin_b']
		kwargs['height'] = margins + kwargs['header_height'] + \
			kwargs['cell_height']*len(cells[0]) + 4

	self.layout.update(dict())

	self.kwargs.update(kwargs)
