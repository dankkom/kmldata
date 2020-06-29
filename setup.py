"""Setup for table2kml package."""


import setuptools

import kmldata


with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="kmldata",
    author=kmldata.__author__,
    author_email=kmldata.__author_email__,
    description="Transform tabular data into KML and vice-versa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU LGPLv3",
    license_file="LICENSE",
    keywords="kml geospatial pandas GIS",
    url="https://github.com/dkkomesu/kmldata",
    packages=setuptools.find_packages(include=["kmldata"]),
    install_requires=["lxml", "pykml"],
    python_requires=">=3.8, <4",
    package_data={
        "kmldata": ["icons.json"],
    },
    include_package_data=True,
    project_urls={
        "Source Code": "https://github.com/dkkomesu/kmldata",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    test_suite="TestTable2KML",
)
