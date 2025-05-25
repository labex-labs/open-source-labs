# 썸네일 생성 (Generate Thumbnails)

이 단계에서는 지정된 디렉토리의 모든 이미지에 대한 썸네일을 생성합니다. for 루프를 사용하여 지정된 디렉토리에서 `.png` 확장자를 가진 모든 이미지를 반복합니다. 각 이미지에 대해 썸네일을 생성하여 `thumbs` 디렉토리에 저장합니다.

```python
for path in args.imagedir.glob("*.png"):
    outpath = outdir / path.name
    fig = image.thumbnail(path, outpath, scale=0.15)
    print(f"saved thumbnail of {path} to {outpath}")
```
