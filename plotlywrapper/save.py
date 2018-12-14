import plotly.plotly as py
from .add_footer import add_footer

def save(self, filename, kwargs):

    kwargs['filename'] = filename
    self.kwargs.update(kwargs)

    try:
        py.sign_in(self.username, self.api_key)
        py.image.save_as(
            dict(data=self.data, layout=self.layout),
            filename=filename,
            scale=self.kwargs.get('scale', 5),
        )
        add_footer(self)
        self.reset()

    except Exception as e:
        print(e)
        print('\n\nImage export error. Check Plotly username and API key.')
