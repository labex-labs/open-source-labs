# Comments on importing

Variations on import do _not_ change the way that modules work.

```python
import math
# vs
import math as m
# vs
from math import cos, sin
...
```

Specifically, `import` always executes the _entire_ file and modules
are still isolated environments.

The `import module as` statement is only changing the name locally.
The `from math import cos, sin` statement still loads the entire
math module behind the scenes. It's merely copying the `cos` and `sin`
names from the module into the local space after it's done.
