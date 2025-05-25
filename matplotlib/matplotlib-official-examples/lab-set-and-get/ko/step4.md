# 속성 가져오기

`getp` 메서드를 사용하여 객체의 속성을 가져올 수 있습니다. 단일 속성의 값을 쿼리하는 데 사용할 수 있습니다.

```python
plt.getp(line, 'linewidth')
```

그러면 line 객체의 linewidth 속성 값이 반환됩니다.

`getp`를 사용하여 객체의 모든 속성/값 쌍을 가져올 수도 있습니다.

```python
plt.getp(line)
```

그러면 모든 속성과 해당 값의 긴 목록이 반환됩니다.
