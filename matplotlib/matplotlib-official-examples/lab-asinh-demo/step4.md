# Compare "symlog" and "asinh" behaviour on sample y=x graph

We will compare the behaviour of "symlog" and "asinh" on a sample y=x graph. We will plot the same graph twice, once with "symlog" and once with "asinh".

```python
fig1 = plt.figure()
ax0, ax1 = fig1.subplots(1, 2, sharex=True)

ax0.plot(x, x)
ax0.set_yscale('symlog')
ax0.grid()
ax0.set_title('symlog')

ax1.plot(x, x)
ax1.set_yscale('asinh')
ax1.grid()
ax1.set_title('asinh')
```
