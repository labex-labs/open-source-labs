# Aplicar NMF

Aplicaremos NMF com duas funções objetivo diferentes: a norma de Frobenius e a divergência generalizada de Kullback-Leibler. Esta última é equivalente à Indexação Semântica de Palavras Latentes Probabilística.

```python
from sklearn.decomposition import NMF

n_components = 10
n_top_words = 20
init = "nndsvda"

# Ajustar o modelo NMF
print(
    "Ajustando o modelo NMF (norma de Frobenius) com recursos tf-idf, "
    "n_samples=%d e n_features=%d..." % (n_samples, n_features)
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

# Plotar as palavras principais para o modelo NMF
def plot_top_words(model, feature_names, n_top_words, title):
    fig, axes = plt.subplots(2, 5, figsize=(30, 15), sharex=True)
    axes = axes.flatten()
    for topic_idx, topic in enumerate(model.components_):
        top_features_ind = topic.argsort()[: -n_top_words - 1 : -1]
        top_features = [feature_names[i] for i in top_features_ind]
        weights = topic[top_features_ind]

        ax = axes[topic_idx]
        ax.barh(top_features, weights, height=0.7)
        ax.set_title(f"Tópico {topic_idx +1}", fontdict={"fontsize": 30})
        ax.invert_yaxis()
        ax.tick_params(axis="both", which="major", labelsize=20)
        for i in "top right left".split():
            ax.spines[i].set_visible(False)
        fig.suptitle(title, fontsize=40)

    plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
    plt.show()

tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
plot_top_words(
    nmf, tfidf_feature_names, n_top_words, "Tópicos no modelo NMF (norma de Frobenius)"
)

# Ajustar o modelo NMF com a divergência generalizada de Kullback-Leibler
print(
    "\n" * 2,
    "Ajustando o modelo NMF (divergência generalizada de Kullback-Leibler "
    "com recursos tf-idf, n_samples=%d e n_features=%d..."
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

# Plotar as palavras principais para o modelo NMF com a divergência generalizada de Kullback-Leibler
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
plot_top_words(
    nmf,
    tfidf_feature_names,
    n_top_words,
    "Tópicos no modelo NMF (divergência generalizada de Kullback-Leibler)",
)

# Ajustar o modelo MiniBatchNMF
from sklearn.decomposition import MiniBatchNMF

batch_size = 128

print(
    "\n" * 2,
    "Ajustando o modelo MiniBatchNMF (norma de Frobenius) com recursos tf-idf "
    "n_samples=%d e n_features=%d, batch_size=%d..."
    % (n_samples, n_features, batch_size),
)
# ... (restante do código)
```
