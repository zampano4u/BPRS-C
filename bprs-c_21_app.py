
# pip install streamlit

import streamlit as st


bprs_c_21_items = [
    {"id": 1, "question_ko": "협조성 결여", "question_en": "Uncooperativeness", "description_ko": "부정적이고, 협조적이지 않으며, 저항적이고, 다루기 어려운 태도", "description_en": "Negative, uncooperative, resistant, difficult to manage"},
    {"id": 2, "question_ko": "적대감", "question_en": "Hostility", "description_ko": "분노하거나 의심스러운 정서 표현, 호전성, 비난 및 타인을 향한 언어적 비판", "description_en": "Angry or suspicious affect, belligerence, accusations & verbal condemnation of others"},
    {"id": 3, "question_ko": "조종적 태도", "question_en": "Manipulativeness", "description_ko": "거짓말을 하거나, 속이거나, 타인을 착취하는 행동", "description_en": "Lying, cheating, exploitive of others"},
    {"id": 4, "question_ko": "우울한 기분", "question_en": "Depressed Mood", "description_ko": "슬픔, 눈물을 흘림, 우울한 외양", "description_en": "Sad, tearful, depressive demeanor"},
    {"id": 5, "question_ko": "열등감", "question_en": "Feelings of Inferiority", "description_ko": "자신감이 부족하고, 자기 비하적인 태도", "description_en": "Lacking self-confidence, self-depreciatory"},
    {"id": 6, "question_ko": "자살 사고", "question_en": "Suicidal Ideation", "description_ko": "자살에 대한 생각, 위협 또는 시도", "description_en": "Thoughts, threats, or attempts of suicide"},
    {"id": 7, "question_ko": "기이한 환상", "question_en": "Peculiar Fantasies", "description_ko": "반복적이며, 이상하거나 비정상적이거나 자폐적인 환상", "description_en": "Recurrent, odd, unusual, or autistic fantasies"},
    {"id": 8, "question_ko": "망상", "question_en": "Delusions", "description_ko": "관계 망상, 피해 망상 또는 과대 망상", "description_en": "Ideas of reference, persecutory or grandiose delusions"},
    {"id": 9, "question_ko": "환각", "question_en": "Hallucinations", "description_ko": "시각, 청각 또는 기타 감각 환각", "description_en": "Visual, auditory, or other hallucinatory perceptions"},
    {"id": 10, "question_ko": "과잉행동", "question_en": "Hyperactivity", "description_ko": "과도한 에너지 소비, 자세의 잦은 변화, 끊임없는 움직임", "description_en": "Excessive energy expenditure, frequent changes in posture, perpetual motion"},
    {"id": 11, "question_ko": "산만함", "question_en": "Distractibility", "description_ko": "집중력 저하, 주의 집중 지속 시간 단축, 주변 자극에 대한 민감한 반응", "description_en": "Poor concentration, shortened attention span, reactivity to peripheral stimuli"},
    {"id": 12, "question_ko": "압박된 말투 또는 음성", "question_en": "Speech or Voice Pressure", "description_ko": "목소리가 크거나 과도하게 많고, 압박된 언어 표현", "description_en": "Loud, excessive, or pressured speech"},
    {"id": 13, "question_ko": "말의 빈약함", "question_en": "Underproductive Speech", "description_ko": "최소한의, 드문드문하거나 억제된 언어 반응 양상, 약하고 낮은 목소리", "description_en": "Minimal, sparse, inhibited verbal response pattern, or weak low voice"},
    {"id": 14, "question_ko": "정서적 위축", "question_en": "Emotional Withdrawal", "description_ko": "검사자와의 자발적인 관계 결여, 또래와의 상호작용 부족, 저활동성", "description_en": "Unspontaneous relations to examiner, lack of peer interaction, hypoactivity"},
    {"id": 15, "question_ko": "정서 표현의 둔마", "question_en": "Blunted Affect", "description_ko": "정서 표현이 부족하고, 무표정하거나 정서 반응이 평탄한 상태", "description_en": "Deficient emotional expression, blankness, flatness of affect"},
    {"id": 16, "question_ko": "긴장", "question_en": "Tension", "description_ko": "긴장감, 안절부절 못함, 손이나 발의 신경질적 움직임", "description_en": "Nervousness, fidgetiness, nervous movement of hands or feet"},
    {"id": 17, "question_ko": "불안", "question_en": "Anxiety", "description_ko": "매달리는 행동, 분리불안, 불안 주제에 대한 집착, 공포 또는 공포증", "description_en": "Clinging behavior, separation anxiety, preoccupation with anxiety topics, fears or phobias"},
    {"id": 18, "question_ko": "수면 장애", "question_en": "Sleep Difficulties", "description_ko": "잠들기 어려움, 간헐적 각성, 수면 시간 단축", "description_en": "Inability to fall asleep, intermittent awakening, shortened sleep time"},
    {"id": 19, "question_ko": "지남력 장애", "question_en": "Disorientation", "description_ko": "사람, 장소 또는 사물에 대한 혼란", "description_en": "Confusion over persons, places or things"},
    {"id": 20, "question_ko": "언어 이상", "question_en": "Speech Deviance", "description_ko": "낮은 수준의 언어 발달, 어휘 부족, 발음 오류", "description_en": "Inferior level of speech development, underdeveloped vocabulary, mispronunciations"},
    {"id": 21, "question_ko": "상동증", "question_en": "Stereotypy", "description_ko": "리드미컬하고 반복적이며 기이한 움직임 또는 자세", "description_en": "Rhythmic, repetitive, manneristic movements or posture"}
]


