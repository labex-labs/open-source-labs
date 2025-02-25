# Broadcasting mit einem Skalarwert

Das Broadcasting ermöglicht auch elementweise Operationen zwischen einem Array und einem Skalarwert. Der Skalarwert wird automatisch "ausgedehnt", um der Form des Arrays zu entsprechen. Beispielsweise:

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = 2.0
result = a * b
```

In diesem Fall ist `b` ein Skalarwert, wird jedoch ausgedehnt, um ein Array mit der gleichen Form wie `a` zu werden. Die Multiplikation erfolgt dann elementweise, was zu `[2.0, 4.0, 6.0]` führt.
