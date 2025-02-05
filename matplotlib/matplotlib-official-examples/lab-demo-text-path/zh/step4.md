# 创建一个偏移框

使用AuxTransformBox创建一个偏移框，以添加PathClippedImagePatch对象。使用以下代码创建偏移框：

```python
offsetbox = AuxTransformBox(IdentityTransform())
offsetbox.add_artist(p)
```
