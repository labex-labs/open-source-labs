# 创建一个偏移框

使用 AuxTransformBox 创建一个偏移框，以添加 PathClippedImagePatch 对象。使用以下代码创建偏移框：

```python
offsetbox = AuxTransformBox(IdentityTransform())
offsetbox.add_artist(p)
```
