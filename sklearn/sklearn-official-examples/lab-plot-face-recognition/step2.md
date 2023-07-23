# Load and Explore Dataset

```python
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
n_samples, h, w = lfw_people.images.shape
X = lfw_people.data
n_features = X.shape[1]
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]
```

We download the dataset using the `fetch_lfw_people()` function from scikit-learn. We then explore the dataset by getting the number of samples, height, and width of the images. We also get the input data `X`, target `y`, target names `target_names`, and number of classes `n_classes`.