bprs_c_21_choices = [
    {"score": 0, "label_en": "Not Present", "label_ko": "없음"},
    {"score": 1, "label_en": "Very Mild", "label_ko": "매우 경미"},
    {"score": 2, "label_en": "Mild", "label_ko": "경미"},
    {"score": 3, "label_en": "Moderate", "label_ko": "중간"},
    {"score": 4, "label_en": "Moderate/Severe", "label_ko": "중등도/중증"},
    {"score": 5, "label_en": "Severe", "label_ko": "중증"},
    {"score": 6, "label_en": "Extremely Severe", "label_ko": "극심"}
]

bprs_c_mapping = {
 {
    1: {
        0: "Not Present – Cooperative, pleasant.",
        1: "Very Mild",
        2: "Mild – Occasionally refuses to comply with rules and expectations, in only one situation or setting.",
        3: "Moderate",
        4: "Moderate/Severe – Persistent failure to comply with rules/expectations in more than one setting.",
        5: "Severe",
        6: "Extremely Severe – Constantly refuses to comply with rules and expectations, delinquent behaviors, running away. Causes severe impairment in functioning in most situations/settings."
    },
    2: {
        0: "Not Present – Cooperative, pleasant.",
        1: "Very Mild",
        2: "Mild – Occasionally sarcastic, loud, guarded, quarrelsome. Causes mild dysfunction in one situation or setting.",
        3: "Moderate",
        4: "Moderate/Severe – Causes frequent impairment in several situations/settings.",
        5: "Severe",
        6: "Extremely Severe – Assaultive, destructive. Causes severe impairment in functioning in most situations/settings."
    },
    3: {
        0: "Not Present – Not at all.",
        1: "Very Mild",
        2: "Mild – Occasionally gets in trouble for lying, may cheat on occasions.",
        3: "Moderate",
        4: "Moderate/Severe – Frequently lies/cons/manipulates people he knows. Causes frequent impairment in functioning in several situations/settings.",
        5: "Severe",
        6: "Extremely Severe – Constantly relates to others in an exploitive/manipulative manner, cons strangers out of money/situations. Causes severe impairment in functioning in most situations/settings."
    },

    4: {
        0: "Not Present – Occasionally/quickly disappears.",
        1: "Very Mild",
        2: "Mild – Sustained periods/excessive for event.",
        3: "Moderate",
        4: "Moderate/Severe – Unhappy most of the time/no precipitant.",
        5: "Severe",
        6: "Extremely Severe – Unhappy all the time/psychic pain. Causes severe impairment in functioning."
    },
    5: {
        0: "Not Present – Feels good/positive about self.",
        1: "Very Mild",
        2: "Mild – Occasionally feels not as good as others/deficits in one area.",
        3: "Moderate",
        4: "Moderate/Severe – Feels others are better than they are. Gives negative, bland answers, can’t think of anything good about themselves.",
        5: "Severe",
        6: "Extremely Severe – Constantly feels others are better. Feels worthless/unlovable."
    },
    6: {
        0: "Not Present – Not at all.",
        1: "Very Mild",
        2: "Mild – Thought when angry.",
        3: "Moderate",
        4: "Moderate/Severe – Recurrent thoughts of suicide/plans.",
        5: "Severe",
        6: "Extremely Severe – Attempted within last month/actively."
    },

    7: {
        0: "Not Present – Not at all.",
        1: "Very Mild",
        2: "Mild – Occasionally has elaborate fantasies, imaginary companions.",
        3: "Moderate",
        4: "Moderate/Severe – Frequently has elaborate fantasies (exclude imaginary friends). Interferes occasionally with perception of reality.",
        5: "Severe",
        6: "Extremely Severe – Often absorbed in elaborate fantasies, has a difficult time distinguishing reality from fantasy."
    },
    8: {
        0: "Not Present – No delusions or ideas of reference.",
        1: "Very Mild",
        2: "Mild – Occasionally feels strangers may be looking/talking/laughing about them.",
        3: "Moderate",
        4: "Moderate/Severe – Frequent distortion of thinking, mistrust, suspicion of others.",
        5: "Severe",
        6: "Extremely Severe – Mistrust/suspicious of everyone/thing. Can’t distinguish from reality."
    },
    9: {
        0: "Not Present – No visual, auditory, sensory experiences.",
        1: "Very Mild",
        2: "Mild – Hears name called, experiences after an event, active/vivid imagination.",
        3: "Moderate",
        4: "Moderate/Severe – Definite experienced auditory (voices), visual (daytime or several incidences), sensory (specific orders).",
        5: "Severe",
        6: "Extremely Severe – Constantly experiences auditory (commanding voices), visual (images present during interview), or other experiences or perceptions."
    },

    10: {
        0: "Not Present – Slight restlessness, fidgeting. No impact on functioning.",
        1: "Very Mild",
        2: "Mild – Occasional restlessness, fidgeting, frequent changes of posture. Noticeable, but does not cause impairment in functioning.",
        3: "Moderate",
        4: "Moderate/Severe – Excessive energy, movement, cannot stay still or seated. Causes dysfunction on numerous occasions/situations. Seeks help for behaviors.",
        5: "Severe",
        6: "Extremely Severe – Continuous motor excitement, cannot be stilled. Causes major interference in functioning on most occasions/situations."
    },
    11: {
        0: "Not Present – Performance consistent with ability.",
        1: "Very Mild",
        2: "Mild – Occasionally daydreams, easily distracted. Is able to focus with prompting.",
        3: "Moderate",
        4: "Moderate/Severe – Frequently has trouble concentrating, avoids mental tasks, disruptive. Needs frequent assistance to stay focused. Causes decreased performance.",
        5: "Severe",
        6: "Extremely Severe – Constant; needs 1 to 1 assistance to stay focused."
    },
    12: {
        0: "Not Present – Not at all.",
        1: "Very Mild",
        2: "Mild – Noticeably more verbose than normal, conversation is not strained.",
        3: "Moderate",
        4: "Moderate/Severe – Very verbose or rapid, making conversation strained or difficult to maintain.",
        5: "Severe",
        6: "Extremely Severe – Talks rapidly, continuously, and cannot be interrupted. Conversation is extremely difficult or impossible."
    },

    13: {
        0: "Not Present – Not at all.",
        1: "Very Mild",
        2: "Mild – Occasionally conveys little information because of minimal speech, vague, sparse, low or weak voice.",
        3: "Moderate",
        4: "Moderate/Severe – Persistently the client is vague, low or weak voice, in which at least ¼–½ of the conversation comprehension is impaired.",
        5: "Severe",
        6: "Extremely Severe – On numerous occasions/situations conversation is severely impaired."
    },
    14: {
        0: "Not Present – Not at all.",
        1: "Very Mild",
        2: "Mild – Occasionally is unresponsive, sometimes refuses peer interaction.",
        3: "Moderate",
        4: "Moderate/Severe – Frequently unresponsive, lacks peer interaction, hypoactive. Interferes with relationships.",
        5: "Severe",
        6: "Extremely Severe – Constantly oblivious to those around. Preoccupied facial expressions, does not respond to questions or look at interviewer."
    },
    15: {
        0: "Not Present – Not at all.",
        1: "Very Mild",
        2: "Mild – Some flattening of affect. Occasionally shows emotional response during interview (smiles, laughs, tearful).",
        3: "Moderate",
        4: "Moderate/Severe – Considerable flattening. Frequently the client does not show emotional response (does not smile, laugh, look, cry).",
        5: "Severe",
        6: "Extremely Severe – Constantly flat. The client does not show emotional response (does not smile, laugh, look, cry)."
    },

    16: {
        0: "Not Present – Not at all.",
        1: "Very Mild",
        2: "Mild – Occasionally feels nervous or fidgets. Can be relaxed or reassured.",
        3: "Moderate",
        4: "Moderate/Severe – Most days/time feels nervous/fidgety. Causes mental or physical distress.",
        5: "Severe",
        6: "Extremely Severe – Pervasive and extreme nervousness, fidgeting, nervous movements of hands or feet."
    },
    17: {
        0: "Not Present – Not at all.",
        1: "Very Mild",
        2: "Mild – Occasionally worries (at least 3 times a week) about anticipated/current events, separation, fears or phobias. These worries appear excessive for situation.",
        3: "Moderate",
        4: "Moderate/Severe – Most days/time worries about at least 2 life circumstances, or anticipated/current events.",
        5: "Severe",
        6: "Extremely Severe – Pervasive and extreme worry about most everything, real or imagined."
    },
    18: {
        0: "Not Present – Not at all.",
        1: "Very Mild",
        2: "Mild – Some difficulty (at least 1 hour initial, no middle or terminal insomnia).",
        3: "Moderate",
        4: "Moderate/Severe – Definitely has difficulty (at least 2 hours initial insomnia, any middle, or terminal lasting up to half an hour). Feelings of unrestorative sleep, evidence of mild circadian reversal.",
        5: "Severe",
        6: "Extremely Severe – Claims to never sleep, feels exhausted the rest of day, or severe circadian reversal."
    },
    19: {
        0: "Not Present – Not at all.",
        1: "Very Mild",
        2: "Mild – Occasionally appears confused or puzzled. Easily reacquainted with surroundings when prompted.",
        3: "Moderate",
        4: "Moderate/Severe – Frequently appears puzzled, confused, baffled regarding familiar surroundings, people, or things.",
        5: "Severe",
        6: "Extremely Severe – Constantly confused. Perplexed."
    },
    20: {
        0: "Not Present – Not at all.",
        1: "Very Mild",
        2: "Mild – Occasional instances of distorted or idiosyncratic speech. Little impairment of understandability.",
        3: "Moderate",
        4: "Moderate/Severe – Frequent instances with definite impairment in understandability.",
        5: "Severe",
        6: "Extremely Severe – Constant speech distortion, almost incomprehensible."
    },
    21: {
        0: "Not Present – Not at all.",
        1: "Very Mild",
        2: "Mild – Occasionally displays rhythmic, repetitive, manneristic movements or posture.",
        3: "Moderate",
        4: "Moderate/Severe – Frequent rhythmic, repetitive, manneristic movements or posture.",
        5: "Severe",
        6: "Extremely Severe – Most of the time (>50%) displays rhythmic, repetitive, manneristic movement or posture."
    }
}

}


