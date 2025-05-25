# 호스트 및 기생 축 생성

`host_subplot()` 및 `twinx()` 함수를 사용하여 호스트 축과 두 개의 기생 축을 생성합니다. `host_subplot()` 함수는 호스트 축을 생성하고, `twinx()` 함수는 호스트 축과 동일한 x 축을 공유하는 기생 축을 생성합니다.

```python
host = host_subplot(111, axes_class=axisartist.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()
```
