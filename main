import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="파리 감성 지도", layout="wide")

st.title("🗺️ 파리 감성 명소 & 쇼핑 안내")
st.markdown("숙소, 명소, 쇼핑, 약국 등 위치를 설명과 함께 확인하고, 구글맵 링크도 클릭해보세요!")

places = [
    # 숙소
    {"이름": "첫 번째 숙소 (Rue des Écoles)", "분류": "숙소", "위도": 48.8485, "경도": 2.3499,
     "설명": "라탱 지구에 위치한 감성 숙소. 셰익스피어 앤 컴퍼니, 생트 샤펠과 가까움.",
     "이미지": "https://tse2.mm.bing.net/th/id/OIP.ZmWFriGpyMVAPOlZPD1VNwHaEK?pid=Api",
     "링크": "https://maps.google.com/?q=44 Rue des Écoles, Paris"},

    {"이름": "두 번째 숙소 (Rue Barbet de Jouy)", "분류": "숙소", "위도": 48.8517, "경도": 2.3168,
     "설명": "고급스러운 7구 인발리드 지구. 르클레르 거리, 생제르맹 근처.",
     "이미지": "https://tse1.mm.bing.net/th/id/OIP.oxfQe59zFE06R7m6fCVBRQHaE8?pid=Api",
     "링크": "https://maps.google.com/?q=21 Rue Barbet de Jouy, Paris"},

    # 명소
    {"이름": "루브르 박물관", "분류": "명소", "위도": 48.8606, "경도": 2.3376,
     "설명": "세계 최대 미술관 중 하나. 모나리자가 여기 있어요.",
     "이미지": "https://tse1.mm.bing.net/th/id/OIP.Dnw24KjSigEu6SJ7KcAb0wHaEK&pid=Api",
     "링크": "https://maps.google.com/?q=Louvre Museum Paris"},

    {"이름": "오르세 미술관", "분류": "명소", "위도": 48.8600, "경도": 2.3266,
     "설명": "인상파 화가들의 천국. 모네, 반 고흐, 드가 작품 감상 가능.",
     "이미지": "https://tse2.mm.bing.net/th?id=OIP.jcYRnwXqdGRp5Wy9_520cQHaE8&pid=Api",
     "링크": "https://maps.google.com/?q=Musée d'Orsay Paris"},

    {"이름": "몽마르뜨 언덕", "분류": "명소", "위도": 48.8867, "경도": 2.3431,
     "설명": "파리 예술가들의 거리와 사크레쾨르 대성당이 있는 언덕.",
     "이미지": "https://tse2.mm.bing.net/th/id/OIP.toNVdv6dL5L-1XiVggbPLQHaFj?pid=Api",
     "링크": "https://maps.google.com/?q=Montmartre Paris"},

    {"이름": "에펠탑", "분류": "명소", "위도": 48.8584, "경도": 2.2945,
     "설명": "말이 필요 없는 파리의 상징.",
     "이미지": "https://tse2.mm.bing.net/th?id=OIP.jcYRnwXqdGRp5Wy9_520cQHaE8&pid=Api",
     "링크": "https://maps.google.com/?q=Eiffel Tower Paris"},

    {"이름": "뤽상부르 공원", "분류": "명소", "위도": 48.8462, "경도": 2.3372,
     "설명": "벤치에 앉아 파리지앵처럼 책 읽기 좋은 조용한 정원.",
     "이미지": "https://tse1.mm.bing.net/th/id/OIP.muH2VW1Rvyz68nwJN3bJogHaE7?pid=Api",
     "링크": "https://maps.google.com/?q=Luxembourg Gardens Paris"},

    # 쇼핑 & 약국
    {"이름": "La Vallée Village 아울렛", "분류": "쇼핑", "위도": 48.8386, "경도": 2.7806,
     "설명": "명품을 저렴하게 살 수 있는 파리 근교 아울렛.",
     "이미지": "https://www.thebicestercollection.com/la-vallee-village/en/~/media/images/lvv/hero/2023/09/06/14/19/lvv-hero-desktop-1.jpg",
     "링크": "https://maps.google.com/?q=La Vallée Village"},

    {"이름": "Citypharma", "분류": "약국", "위도": 48.8525, "경도": 2.3328,
     "설명": "파리에서 가장 유명한 약국. 프랑스 약국 화장품 싸게 삼.",
     "이미지": "https://www.sortiraparis.com/images/80/66185/1329512-citypharma.jpg",
     "링크": "https://maps.google.com/?q=Citypharma Paris"},
]

# 선택 필터
분류옵션 = st.multiselect("🔍 보고 싶은 분류 선택:", options=list(set(p["분류"] for p in places)), default=["숙소", "명소", "쇼핑", "약국"])

# 필터된 데이터프레임 만들기
df = pd.DataFrame([p for p in places if p["분류"] in 분류옵션])

# 지도 시각화
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/streets-v12",
    initial_view_state=pdk.ViewState(latitude=48.8566, longitude=2.3522, zoom=12),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[경도, 위도]',
            get_fill_color='[180, 0, 200, 160]',
            get_radius=120,
            pickable=True
        )
    ],
    tooltip={"text": "{이름}\n{설명}"}
))

# 상세 정보 카드
st.markdown("## 📍 장소 상세 정보")
for _, row in df.iterrows():
    with st.container():
        st.image(row["이미지"], width=500)
        st.subheader(row["이름"])
        st.write(f"**분류:** {row['분류']}")
        st.write(row["설명"])
        st.markdown(f"[📍 구글맵으로 열기]({row['링크']})")
        st.markdown("---")
