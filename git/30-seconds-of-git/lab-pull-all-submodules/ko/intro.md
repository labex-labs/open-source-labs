# 소개

<div class="alert alert-warning" role="alert">
<p>🧑‍💻 Git 또는 LabEx 를 처음 사용하시나요? <b><a style="color: unset;text-decoration: underline;" href="https://labex.io/courses/quick-start-with-git" target="_blank">Git 퀵 스타트</a></b> 강좌부터 시작하는 것을 권장합니다.</p>
</div>

Git 저장소 (repository) 로 작업할 때, 서브모듈 (submodule) 을 사용하여 다른 저장소를 종속성 (dependency) 으로 포함할 수 있습니다. 하지만 이러한 종속성이 각 원격 저장소 (remote) 에서 업데이트될 때, 변경 사항이 메인 저장소에 자동으로 반영되지 않습니다. 서브모듈을 업데이트하려면, 각 원격 저장소에서 해당 서브모듈을 pull 해야 합니다.
