# Broadcasting mit Arrays der gleichen Form

Im einfachsten Fall müssen zwei Arrays genau die gleiche Form haben, um elementweise Operationen durchzuführen. Beispielsweise:

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
result = a * b
```

In diesem Fall haben `a` und `b` die gleiche Form, sodass die Multiplikation elementweise durchgeführt wird und das Ergebnis `[2.0, 4.0, 6.0]` ist.
