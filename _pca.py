def pca(ds):

    import numpy as np
    import pandas as pd
    import seaborn as sn
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import StandardScaler
    from scipy.linalg import eigh
    leb = ds["label"]
    d = ds.drop("label",axis=1)
    labels = leb.head(16000)
    data = d.head(16000)
    standardized_data = StandardScaler().fit_transform(data)
    sample_data = standardized_data
    cov_matrix = np.matmul(sample_data.T,sample_data)
    std_cov_matrix = np.true_divide(cov_matrix,sample_data.shape[0])
    values, vectors = eigh(std_cov_matrix, eigvals=(782,783))
    vectors = vectors.T
    new_coordinates = np.vstack((np.matmul(vectors, sample_data.T),labels)).T
    return pd.DataFrame(data=new_coordinates, columns=("Dim_1","Dim_2","label"))
import pandas as pd

pca(pd.read_csv("mnist.csv"))
