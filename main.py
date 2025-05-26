import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="파리 감성 명소 & 쇼핑 안내", layout="wide")

st.title("🗺️ 파리 감성 명소 & 쇼핑 안내")
st.markdown("숙소 주변 명소, 쇼핑, 맛집, 약국 위치를 설명과 함께 확인하세요. 구글맵 링크도 제공됩니다.")

# 장소 데이터
places = [
    # 첫 번째 숙소 근처 (44 Rue des Écoles, 5구 라탱 지구)
    {"이름": "첫 번째 숙소 (Rue des Écoles)", "분류": "숙소", "위도": 48.8485, "경도": 2.3499,
     "설명": "라탱 지구에 위치한 감성 숙소. 셰익스피어 앤 컴퍼니, 생트 샤펠과 가까움.",
     "이미지": "https://tse2.mm.bing.net/th/id/OIP.ZmWFriGpyMVAPOlZPD1VNwHaE8?pid=Api",
     "링크": "https://maps.google.com/?q=44 Rue des Écoles, Paris"},

    {"이름": "셰익스피어 앤 컴퍼니 서점", "분류": "명소", "위도": 48.8528, "경도": 2.3470,
     "설명": "전설적인 영어 서점으로, 문학 애호가들에게 성지와 같은 곳입니다.",
     "이미지": "https://tse1.mm.bing.net/th/id/OIP.Dnw24KjSigEu6SJ7KcAb0wHaE8?pid=Api",
     "링크": "https://maps.google.com/?q=Shakespeare+and+Company+Paris"},

    {"이름": "생트 샤펠", "분류": "명소", "위도": 48.8554, "경도": 2.3450,
     "설명": "화려한 스테인드글라스로 유명한 고딕 양식의 예배당입니다.",
     "이미지": "https://tse2.mm.bing.net/th/id/OIP.jcYRnwXqdGRp5Wy9_520cQHaE8?pid=Api",
     "링크": "https://maps.google.com/?q=Sainte+Chapelle+Paris"},

    {"이름": "Guerrisol 빈티지숍", "분류": "쇼핑", "위도": 48.8530, "경도": 2.3563,
     "설명": "저렴한 가격에 다양한 빈티지 의류를 판매하는 중고 옷가게입니다.",
     "이미지": "https://tse2.mm.bing.net/th/id/OIP.toNVdv6dL5L-1XiVggbPLQHaFj?pid=Api",
     "링크": "https://maps.google.com/?q=Guerrisol+Paris"},

    {"이름": "Marché d'Aligre", "분류": "쇼핑", "위도": 48.8492, "경도": 2.3805,
     "설명": "식료품부터 빈티지 소품까지 다양한 상품을 판매하는 활기찬 플리마켓입니다.",
     "이미지": "https://tse2.mm.bing.net/th/id/OIP.t9GvxinkLDcERFdGd6AKeQHaEo?pid=Api",
     "링크": "https://maps.google.com/?q=March%C3%A9+d'Aligre+Paris"},

    {"이름": "Photo Vincent 필름카메라 샵", "분류": "쇼핑", "위도": 48.8600, "경도": 2.3380,
     "설명": "빈티지 필름 카메라를 전문으로 판매하는 카메라 샵입니다.",
     "이미지": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Paris_Camera_Store.JPG",
     "링크": "https://maps.google.com/?q=Photo+Vincent+Paris"},

    {"이름": "BO&MIE Saint-Michel", "분류": "빵/커피", "위도": 48.8530, "경도": 2.3430,
     "설명": "현대적인 감성의 베이커리로, 다양한 페이스트리와 커피를 즐길 수 있습니다.",
     "이미지": "https://cdn.tasteatlas.com/images/dishes/226153ca32f24a918a01a9a76d968aa1.jpg",
     "링크": "https://maps.google.com/?q=BO%26MIE+Saint-Michel+Paris"},

    {"이름": "Eric Kayser (8 Rue Monge)", "분류": "빵/커피", "위도": 48.8490, "경도": 2.3520,
     "설명": "유기농 재료를 사용하는 고급 베이커리로, 다양한 빵과 페이스트리를 제공합니다.",
     "이미지": "https://upload.wikimedia.org/wikipedia/commons/2/25/Eric_Kayser_-_Montparnasse%2C_Paris_7.jpg",
     "링크": "https://maps.google.com/?q=Eric+Kayser+8+Rue+Monge+Paris"},

    {"이름": "Pharmacie Monge", "분류": "약국", "위도": 48.8498, "경도": 2.3510,
     "설명": "한국인 관광객들에게 인기 있는 약국으로, 다양한 프랑스 화장품을 저렴한 가격에 구매할 수 있습니다.",
     "이미지": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKgK_d9TW9Q2CZ4pCn29i1YrrYgQ9tLxt3TQ&usqp=CAU",
     "링크": "https://maps.google.com/?q=Pharmacie+Monge+Paris"},

    # 두 번째 숙소 근처 (21 Rue Barbet de Jouy, 7구 인발리드 지구)
    {"이름": "두 번째 숙소 (Rue Barbet de Jouy)", "분류": "숙소", "위도": 48.8517, "경도": 2.3168,
     "설명": "고급스러운 7구 인발리드 지구. 르클레르 거리, 생제르맹 근처.",
     "이미지": "https://tse1.mm.bing.net/th/id/OIP.oxfQe59zFE06R7m6fCVBRQHaE8?pid=Api",
     "링크": "https://maps.google.com/?q=21 Rue Barbet de Jouy, Paris"},

    {"이름": "르 클레르 거리 (Rue Cler)", "분류": "명소", "위도": 48.8558, "경도": 2.3040,
     "설명": "현지인들이 사랑하는 식료품 거리로, 다양한 상점과 카페가 즐비합니다.",
     "이미지": "https://cdn.parisinfo.com/var/otcp/sites/images/media/1.-photos/06.-quartier/saint-germain-des-pres-%7C-les-quartiers-de-paris-%7C-paris-tourisme/183145-1-fre-FR/Saint-Germain-des-Pr%C3%A9s_%7C_les_quartiers_de_Paris_%7C_Paris_Tourisme.jpg",
     "링크": "https://maps.google.com/?q=Rue+Cler+Paris"},

    {"이름": "생제르맹 데 프레 (Saint-Germain-des-Prés)", "분류": "명소", "위도": 48.8546, "경도": 2.3335,
     "설명": "분위기 있는 카페와 부티크가 잔뜩 있는 지적인 감성의 성지입니다.",
     "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Saint_Germain_des_Pres_par_Clautin_2.jpg/1200px-Saint_Germain_des_Pres_par_Clautin_2.jpg",
     "링크": "https://maps.google.com/?q=Saint-Germain-des-Pr%C3%A9s+Paris"},

    {"이름": "Le Bon Marché", "분류": "쇼핑", "위도": 48.8519, "경도": 2.3254,
     "설명": "파리 최고급 백화점으로, 옷부터 리빙까지 다양한 상품을 취급합니다.",
     "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Le_Bon_March%C3%A9_Paris_2010_07.jpg/1200px-Le_Bon_March%C3%A9_Paris_2010_07.jpg",
     "링크": "https://maps.google.com/?q=Le+Bon+March%C3%A9+Paris"},

    {"이름": "Sézane", "분류": "쇼핑", "위도": 48.8719, "경도": 2.3473,
     "설명": "프렌치 시크 스타일의 대표 브랜드로, 고급스러우면서도 실용적인 의류를 제공합니다.",
     "이미지": "https://media.vogue.fr/photos/60d39a3a3f1a15493aafaf97/master/w_2560%2Cc_limit/s%C3%A9zane-boutique-paris.jpg",
     "링크": "https://maps.google.com/?q=S%C3%A9zane+Paris"},

    {"이름": "Café Varenne", "분류": "빵/커피", "위도": 48.8584, "경도": 2.3165,
     "설명": "아늑한 분위기의 카페로, 커피와 간단한 식사를 즐길 수 있습니다.",
     "이미지": "https://cdn.getyourguide.com/img/location/5ffeb8a1de62c.jpeg/146.jpg",
     "링크": "https://maps.google.com/?q=Caf%C3%A9+Varenne+Paris"},

    {"이름": "Notre Pâtisserie", "분류": "빵/커피", "위도": 48.8551, "경도": 2.3119,
     "설명": "수제 디저트와 페이스트리를 전문으로 하는 베이커리로, 다양한 종류의 케이크와 타르트를 제공합니다.",
     "이미지": "https://cdn.getyourguide.com/img/location/5ffeb8a1de62c.jpeg/146.jpg",
     "링크": "https://maps.google.com/?q=Notre+P%C3%A2tisserie+Paris"},

    {"이름": "Citypharma", "분류": "약국", "위도": 48.8525, "경도": 2.3328,
     "설명": "파리에서 가장 유명한 약국 중 하나로, 다양한 프랑스 스킨케어 제품을 저렴한 가격에 구매할 수 있어 관광객들에게 인기가 많습니다.",
     "이미지": "https://www.sortiraparis.com/images/80/66185/1329512-citypharma.jpg",
     "링크": "https://maps.google.com/?q=Citypharma+Paris"},
]

