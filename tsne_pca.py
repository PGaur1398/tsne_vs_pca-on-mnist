class tsne_pca:

    def plot_pca(self):
        import seaborn as sn
        import matplotlib.pyplot as plt
        from _pca import pca
        sn.FacetGrid(pca(), hue="label", size=6).map(plt.scatter, 'Dim_1', 'Dim_2').add_legend()
        plt.show()
    def plot_tsne(self):
        import seaborn as sn
        import matplotlib.pyplot as plt
        from _tsne import tsne
        sn.FacetGrid(tsne(), hue="label", size=6).map(plt.scatter, 'Dim_1', 'Dim_2').add_legend()
        plt.show()
