# MRI with EEG Visualization

## Introduction

This lab will guide you through creating a visualization of an MRI image with EEG traces using Python Matplotlib. You will learn how to load and display MRI and EEG data, plot an intensity histogram of the MRI image, and plot EEG traces with time on the x-axis and electrode channels on the y-axis.

## Steps

### Step 1: Load MRI Data and Display the Image

The first step is to load the MRI data and display the image. We will use the `imshow()` function to display the image and `axis('off')` to remove the axis labels.

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("MRI_with_EEG")

# Load the MRI data (256x256 16-bit integers)
im = np.load('mri_data.npy')

# Plot the MRI image
ax0 = fig.add_subplot(2, 2, 1)
ax0.imshow(im, cmap='gray')
ax0.axis('off')
```

### Step 2: Plot the Histogram of MRI Intensity

Next, we will plot the histogram of MRI intensity using the `hist()` function. We will normalize the intensity values to range between 0 and 1.

```python
# Plot the histogram of MRI intensity
ax1 = fig.add_subplot(2, 2, 2)
im = np.ravel(im)
im = im[np.nonzero(im)]  # Ignore the background
im = im / im.max()  # Normalize
ax1.hist(im, bins=100)
ax1.set_xlabel('Intensity (a.u.)')
ax1.set_ylabel('MRI density')
```

### Step 3: Load EEG Data and Plot Traces

The next step is to load the EEG data and plot the traces. We will use the `fromfile()` function to load the data from a file and `LineCollection()` to plot the traces. We will also set the y-axis tick labels to the electrode channels.

```python
# Load the EEG data
n_samples, n_rows = 800, 4
data = np.load('eeg_data.npy')
t = 10 * np.arange(n_samples) / n_samples

# Plot the EEG
ax2 = fig.add_subplot(2, 1, 2)
ax2.set_xlim(0, 10)
ax2.set_xticks(np.arange(10))
dmin = data.min()
dmax = data.max()
dr = (dmax - dmin) * 0.7  # Crowd them a bit.
y0 = dmin
y1 = (n_rows - 1) * dr + dmax
ax2.set_ylim(y0, y1)

segs = []
for i in range(n_rows):
    segs.append(np.column_stack((t, data[:, i])))

offsets = np.zeros((n_rows, 2), dtype=float)
offsets[:, 1] = np.arange(n_rows) * dr

lines = LineCollection(segs, offsets=offsets, transOffset=None)
ax2.add_collection(lines)

# Set the yticks to use axes coordinates on the y-axis
ax2.set_yticks(offsets[:, 1])
ax2.set_yticklabels(['PG3', 'PG5', 'PG7', 'PG9'])
ax2.set_xlabel('Time (s)')
```

### Step 4: Display the Visualization

Finally, we will display the visualization using the `show()` function.

```python
plt.tight_layout()
plt.show()
```

## Summary

In this lab, you learned how to create a visualization of an MRI image with EEG traces using Python Matplotlib. You loaded and displayed the MRI image, plotted an intensity histogram of the MRI image, and plotted EEG traces with time on the x-axis and electrode channels on the y-axis.
