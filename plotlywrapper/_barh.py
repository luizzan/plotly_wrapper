from ._basic_bar_scatter import _basic_bar_scatter

def _barh(self, kwargs):

	kwargs['plot_type'] = 'bar'
	kwargs['orientation'] = kwargs.pop('orientation', 'h')
	kwargs['y_autorange'] = kwargs.pop('y_autorange', 'reversed')

	return _basic_bar_scatter(self, kwargs)