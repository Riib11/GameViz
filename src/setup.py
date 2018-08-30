from setuptools import setup
setup(
    name = 'gameviz',
    version = '0.0.0',
    packages = ['gameviz'],
    entry_points = { 'console_scripts': [
        'gameviz = gameviz.__main__:main'
    ]},
    author="Henry Blanchette",
    description="A graph notation format for game theory.",
    url="https://github.com/Riib11/GameViz"
)