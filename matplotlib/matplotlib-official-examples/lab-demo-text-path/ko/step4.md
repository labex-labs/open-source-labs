# Offset Box 생성

PathClippedImagePatch 객체를 추가하기 위해 AuxTransformBox 를 사용하여 offset box 를 생성합니다. 다음 코드를 사용하여 offset box 를 생성합니다.

```python
offsetbox = AuxTransformBox(IdentityTransform())
offsetbox.add_artist(p)
```
