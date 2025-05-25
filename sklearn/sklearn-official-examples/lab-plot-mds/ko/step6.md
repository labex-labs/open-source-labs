# 데이터 재조정 및 회전

그런 다음 scikit-learn 의 PCA 를 사용하여 시각화를 위해 데이터를 재조정하고 회전합니다.

```python
# 데이터 재조정
pos *= np.sqrt((X_true**2).sum()) / np.sqrt((pos**2).sum())
npos *= np.sqrt((X_true**2).sum()) / np.sqrt((npos**2).sum())

# 데이터 회전
clf = PCA(n_components=2)
X_true = clf.fit_transform(X_true)
pos = clf.fit_transform(pos)
npos = clf.fit_transform(npos)
```
