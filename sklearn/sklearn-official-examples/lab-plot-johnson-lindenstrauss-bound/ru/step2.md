# Теоретические границы (продолжение)

Второй график показывает, что увеличение допустимой искажения `eps` позволяет уменьшить минимальное число размерностей `n_components` для заданного числа выборок `n_samples`.

```python
# диапазон допустимых искажений
eps_range = np.linspace(0.01, 0.99, 100)

# диапазон числа выборок (наблюдений) для встраивания
n_samples_range = np.logspace(2, 6, 5)
colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(n_samples_range)))

plt.figure()
for n_samples, color in zip(n_samples_range, colors):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples, eps=eps_range)
    plt.semilogy(eps_range, min_n_components, color=color)

plt.legend([f"n_samples = {n}" for n in n_samples_range], loc="upper right")
plt.xlabel("Искажение eps")
plt.ylabel("Минимальное число размерностей")
plt.title("Границы Джонсона-Линденштрасса:\nn_components vs eps")
plt.show()
```
