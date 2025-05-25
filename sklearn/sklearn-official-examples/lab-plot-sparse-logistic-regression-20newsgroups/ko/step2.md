# 데이터 로드 및 준비

다음으로 `20newsgroups` 데이터셋을 로드하고 학습 및 테스트 데이터를 준비합니다.

```python
# SAGA solver 를 사용합니다.
solver = "saga"

# 실행 시간을 단축하기 위해 샘플 수를 줄입니다.
n_samples = 5000

X, y = fetch_20newsgroups_vectorized(subset="all", return_X_y=True)
X = X[:n_samples]
y = y[:n_samples]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, stratify=y, test_size=0.1
)
train_samples, n_features = X_train.shape
n_classes = np.unique(y).shape[0]

print(
    "데이터셋 20newsgroup, train_samples=%i, n_features=%i, n_classes=%i"
    % (train_samples, n_features, n_classes)
)
```
