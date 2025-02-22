from setuptools import setup, find_packages

setup(
    name='common_streaming',
    version='0.1.0',
    description='Shared streaming logic for microservices',
    packages=find_packages(),
    install_requires=[

        'redis>=3.5.3',
        'kafka-python>=2.0.4'

    ],
)