# Streamlit 앱 시작
st.set_page_config(page_title="BPRS-C-21 평가", layout="wide")

st.title("🧠 BPRS-C-21 평가도구")
st.markdown("21개 항목에 대해 현재 상태에 가장 적합한 수준을 선택해 주세요.")

if "responses" not in st.session_state:
    st.session_state.responses = [0] * 21

# 사용자 응답 수집
for i, item in enumerate(bprs_c_21_items):
    st.subheader(f"{item['id']}. {item['question_ko']}")
    st.caption(item['description_ko'])

    options = [f"{c['score']}: {c['label_ko']}" for c in bprs_c_21_choices]
    default_index = st.session_state.responses[i]
    selection = st.selectbox("점수를 선택하세요", options, index=default_index, key=f"q_{i}")
    score = int(selection.split(":")[0])
    st.session_state.responses[i] = score

# 결과 출력
if st.button("결과 보기"):
    total_score = sum(st.session_state.responses)

    symptom_clusters = {
        "Behavior Problems (Items 1-3)": [0, 1, 2],
        "Depression (Items 4-6)": [3, 4, 5],
        "Thinking Disturbance (Items 7-9)": [6, 7, 8],
        "Psychomotor Excitation (Items 10-12)": [9, 10, 11],
        "Withdrawal (Items 13-15)": [12, 13, 14],
        "Anxiety (Items 16-18)": [15, 16, 17],
        "Organicity (Items 19-21)": [18, 19, 20]
    }

    cluster_scores = {name: sum([st.session_state.responses[i] for i in indices]) for name, indices in symptom_clusters.items()}

    result_lines = []
    for i, item in enumerate(bprs_c_21_items):
        score = st.session_state.responses[i]
        label_en = next(c['label_en'] for c in bprs_c_21_choices if c['score'] == score)
        desc_en = bprs_c_mapping[item['id']][score]
        result_lines.append(f"{item['id']}. {item['question_en']} – {item['description_en']}\n    ({score}) {label_en} – {desc_en}")

    result_lines.append(f"\nTotal Score: {total_score}")
    result_lines.append("\nSymptom Group scores")
    for name, value in cluster_scores.items():
        result_lines.append(f"{name}: {value}")

    result_text = "\n\n".join(result_lines)
    st.code(result_text)
    st.download_button("📋 결과 복사 (텍스트 파일)", result_text, file_name="bprs_c_21_result.txt")
