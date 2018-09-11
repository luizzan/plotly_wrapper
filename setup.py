from setuptools import setup
from plotly_wrapper.version import version

setup(
    name='Plotly wrapper',
    url='https://github.com/luizzan/plotly_wrapper',
    author='Luiz Zanini',
    author_email='plotly_wrapper@luizzanini.com',
    packages=['plotly_wrapper'],
    version=version,
    install_requires = [
    	'numpy',
        'plotly',
        'Pillow',
    ],
)
