# Создайте вторую страницу

В этом шаге вы создадите вторую страницу PDF-файла. На странице будет график синусоидальной волны.

```python
plt.rcParams['text.usetex'] = True
plt.figure(figsize=(8, 6))
x = np.arange(0, 5, 0.1)
plt.plot(x, np.sin(x), 'b-')
plt.title('Page Two')
pdf.attach_note("plot of sin(x)")  # attach metadata (as pdf note) to page
pdf.savefig()
plt.close()
```
