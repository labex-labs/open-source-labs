# Anchored Offset Box 생성

offset box 를 추가하고 위치를 설정하기 위해 AnnotationBbox 를 사용하여 anchored offset box 를 생성합니다. 다음 코드를 사용하여 anchored offset box 를 생성합니다.

```python
ao = AnchoredOffsetbox(loc='upper left', child=offsetbox, frameon=True,
                           borderpad=0.2)
ax1.add_artist(ao)
```
