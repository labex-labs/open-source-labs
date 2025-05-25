# 필요한 라이브러리 가져오기

이 튜토리얼에 필요한 라이브러리를 가져오는 것으로 시작합니다. `matplotlib`와 `numpy`를 사용할 것입니다.

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
