# Импорт необходимых библиотек

Начнем с импорта необходимых библиотек для этого руководства. Будем использовать `matplotlib` и `numpy`.

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
