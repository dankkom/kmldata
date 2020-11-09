"""Setup for table2kml package."""


import codecs
import os.path
import setuptools


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="kmldata",
    version=get_version("kmldata/__init__.py"),
    author="Daniel Komesu",
    author_email="contact@dkko.me",
    description="Transform tabular data into KML and vice-versa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU GPLv3",
    keywords="kml geospatial pandas GIS",
    url="https://github.com/dankkom/kmldata",
    packages=setuptools.find_packages(include=["kmldata"]),
    install_requires=["lxml", "pykml", "pandas", "numpy"],
    python_requires=">=3.8, <4",
    package_data={
        "kmldata": ["icons.json"],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering :: GIS",
    ],
)
