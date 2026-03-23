import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="타로 마스터 v1.4", layout="centered")

# 2. 타로 카드 데이터 (내용 동일)
tarot_data = [
    {"no": "0", "name": "The Fool (광대)", "keywords": ["자유", "모험", "순수", "시작"], "desc": "아무것도 가진 것 없지만 어디든 갈 수 있는 여행자", "img": "https://upload.wikimedia.org/wikipedia/commons/9/90/RWS_Tarot_00_Fool.jpg"},
    {"no": "1", "name": "The Magician (마법사)", "keywords": ["창조", "능력", "자신감", "잠재력"], "desc": "무엇이든 만들어낼 수 있는 준비된 능력자", "img": "https://upload.wikimedia.org/wikipedia/commons/d/de/RWS_Tarot_01_Magician.jpg"},
    {"no": "2", "name": "The High Priestess (고위 여사제)", "keywords": ["직관", "지혜", "신비", "무의식"], "desc": "침묵 속에서 깊은 통찰력을 가진 지혜의 수호자", "img": "https://upload.wikimedia.org/wikipedia/commons/8/88/RWS_Tarot_02_High_Priestess.jpg"},
    {"no": "3", "name": "The Empress (여황제)", "keywords": ["풍요", "모성애", "번영", "자연"], "desc": "모든 것을 품어 기르는 풍요롭고 따뜻한 어머니", "img": "https://upload.wikimedia.org/wikipedia/commons/d/d2/RWS_Tarot_03_Empress.jpg"},
    {"no": "4", "name": "The Emperor (황제)", "keywords": ["권위", "질서", "지배", "책임감"], "desc": "나라를 다스리는 강력한 지도력과 체계의 상징", "img": "https://upload.wikimedia.org/wikipedia/commons/c/c3/RWS_Tarot_04_Emperor.jpg"},
    {"no": "5", "name": "The Hierophant (교황)", "keywords": ["전통", "교육", "조언", "자비"], "desc": "정신적인 인도자이자 전통과 규칙을 가르치는 스승", "img": "https://upload.wikimedia.org/wikipedia/commons/8/8d/RWS_Tarot_05_Hierophant.jpg"},
    {"no": "6", "name": "The Lovers (연인)", "keywords": ["선택", "사랑", "조화", "관계"], "desc": "마음이 맞는 파트너와의 결합과 중요한 가치관의 선택", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3a/RWS_Tarot_06_Lovers.jpg"},
    {"no": "7", "name": "The Chariot (전차)", "keywords": ["승리", "의지", "전진", "통제"], "desc": "강한 목표 의식으로 장애물을 돌파하며 나아가는 추진력", "img": "https://upload.wikimedia.org/wikipedia/commons/9/9b/RWS_Tarot_07_Chariot.jpg"},
    {"no": "8", "name": "Strength (힘)", "keywords": ["인내", "용기", "부드러움", "자제력"], "desc": "외면의 힘보다 강한 내면의 인내심으로 야성을 길들이는 힘", "img": "https://upload.wikimedia.org/wikipedia/commons/f/f5/RWS_Tarot_08_Strength.jpg"},
    {"no": "9", "name": "The Hermit (은둔자)", "keywords": ["성찰", "탐구", "고독", "진리"], "desc": "세상에서 한 발짝 물러나 내면의 빛을 찾는 구도자", "img": "https://upload.wikimedia.org/wikipedia/commons/4/4d/RWS_Tarot_09_Hermit.jpg"},
    {"no": "10", "name": "Wheel of Fortune (운명의 수레바퀴)", "keywords": ["변화", "행운", "윤회", "전환점"], "desc": "거스를 수 없는 운명의 흐름과 새로운 기회의 시작", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3c/RWS_Tarot_10_Wheel_of_Fortune.jpg"},
    {"no": "11", "name": "Justice (정의)", "keywords": ["균형", "공정", "결단", "인과응보"], "desc": "감정에 치우치지 않고 객관적인 사실로 판단하는 냉철함", "img": "https://upload.wikimedia.org/wikipedia/commons/e/e0/RWS_Tarot_11_Justice.jpg"},
    {"no": "12", "name": "The Hanged Man (매달린 사람)", "keywords": ["희생", "인내", "새로운 시각", "정지"], "desc": "자발적인 멈춤을 통해 세상을 거꾸로 보며 깨달음을 얻음", "img": "https://upload.wikimedia.org/wikipedia/commons/2/2b/RWS_Tarot_12_Hanged_Man.jpg"},
    {"no": "13", "name": "Death (죽음)", "keywords": ["종결", "이별", "변화", "새로운 시작"], "desc": "낡은 것을 끝내고 완전히 새로운 단계로 나아가기 위한 변화", "img": "https://upload.wikimedia.org/wikipedia/commons/d/d7/RWS_Tarot_13_Death.jpg"},
    {"no": "14", "name": "Temperance (절제)", "keywords": ["조화", "중용", "순환", "인내"], "desc": "서로 다른 두 요소를 적절히 섞어 평온을 유지하는 연금술", "img": "https://upload.wikimedia.org/wikipedia/commons/f/f8/RWS_Tarot_14_Temperance.jpg"},
    {"no": "15", "name": "The Devil (악마)", "keywords": ["속박", "유혹", "집착", "본능"], "desc": "물질적인 욕망이나 나쁜 습관에 얽매여 있는 상태", "img": "https://upload.wikimedia.org/wikipedia/commons/5/55/RWS_Tarot_15_Devil.jpg"},
    {"no": "16", "name": "The Tower (탑)", "keywords": ["붕괴", "충격", "해방", "갑작스러운 변화"], "desc": "기존의 가치관이 무너지며 겪는 시련과 그 뒤의 진실", "img": "https://upload.wikimedia.org/wikipedia/commons/5/53/RWS_Tarot_16_Tower.jpg"},
    {"no": "17", "name": "The Star (별)", "keywords": ["희망", "영감", "치유", "낙천주의"], "desc": "어둠 속에서 길을 안내하는 희망의 빛과 평화로운 마음", "img": "https://upload.wikimedia.org/wikipedia/commons/d/db/RWS_Tarot_17_Star.jpg"},
    {"no": "18", "name": "The Moon (달)", "keywords": ["불안", "혼란", "직관", "모호함"], "desc": "보이지 않는 두려움과 불확실한 상황 속의 예민한 감각", "img": "https://upload.wikimedia.org/wikipedia/commons/7/7f/RWS_Tarot_18_Moon.jpg"},
    {"no": "19", "name": "The Sun (태양)", "keywords": ["성공", "기쁨", "활기", "긍정"], "desc": "모든 것이 명확하게 밝혀지는 찬란한 성공과 어린이 같은 순수함", "img": "https://upload.wikimedia.org/wikipedia/commons/1/1b/RWS_Tarot_19_Sun.jpg"},
    {"no": "20", "name": "Judgement (심판)", "keywords": ["부활", "보상", "결과", "재생"], "desc": "과거의 행동에 대한 부름을 받고 새로운 삶으로 깨어남", "img": "https://upload.wikimedia.org/wikipedia/commons/d/dd/RWS_Tarot_20_Judgement.jpg"},
    {"no": "21", "name": "The World (세계)", "keywords": ["완성", "통합", "여행", "완벽"], "desc": "긴 여정의 마침표이자 완벽한 조화를 이룬 최고의 단계", "img": "https://upload.wikimedia.org/wikipedia/commons/f/ff/RWS_Tarot_21_World.jpg"}
]

# 3. 사이드바 메뉴
st.sidebar.title("🃏 타로 동아리")
menu = st.sidebar.radio("활동 선택", ["카드 도감 암기", "객관식 복습 퀴즈"])

# 4. 카드 도감 암기 모드
if menu == "카드 도감 암기":
    st.title("📖 메이저 카드 핵심 암기")
    
    if 'card_idx' not in st.session_state:
        st.session_state.card_idx = 0
        
    current_card = tarot_data[st.session_state.card_idx]
    
    # [수정] 이미지 중앙 정렬 및 선출력 (경고 해결 버전)
    _, col_img, _ = st.columns([1, 2, 1])
    with col_img:
        # use_column_width 대신 use_container_width 사용
        st.image(current_card['img'], use_container_width=True)
    
    # [수정] 카드 이름 박스 후출력
    st.markdown(f"""
    <div style="background-color: #f3e5f5; border: 5px solid #7b1fa2; border-radius: 20px; padding: 20px; text-align: center; margin-top: 10px;">
        <h1 style="color: #4a148c; font-size: 3.5rem; margin: 0;">{current_card['no']}</h1>
        <h2 style="color: #7b1fa2; margin-bottom: 5px;">{current_card['name']}</h2>
        <p style="font-style: italic; color: #666; margin: 0;">"{current_card['desc']}"</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 키워드 4개 배치
    st.markdown("---")
    cols = st.columns(4)
    for i, kw in enumerate(current_card['keywords']):
        cols[i].success(f"**{kw}**")
        
    # 이동 버튼
    st.write("")
    c1, c2 = st.columns(2)
    if c1.button("⬅️ 이전 카드", use_container_width=True) and st.session_state.card_idx > 0:
        st.session_state.card_idx -= 1
        st.rerun()
    if c2.button("다음 카드 ➡️", use_container_width=True) and st.session_state.card_idx < len(tarot_data) - 1:
        st.session_state.card_idx += 1
        st.rerun()

# 5. 객관식 퀴즈 모드
elif menu == "객관식 복습 퀴즈":
    st.title("🎯 키워드 맞히기 퀴즈")
    
    if 'quiz_card' not in st.session_state:
        st.session_state.quiz_card = random.choice(tarot_data)
        
    target = st.session_state.quiz_card
    st.info(f"**문제: 다음 키워드들을 가진 카드의 이름은 무엇일까요?**\n\n🔹 {', '.join(target['keywords'])}")
    
    # 퀴즈 보기 세션 고정
    if 'quiz_options' not in st.session_state:
        options = [target['name']]
        while len(options) < 4:
            wrong_opt = random.choice(tarot_data)['name']
            if wrong_opt not in options:
                options.append(wrong_opt)
        random.shuffle(options)
        st.session_state.quiz_options = options
    
    # 4지선다 버튼 배치
    cols = st.columns(2)
    for i, opt in enumerate(st.session_state.quiz_options):
        with cols[i%2]:
            if st.button(opt, key=f"quiz_opt_{i}", use_container_width=True):
                if opt == target['name']:
                    st.balloons()
                    st.success(f"정답입니다! 🎉 이 카드는 **{target['name']}**입니다.")
                    if st.button("다음 문제 풀기", use_container_width=True):
                        if 'quiz_card' in st.session_state: del st.session_state.quiz_card
                        if 'quiz_options' in st.session_state: del st.session_state.quiz_options
                        st.rerun()
                else:
                    st.error("아쉽네요! 다시 한번 확인해 보세요. 🤔")