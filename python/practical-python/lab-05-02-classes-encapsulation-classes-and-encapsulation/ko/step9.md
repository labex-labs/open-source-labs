# 데코레이터 구문 (Decorator Syntax)

`@` 구문은 "데코레이션 (decoration)"으로 알려져 있습니다. 이는 바로 뒤에 오는 함수 정의에 적용되는 수정자를 지정합니다.

```python
...
@property
def cost(self):
    return self.shares * self.price
```

자세한 내용은 섹션 7 에서 제공됩니다.
