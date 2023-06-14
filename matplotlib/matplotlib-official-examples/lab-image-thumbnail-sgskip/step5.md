# Create Output Directory

In this step, you will create a directory named `thumbs` where the thumbnails will be saved. If the directory already exists, it will not be created again.

```python
outdir = Path("thumbs")
outdir.mkdir(parents=True, exist_ok=True)
```
