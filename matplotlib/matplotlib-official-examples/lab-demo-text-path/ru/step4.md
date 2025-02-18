# Создание смещенного контейнера (offset box)

Создайте смещенный контейнер с использованием `AuxTransformBox` для добавления объекта `PathClippedImagePatch`. Используйте следующий код для создания смещенного контейнера:

```python
offsetbox = AuxTransformBox(IdentityTransform())
offsetbox.add_artist(p)
```
