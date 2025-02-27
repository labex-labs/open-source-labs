# Analyse des résultats

L'attribut `cv_results_` de l'objet de recherche contient les résultats de la recherche. Convertissez-le en un DataFrame pandas à l'aide du code suivant :

```python
results = pd.DataFrame(rsh.cv_results_)
```

La colonne `params_str` est créée en convertissant la colonne `params` en chaîne de caractères. Supprimez les lignes dupliquées qui ont les mêmes valeurs pour `params_str` et `iter` :

```python
results["params_str"] = results.params.apply(str)
results.drop_duplicates(subset=("params_str", "iter"), inplace=True)
```

Les scores moyens de test sont ensuite pivotés par rapport au numéro d'itération et à la combinaison de paramètres à l'aide de la méthode `pivot` :

```python
mean_scores = results.pivot(
    index="iter", columns="params_str", values="mean_test_score"
)
```

Enfin, tracez les scores moyens de test au cours des itérations à l'aide du code suivant :

```python
ax = mean_scores.plot(legend=False, alpha=0.6)

labels = [
    f"itération={i}\nn_échantillons={rsh.n_resources_[i]}\nn_candidats={rsh.n_candidates_[i]}"
    for i in range(rsh.n_iterations_)
]

ax.set_xticks(range(rsh.n_iterations_))
ax.set_xticklabels(labels, rotation=45, multialignment="left")
ax.set_title("Scores des candidats au cours des itérations")
ax.set_ylabel("score moyen de test", fontsize=15)
ax.set_xlabel("itérations", fontsize=15)
plt.tight_layout()
plt.show()
```
