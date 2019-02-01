class tsne_pca:

    def plot_pca(self,csv_file):
        import seaborn as sn
        import matplotlib.pyplot as plt
        from _pca import pca
        sn.FacetGrid(pca(csv_file), hue="label", size=6).map(plt.scatter, 'Dim_1', 'Dim_2').add_legend()
        plt.title("PCA")
        plt.show()

    def plot_tsne(self,csv_file):
        import seaborn as sn
        import matplotlib.pyplot as plt
        from tsne._tsne import tsne
        sn.FacetGrid(tsne(csv_file), hue="label", size=6).map(plt.scatter, 'Dim_1', 'Dim_2').add_legend()
        plt.title("T-SNE")
        plt.show()
# if __name__ == "__main__":
#     import pandas as pd
#     ob = tsne_pca()
#     ob.plot_pca(pd.read_csv("mnist.csv"))
#     ob.plot_tsne(pd.read_csv("mnist.csv"))
