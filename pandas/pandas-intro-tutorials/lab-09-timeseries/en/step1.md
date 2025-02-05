# Import the necessary libraries and load the data

First, we need to import the required Python libraries and load the air quality data. The data will be read into a pandas DataFrame, which is a 2-dimensional labeled data structure.

```python
# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# load the air quality data
air_quality = pd.read_csv("data/air_quality_no2_long.csv")

# rename the "date.utc" column to "datetime"
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
```
