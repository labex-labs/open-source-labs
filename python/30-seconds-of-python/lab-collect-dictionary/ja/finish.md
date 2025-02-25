# まとめ

このチャレンジでは、非一意のハッシュ可能な値を持つ辞書を反転させる方法を学びました。各キーの既定値として `list` を持つ `collections.defaultdict` を使用し、その後 `dict.append()` を使って辞書の値をキーにマッピングしました。最後に、`dict()` を使って `collections.defaultdict` を通常の辞書に変換しました。
