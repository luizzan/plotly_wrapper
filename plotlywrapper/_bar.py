from ._basic_bar_scatter import _basic_bar_scatter

def _bar(self, kwargs):

	kwargs['plot_type'] = 'bar'
	
	return _basic_bar_scatter(self, kwargs)