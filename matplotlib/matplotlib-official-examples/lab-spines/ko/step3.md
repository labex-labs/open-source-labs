# 서브플롯 생성

다양한 스파인 (spine) 사용자 정의를 시연하기 위해 세 개의 서브플롯을 생성합니다. 레이블이 축과 겹치지 않도록 제한된 레이아웃 (constrained layout) 을 사용합니다.

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, layout='constrained')
```
