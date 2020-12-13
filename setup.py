import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="edges-nodes-py", # Replace with your own username
    version="1.0.0",
    author="Luca Comba",
    author_email="luca.comba98@gmail.com",
    description="Python library for converting datasets to edges and nodes csv files for network analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lukfd/enpy",
    packages=setuptools.find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)