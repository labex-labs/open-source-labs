# Introduction

In this lab, we will use the Spectral Co-clustering algorithm on the twenty newsgroups dataset to bicluster the documents. The dataset has 20 categories of documents and we will exclude the "comp.os.ms-windows.misc" category as it contains posts with no data. The TF-IDF vectorized posts form a word frequency matrix which is then biclustered using Dhillon's Spectral Co-Clustering algorithm. The resulting document-word biclusters indicate subsets of words used more often in those subsets of documents. We will also cluster the documents using MiniBatchKMeans for comparison.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
