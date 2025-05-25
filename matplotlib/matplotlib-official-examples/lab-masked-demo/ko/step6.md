# 데이터 플롯

네 개의 모든 데이터 세트를 서로 구별하기 위해 다른 마커와 색상을 사용하여 플롯합니다.

```python
plt.plot(x*0.1, y, 'o-', color='lightgrey', label='No mask')
plt.plot(x2*0.4, y2, 'o-', label='Points removed')
plt.plot(x*0.7, y3, 'o-', label='Masked values')
plt.plot(x*1.0, y4, 'o-', label='NaN values')
plt.legend()
plt.title('Masked and NaN data')
plt.show()
```
