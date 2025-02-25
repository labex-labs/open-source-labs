# トグルセレクタ関数を定義する

ユーザーが「t」キーを押すたびに、トグルセレクタ関数が呼び出されます。この関数は、RectangleSelectorとEllipseSelectorウィジェットのアクティブ状態を切り替えます。

```python
def toggle_selector(event):
    print('Key pressed.')
    if event.key == 't':
        for selector in selectors:
            name = type(selector).__name__
            if selector.active:
                print(f'{name} deactivated.')
                selector.set_active(False)
            else:
                print(f'{name} activated.')
                selector.set_active(True)
```
