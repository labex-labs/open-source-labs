# Define Data

Next, we need to define the data that will be plotted. In this example, we have a set of observations with four variables: name, angular proper motion, angular proper motion error, and distance. We will convert the angular proper motion to linear velocity and plot it against the FWHM (full width at half maximum) of the observations.

```python
obs = [["01_S1", 3.88, 0.14, 1970, 63],
       ["01_S4", 5.6, 0.82, 1622, 150],
       ["02_S1", 2.4, 0.54, 1570, 40],
       ["03_S1", 4.1, 0.62, 2380, 170]]

# Conversion factor from angular proper motion to linear velocity
pm_to_kms = 1./206265.*2300*3.085e18/3.15e7/1.e5
```
