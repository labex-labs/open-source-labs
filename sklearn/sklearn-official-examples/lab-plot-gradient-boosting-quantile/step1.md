# Generate Synthetic Data

We will generate synthetic data for a regression problem by applying the function to uniformly sampled random inputs. To make the problem interesting, we generate observations of the target y as the sum of a deterministic term computed by the function f and a random noise term that follows a centered log-normal distribution. The lognormal distribution is non-symmetric and long tailed: observing large outliers is likely but it is impossible to observe small outliers.


