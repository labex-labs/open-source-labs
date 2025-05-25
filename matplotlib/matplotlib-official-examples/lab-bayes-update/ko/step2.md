# 베타 분포 PDF 정의

베타 분포는 확률의 분포를 나타내는 데 자주 사용되는 연속 확률 분포입니다. 베이즈 업데이트에서 우리는 베타 분포를 사전 분포 (prior distribution) 로 사용하여 데이터를 관찰하기 전에 가설의 확률에 대한 우리의 믿음을 나타냅니다. 그런 다음 새로운 데이터를 관찰하면서 베타 분포를 업데이트합니다.

베이즈 업데이트를 시뮬레이션하기 위해, 베타 분포의 확률 밀도 함수 (PDF, Probability Density Function) 를 계산하는 함수를 정의해야 합니다. 베타 분포 PDF 에 사용되는 감마 함수를 계산하기 위해 `math.gamma` 함수를 사용할 수 있습니다.

```python
def beta_pdf(x, a, b):
    return (x**(a-1) * (1-x)**(b-1) * math.gamma(a + b)
            / (math.gamma(a) * math.gamma(b)))
```
