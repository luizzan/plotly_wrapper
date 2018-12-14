import plotly.offline as po
po.init_notebook_mode(connected=True)

def plot(self):        

    po.plot(
        dict(data=self.data, layout=self.layout),
        filename='temp-plot.html',
        auto_open=not self.plot_inline,
    )

    self.reset()  # Remove previous plot and layout data

    # Plotly's iplot often has issues, so this shows the plot inline instead
    if self.plot_inline:
        import IPython
        return IPython.display.HTML('temp-plot.html')
