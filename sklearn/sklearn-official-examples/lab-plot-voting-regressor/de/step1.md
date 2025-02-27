# Bibliotheken importieren

Lassen Sie uns die erforderlichen Bibliotheken importieren, um die Diabetes-Vorhersage mit dem Voting Regressor durchzuführen.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor
```
