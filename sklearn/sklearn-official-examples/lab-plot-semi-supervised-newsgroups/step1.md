# Load the Dataset

We will be using the 20 newsgroups dataset, which contains around 18,000 newsgroup posts on 20 topics. In this step, we will load the dataset and print out some basic information about it.

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups

# Load the dataset with the first five categories
data = fetch_20newsgroups(
    subset="train",
    categories=[
        "alt.atheism",
        "comp.graphics",
        "comp.os.ms-windows.misc",
        "comp.sys.ibm.pc.hardware",
        "comp.sys.mac.hardware",
    ],
)

# Print out information about the dataset
print("%d documents" % len(data.filenames))
print("%d categories" % len(data.target_names))
```
