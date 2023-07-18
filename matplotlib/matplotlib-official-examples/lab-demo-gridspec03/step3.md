# Control Spacing Around and Between Subplots

In this step, we will use `GridSpec` to control the spacing around and between subplots. We will create a figure with 2 gridspecs, each with 3 rows and 3 columns. We will specify the `left`, `right`, `bottom`, `top`, `wspace`, and `hspace` parameters to control the spacing.

```python
fig = plt.figure()
gs1 = GridSpec(3, 3, left=0.05, right=0.48, wspace=0.05)
ax1 = fig.add_subplot(gs1[:-1, :])
ax2 = fig.add_subplot(gs1[-1, :-1])
ax3 = fig.add_subplot(gs1[-1, -1])

gs2 = GridSpec(3, 3, left=0.55, right=0.98, hspace=0.05)
ax4 = fig.add_subplot(gs2[:, :-1])
ax5 = fig.add_subplot(gs2[:-1, -1])
ax6 = fig.add_subplot(gs2[-1, -1])
```
