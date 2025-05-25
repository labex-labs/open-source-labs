# 보조 눈금 레이블 정렬

마지막으로, 보조 눈금 레이블을 주요 눈금 사이의 가운데에 정렬해야 합니다. `get_xticklabels()` 함수를 사용하고 `minor` 매개변수를 `True`로 설정하여 보조 눈금 레이블을 가져올 수 있습니다. 그런 다음 레이블을 반복 처리하고 수평 정렬을 `'center'`로 설정할 수 있습니다.

```python
# Align the minor tick label
for label in ax.get_xticklabels(minor=True):
    label.set_horizontalalignment('center')
imid = len(r) // 2
ax.set_xlabel(str(r.date[imid].item().year))
```
