# 컬러 바 위치 조정

`plt.axes`를 사용하여 컬러 바의 위치를 조정할 수도 있습니다. 이 함수는 축의 위치와 크기를 지정하기 위해 `[left, bottom, width, height]` 값의 목록을 인수로 사용합니다. 다음 코드를 실행하세요:

```python
cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)
```
