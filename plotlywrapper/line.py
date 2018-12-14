from .basic_bar_scatter import basic_bar_scatter

def line(self, x, y, kwargs):

	kwargs['plot_type'] = 'scatter'
	kwargs['mode']='lines'

	basic_bar_scatter(self, x, y, kwargs)
