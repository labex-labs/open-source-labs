# Import Libraries and Load Data

First, let's import the required libraries and load the datasets.

```python
import pandas as pd

# Load Titanic dataset
titanic = pd.read_csv("data/titanic.csv")

# Load Air Quality dataset
air_quality = pd.read_csv("data/air_quality_long.csv", index_col="date.utc", parse_dates=True)
```
