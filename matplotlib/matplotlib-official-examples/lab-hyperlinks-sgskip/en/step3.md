# Create an Image with a Hyperlink

In this step, we will create an image and add a hyperlink to it. Here's the code to create the image:

```python
fig = plt.figure()
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

im = plt.imshow(Z, interpolation='bilinear', cmap=cm.gray,
                origin='lower', extent=[-3, 3, -3, 3])
```

To add a hyperlink to the image, we need to use the `set_url()` method of the image object. This method takes a URL as its argument. Here's the updated code:

```python
im.set_url('https://www.google.com/')
```

The image will have a hyperlink to `https://www.google.com/`. Finally, we can save the plot as an SVG file using `fig.savefig()`:

```python
fig.savefig('image.svg')
```
