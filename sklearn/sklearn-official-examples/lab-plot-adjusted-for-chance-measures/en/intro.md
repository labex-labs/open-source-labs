# Introduction

This lab explores the impact of uniformly-distributed random labeling on the behavior of some clustering evaluation metrics. Clustering algorithms are fundamentally unsupervised learning methods and evaluation metrics that leverage "supervised" ground truth information to quantify the quality of the resulting clusters. However, non-adjusted clustering evaluation metrics can be misleading as they output large values for fine-grained labelings, which can be totally random. Therefore, only adjusted measures can be safely used as a consensus index to evaluate the average stability of clustering algorithms for a given value of k on various overlapping sub-samples of the dataset.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
