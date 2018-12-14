import json
import requests
import pandas as pd
import matplotlib.cm as cm
from matplotlib.colors import LinearSegmentedColormap as lsc

def rgb_from_cmap(cmap, value):
	color = cmap(value)
	color = tuple([int(i*255) for i in color[:3]])
	color = 'rgb{}'.format(color)
	return color

def scattermapbox(self, location, values, kwargs):

	# Convert dataframe to dict
	if type(values) == pd.DataFrame:
		values = list(values.to_dict().values())[0]

	# Get colorscale
	colorscale = kwargs.get('colorscale', self.colorscale)
	if type(colorscale) == list:
		cmap = lsc.from_list('', colorscale)
	else:
		cmap = cm.get_cmap(colorscale)
	colorscale = [[i/10, rgb_from_cmap(cmap, i/10)] for i in range(11)]

	# Databases: geojson, center (lat, lon)
	dbs = {
		'brazil_states' : [
			'https://raw.githubusercontent.com/luizzan/files/master/geojson/br_states.geojson',
			-15.460556, -55.749722],
		'us_states' : [
			'https://raw.githubusercontent.com/luizzan/files/master/geojson/us_states.geojson',
			39.833333, -98.583333],
	}

	url, lat, lon = dbs[location]
	sources = json.loads(requests.get(url).content)['features']

	ls_geo = {}
	for source in sources:
		ls_geo[source['properties']['code']] = source['geometry']

	layers = []
	_range = kwargs.get('range', [min(values.values()), max(values.values())])
	if _range[0] == _range[1]:
		_range = [0, _range[0]]

	for k, v in values.items():
		# Get color in colorscale
		color = rgb_from_cmap(cmap, (v-_range[0])/(_range[1]-_range[0]))

		layers.append(dict(
			sourcetype = 'geojson',
			source = ls_geo[k],
			type = 'fill',
			color = color,
		))

	data = dict(
			type = 'scattermapbox',
			mode = kwargs.get('mode', 'markers'),
	)
	if kwargs.get('showscale', True):
		data.update(dict(
				name = '',
				lat = [0],
				lon = [0],
				marker = dict(
					showscale = kwargs.get('showscale', True),
					cmin = _range[0],
					cmax = _range[1],
					colorscale = colorscale,
					size = 0,
					autocolorscale = kwargs.get('autocolorscale', False),
					colorbar = dict(
						thickness = kwargs.get('colorbar_thickness', 25),
						titleside = kwargs.get('colorbar_titleside', 'right'),
						outlinecolor = kwargs.get('colorbar_outlinecolor', '#FFFFFF'),
						ticks = kwargs.get('colorbar_ticks', 'inside'),
						ticklen = kwargs.get('colorbar_ticklen', 5),
						ticksuffix = kwargs.get('colorbar_ticksuffix', ''),
						dtick = kwargs.get('colorbar_dtick', None),
					)
				),
		))
	self.data.append(data)

	kwargs['margin_t'] = kwargs.get('margin_t', 0)
	kwargs['margin_b'] = kwargs.get('margin_b', 0)
	kwargs['margin_l'] = kwargs.get('margin_l', 0)
	kwargs['margin_r'] = kwargs.get('margin_r', 0)
	kwargs['width'] = kwargs.get('width', 900)
	kwargs['height'] = kwargs.get('height', 800)

	self.layout.update(dict(
		mapbox=dict(
			layers=layers,
			accesstoken=self.mapbox_token,
			bearing=kwargs.get('bearing', 0),
			center=dict(
				lat = kwargs.get('lat', lat),
				lon = kwargs.get('lon', lon),
			),
			pitch=kwargs.get('pitch', 0),
			zoom=kwargs.get('zoom', 3.5),
			style=kwargs.get('style', 'light'),
		),
	))

	self.kwargs.update(kwargs)
