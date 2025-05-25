# 서드 파티 모듈

서드 파티 모듈은 일반적으로 전용 `site-packages` 디렉토리에 위치합니다. 위와 동일한 단계를 수행하면 확인할 수 있습니다:

```python
>>> import numpy
>>> numpy
<module 'numpy' from '/usr/local/lib/python3.6/site-packages/numpy/__init__.py'>
>>>
```

다시 말하지만, `import`와 관련된 문제가 예상대로 작동하지 않는 이유를 파악하려는 경우 모듈을 살펴보는 것은 좋은 디버깅 팁입니다.
