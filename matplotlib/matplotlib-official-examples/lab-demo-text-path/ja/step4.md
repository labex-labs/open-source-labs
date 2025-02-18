# オフセットボックスを作成する

AuxTransformBox を使用してオフセットボックスを作成し、PathClippedImagePatch オブジェクトを追加します。以下のコードを使用してオフセットボックスを作成します。

```python
offsetbox = AuxTransformBox(IdentityTransform())
offsetbox.add_artist(p)
```
