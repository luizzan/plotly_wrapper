from ._basic_bar_scatter import _basic_bar_scatter

def _scatter(self, kwargs):

	kwargs['plot_type'] = 'scatter'
	kwargs['mode']='markers'

	return _basic_bar_scatter(self, kwargs)