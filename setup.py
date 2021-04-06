from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tidytuesday",
    version="0.0.1",
    description="Download #TidyTuesday data",
    py_modules=["tidytuesday"],
    package_dir={"": "src"},
    url="https://github.com/ilnaes/tidytuesdaypy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author="Sean Li",
    author_email="seanli646@gmail.com",
    install_requires=[
        "pandas >= 1.0",
        "PyGithub >= 1.54",
    ],
)
