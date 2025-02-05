# 应用非负矩阵分解（NMF）

我们将使用两种不同的目标函数应用非负矩阵分解（NMF）：弗罗贝尼乌斯范数（Frobenius norm）和广义库尔贝克 - 莱布勒散度（generalized Kullback-Leibler divergence）。后者等同于概率潜在语义索引（Probabilistic Latent Semantic Indexing）。

```python
from sklearn.decomposition import NMF

n_components = 10
n_top_words = 20
init = "nndsvda"

# 拟合NMF模型
print(
    "使用tf - idf特征拟合NMF模型（弗罗贝尼乌斯范数），"
    "n_samples = %d 且 n_features = %d..." % (n_samples, n_features)
)
nmf = NMF(
    n_components=n_components,
    random_state=1,
    init=init,
    beta_loss="frobenius",
    alpha_W=0.00005,
    alpha_H=0.00005,
    l1_ratio=1,
).fit(tfidf)

# 绘制NMF模型的前几个关键词
def plot_top_words(model, feature_names, n_top_words, title):
    fig, axes = plt.subplots(2, 5, figsize=(30, 15), sharex=True)
    axes = axes.flatten()
    for topic_idx, topic in enumerate(model.components_):
        top_features_ind = topic.argsort()[: -n_top_words - 1 : -1]
        top_features = [feature_names[i] for i in top_features_ind]
        weights = topic[top_features_ind]

        ax = axes[topic_idx]
        ax.barh(top_features, weights, height=0.7)
        ax.set_title(f"主题 {topic_idx +1}", fontdict={"fontsize": 30})
        ax.invert_yaxis()
        ax.tick_params(axis="both", which="major", labelsize=20)
        for i in "top right left".split():
            ax.spines[i].set_visible(False)
        fig.suptitle(title, fontsize=40)

    plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
    plt.show()

tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
plot_top_words(
    nmf, tfidf_feature_names, n_top_words, "NMF模型中的主题（弗罗贝尼乌斯范数）"
)

# 使用广义库尔贝克 - 莱布勒散度拟合NMF模型
print(
    "\n" * 2,
    "使用tf - idf特征拟合NMF模型（广义库尔贝克 - 莱布勒散度），"
    "n_samples = %d 且 n_features = %d..."
    % (n_samples, n_features),
)
nmf = NMF(
    n_components=n_components,
    random_state=1,
    init=init,
    beta_loss="kullback-leibler",
    solver="mu",
    max_iter=1000,
    alpha_W=0.00005,
    alpha_H=0.00005,
    l1_ratio=0.5,
).fit(tfidf)

# 绘制使用广义库尔贝克 - 莱布勒散度的NMF模型的前几个关键词
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
plot_top_words(
    nmf,
    tfidf_feature_names,
    n_top_words,
    "NMF模型中的主题（广义库尔贝克 - 莱布勒散度）"
)

# 拟合MiniBatchNMF模型
from sklearn.decomposition import MiniBatchNMF

batch_size = 128

print(
    "\n" * 2,
    "使用tf - idf特征拟合MiniBatchNMF模型（弗罗贝尼乌斯范数），"
    "n_samples = %d 且 n_features = %d，batch_size = %d..."
    % (n_samples, n_features, batch_size),
)
mbnmf = MiniBatchNMF(
    n_components=n_components,
    random_state=1,
    batch_size=batch_size,
    init=init,
    beta_loss="frobenius",
    alpha_W=0.00005,
    alpha_H=0.00005,
    l1_ratio=0.5,
).fit(tfidf)

# 绘制使用弗罗贝尼乌斯范数的MiniBatchNMF模型的前几个关键词
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
plot_top_words(
    mbnmf,
    tfidf_feature_names,
    n_top_words,
    "MiniBatchNMF模型中的主题（弗罗贝尼乌斯范数）"
)

# 使用广义库尔贝克 - 莱布勒散度拟合MiniBatchNMF模型
print(
    "\n" * 2,
    "使用tf - idf特征拟合MiniBatchNMF模型（广义库尔贝克 - 莱布勒散度），"
    "n_samples = %d 且 n_features = %d，batch_size = %d..."
    % (n_samples, n_features, batch_size),
)
mbnmf = MiniBatchNMF(
    n_components=n_components,
    random_state=1,
    batch_size=batch_size,
    init=init,
    beta_loss="kullback-leibler",
    alpha_W=0.00005,
    alpha_H=0.00005,
    l1_ratio=0.5,
).fit(tfidf)

# 绘制使用广义库尔贝克 - 莱布勒散度的MiniBatchNMF模型的前几个关键词
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
plot_top_words(
    mbnmf,
    tfidf_feature_names,
    n_top_words,
    "MiniBatchNMF模型中的主题（广义库尔贝克 - 莱布勒散度）"
)


```
