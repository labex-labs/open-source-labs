# 플롯 생성 및 키 누름 이벤트 리스너 연결

`np.random.rand()`를 사용하여 임의의 데이터를 생성하여 간단한 플롯을 만듭니다. 그런 다음, `fig.canvas.mpl_connect()`를 사용하여 키 누름 이벤트 리스너를 설정하고, 우리가 감지하려는 이벤트의 이름 (`'key_press_event'`) 과 이벤트가 발생했을 때 호출할 함수 (`on_press`) 를 전달합니다.

```python
fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', on_press)

ax.plot(np.random.rand(12), np.random.rand(12), 'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()
```
