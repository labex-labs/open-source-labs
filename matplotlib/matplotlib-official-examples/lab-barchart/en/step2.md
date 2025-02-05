# Prepare Data

Next, we will prepare the data for our chart. We have three species of penguins and three attributes, so we will create a dictionary with the means for each attribute by species.

```python
species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}
```
