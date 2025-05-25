# 데이터 관리자 윈도우 생성

이 단계에서는 `Gtk.Window` 클래스를 상속하는 `DataManager` 클래스를 생성합니다. 이 클래스는 우리가 플롯 (plot) 하려는 데이터를 관리하는 역할을 합니다.

```python
class DataManager(Gtk.Window):
    num_rows, num_cols = 20, 10
    data = random((num_rows, num_cols))
```
