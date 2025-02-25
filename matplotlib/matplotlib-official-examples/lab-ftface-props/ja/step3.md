# フォントのプロパティを表示する

このステップでは、フォントのプロパティを表示します。

```python
print('Num faces:  ', font.num_faces)        # ファイル内のフェイス数
print('Num glyphs: ', font.num_glyphs)       # フェイス内のグリフ数
print('Family name:', font.family_name)      # フェイスのファミリ名
print('Style name: ', font.style_name)       # フェイスのスタイル名
print('PS name:    ', font.postscript_name)  # ポストスクリプト名
print('Num fixed:  ', font.num_fixed_sizes)  # 埋め込まれたビットマップの数
```
