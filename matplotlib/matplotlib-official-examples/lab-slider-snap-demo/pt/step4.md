# Definir Valores Permitidos para o _Slider_ de Amplitude

Nesta etapa, você definirá os valores permitidos para o _slider_ de amplitude. O _slider_ de amplitude usará esses valores para se ajustar ao valor permitido mais próximo.

```python
# define the values to use for snapping
allowed_amplitudes = np.concatenate([np.linspace(.1, 5, 100), [6, 7, 8, 9]])
```
