# Summary

In this tutorial, we learned how to use Matplotlib to antialias an image to reduce Moiré patterns caused by subsampling high-frequency data. We generated a 450x450 pixel image with varying frequency content, and subsampled the image from 450 data pixels to either 125 pixels or 250 pixels using 'nearest' and 'antialiased' interpolation. We also demonstrated how upsampling an image using 'nearest' interpolation can still lead to Moiré patterns, but using better antialiasing algorithms can reduce these effects.
