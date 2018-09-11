from setuptools import setup

setup(
    name='Plotly wrapper',
    url='https://github.com/luizzan/plotly_wrapper',
    author='Luiz Zanini',
    author_email='plotly_wrapper@luizzanini.com',
    packages=['plotly_wrapper'],
    install_requires = [
    	'numpy',
        'plotly',
        'Pillow',
    ],
)
