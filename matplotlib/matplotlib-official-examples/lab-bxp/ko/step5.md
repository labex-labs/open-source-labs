# 다양한 요소의 표시 전환

`bxp()` 함수의 다양한 매개변수를 사용하여 상자 그림의 다양한 요소 표시를 전환할 수 있습니다. 이 예제에서는 평균, 상자, 캡, 노치 (notches), 이상치 (fliers) 를 표시하거나 숨기는 방법을 보여줍니다.

```python
# Toggle the display of different elements
plt.bxp(stats, showmeans=True, showbox=False, showcaps=False, shownotches=True, showfliers=False)
plt.show()
```
