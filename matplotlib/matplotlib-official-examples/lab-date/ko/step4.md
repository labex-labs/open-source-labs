# 데이터 플롯

`plot` 함수를 사용하여 세 개의 모든 서브플롯에 데이터를 플롯합니다.

```python
for ax in axs:
    ax.plot('date', 'adj_close', data=data)
    ax.grid(True)
    ax.set_ylabel(r'Price [\$]')
```
