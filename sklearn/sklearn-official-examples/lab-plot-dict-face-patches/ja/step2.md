# 画像の辞書を学習する

画像の辞書を学習するために MiniBatchKMeans を使用します。クラスタ数を 81 に設定し、乱数シードを設定し、詳細モードを有効にします。その後、パッチを格納するためのバッファを作成し、データセット内の各画像を反復処理します。各画像から 50 個のパッチを抽出し、データを整形します。その後、データをバッファに追加し、インデックスをインクリメントします。インデックスが 10 の倍数の場合、バッファを連結し、データに対して partial_fit を実行します。インデックスが 100 の倍数の場合、これまでにフィットさせたパッチの数を表示するメッセージを出力します。

```python
import time
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.image import extract_patches_2d

print("Learning the dictionary... ")
rng = np.random.RandomState(0)
kmeans = MiniBatchKMeans(n_clusters=81, random_state=rng, verbose=True, n_init=3)
patch_size = (20, 20)

buffer = []
t0 = time.time()

# The online learning part: cycle over the whole dataset 6 times
index = 0
for _ in range(6):
    for img in faces.images:
        data = extract_patches_2d(img, patch_size, max_patches=50, random_state=rng)
        data = np.reshape(data, (len(data), -1))
        buffer.append(data)
        index += 1
        if index % 10 == 0:
            data = np.concatenate(buffer, axis=0)
            data -= np.mean(data, axis=0)
            data /= np.std(data, axis=0)
            kmeans.partial_fit(data)
            buffer = []
        if index % 100 == 0:
            print("Partial fit of %4i out of %i" % (index, 6 * len(faces.images)))

dt = time.time() - t0
print("done in %.2fs." % dt)
```
