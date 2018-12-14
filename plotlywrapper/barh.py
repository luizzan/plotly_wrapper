from .basic_bar_scatter import basic_bar_scatter

def barh(self, x, y, kwargs):

	kwargs['plot_type'] = 'bar'
	kwargs['orientation'] = kwargs.pop('orientation', 'h')
	kwargs['y_autorange'] = kwargs.pop('y_autorange', 'reversed')

	basic_bar_scatter(self, x, y, kwargs)