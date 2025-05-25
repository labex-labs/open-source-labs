# 플롯 사용자 정의

네 번째 단계는 범례를 추가하고, 축 제한 및 레이블을 설정하고, 뷰 각도를 변경하여 플롯을 사용자 정의하는 것입니다.

```python
# Make legend, set axes limits and labels
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=20., azim=-35, roll=0)

plt.show()
```
