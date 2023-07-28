# Face Completion with Multi-Output Estimators

## Introduction

This lab demonstrates how to use multi-output estimators to complete images. The goal is to predict the lower half of a face given its upper half. Different algorithms such as extremely randomized trees, k-nearest neighbors, linear regression, and ridge regression will be used to complete the lower half of the faces. The completed faces will be compared with the original faces to evaluate the performance of the algorithms.

## Steps

### Step 1: Load the Data

The first step is to load the Olivetti faces dataset, which contains 400 grayscale images of 64x64 pixels each. The data is split into training and testing sets. The training set contains the faces of 30 people, and the testing set contains the faces of the remaining people. For this lab, we will test the algorithms on a subset of five people.

```python
# Load the faces datasets
data, targets = fetch_olivetti_faces(return_X_y=True)

train = data[targets < 30]
test = data[targets >= 30]  # Test on independent people

# Test on a subset of people
n_faces = 5
rng = check_random_state(4)
face_ids = rng.randint(test.shape[0], size=(n_faces,))
test = test[face_ids, :]

n_pixels = data.shape[1]
# Upper half of the faces
X_train = train[:, : (n_pixels + 1) // 2]
# Lower half of the faces
y_train = train[:, n_pixels // 2 :]
X_test = test[:, : (n_pixels + 1) // 2]
y_test = test[:, n_pixels // 2 :]
```

### Step 2: Fit Estimators

The second step is to fit the multi-output estimators to the training data. We will use four different algorithms: extremely randomized trees, k-nearest neighbors, linear regression, and ridge regression. The estimators will predict the lower half of the faces based on the upper half.

```python
# Fit estimators
ESTIMATORS = {
    "Extra trees": ExtraTreesRegressor(
        n_estimators=10, max_features=32, random_state=0
    ),
    "K-nn": KNeighborsRegressor(),
    "Linear regression": LinearRegression(),
    "Ridge": RidgeCV(),
}

y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    estimator.fit(X_train, y_train)
    y_test_predict[name] = estimator.predict(X_test)
```

### Step 3: Plot the Completed Faces

The final step is to plot the completed faces for each algorithm and compare them with the original faces. The original faces are shown in the first column, and the completed faces are shown in the subsequent columns for each algorithm. The performance of the algorithms can be evaluated by comparing the completed faces with the original faces.

```python
# Plot the completed faces
image_shape = (64, 64)

n_cols = 1 + len(ESTIMATORS)
plt.figure(figsize=(2.0 * n_cols, 2.26 * n_faces))
plt.suptitle("Face completion with multi-output estimators", size=16)

for i in range(n_faces):
    true_face = np.hstack((X_test[i], y_test[i]))

    if i:
        sub = plt.subplot(n_faces, n_cols, i * n_cols + 1)
    else:
        sub = plt.subplot(n_faces, n_cols, i * n_cols + 1, title="true faces")

    sub.axis("off")
    sub.imshow(
        true_face.reshape(image_shape), cmap=plt.cm.gray, interpolation="nearest"
    )

    for j, est in enumerate(sorted(ESTIMATORS)):
        completed_face = np.hstack((X_test[i], y_test_predict[est][i]))

        if i:
            sub = plt.subplot(n_faces, n_cols, i * n_cols + 2 + j)

        else:
            sub = plt.subplot(n_faces, n_cols, i * n_cols + 2 + j, title=est)

        sub.axis("off")
        sub.imshow(
            completed_face.reshape(image_shape),
            cmap=plt.cm.gray,
            interpolation="nearest",
        )

plt.show()
```

## Summary

This lab demonstrated how to use multi-output estimators to complete images. We used four different algorithms to predict the lower half of a face based on the upper half. The performance of the algorithms was evaluated by comparing the completed faces with the original faces.
