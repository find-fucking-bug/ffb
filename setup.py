import sys
from setuptools import setup

if sys.version_info[0] < 3:
    with open("README.md") as f:
        README = f.read()
else:
    with open("README.md", encoding="utf-8") as f:
        README = f.read()

setup(
    name="ffb",
    version="0.0.6",
    author="Ali Yaman, Umut Deniz",
    author_email="aliymn.db@gmail.com, umutdeniz609@gmail.com",
    description="Find Fucking Bug",
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=README,
    keywords="Find Fucking Bug",
    packages=["ffb", "ffb.core", "ffb.helper"],
    url="https://github.com/find-fucking-bug",
    download_url="https://github.com/find-fucking-bug",
    install_requires=[
        "ollama==0.3.2",
        "tqdm==4.66.5",
        "rich==13.8.0",
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    entry_points={"console_scripts": ["ffb=ffb.core.run:main"]},
)
