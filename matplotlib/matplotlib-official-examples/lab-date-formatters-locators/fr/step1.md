# Importation des bibliothèques requises

Nous commençons par importer les bibliothèques nécessaires pour ce tutoriel. Nous utiliserons `matplotlib` et `numpy`.

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
