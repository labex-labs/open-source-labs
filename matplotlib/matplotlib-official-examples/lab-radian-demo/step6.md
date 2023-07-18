# Add labels and adjust layout

Add a title and axis labels to the subplots using the title, xlabel, and ylabel functions from matplotlib.pyplot. Adjust the layout of the subplots using the tight_layout function.

```python
axs[0].set_title('Cosine with Radian X-Axis')
axs[0].set_xlabel('Radians')
axs[0].set_ylabel('Cosine')
axs[1].set_title('Cosine with Degree X-Axis')
axs[1].set_xlabel('Degrees')
axs[1].set_ylabel('Cosine')
fig.tight_layout()
```
