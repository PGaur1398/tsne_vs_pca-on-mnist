import setuptools

setuptools.setup (
name = "pca_tsne",
version = "0.1",
description  = "Comparision between two dimensionality reduction algorithm",
author = "Pankaj Gaur",
url = "https://github.com/PGaur1398/tsne_vs_pca-on-mnist.git",
author_email = "pankajs98@outlook.com",
py_modules = ['tsne_pca','_pca','_tsne'],
include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    dependency_links=[
    "git+https://github.com/PGaur1398/tsne_vs_pca-on-mnist.git"

    ]
)
