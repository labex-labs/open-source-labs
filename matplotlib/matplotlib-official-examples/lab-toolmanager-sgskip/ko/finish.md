# 요약

이 튜토리얼에서는 `matplotlib.backend_managers.ToolManager`를 사용하여 Toolbar 를 수정하고, 사용자 정의 도구를 생성하고, 도구를 추가하고, 도구를 제거하는 방법을 배웠습니다. `ToolManager`에 의해 제어되는 모든 도구를 나열하는 `ListTools`라는 사용자 정의 도구를 만들었습니다. 또한, 도구가 활성화되었는지 또는 비활성화되었는지에 따라 지정된 `gid`를 가진 플롯의 모든 선의 가시성을 True 또는 False 로 설정하는 `GroupHideTool`이라는 사용자 정의 도구도 만들었습니다. 마지막으로, 사용자 정의 도구를 `ToolManager`에 추가하고, `Show` 도구를 `Toolbar`에 추가했으며, `Toolbar`에서 `forward` 버튼을 제거했습니다.
