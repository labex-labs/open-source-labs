# Introduction

This lab explores the impact of uniformly-distributed random labeling on the behavior of some clustering evaluation metrics. Clustering algorithms are fundamentally unsupervised learning methods and evaluation metrics that leverage "supervised" ground truth information to quantify the quality of the resulting clusters. However, non-adjusted clustering evaluation metrics can be misleading as they output large values for fine-grained labelings, which can be totally random. Therefore, only adjusted measures can be safely used as a consensus index to evaluate the average stability of clustering algorithms for a given value of k on various overlapping sub-samples of the dataset.

> You can open the `plot-adjusted-for-chance-measures.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.
