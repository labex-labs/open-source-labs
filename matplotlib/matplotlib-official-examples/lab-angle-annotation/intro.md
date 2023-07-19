# Introduction

In this tutorial, you will learn how to create a scale invariant angle label using Matplotlib. Angle annotation is often used to mark angles between lines or inside shapes with a circular arc. While Matplotlib provides an `~.patches.Arc`, an inherent problem when directly using it for such purposes is that an arc being circular in data space is not necessarily circular in display space. Also, the arc's radius is often best defined in a coordinate system which is independent of the actual data coordinates - at least if you want to be able to freely zoom into your plot without the annotation growing to infinity. This calls for a solution where the arc's center is defined in data space, but its radius in a physical unit like points or pixels, or as a ratio of the Axes dimension.

> You can write code in `angle-annotation.ipynb`.
