# Create Fake Data

Create fake data to plot by using a formula to calculate data based on the values of X, Y, and Z. We will add one to the result to ensure that the minimum value is greater than zero.

```python
# Create fake data
data = (((X+100)**2 + (Y-20)**2 + 2*Z)/1000+1)
```
