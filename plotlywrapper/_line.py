from ._basic_bar_scatter import _basic_bar_scatter

def _line(self, kwargs):

	kwargs['plot_type'] = 'scatter'
	kwargs['mode']='lines'

	return _basic_bar_scatter(self, kwargs)