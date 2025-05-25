# 트리의 노드 수와 깊이 시각화

alpha 값이 증가함에 따라 트리의 노드 수와 깊이를 시각화합니다.

```python
node_counts = [clf.tree_.node_count for clf in clfs]
depth = [clf.tree_.max_depth for clf in clfs]
fig, ax = plt.subplots(2, 1)
ax[0].plot(ccp_alphas, node_counts, marker="o", drawstyle="steps-post")
ax[0].set_xlabel("alpha")
ax[0].set_ylabel("노드 수")
ax[0].set_title("alpha 에 따른 노드 수")
ax[1].plot(ccp_alphas, depth, marker="o", drawstyle="steps-post")
ax[1].set_xlabel("alpha")
ax[1].set_ylabel("트리 깊이")
ax[1].set_title("alpha 에 따른 트리 깊이")
fig.tight_layout()
```
