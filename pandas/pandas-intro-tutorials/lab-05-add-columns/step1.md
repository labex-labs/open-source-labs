# Import Pandas and Load Data

First, we'll import the pandas library and load the air quality data from a CSV file.

```python
# Import pandas library
import pandas as pd

# Load air quality data
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
```
