# 텍스트 아티스트 생성

다음으로, `matplotlib.text`에서 `Text` 클래스를 사용하여 텍스트 아티스트를 생성합니다. x 및 y 좌표, 텍스트 레이블, 수평 및 수직 정렬, 그리고 축 객체를 인수로 지정할 수 있습니다.

```python
t = text.Text(3, 2.5, 'text label', ha='left', va='bottom', axes=ax)
```
