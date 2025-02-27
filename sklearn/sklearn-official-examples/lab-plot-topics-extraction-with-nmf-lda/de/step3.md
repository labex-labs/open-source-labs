# Wendet NMF an

Wir werden NMF mit zwei verschiedenen Zielfunktionen anwenden: die Frobenius-Norm und die verallgemeinerte Kullback-Leibler-Divergenz. Letztere ist äquivalent zu Probabilistic Latent Semantic Indexing.

```python
from sklearn.decomposition import NMF

n_components = 10
n_top_words = 20
init = "nndsvda"

# Passt das NMF-Modell an
print(
    "Passt das NMF-Modell (Frobenius-Norm) mit tf-idf-Merkmalen, "
    "n_samples=%d und n_features=%d an..." % (n_samples, n_features)
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

# Zeichnet die wichtigsten Wörter für das NMF-Modell
def plot_top_words(model, feature_names, n_top_words, title):
    fig, axes = plt.subplots(2, 5, figsize=(30, 15), sharex=True)
    axes = axes.flatten()
    for topic_idx, topic in enumerate(model.components_):
        top_features_ind = topic.argsort()[: -n_top_words - 1 : -1]
        top_features = [feature_names[i] for i in top_features_ind]
        weights = topic[top_features_ind]

        ax = axes[topic_idx]
        ax.barh(top_features, weights, height=0.7)
        ax.set_title(f"Topic {topic_idx +1}", fontdict={"fontsize": 30})
        ax.invert_yaxis()
        ax.tick_params(axis="both", which="major", labelsize=20)
        for i in "top right left".split():
            ax.spines[i].set_visible(False)
        fig.suptitle(title, fontsize=40)

    plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
    plt.show()

tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
plot_top_words(
    nmf, tfidf_feature_names, n_top_words, "Topics in NMF model (Frobenius norm)"
)

# Passt das NMF-Modell mit der verallgemeinerten Kullback-Leibler-Divergenz an
print(
    "\n" * 2,
    "Passt das NMF-Modell (verallgemeinerte Kullback-Leibler "
    "Divergenz) mit tf-idf-Merkmalen, n_samples=%d und n_features=%d an..."
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

# Zeichnet die wichtigsten Wörter für das NMF-Modell mit der verallgemeinerten Kullback-Leibler-Divergenz
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
plot_top_words(
    nmf,
    tfidf_feature_names,
    n_top_words,
    "Topics in NMF model (generalized Kullback-Leibler divergence)",
)

# Passt das MiniBatchNMF-Modell an
from sklearn.decomposition import MiniBatchNMF

batch_size = 128

print(
    "\n" * 2,
    "Passt das MiniBatchNMF-Modell (Frobenius-Norm) mit tf-idf "
    "Merkmalen, n_samples=%d und n_features=%d, batch_size=%d an..."
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

# Zeichnet die wichtigsten Wörter für das MiniBatchNMF-Modell mit der Frobenius-Norm
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
plot_top_words(
    mbnmf,
    tfidf_feature_names,
    n_top_words,
    "Topics in MiniBatchNMF model (Frobenius norm)",
)

# Passt das MiniBatchNMF-Modell mit der verallgemeinerten Kullback-Leibler-Divergenz an
print(
    "\n" * 2,
    "Passt das MiniBatchNMF-Modell (verallgemeinerte Kullback-Leibler "
    "Divergenz) mit tf-idf Merkmalen, n_samples=%d und n_features=%d, "
    "batch_size=%d an..." % (n_samples, n_features, batch_size),
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

# Zeichnet die wichtigsten Wörter für das MiniBatchNMF-Modell mit der verallgemeinerten Kullback-Leibler-Divergenz
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
plot_top_words(
    mbnmf,
    tfidf_feature_names,
    n_top_words,
    "Topics in MiniBatchNMF model (generalized Kullback-Leibler divergence)",
)


```
