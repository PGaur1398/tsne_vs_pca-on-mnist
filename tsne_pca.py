class tsne_pca:

    def plot_pca(self):
        import seaborn as sn
        import matplotlib.pyplot as plt
        from pca._pca import pca
        sn.FacetGrid(pca(), hue="label", size=6).map(plt.scatter, 'Dim_1', 'Dim_2').add_legend()
        plt.title("PCA")
        plt.show()

    def plot_tsne(self):
        import seaborn as sn
        import matplotlib.pyplot as plt
        from tsne._tsne import tsne
        sn.FacetGrid(tsne(), hue="label", size=6).map(plt.scatter, 'Dim_1', 'Dim_2').add_legend()
        plt.title("T-SNE")
        plt.show()
if __name__ == "__main__":
    ob = tsne_pca()
    ob.plot_pca()
