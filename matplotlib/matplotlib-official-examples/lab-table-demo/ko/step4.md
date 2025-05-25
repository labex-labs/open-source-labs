# 색상 구성표 생성

`plt.cm.BuPu` 함수를 사용하여 테이블에 대한 색상 구성표를 생성합니다. 행에 대해 파스텔톤의 파란색과 보라색을 사용합니다.

```python
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
```
