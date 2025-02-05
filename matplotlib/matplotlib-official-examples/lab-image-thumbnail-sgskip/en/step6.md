# Generate Thumbnails

In this step, you will generate thumbnails for all the images in the specified directory. You will use a for loop to iterate over all the images with the `.png` extension in the specified directory. For each image, you will generate a thumbnail and save it in the `thumbs` directory.

```python
for path in args.imagedir.glob("*.png"):
    outpath = outdir / path.name
    fig = image.thumbnail(path, outpath, scale=0.15)
    print(f"saved thumbnail of {path} to {outpath}")
```
