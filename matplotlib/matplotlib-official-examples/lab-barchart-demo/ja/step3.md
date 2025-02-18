# ヘルパー関数の定義

2つのヘルパー関数を定義します。最初の関数 `to_ordinal` は、整数を序数の文字列に変換します（例: 2 -> '2nd'）。2番目の関数 `format_score` は、右側のy軸のスコアラベルを作成します。テスト名の後に測定単位（あれば）が続き、2行に分割されます。

```python
def to_ordinal(num):
    suffixes = {str(i): v
                for i, v in enumerate(['th', 'st', 'nd', 'rd', 'th',
                                       'th', 'th', 'th', 'th', 'th'])}
    v = str(num)
    if v in {'11', '12', '13'}:
        return v + 'th'
    return v + suffixes[v[-1]]

def format_score(score):
    return f'{score.value}\n{score.unit}' if score.unit else str(score.value)
```
