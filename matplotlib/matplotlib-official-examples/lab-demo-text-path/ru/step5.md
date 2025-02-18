# Создание закрепленного смещенного контейнера (anchored offset box)

Создайте закрепленный смещенный контейнер с использованием `AnnotationBbox` для добавления смещенного контейнера и установки его позиции. Используйте следующий код для создания закрепленного смещенного контейнера:

```python
ao = AnchoredOffsetbox(loc='upper left', child=offsetbox, frameon=True,
                           borderpad=0.2)
ax1.add_artist(ao)
```
