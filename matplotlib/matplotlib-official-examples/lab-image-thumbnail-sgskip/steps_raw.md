# Matplotlib Image Thumbnail Lab

## Introduction

This lab will guide you through the process of generating thumbnails from existing images using Matplotlib library in Python. Thumbnails are smaller versions of images that can be used to display a preview of the larger image. Matplotlib depends on Pillow library for reading images and supports all formats supported by Pillow.

## Steps

### Step 1: Install Required Libraries

First, you need to install the required libraries. Open your terminal and type the following commands to install Matplotlib and Pillow:

```python
pip install matplotlib
pip install pillow
```

### Step 2: Import Libraries

In this step, you will import the libraries you installed in the previous step. You need to import `ArgumentParser` and `Path` from `argparse` and `pathlib` modules respectively. Also, import `sys` and `image` modules from `sys` and `matplotlib.image` modules respectively.

```python
from argparse import ArgumentParser
from pathlib import Path
import sys
import matplotlib.image as image
```

### Step 3: Parse Arguments

In this step, you will parse the arguments passed to your program. You need to create an `ArgumentParser` object and add an argument named `imagedir`. This argument specifies the path to the directory containing the images. You can use the `type` parameter to specify the data type of the argument. In this case, the argument should be of type `Path`.

```python
parser = ArgumentParser(description="Build thumbnails of all images in a directory.")
parser.add_argument("imagedir", type=Path)
args = parser.parse_args()
```

### Step 4: Verify Directory

In this step, you will check if the specified directory exists. If the directory does not exist, you will exit the program and print an error message.

```python
if not args.imagedir.is_dir():
    sys.exit(f"Could not find input directory {args.imagedir}")
```

### Step 5: Create Output Directory

In this step, you will create a directory named `thumbs` where the thumbnails will be saved. If the directory already exists, it will not be created again.

```python
outdir = Path("thumbs")
outdir.mkdir(parents=True, exist_ok=True)
```

### Step 6: Generate Thumbnails

In this step, you will generate thumbnails for all the images in the specified directory. You will use a for loop to iterate over all the images with the `.png` extension in the specified directory. For each image, you will generate a thumbnail and save it in the `thumbs` directory.

```python
for path in args.imagedir.glob("*.png"):
    outpath = outdir / path.name
    fig = image.thumbnail(path, outpath, scale=0.15)
    print(f"saved thumbnail of {path} to {outpath}")
```

## Summary

In this lab, you have learned how to generate thumbnails from existing images using Matplotlib in Python. You have learned how to import libraries, parse arguments, verify directories, create output directories and generate thumbnails. By following the steps in this lab, you can easily generate thumbnails for all the images in a directory.
