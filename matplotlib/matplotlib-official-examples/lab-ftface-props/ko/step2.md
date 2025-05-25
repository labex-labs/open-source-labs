# 글꼴 로드

이 단계에서는 작업할 글꼴을 로드합니다. Matplotlib 과 함께 제공되는 글꼴을 사용합니다.

```python
font = ft.FT2Font(
    os.path.join(matplotlib.get_data_path(),
                 'fonts/ttf/DejaVuSans-Oblique.ttf'))
```
