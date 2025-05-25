# 바이트 순서 문제 처리

다른 바이트 순서를 가진 머신에서 생성된 데이터를 다룰 때 바이트 순서 문제에 직면할 수 있습니다. Pandas 에 전달하기 전에 데이터를 네이티브 시스템 바이트 순서로 변환하십시오.

```python
x = np.array(list(range(10)), ">i4")  # big endian
newx = x.byteswap().newbyteorder()  # force native byteorder
s = pd.Series(newx)
```
