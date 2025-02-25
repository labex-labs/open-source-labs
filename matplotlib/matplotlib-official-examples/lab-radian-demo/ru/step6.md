# Добавить подписи и настроить макет

Добавьте заголовок и подписи осей к подграфикам с использованием функций title, xlabel и ylabel из matplotlib.pyplot. Настройте макет подграфиков с использованием функции tight_layout.

```python
axs[0].set_title('Cosine with Radian X-Axis')
axs[0].set_xlabel('Radians')
axs[0].set_ylabel('Cosine')
axs[1].set_title('Cosine with Degree X-Axis')
axs[1].set_xlabel('Degrees')
axs[1].set_ylabel('Cosine')
fig.tight_layout()
```
