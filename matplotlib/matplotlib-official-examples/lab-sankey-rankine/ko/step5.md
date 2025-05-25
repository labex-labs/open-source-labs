# 레이블 및 서식 추가

각 패치의 `text` 속성을 사용하여 Sankey 다이어그램의 패치에 레이블을 추가합니다. 또한 텍스트를 굵게 표시하고 글꼴 크기를 늘립니다.

```python
diagrams = sankey.finish()
for diagram in diagrams:
    diagram.text.set_fontweight('bold')
    diagram.text.set_fontsize('10')
    for text in diagram.texts:
        text.set_fontsize('10')
```
