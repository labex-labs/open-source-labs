# Anzahl der Features gegen Kreuzvalidierungsscores plotten

Wir werden die Anzahl der ausgewählten Features gegen die Kreuzvalidierungsscores plotten. Wir werden matplotlib verwenden, um das Diagramm zu erstellen.

```python
import matplotlib.pyplot as plt

n_scores = len(rfecv.cv_results_["mean_test_score"])
plt.figure()
plt.xlabel("Anzahl der ausgewählten Features")
plt.ylabel("Durchschnittliche Testgenauigkeit")
plt.errorbar(
    range(min_features_to_select, n_scores + min_features_to_select),
    rfecv.cv_results_["mean_test_score"],
    yerr=rfecv.cv_results_["std_test_score"],
)
plt.title("Rekursive Feature-Eliminierung \nmit korrelierten Features")
plt.show()
```
