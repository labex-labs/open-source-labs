# Define Number Normalizer

We will define a function `number_normalizer()` to map all numeric tokens to a placeholder. This is used for dimensionality reduction.

```python
def number_normalizer(tokens):
    """Map all numeric tokens to a placeholder.

    For many applications, tokens that begin with a number are not directly
    useful, but the fact that such a token exists can be relevant.  By applying
    this form of dimensionality reduction, some methods may perform better.
    """
    return ("#NUMBER" if token[0].isdigit() else token for token in tokens)
```


