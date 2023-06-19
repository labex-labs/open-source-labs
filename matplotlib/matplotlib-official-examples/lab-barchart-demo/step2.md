# Define the Data

We define our data using named tuples. We define a `Student` tuple with the student's name, grade, and gender. We also define a `Score` tuple with the score value, unit, and percentile.

```python
from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade', 'gender'])
Score = namedtuple('Score', ['value', 'unit', 'percentile'])
```
