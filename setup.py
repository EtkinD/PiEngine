from setuptools import setup, find_packages

setup(
    name="picengine",
    version="0.0.1",
    description="Pi Game Engine",
    author="Etkin Dogan",
    author_email="etkindogan@gmail.com",
    packages=find_packages(
        exclude=['tests', 'samples', 'docs', 'dist', 'build', 'picengine.egg-info']
    ),
    install_requires=[
        'pygame',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'picengine = picengine.__main__:main'
        ]
    }
)
