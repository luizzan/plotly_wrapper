import json

def load_settings(self, json_settings):

    with open(json_settings, 'r') as f:
        kwargs = json.load(f)

    self.username = kwargs.get('username', '')
    self.api_key = kwargs.get('api_key', '')
    self.colors = kwargs.get('colors', None)
    self.colorscale = kwargs.get('colorscale', 'RdBu')
    self.footer = kwargs.get('footer', '')
    self.footer_left = kwargs.get('footer_left', '')
    self.footer_right = kwargs.get('footer_right', '')
    self.mapbox_token = kwargs.get('mapbox_token', '')
    self.plot_inline = kwargs.get('plot_inline', False)
    self.bg_image = kwargs.get('bg_image', '')
