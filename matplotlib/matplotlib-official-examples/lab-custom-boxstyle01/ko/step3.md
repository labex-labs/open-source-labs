# Matplotlib 에 사용자 정의 박스 스타일 등록하기

클래스로 사용자 정의 박스 스타일을 구현한 후에는 Matplotlib 에 등록할 수 있습니다. 이렇게 하면 문자열로 박스 스타일을 지정할 수 있습니다. `bbox=dict(boxstyle="registered_name,param=value,...", ...)`.

```python
BoxStyle._style_list["angled"] = MyStyle  # 사용자 정의 스타일 등록.
```
