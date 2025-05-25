# Figure 및 Subplot 생성

두 개의 서브플롯이 있는 figure 를 생성합니다. 첫 번째 서브플롯은 3D surface plot 이고, 두 번째 서브플롯은 3D wireframe plot 입니다.

```python
# Create a figure with two subplots
fig = plt.figure(figsize=plt.figaspect(0.5))

# Add the first subplot with 3D projection
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# Add the second subplot with 3D projection
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
```
