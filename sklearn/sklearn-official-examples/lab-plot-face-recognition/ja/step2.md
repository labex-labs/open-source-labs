# データセットの読み込みと探索

```python
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
n_samples, h, w = lfw_people.images.shape
X = lfw_people.data
n_features = X.shape[1]
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]
```

scikit-learn の`fetch_lfw_people()`関数を使用してデータセットをダウンロードします。次に、画像のサンプル数、高さ、幅を取得することでデータセットを探索します。また、入力データ`X`、ターゲット`y`、ターゲット名`target_names`、クラス数`n_classes`も取得します。
