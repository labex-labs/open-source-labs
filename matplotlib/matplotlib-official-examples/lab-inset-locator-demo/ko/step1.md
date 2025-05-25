# 두 개의 서브플롯 (subplot) 이 있는 Figure 생성

먼저, 두 개의 서브플롯이 있는 figure 를 생성해야 합니다. `plt.subplots()` 메서드를 사용하여 나란히 두 개의 서브플롯이 있는 figure 를 생성합니다.

```python
import matplotlib.pyplot as plt

fig, (ax, ax2) = plt.subplots(1, 2, figsize=[5.5, 2.8])
```
