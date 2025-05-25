# 기생 축 생성

`host.get_aux_axes()` 메서드를 사용하여 두 개의 기생 축 (parasite axes) 을 생성합니다. 기생 축이 호스트 축과 동일한 x 축 스케일을 공유하도록 `viewlim_mode=None`을 설정합니다. 또한 x 축 스케일이 공유되도록 `sharex=host`를 설정합니다.

```python
par1 = host.get_aux_axes(viewlim_mode=None, sharex=host)
par2 = host.get_aux_axes(viewlim_mode=None, sharex=host)
```
