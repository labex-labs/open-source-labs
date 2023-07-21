"""
==================
Styling text boxes
==================

This example shows how to style text boxes using *bbox* parameters.
"""
import matplotlib.pyplot as plt

plt.text(
    0.6,
    0.7,
    "eggs",
    size=50,
    rotation=30.0,
    ha="center",
    va="center",
    bbox=dict(
        boxstyle="round",
        ec=(1.0, 0.5, 0.5),
        fc=(1.0, 0.8, 0.8),
    ),
)

plt.text(
    0.55,
    0.6,
    "spam",
    size=50,
    rotation=-25.0,
    ha="right",
    va="top",
    bbox=dict(
        boxstyle="square",
        ec=(1.0, 0.5, 0.5),
        fc=(1.0, 0.8, 0.8),
    ),
)

plt.show()
