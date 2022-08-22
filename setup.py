from setuptools import setup, find_packages

setup(
    name="speedfft",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "wheel",
        "numpy",
        "matplotlib",
        "scipy"
    ]
)
