# Importieren der erforderlichen Bibliotheken

Wir beginnen mit dem Importieren der erforderlichen Bibliotheken für dieses Tutorial. Wir werden `matplotlib` und `numpy` verwenden.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import (
    FR, MO, MONTHLY, SA, SU, TH, TU, WE, AutoDateFormatter, AutoDateLocator,
    ConciseDateFormatter, DateFormatter, DayLocator, HourLocator,
    MicrosecondLocator, MinuteLocator, MonthLocator, RRuleLocator, SecondLocator,
    WeekdayLocator, YearLocator, rrulewrapper)
import matplotlib.ticker as ticker
```
