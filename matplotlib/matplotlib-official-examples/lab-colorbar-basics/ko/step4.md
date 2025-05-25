# 음수 데이터 플롯 및 컬러바 생성

음수 데이터의 플롯을 생성하고, `colorbar` 함수를 사용하여 플롯에 컬러바를 추가합니다. 이번에는 컬러바의 위치와 앵커 (anchor) 및 축소 (shrink) 매개변수를 지정합니다.

```python
# repeat everything above for the negative data
# you can specify location, anchor and shrink the colorbar
neg = plt.imshow(Zneg, cmap='Reds_r', interpolation='none')
plt.colorbar(neg, location='right', anchor=(0, 0.3), shrink=0.7)
```
