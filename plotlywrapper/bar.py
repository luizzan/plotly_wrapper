from .basic_bar_scatter import basic_bar_scatter

def bar(self, x, y, kwargs):

	kwargs['plot_type'] = 'bar'
	
	basic_bar_scatter(self, x, y, kwargs)