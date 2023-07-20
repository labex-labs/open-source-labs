# Define Beta Distribution PDF

The beta distribution is a continuous probability distribution that is often used to represent the distribution of probabilities. In Bayesian updating, we use the beta distribution as a prior distribution to represent our beliefs about the probability of a hypothesis before observing any data. We then update the beta distribution as we observe new data.

To simulate Bayesian updating, we need to define a function that calculates the probability density function (PDF) of the beta distribution. We can use the `math.gamma` function to compute the gamma function, which is used in the beta distribution PDF.

```python
def beta_pdf(x, a, b):
    return (x**(a-1) * (1-x)**(b-1) * math.gamma(a + b)
            / (math.gamma(a) * math.gamma(b)))
```
