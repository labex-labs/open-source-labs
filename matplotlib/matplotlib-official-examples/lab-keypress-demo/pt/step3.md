# Criar o Gráfico e Conectar o Listener de Evento de Pressionamento de Tecla

Criamos um gráfico simples usando `np.random.rand()` para gerar dados aleatórios. Em seguida, configuramos o listener de evento de pressionamento de tecla usando `fig.canvas.mpl_connect()` e passando o nome do evento que queremos ouvir (`'key_press_event'`) e a função que queremos chamar quando o evento ocorre (`on_press`).

```python
fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', on_press)

ax.plot(np.random.rand(12), np.random.rand(12), 'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()
```
