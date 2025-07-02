# 소개

이 실험실에서는 균일 분포 랜덤 레이블링이 일부 클러스터링 평가 지표의 동작에 미치는 영향을 탐구합니다. 클러스터링 알고리즘은 근본적으로 지도 학습이 아닌 방법이며, 평가 지표는 "지도" 기준 정보를 활용하여 생성된 클러스터의 품질을 정량화합니다. 그러나 조정되지 않은 클러스터링 평가 지표는 세분화된 레이블링에 대해 큰 값을 출력하여 완전히 랜덤일 수 있으므로 오해의 소지가 있습니다. 따라서, 조정된 지표만이 주어진 k 값에 대해 데이터 세트의 다양한 중첩된 하위 샘플에 대한 클러스터링 알고리즘의 평균 안정성을 평가하는 합의 지표로 안전하게 사용될 수 있습니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
이것은 가이드 실험입니다. 학습과 실습을 돕기 위한 단계별 지침을 제공합니다.각 단계를 완료하고 실무 경험을 쌓기 위해 지침을 주의 깊게 따르세요. 과거 데이터에 따르면, 이것은 <span class="text-red-600 dark:text-red-400">고급</span> 레벨의 실험이며 완료율은 <span class="text-red-600 dark:text-red-400">31%</span>입니다.학습자들로부터 <span class="text-primary-600 dark:text-primary-400">100%</span>의 긍정적인 리뷰율을 받았습니다.
</div>
