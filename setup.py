from setuptools import setup

setup(
    zip_safe=True,
    name='cloudify-nso-plugin',
    version='1.0',
    author='Data Vision',
    author_email='info@datavision.com',
    packages=[
        'nso_sdk',
        'nso_plugin'
    ],
    license='LICENSE',
    description='Cloudify plugin for Cisco NSO',
    install_requires=[
        'cloudify-plugins-common>=4.3.1',
        'requests'
    ]
)