df = pd.DataFrame(places)

# 필터링 옵션
분류옵션 = st.multiselect("🔍 보고 싶은 분류 선택 (기본 전체 선택):",
                     options=df['분류'].unique(),
                     default=list(df['분류'].unique()))

# 숙소별 필터링 옵션 추가 (숙소 주변만 보고 싶을 때)
숙소옵션 = ["전체", "첫 번째 숙소 주변", "두 번째 숙소 주변"]
숙소선택 = st.selectbox("🏨 숙소 주변 장소만 보기 옵션:", options=숙소옵션)

if 숙소선택 == "첫 번째 숙소 주변":
    필터조건 = ((df['이름'] == "첫 번째 숙소 (Rue des Écoles)") |
             (df['설명'].str.contains("라탱|Rue des Écoles|셰익스피어|생트 샤펠|Guerrisol|Marché d'Aligre|BO&MIE|Eric Kayser|Pharmacie Monge|Photo Vincent", case=False)))
elif 숙소선택 == "두 번째 숙소 주변":
    필터조건 = ((df['이름'] == "두 번째 숙소 (Rue Barbet de Jouy)") |
             (df['설명'].str.contains("인발리드|Rue Barbet|르 클레르|생제르맹|Le Bon Marché|Sézane|Café Varenne|Notre Pâtisserie|Citypharma", case=False)))
else:
    필터조건 = pd.Series([True] * len(df))

filtered_df = df[필터조건 & df['분류'].isin(분류옵션)]

# 지도 표시
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/streets-v12",
    initial_view_state=pdk.ViewState(
        latitude=48.8566,
        longitude=2.3522,
        zoom=12,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=filtered_df,
            get_position='[경도, 위도]',
            get_fill_color='[255, 140, 0, 180]',
            get_radius=150,
            pickable=True,
            auto_highlight=True,
        ),
    ],
    tooltip={"text": "{이름}\n{설명}"}
))

# 상세 정보
st.markdown("## 📋 선택된 장소 상세 정보")
for _, row in filtered_df.iterrows():
    with st.container():
        st.image(row["이미지"], width=500)
        st.subheader(row["이름"])
        st.write(f"**분류:** {row['분류']}")
        st.write(row["설명"])
        st.markdown(f"[🔗 구글맵에서 보기]({row['링크']})")
        st.markdown("---")
