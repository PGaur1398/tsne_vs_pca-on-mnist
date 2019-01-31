from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup (
name = "tsne_pca",
version = "0.01",
description  = "Comparision between two dimensionality reduction algorithm",
author = "Pankaj Gaur",
author_email = "pankajs98@outlook.com",
py_modules = ["tsne_pca"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
