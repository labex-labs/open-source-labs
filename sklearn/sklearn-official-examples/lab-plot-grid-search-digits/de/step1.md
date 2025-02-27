# Daten laden

Wir werden den digits-Datensatz laden und die Bilder zu Vektoren flachziehen. Jede 8x8-Pixel-Bild muss in einen Vektor von 64 Pixeln transformiert werden. Somit erhalten wir ein endgültiges Datenarray der Form `(n_images, n_pixels)`. Wir werden die Daten auch in einen Trainings- und einen Testsatz gleicher Größe unterteilen.

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

n_samples = len(digits.images)
X = digits.images.reshape((n_samples, -1))
y = digits.target == 8

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```
