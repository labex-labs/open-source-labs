# データセットの読み込み

20 ニュースグループのデータセットを読み込み、ベクトル化します。最初に、いくつかのヒューリスティックを使って無用な用語をフィルタリングします。投稿からヘッダー、フッター、引用返信を取り除き、一般的な英単語、1 つの文書にのみ出現する単語、または少なくとも 95% の文書に出現する単語を削除します。

```python
from sklearn.datasets import fetch_20newsgroups

n_samples = 2000
n_features = 1000

print("Loading dataset...")
data, _ = fetch_20newsgroups(
    shuffle=True,
    random_state=1,
    remove=("headers", "footers", "quotes"),
    return_X_y=True,
)
data_samples = data[:n_samples]
```
