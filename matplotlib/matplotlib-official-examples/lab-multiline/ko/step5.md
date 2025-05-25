# 플롯에 텍스트 추가

`text` 함수를 사용하여 플롯에 텍스트를 추가할 수 있습니다. 텍스트의 위치, 회전, 수평 및 수직 정렬, 그리고 다중 정렬 (multialignment) 을 지정할 수 있습니다.

```python
ax0.text(2, 7, 'this is\nyet another test',
         rotation=45,
         horizontalalignment='center',
         verticalalignment='top',
         multialignment='center')
```
