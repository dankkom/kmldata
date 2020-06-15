"""Setup for table2kml package."""


import setuptools

import table2kml


with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="table2kml",
    author=table2kml.__author__,
    author_email=table2kml.__author_email__,
    description="Transform data tables into KML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU LGPLv3",
    license_file="LICENSE",
    keywords="kml geospatial pandas GIS",
    url="https://github.com/dkkomesu/table2kml",
    packages=setuptools.find_packages(include=["table2kml"]),
    install_requires=["lxml", "pykml"],
    python_requires=">=3.8, <4",
    package_data={
        "table2kml": ["icons.json"],
        "": ["*.png"],
    },
    include_package_data=True,
    entry_points={
        "console_scripts": ["table2kml=table2kml.cli:main"]
    },
    project_urls={
        "Source Code": "https://github.com/dkkomesu/table2kml",
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
