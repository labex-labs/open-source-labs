# 플롯 생성

다음으로, 호스트 축 (host axis) 과 기생 축 (parasite axis) 을 정의하여 플롯을 생성합니다. 호스트 축은 기본 데이터에 사용되고, 기생 축은 보조 데이터에 사용됩니다.

```python
host = host_subplot(111)
par = host.twinx()
```
