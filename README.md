# tsne_vs_pca-on-mnist
PCA and T-SNE are both dimensionality reduction algorithm
Though T-SNE  gets slower on large data sets but is pretty fast on gpu.checkout the link
[Optimized Cuda Version](https://github.com/user/CannyLab/tsne-cuda)



Requirements
------------


* [numpy]
* [pandas]
* [seaborn]
* [scipy]
* [sklearn]
* [Anaconda](http://continuum.io/downloads) is recommended.


Installations
-------------
Pip can install package from a git repo

```
pip install
git+https://github.com/PGaur1398/tsne_vs_pca-on-mnist.git
```
Usage
-----
for PCA:
```
from tsne_pca import tsne_pca.plot_pca
```
for t-sne:
```
from tsne_pca import tsne_pca.plot_tsne
```
pass read_csv list to the plot_pca and plot_tsne method

