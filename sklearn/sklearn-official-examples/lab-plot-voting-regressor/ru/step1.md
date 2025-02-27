# Импортируем библиотеки

Импортируем необходимые библиотеки для выполнения прогноза диабета с использованием Регурессора голосования.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor
```
