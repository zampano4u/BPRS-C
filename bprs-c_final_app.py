import streamlit as st
import streamlit.components.v1 as components
import json

# BPRS-C-21 문항 리스트
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

# BPRS-C-21 선택지 매핑 (영어 라벨 매핑)
bprs_c_21_mapping_full = {
    "1. Uncooperativeness": {
        0: {"ko": "해당 없음 – 협조적이고, 호의적입니다.", "en": "Not Present – Cooperative, pleasant."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 특정한 한 가지 상황이나 환경에서만 간헐적으로 규칙이나 기대에 따르기를 거부합니다.", "en": "Mild – Occasionally refuses to comply with rules and expectations, in only one situation or setting."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 둘 이상의 환경에서 지속적으로 규칙이나 기대에 따르지 않습니다.", "en": "Moderate/Severe – Persistent failure to comply with rules/expectations in more than one setting."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 지속적으로 규칙이나 기대에 따르기를 거부하고, 비행 행동이나 가출을 보입니다. 대부분의 상황이나 환경에서 기능에 심각한 손상을 초래합니다.", "en": "Extremely Severe – Constantly refuses to comply with rules and expectations, delinquent behaviors, running away. Causes severe impairment in functioning in most situations/settings."}
    },
    "2. Hostility": {
        0: {"ko": "해당 없음 – 협조적이고, 호의적입니다.", "en": "Not Present – Cooperative, pleasant."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 때때로 빈정거리거나, 목소리가 크고, 경계적이며, 싸우려 드는 태도를 보입니다. 하나의 상황이나 환경에서 경미한 기능 저하를 유발합니다.", "en": "Mild – Occasionally sarcastic, loud, guarded, quarrelsome. Causes mild dysfunction in one situation or setting."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 여러 상황이나 환경에서 자주 기능 손상을 초래합니다.", "en": "Moderate/Severe – Causes frequent impairment in several situations/settings."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 공격적이거나 파괴적입니다. 대부분의 상황이나 환경에서 기능에 심각한 손상을 초래합니다.", "en": "Extremely Severe – Assaultive, destructive. Causes severe impairment in functioning in most situations/settings."}
    },
    "3. Manipulativeness": {
        0: {"ko": "해당 없음 – 전혀 그렇지 않습니다.", "en": "Not Present – Not at all."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 때때로 거짓말을 하거나, 가끔 부정행위를 저지르기도 합니다.", "en": "Mild – Occasionally gets in trouble for lying, may cheat on occasions."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 자주 거짓말을 하거나, 속이거나, 아는 사람들을 조종합니다. 여러 상황이나 환경에서 자주 기능 손상을 유발합니다.", "en": "Moderate/Severe – Frequently lies/cons/manipulates people he knows. Causes frequent impairment in functioning in several situations/settings."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 지속적으로 타인과의 관계에서 착취적이거나 조종적인 방식으로 행동합니다. 낯선 사람을 속여 금전이나 상황을 이용합니다. 대부분의 상황이나 환경에서 기능에 심각한 손상을 초래합니다.", "en": "Extremely Severe – Constantly relates to others in an exploitive/manipulative manner, cons strangers out of money/situations. Causes severe impairment in functioning in most situations/settings."}
    },
    "4. Depressed Mood": {
        0: {"ko": "해당 없음 – 가끔 또는 금방 사라집니다.", "en": "Not Present – Occasionally/quickly disappears."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 지속되는 기간이 있으며, 사건에 비해 과도합니다.", "en": "Mild – Sustained periods/excessive for event."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 대부분의 시간 동안 불행하며, 명확한 유발 요인이 없습니다.", "en": "Moderate/Severe – Unhappy most of the time/no precipitant."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 항상 불행하고, 심리적 고통을 호소합니다. 기능에 심각한 손상을 초래합니다.", "en": "Extremely Severe – Unhappy all the time/psychic pain. Causes severe impairment in functioning."}
    },
    "5. Feelings of Inferiority": {
        0: {"ko": "해당 없음 – 자신에 대해 긍정적이고 좋은 감정을 가지고 있습니다.", "en": "Not Present – Feels good/positive about self."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 때때로 다른 사람보다 자신이 못하다고 느끼거나, 특정 영역에서 결핍을 느낍니다.", "en": "Mild – Occasionally feels not as good as others/deficits in one area."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 다른 사람들이 자신보다 더 낫다고 느낍니다. 부정적이고 무미건조한 응답을 하며, 자신에 대해 긍정적인 점을 떠올리지 못합니다.", "en": "Moderate/Severe – Feels others are better than they are. Gives negative, bland answers, can’t think of anything good about themselves."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 지속적으로 다른 사람들이 자신보다 낫다고 느낍니다. 자신을 무가치하거나 사랑받을 수 없는 존재라고 여깁니다.", "en": "Extremely Severe – Constantly feels others are better. Feels worthless/unlovable."}
    },
    "6. Suicidal Ideation": {
        0: {"ko": "해당 없음 – 전혀 그렇지 않습니다.", "en": "Not Present – Not at all."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 화가 났을 때 자살 생각을 한 적이 있습니다.", "en": "Mild – Thought when angry."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 자살에 대한 반복적인 생각이나 계획이 있습니다.", "en": "Moderate/Severe – Recurrent thoughts of suicide/plans."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 지난 한 달 이내에 실제로 자살을 시도했거나 현재 적극적으로 자살을 시도하려는 상태입니다.", "en": "Extremely Severe – Attempted within last month/actively."}
    },
    "7. Peculiar Fantasies": {
        0: {"ko": "해당 없음 – 전혀 그렇지 않습니다.", "en": "Not Present – Not at all."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 때때로 정교한 환상을 가지거나, 상상의 친구가 있습니다.", "en": "Mild – Occasionally has elaborate fantasies, imaginary companions."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 정교한 환상이 자주 있으며(상상의 친구는 제외), 때때로 현실 인식에 간섭을 일으킵니다.", "en": "Moderate/Severe – Frequently has elaborate fantasies (exclude imaginary friends). Interferes occasionally with perception of reality."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 정교한 환상에 자주 몰두하며, 현실과 환상을 구별하는 데 어려움을 겪습니다.", "en": "Extremely Severe – Often absorbed in elaborate fantasies, has a difficult time distinguishing reality from fantasy."}
    },
    "8. Delusions": {
        0: {"ko": "해당 없음 – 망상이나 관계 망상은 없습니다.", "en": "Not Present – No delusions or ideas of reference."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 때때로 낯선 사람들이 자신을 쳐다보거나 이야기하거나 비웃는다고 느낍니다.", "en": "Mild – Occasionally feels strangers may be looking/talking/laughing about them."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 사고의 왜곡, 타인에 대한 불신과 의심이 자주 나타납니다.", "en": "Moderate/Severe – Frequent distortion of thinking, mistrust, suspicion of others."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 모든 사람과 사물을 불신하거나 의심합니다. 현실과의 구분이 불가능합니다.", "en": "Extremely Severe – Mistrust/suspicious of everyone/thing. Can’t distinguish from reality."}
    },
    "9. Hallucinations": {
        0: {"ko": "해당 없음 – 시각, 청각, 감각적 환각이 없습니다.", "en": "Not Present – No visual, auditory, sensory experiences."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 이름을 부르는 소리를 듣거나, 사건 이후의 경험, 활발한 상상력을 보입니다.", "en": "Mild – Hears name called, experiences after an event, active/vivid imagination."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 명확하게 청각적(목소리), 시각적(낮 시간대 또는 여러 차례 발생), 감각적(특정한 냄새 등) 환각이 경험됩니다.", "en": "Moderate/Severe – Definite experienced auditory (voices), visual (daytime or several incidences), sensory (specific odors)."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 지속적으로 청각적 환각(명령하는 목소리), 시각적 환각(면담 중 나타나는 이미지), 기타 환각 또는 지각 경험이 나타납니다.", "en": "Extremely Severe – Constantly experiences auditory (commanding voices), visual (images present during interview), or other experiences or perceptions."}
    },
    "10. Hyperactivity": {
        0: {"ko": "해당 없음 – 약간의 안절부절함이나 손장난이 있으나 기능에는 영향이 없습니다.", "en": "Not Present – Slight restlessness, fidgeting. No impact on functioning."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 가끔 안절부절하거나 손장난을 하며, 자세를 자주 바꿉니다. 눈에 띄지만 기능 손상은 일으키지 않습니다.", "en": "Mild – Occasional restlessness, fidgeting, frequent changes of posture. Noticeable, but does not cause impairment in functioning."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 과도한 에너지와 움직임, 가만히 앉아 있거나 정지해 있지 못합니다. 여러 상황에서 기능 저하를 유발하며, 이러한 행동에 대해 도움을 요청합니다.", "en": "Moderate/Severe – Excessive energy, movement, cannot stay still or seated. Causes dysfunction on numerous occasions/situations. Seeks help for behaviors."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 끊임없이 움직이며, 진정시킬 수 없습니다. 대부분의 상황에서 기능에 심각한 방해를 초래합니다.", "en": "Extremely Severe – Continuous motor excitement, cannot be stilled. Causes major interference in functioning in most occasions/situations."}
    },
    "11. Distractibility": {
        0: {"ko": "해당 없음 – 수행 능력이 인지적 능력과 일치합니다.", "en": "Not Present – Performance consistent with ability."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 때때로 멍하게 있거나, 쉽게 산만해지며, 자극을 주면 집중할 수 있습니다.", "en": "Mild – Occasionally daydreams, easily distracted. Is able to focus with prompting."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 자주 집중에 어려움을 보이며, 인지적 과제를 회피하고, 방해 요소가 됩니다. 집중을 유지하기 위해 반복적인 도움이 필요하며, 수행 저하를 초래합니다.", "en": "Moderate/Severe – Frequently has trouble concentrating, avoids mental tasks, disruptive. Needs frequent assistance to stay focused. Causes decreased performance."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 지속적으로 산만하며, 1:1 집중 보조가 필요합니다.", "en": "Extremely Severe – Constant; needs 1 to 1 assistance to stay focused."}
    },
    "12. Speech or Voice Pressure": {
        0: {"ko": "해당 없음 – 전혀 그런 증상이 없습니다.", "en": "Not Present – Not at all."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 평소보다 말이 많기는 하나, 대화에 어려움을 줄 정도는 아닙니다.", "en": "Mild – Noticeably more verbose than normal, conversation is not strained."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 말이 매우 많거나 빠르며, 대화를 이어가기 어렵거나 부담스럽게 만듭니다.", "en": "Moderate/Severe – Very verbose or rapid, making conversation strained or difficult to maintain."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 말을 매우 빠르고 계속해서 하며, 중단시킬 수 없습니다. 대화가 극도로 어렵거나 불가능합니다.", "en": "Extremely Severe – Talks rapidly, continuously, and cannot be interrupted. Conversation is extremely difficult or impossible."}
    },
    "13. Underproductive Speech": {
        0: {"ko": "해당 없음 – 전혀 그렇지 않습니다.", "en": "Not Present – Not at all."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 때때로 말이 적거나, 모호하고, 드물게 이야기하며, 목소리가 낮거나 약합니다.", "en": "Mild – Occasionally conveys little information because of minimal speech, vague, sparse, low or weak voice."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 지속적으로 모호하거나 목소리가 낮고 약하여, 대화의 ¼에서 ½ 정도 이해가 어렵습니다.", "en": "Moderate/Severe – Persistently the client is vague, low or weak voice, in which at least ¼–½ of the conversation comprehension is impaired."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 여러 상황에서 대화가 심각하게 제한되며, 의사소통에 큰 지장을 줍니다.", "en": "Extremely Severe – On numerous occasions/situations conversation is severely impaired."}
    },
    "14. Emotional Withdrawal": {
        0: {"ko": "해당 없음 – 전혀 그렇지 않습니다.", "en": "Not Present – Not at all."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 때때로 반응이 없거나, 또래와의 상호작용을 거부합니다.", "en": "Mild – Occasionally is unresponsive, sometimes refuses peer interaction."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 자주 반응이 없고, 또래와의 상호작용이 부족하며, 활동성이 떨어집니다. 대인관계에 방해가 됩니다.", "en": "Moderate/Severe – Frequently unresponsive, lacks peer interaction, hypoactive. Interferes with relationships."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 주변 사람들에게 완전히 무관심하며, 표정이 몰두한 상태로 질문에 반응하지 않고 검사자를 쳐다보지 않습니다.", "en": "Extremely Severe – Constantly oblivious to those around. Preoccupied facial expressions, does not respond to questions or look at interviewer."}
    },
    "15. Blunted Affect": {
        0: {"ko": "해당 없음 – 전혀 그렇지 않습니다.", "en": "Not Present – Not at all."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 다소 정서가 평탄하지만, 면담 중 간혹 미소를 짓거나 웃거나 눈물을 흘리는 등 정서 반응이 나타납니다.", "en": "Mild – Some flattening of affect. Occasionally shows emotional response during interview (smiles, laughs, tearful)."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 뚜렷한 정서 둔마가 있으며, 자주 미소, 웃음, 응시, 울음 등의 정서 반응이 없습니다.", "en": "Moderate/Severe – Considerable flattening. Frequently the client does not show emotional response (does not smile, laugh, look, cry)."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 지속적으로 정서 표현이 없으며, 미소, 웃음, 응시, 울음 등 정서 반응이 전혀 없습니다.", "en": "Extremely Severe – Constantly flat. The client does not show emotional response (does not smile, laugh, look, cry)."}
    },
    "16. Tension": {
        0: {"ko": "해당 없음 – 전혀 그렇지 않습니다.", "en": "Not Present – Not at all."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 때때로 긴장하거나 안절부절 못합니다. 이완되거나 안심시킬 수 있습니다.", "en": "Mild – Occasionally feels nervous or fidgets. Can be relaxed or reassured."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 대부분의 날 또는 시간 동안 긴장하거나 안절부절 못하며, 심리적 또는 신체적 고통을 유발합니다.", "en": "Moderate/Severe – Most days/time feels nervous/fidgety. Causes mental or physical distress."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 광범위하고 극단적인 긴장감, 안절부절못함, 손이나 발의 신경질적 움직임이 지속적으로 나타납니다.", "en": "Extremely Severe – Pervasive and extreme nervousness, fidgeting, nervous movements of hands or feet."}
    },
    "17. Anxiety": {
        0: {"ko": "해당 없음 – 전혀 그렇지 않습니다.", "en": "Not Present – Not at all."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 예상되는 사건, 현재 상황, 분리, 공포 또는 공포증에 대해 가끔(일주일에 세 번 이상) 걱정합니다. 이러한 걱정은 상황에 비해 과도하게 보입니다.", "en": "Mild – Occasionally worries (at least 3 times a week) about anticipated/current events, separation, fears or phobias. These worries appear excessive for situation."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 대부분의 날 또는 시간 동안 두 가지 이상의 삶의 상황이나 현재/예상 사건에 대해 걱정합니다.", "en": "Moderate/Severe – Most days/time worries about at least 2 life circumstances, or anticipated/current events."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 대부분의 사안, 실제이든 상상이든, 거의 모든 것에 대해 광범위하고 극단적인 걱정을 합니다.", "en": "Extremely Severe – Pervasive and extreme worry about most everything, real or imagined."}
    },
    "18. Sleep Difficulties": {
        0: {"ko": "해당 없음 – 전혀 그렇지 않습니다.", "en": "Not Present – Not at all."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 초기 불면이 최소 1시간 이상이지만, 중간이나 말기의 불면은 없습니다.", "en": "Mild – Some difficulty (at least 1 hour initial, no middle or terminal insomnia)."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 초기 불면이 최소 2시간 이상이거나, 중간 또는 말기 불면이 30분 이내 지속됩니다. 회복되지 않은 수면 느낌, 경미한 일주기 리듬의 역전이 나타납니다.", "en": "Moderate/Severe – Definitely has difficulty (at least 2 hours initial insomnia, any middle, or terminal lasting up to half an hour). Feelings of unrestorative sleep, evidence of mild circadian reversal."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 전혀 잠을 자지 않는다고 주장하거나, 하루 종일 피곤함을 느끼며, 심한 일주기 리듬 역전이 나타납니다.", "en": "Extremely Severe – Claims to never sleep, feels exhausted the rest of day, or severe circadian reversal."}
    },
    "19. Disorientation": {
        0: {"ko": "해당 없음 – 전혀 그렇지 않습니다.", "en": "Not Present – Not at all."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 때때로 혼란스러워 보이거나 당황한 표정을 짓지만, 주변의 도움을 받으면 쉽게 다시 상황에 익숙해집니다.", "en": "Mild – Occasionally appears confused or puzzled. Easily reacquainted with surroundings when prompted."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 친숙한 사람, 장소, 사물에 대해 자주 당황하거나 혼란스러워하며, 어리둥절해 합니다.", "en": "Moderate/Severe – Frequently appears puzzled, confused, baffled regarding familiar surroundings, people, or things."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 지속적으로 혼란스러운 상태이며, 몹시 당황해 보입니다.", "en": "Extremely Severe – Constantly confused. Perplexed."}
    },
    "20. Speech Deviance": {
        0: {"ko": "해당 없음 – 전혀 그렇지 않습니다.", "en": "Not Present – Not at all."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 왜곡되거나 독특한 언어 표현이 간헐적으로 나타나며, 이해 가능성에 거의 영향을 주지 않습니다.", "en": "Mild – Occasional instances of distorted or idiosyncratic speech. Little impairment of understandability."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 이러한 언어 표현이 자주 나타나고, 이해에 뚜렷한 장애를 줍니다.", "en": "Moderate/Severe – Frequent instances with definite impairment in understandability."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 언어 왜곡이 지속적으로 나타나며, 거의 알아들을 수 없습니다.", "en": "Extremely Severe – Constant speech distortion, almost incomprehensible."}
    },
    "21. Stereotypy": {
        0: {"ko": "해당 없음 – 전혀 그렇지 않습니다.", "en": "Not Present – Not at all."},
        1: {"ko": "매우 경미함", "en": "Very Mild"},
        2: {"ko": "경미함 – 때때로 리드미컬하고 반복적이며 기이한 움직임이나 자세를 보입니다.", "en": "Mild – Occasionally displays rhythmic, repetitive, manneristic movements or posture."},
        3: {"ko": "중간 정도", "en": "Moderate"},
        4: {"ko": "중등도/심각 – 이러한 움직임이나 자세가 자주 나타납니다.", "en": "Moderate/Severe – Frequent rhythmic, repetitive, manneristic movements or posture."},
        5: {"ko": "심각", "en": "Severe"},
        6: {"ko": "매우 심각 – 대부분의 시간(50% 이상) 동안 리드미컬하고 반복적이며 기이한 움직임이나 자세를 보입니다.", "en": "Extremely Severe – Most of the time (>50%) displays rhythmic, repetitive, manneristic movement or posture."}
    }
}

# st.session_state를 이용한 초기 응답 리스트 생성
if "responses" not in st.session_state:
    st.session_state["responses"] = [0] * len(bprs_c_21_items)

# 응답 변경 시 세션 상태 업데이트 함수
def update_responses():
    for i, item in enumerate(bprs_c_21_items):
        st.session_state["responses"][i] = st.session_state[f"q_{item['id']}"]

st.title("BPRS-C-21 평가 웹앱")

# 각 문항별 드롭다운 선택 (UI: 질문과 선택지는 한국어, 선택지는 드롭다운)
for idx, item in enumerate(bprs_c_21_items):
    mapping_key = f"{item['id']}. {item['question_en']}"
    default_index = st.session_state["responses"][idx] if st.session_state["responses"][idx] is not None else 0
    st.selectbox(
        label=f"{item['id']}. {item['question_ko']} - {item['description_ko']}",
        options=list(range(7)),
        index=default_index,
        format_func=lambda x, mapping_key=mapping_key: bprs_c_21_mapping_full[mapping_key][x]["ko"],
        key=f"q_{item['id']}",
        on_change=update_responses
    )

# 결과 확인 버튼 클릭 시 결과 산출 및 출력 (출력: 영어로)
if st.button("결과 확인"):
    result_lines = ["BPRS-Child"]  # 맨 위에 "BPRS-Child" 추가
    total_score = 0
    for idx, item in enumerate(bprs_c_21_items):
        mapping_key = f"{item['id']}. {item['question_en']}"
        score = st.session_state["responses"][idx]
        total_score += score
        choice_en = bprs_c_21_mapping_full[mapping_key][score]["en"]
        result_lines.append(f"{item['id']}. {item['question_en']} – {item['description_en']}\n    ({score}) {choice_en}")
    group_names = [
        ("Behavior Problems (Items 1-3)", range(0, 3)),
        ("Depression (Items 4-6)", range(3, 6)),
        ("Thinking Disturbance (Items 7-9)", range(6, 9)),
        ("Psychomotor Excitation (Items 10-12)", range(9, 12)),
        ("Withdrawal (Items 13-15)", range(12, 15)),
        ("Anxiety (Items 16-18)", range(15, 18)),
        ("Organicity (Items 19-21)", range(18, 21))
    ]
    group_lines = []
    for group_name, indices in group_names:
        group_score = sum(st.session_state["responses"][i] for i in indices)
        group_lines.append(f"{group_name}: {group_score}")
    result_lines.append("\nTotal Score: " + str(total_score))
    result_lines.append("\nSymptom Group scores")
    result_lines.extend(group_lines)
    result_text = "\n".join(result_lines)
    
    st.code(result_text)
    
    # 클립보드 복사를 위한 HTML 버튼 (st.button을 통한 복사)
    js_result = json.dumps(result_text)
    copy_html = f"<button onclick=\"navigator.clipboard.writeText({js_result})\">Copy Result to Clipboard</button>"
    components.html(copy_html, height=50)
