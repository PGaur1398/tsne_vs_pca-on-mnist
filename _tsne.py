def tsne():

    import numpy as np
    import pandas as pd
    from sklearn.preprocessing import StandardScaler

    from sklearn.manifold import TSNE

    ds = pd.read_csv("mnist.csv")
    leb = ds["label"]
    d = ds.drop("label",axis=1)
    labels = leb.head(16000)
    data = d.head(16000)
    standardized_data = StandardScaler().fit_transform(data)
    data_15000 = standardized_data[0:15000,:]
    labels_15000 = labels[0:15000]
    model = TSNE(n_components=2, random_state=0,perplexity = 40,n_iter = 1000)
    tsne_data = model.fit_transform(data_1000)
    tsne_data = np.vstack((tsne_data.T, labels_1000)).T
    return pd.DataFrame(data=tsne_data, columns=("Dim_1", "Dim_2", "label"))
