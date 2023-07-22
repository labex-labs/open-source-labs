# Introduction

This tutorial will guide you on how to draw a curve with an error band using Python Matplotlib. An error band is used to indicate the uncertainty of the curve. In this example, we assume that the error can be given as a scalar _err_ that describes the uncertainty perpendicular to the curve in every point. We visualize this error as a colored band around the path using a `.PathPatch`. The patch is created from two path segments _(xp, yp)_, and _(xn, yn)_ that are shifted by +/- _err_ perpendicular to the curve _(x, y)_.

> You can write code in `curve-error-band.ipynb`.
