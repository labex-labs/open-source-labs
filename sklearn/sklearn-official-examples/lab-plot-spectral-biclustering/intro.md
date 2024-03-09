# Introduction

In this lab, we will use the Spectral Biclustering algorithm to cluster data by simultaneously considering both the rows (samples) and columns (features) of a matrix. It aims to identify patterns not only between samples but also within subsets of samples, allowing for the detection of localized structure within the data. This makes spectral biclustering particularly well-suited for datasets where the order or arrangement of features is fixed, such as in images, time series, or genomes. We will use the scikit-learn library to generate checkerboard dataset and bicluster it using the Spectral Biclustering algorithm.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
