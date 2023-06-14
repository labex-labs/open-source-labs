# Interpret the results

We can see from the plot that `k-means++` does a good job of both low time to initialize and low number of GaussianMixture iterations to converge. When initialized with `random_from_data` or `random`, the model takes more iterations to converge. All three alternative methods take less time to initialize when compared to `kmeans`.
