# 스타일 사이클 설정

`cycler`를 사용하여 히스토그램에 대한 스타일 사이클을 설정합니다. facecolor, label, 그리고 hatch 패턴에 대한 세 개의 스타일 사이클을 생성합니다.

```python
color_cycle = cycler(facecolor=plt.rcParams['axes.prop_cycle'][:4])
label_cycle = cycler(label=[f'set {n}' for n in range(4)])
hatch_cycle = cycler(hatch=['/', '*', '+', '|'])
```
