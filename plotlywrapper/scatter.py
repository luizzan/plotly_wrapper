from .basic_bar_scatter import basic_bar_scatter

def scatter(self, x, y, kwargs):

	kwargs['plot_type'] = 'scatter'
	kwargs['mode']='markers'

	basic_bar_scatter(self, x, y, kwargs)