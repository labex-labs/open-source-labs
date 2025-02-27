# Appliquer la NMF

Nous allons appliquer la NMF avec deux fonctions objectifs différentes : la norme de Frobenius et la divergence générale de Kullback-Leibler. Cette dernière est équivalente à l'indexation sémantique latente probabiliste.

```python
from sklearn.decomposition import NMF

n_components = 10
n_top_words = 20
init = "nndsvda"

# Ajuster le modèle NMF
print(
    "Ajustement du modèle NMF (norme de Frobenius) avec des caractéristiques tf-idf, "
    "n_samples=%d et n_features=%d..." % (n_samples, n_features)
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

# Tracer les mots les plus fréquents pour le modèle NMF
def plot_top_words(model, feature_names, n_top_words, title):
    fig, axes = plt.subplots(2, 5, figsize=(30, 15), sharex=True)
    axes = axes.flatten()
    for topic_idx, topic in enumerate(model.components_):
        top_features_ind = topic.argsort()[: -n_top_words - 1 : -1]
        top_features = [feature_names[i] for i in top_features_ind]
        weights = topic[top_features_ind]

        ax = axes[topic_idx]
        ax.barh(top_features, weights, height=0.7)
        ax.set_title(f"Sujet {topic_idx +1}", fontdict={"fontsize": 30})
        ax.invert_yaxis()
        ax.tick_params(axis="both", which="major", labelsize=20)
        for i in "top right left".split():
            ax.spines[i].set_visible(False)
        fig.suptitle(title, fontsize=40)

    plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
    plt.show()

tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
plot_top_words(
    nmf, tfidf_feature_names, n_top_words, "Sujets dans le modèle NMF (norme de Frobenius)"
)

# Ajuster le modèle NMF avec la divergence générale de Kullback-Leibler
print(
    "\n" * 2,
    "Ajustement du modèle NMF (divergence générale de Kullback-Leibler "
    "divergence) avec des caractéristiques tf-idf, n_samples=%d et n_features=%d..."
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

# Tracer les mots les plus fréquents pour le modèle NMF avec la divergence générale de Kullback-Leibler
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
plot_top_words(
    nmf,
    tfidf_feature_names,
    n_top_words,
    "Sujets dans le modèle NMF (divergence générale de Kullback-Leibler divergence)",
)

# Ajuster le modèle MiniBatchNMF
from sklearn.decomposition import MiniBatchNMF

batch_size = 128

print(
    "\n" * 2,
    "Ajustement du modèle MiniBatchNMF (norme de Frobenius) avec tf-idf "
    "caractéristiques, n_samples=%d et n_features=%d, batch_size=%d..."
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

# Tracer les mots les plus fréquents pour le modèle MiniBatchNMF avec la norme de Frobenius
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
plot_top_words(
    mbnmf,
    tfidf_feature_names,
    n_top_words,
    "Sujets dans le modèle MiniBatchNMF (norme de Frobenius)",
)

# Ajuster le modèle MiniBatchNMF avec la divergence générale de Kullback-Leibler
print(
    "\n" * 2,
    "Ajustement du modèle MiniBatchNMF (divergence générale de Kullback-Leibler "
    "divergence) avec des caractéristiques tf-idf, n_samples=%d et n_features=%d, "
    "batch_size=%d..." % (n_samples, n_features, batch_size),
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

# Tracer les mots les plus fréquents pour le modèle MiniBatchNMF avec la divergence générale de Kullback-Leibler
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
plot_top_words(
    mbnmf,
    tfidf_feature_names,
    n_top_words,
    "Sujets dans le modèle MiniBatchNMF (divergence générale de Kullback-Leibler divergence)",
)


```
