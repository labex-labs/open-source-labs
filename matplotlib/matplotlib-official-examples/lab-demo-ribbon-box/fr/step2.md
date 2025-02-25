# Création de la classe RibbonBox

Dans cette étape, nous allons créer la classe `RibbonBox` qui sera utilisée pour créer les couleurs graduées des boîtes ruban.

```python
class RibbonBox:
    # Chargez l'image de la boîte ruban
    original_image = plt.imread(cbook.get_sample_data("Minduka_Present_Blue_Pack.png"))
    cut_location = 70
    b_and_h = original_image[:, :, 2:3]
    color = original_image[:, :, 2:3] - original_image[:, :, 0:1]
    alpha = original_image[:, :, 3:4]
    nx = original_image.shape[1]

    def __init__(self, color):
        rgb = mcolors.to_rgb(color)
        self.im = np.dstack([self.b_and_h - self.color * (1 - np.array(rgb)), self.alpha])

    def get_stretched_image(self, stretch_factor):
        stretch_factor = max(stretch_factor, 1)
        ny, nx, nch = self.im.shape
        ny2 = int(ny*stretch_factor)
        return np.vstack([self.im[:self.cut_location],
                          np.broadcast_to(self.im[self.cut_location], (ny2 - ny, nx, nch)),
                          self.im[self.cut_location:]])
```
