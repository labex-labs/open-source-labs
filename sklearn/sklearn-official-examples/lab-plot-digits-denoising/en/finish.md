# Summary

In this lab, we learned how to use Kernel PCA to denoise images. We used USPS digits dataset to demonstrate the process. We learned a PCA basis on noise-free images and used it to reconstruct and denoise the noisy images. We compared the results of both linear PCA and kernel PCA, and found that kernel PCA is more efficient in removing background noise and providing smoother images. However, we need to be careful in selecting the appropriate values for `n_components`, `gamma`, and `alpha`.
