from setuptools import setup

setup(
    name="electrum-twist-server",
    version="1.0",
    scripts=['run_electrum_twist_server.py','electrum-twist-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0'],
    package_dir={
        'electrumtwistserver':'src'
        },
    py_modules=[
        'electrumtwistserver.__init__',
        'electrumtwistserver.utils',
        'electrumtwistserver.storage',
        'electrumtwistserver.deserialize',
        'electrumtwistserver.networks',
        'electrumtwistserver.blockchain_processor',
        'electrumtwistserver.server_processor',
        'electrumtwistserver.processor',
        'electrumtwistserver.version',
        'electrumtwistserver.ircthread',
        'electrumtwistserver.stratum_tcp'
    ],
    description="Twist Electrum Server",
    author="TWISTproject",
    license="MIT Licence",
    url="https://github.com/dev0tion/electrum-twist-server/",
    long_description="""Server for the Electrum Lightweight Twist Wallet"""
)
