import streamlit as st
import re

# BPRS-C 21문항 정의 (ko: 질문용, en: 출력용)
questions = [
    {"id": 1, "ko": "신체적 염려", "en": "1. Somatic Concern"},
    {"id": 2, "ko": "불안", "en": "2. Anxiety"},
    {"id": 3, "ko": "정서적 위축", "en": "3. Emotional Withdrawal"},
    {"id": 4, "ko": "사고 혼란", "en": "4. Conceptual Disorganization"},
    {"id": 5, "ko": "죄책감", "en": "5. Guilt Feelings"},
    {"id": 6, "ko": "긴장", "en": "6. Tension"},
    {"id": 7, "ko": "기이한 자세 및 버릇", "en": "7. Mannerisms and Posturing"},
    {"id": 8, "ko": "과대감", "en": "8. Grandiosity"},
    {"id": 9, "ko": "우울한 기분", "en": "9. Depressive Mood"},
    {"id": 10, "ko": "적대감", "en": "10. Hostility"},
    {"id": 11, "ko": "의심", "en": "11. Suspiciousness"},
    {"id": 12, "ko": "환각행동", "en": "12. Hallucinatory Behavior"},
    {"id": 13, "ko": "운동 지연", "en": "13. Motor Retardation"},
    {"id": 14, "ko": "협조성 부족", "en": "14. Uncooperativeness"},
    {"id": 15, "ko": "이상한 사고 내용", "en": "15. Unusual Thought Content"},
    {"id": 16, "ko": "정서 둔마", "en": "16. Blunted Affect"},
    {"id": 17, "ko": "동요", "en": "17. Excitement"},
    {"id": 18, "ko": "지남력 장애", "en": "18. Disorientation"},
    {"id": 19, "ko": "자살 사고", "en": "19. Suicidal Ideation"},
    {"id": 20, "ko": "관계적 사고", "en": "20. Referential Thinking"},
    {"id": 21, "ko": "분노 조절 어려움", "en": "21. Poor Anger Control"},
]

# 점수 선택지
options = [
    "Not Present (0)",
    "Very Mild (1)",
    "Mild (2)",
    "Moderate (3)",
    "Moderate/Severe (4)",
    "Severe (5)",
    "Extremely Severe (6)"
]

st.title("The Brief Psychiatric Rating Scale - Child version (BPRS-C)")

user_inputs = []
all_answered = True

for q in questions:
    choice = st.selectbox(q["ko"], options, key=q["id"])
    if not choice:
        all_answered = False
    user_inputs.append(f'{q["en"]} {choice}')

if st.button("Show Result"):
    if not all_answered or len(user_inputs) != 21:
        st.warning("모든 21개 문항에 응답해 주세요.")
    else:
        # 점수 추출: 괄호 안 숫자만 추출
        scores = [int(re.search(r"\((\d+)\)", s).group(1)) for s in user_inputs]
        total_score = sum(scores)

        # 증상군 점수 계산
        def subscore(start, end):
            return sum(scores[start - 1:end])

        behavior = subscore(1, 3)
        depression = subscore(4, 6)
        thinking = subscore(7, 9)
        excitement = subscore(10, 12)
        withdrawal = subscore(13, 15)
        anxiety = subscore(16, 18)
        somatic = subscore(19, 21)

        # 출력 포맷
        output = ["The Brief Psychiatric Rating Scale- Child version (BPRS-C)", ""]
        output.extend(user_inputs)
        output.append("")
        output.append("총점")
        output.append(str(total_score))
        output.append("")
        output.append("증상군 별 점수")
        output.append(f"행동 문제: {behavior}")
        output.append(f"우울증: {depression}")
        output.append(f"사고 장애: {thinking}")
        output.append(f"운동 흥분: {excitement}")
        output.append(f"사회적 위축: {withdrawal}")
        output.append(f"불안: {anxiety}")
        output.append(f"신체 증상: {somatic}")

        final_output = "\n".join(output)
        st.code(final_output, language="markdown")
