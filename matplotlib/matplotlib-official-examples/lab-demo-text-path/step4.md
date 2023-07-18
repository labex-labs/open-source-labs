# Create an Offset Box

Create an offset box using AuxTransformBox to add the PathClippedImagePatch object. Use the following code to create the offset box:

```python
offsetbox = AuxTransformBox(IdentityTransform())
offsetbox.add_artist(p)
```
