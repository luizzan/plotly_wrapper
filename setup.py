from setuptools import setup

setup(
    name='plotlywrapper',
    url='https://github.com/luizzan/plotlywrapper',
    author='Luiz Zanini',
    author_email='plotlywrapper@luizzanini.com',
    packages=['plotlywrapper'],
    version='0.1.0',
    install_requires = [
        'numpy',
        'plotly',
        'Pillow',
    ],
)
