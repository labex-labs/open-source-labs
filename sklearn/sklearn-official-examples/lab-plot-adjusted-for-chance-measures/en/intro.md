# Introduction

This lab explores the impact of uniformly-distributed random labeling on the behavior of some clustering evaluation metrics. Clustering algorithms are fundamentally unsupervised learning methods and evaluation metrics that leverage "supervised" ground truth information to quantify the quality of the resulting clusters. However, non-adjusted clustering evaluation metrics can be misleading as they output large values for fine-grained labelings, which can be totally random. Therefore, only adjusted measures can be safely used as a consensus index to evaluate the average stability of clustering algorithms for a given value of k on various overlapping sub-samples of the dataset.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a <span class="text-red-600 dark:text-red-400">advanced</span> level lab with a <span class="text-red-600 dark:text-red-400">25%</span> completion rate.
</div>
