# Parse Arguments

In this step, you will parse the arguments passed to your program. You need to create an `ArgumentParser` object and add an argument named `imagedir`. This argument specifies the path to the directory containing the images. You can use the `type` parameter to specify the data type of the argument. In this case, the argument should be of type `Path`.

```python
parser = ArgumentParser(description="Build thumbnails of all images in a directory.")
parser.add_argument("imagedir", type=Path)
args = parser.parse_args()
```
