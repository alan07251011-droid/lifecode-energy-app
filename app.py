import streamlit as st
from datetime import datetime

st.set_page_config(page_title="探索你與生俱來的先天本質與盲點｜老臣聊心室", page_icon="🌿", layout="centered")

# 自訂森林系療癒 CSS
st.markdown("""
    <style>
    .main { background-color: #F7F4EE; }
    
    /* 表單計算按鈕 */
    .stButton>button {
        background-color: #2D4F38;
        color: white;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-weight: bold;
        width: 100%;
        border: none;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        cursor: pointer !important;
        pointer-events: auto !important;
    }
    .stButton>button:hover, .stButton>button:active {
        background-color: #1E3525;
        color: #E8E3D9;
    }
    
    /* 資訊卡片樣式 */
    .card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
        border-left: 5px solid #2D4F38;
    }
    .support-card {
        background-color: #F0F4F1;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px dashed #2D4F38;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    .badge {
        background-color: #E2ECE5;
        color: #2D4F38;
        padding: 4px 12px;
        border-radius: 16px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 8px;
    }

    /* 原生 st.link_button 森林系樣式美化與觸控優化 */
    .stLinkButton {
        width: 100% !important;
    }
    .stLinkButton > a {
        background-color: #2D4F38 !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        border: 1px solid #2D4F38 !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08) !important;
        transition: all 0.2s ease !important;
        text-align: center !important;
        justify-content: center !important;
        padding: 0.6rem 1rem !important;
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        cursor: pointer !important;
        pointer-events: auto !important;
        text-decoration: none !important;
    }
    .stLinkButton > a:hover, .stLinkButton > a:active {
        background-color: #1E3525 !important;
        color: #E8E3D9 !important;
        border-color: #1E3525 !important;
        transform: translateY(-1px);
    }

    /* 隱藏 Streamlit 預設選單、頁尾、頁首與工具列，並移除佔位與指針事件，防止阻擋手機點擊 */
    header[data-testid="stHeader"], header {
        display: none !important;
        height: 0 !important;
        pointer-events: none !important;
        visibility: hidden !important;
    }
    #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"], .viewerBadge_container__1QSob {
        display: none !important;
        visibility: hidden !important;
        pointer-events: none !important;
        height: 0 !important;
        width: 0 !important;
    }
    
    /* 確保所有互動元素能正常點擊 */
    a, button, input, select {
        pointer-events: auto !important;
        cursor: pointer !important;
    }
    </style>
""", unsafe_allow_html=True)

# 官方 LINE 原生 Scheme 網址
LINE_OFFICIAL_URL = "https://line.me/R/ti/p/@mir4855b"

def calculate_ming_gong(year, gender):
    digits_sum = sum(int(d) for d in str(year))
    while digits_sum > 9:
        digits_sum = sum(int(d) for d in str(digits_sum))
    
    if gender == "男 (乾命)":
        gua_num = (11 - digits_sum) % 9
        if gua_num == 0: gua_num = 9
        if gua_num == 5: gua_num = 2
    else:
        gua_num = (digits_sum + 4) % 9
        if gua_num == 0: gua_num = 9
        if gua_num == 5: gua_num = 8

    stars = {
        1: {
            "title": "坎(水)命人・貪狼星",
            "trait": "隨和型：善解人意、親和力強、直覺與洞察力極為敏銳、深思熟慮",
            "blind": "優柔寡斷、缺乏堅定原則、習慣用「拖延」面對決策而錯失良機",
            "plant": "孔雀椒草、銀葉蔓綠絨、觀音蓮",
            "pos": "正北方（伏位安定）",
            "prompt": "此時此刻，腦海中哪一件懸而未決的事情正消耗你的心力？如果允許自己先放下完美答案，你今天願意跨出的最小一步是什麼？"
        },
        2: {
            "title": "坤(土)命人・巨門星",
            "trait": "穩重型：柔順關懷、條理分明、行事周密、實事求是的實踐家與協調高手",
            "blind": "固執任性、難以妥協、容易過度依賴他人或為成全他人而委屈自己",
            "plant": "短葉虎尾蘭、心葉蔓綠絨、黃金葛",
            "pos": "西南方（伏位安定）",
            "prompt": "今天你是否又為了成全他人而委屈了自己的感受？如果把這份溫柔收回給自己，你現在最想對身體與心靈說哪句感謝？"
        },
        3: {
            "title": "震(木)命人・祿存星",
            "trait": "活躍型：機靈聰慧、充滿冒險精神與創造力、行動敏捷的開創派",
            "blind": "急躁任性、情緒起伏大、容易據理力爭引發衝突、缺乏持久耐心",
            "plant": "圓葉椒草、袖珍椰子、金錢樹",
            "pos": "正東方（伏位安定）",
            "prompt": "最近有哪件事讓你急於看到成果或想據理力爭？試著寫下：這顆種子在破土之前，需要經歷哪些安靜扎根的過程？"
        },
        4: {
            "title": "巽(木)命人・文曲星",
            "trait": "和諧型：聰明伶俐、口才極佳、擅長溝通協調、是非觀強且適應力高",
            "blind": "對金錢敏銳度較低、情緒起伏大、易受外界干擾而陷入情感或人際糾紛",
            "plant": "文竹、福祿桐、羅漢松",
            "pos": "東南方（伏位安定）",
            "prompt": "今天有哪些外在的聲音或情緒悄悄住進了你的心裡？拿起筆，將不屬於你的雜音逐一寫下並在心裡溫柔送走。"
        },
        6: {
            "title": "乾(金)命人・武曲星",
            "trait": "活力型：剛毅果斷、領導力強、品格高尚、志向遠大且不滿足於現狀",
            "blind": "固執己見、嚴肅難親近、對己對人要求過苛而容易陷入孤軍奮戰",
            "plant": "白網紋、白鶴芋、銀杏木",
            "pos": "西北方（伏位安定）",
            "prompt": "今天給自己的哪一項『必須做到』讓你喘不過氣？如果允許今天只有 70 分，你會如何放鬆緊繃的肩膀並向外求助？"
        },
        7: {
            "title": "兌(金)命人・破軍星",
            "trait": "交際型：溫暖包容、心胸寬大、口才與表達能力一流、極具說服力",
            "blind": "易陷入「口舌之爭」、過於善辯、性格較善變且內在不易真正放鬆",
            "plant": "白紋蘭、星光燦爛黛粉葉、雪花福祿桐",
            "pos": "正西方（伏位安定）",
            "prompt": "在那些歡笑與善辯的背後，心底是否有段未曾言說的疲憊？試著在紙上對那個努力撐起場面的自己說一聲：『辛苦了』。"
        },
        8: {
            "title": "艮(土)命人・左輔星",
            "trait": "務實型：謹慎平穩、腳踏實地、實踐力極強、重承諾且有始有終",
            "blind": "過於固執嚴苛、習慣封閉內心、因過度謹慎小心而容易錯失良機",
            "plant": "陽光蔓綠絨、三爪金龍、黃金百合竹",
            "pos": "東北方（伏位安定）",
            "prompt": "此時此刻，有哪一份堅持正讓你感到疲憊？如果允許放下評判、接受外界的幫助，事情會有什麼不一樣的轉機？"
        },
        9: {
            "title": "離(火)命人・右弼星",
            "trait": "表達型：熱情洋溢、樂觀豁達、判斷力強、具備強大感染力與正義感",
            "blind": "處事稍嫌草率、情緒不穩定、心思外放忽略親近之人而容易感到孤獨",
            "plant": "彩虹千年木、紅龍草、嫣紅蔓",
            "pos": "正南方（伏位安定）",
            "prompt": "當掌聲與喧囂安靜下來時，你內心最渴望被看見的是什麼？寫下一件不需要向外界證明、你自己就很喜歡的事物。"
        }
    }
    return stars.get(gua_num, stars[1])

st.title("🌿 探索你與生俱來的先天本質與盲點")
st.caption("綠藝國際學苑 ╳ 老臣聊心室 ╳ 生命密碼能量調頻")

st.markdown("""
> 「八字與數字只是指引天賦與盲點的『地圖』，而非限制生命的『框架』。真正的智慧在於調和能量與修煉心性。」
""")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("如何稱呼您？", placeholder="例如：Alan 或 小晴")
    with col2:
        gender = st.selectbox("性別", ["女 (坤命)", "男 (乾命)"])
    
    birth_date = st.date_input("西元出生年月日", min_value=datetime(1940, 1, 1), max_value=datetime(2026, 12, 31), value=datetime(1990, 1, 1))

if st.button("✨ 立即解鎖我的天賦地圖"):
    res = calculate_ming_gong(birth_date.year, gender)
    
    st.markdown("---")
    st.markdown(f"### 💌 嗨，{name if name else '朋友'}！這是老臣為你解讀的原廠天性：")
    
    st.markdown(f"""
    <div class="card">
        <span class="badge">命宮守護星</span>
        <h3 style="color:#2D4F38; margin:0;">{res['title']}</h3>
        <p style="margin-top:10px;"><b>🌟 天賦（天性本質）：</b>{res['trait']}</p>
        <p style="margin-top:5px; color:#8C4A32;"><b>⚠️ 思維盲點：</b>{res['blind']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card">
        <span class="badge">自然綠植調頻</span>
        <h4 style="margin:0; color:#2D4F38;">🌿 專屬自然綠植：{res['plant']}</h4>
        <p style="margin-top:8px;"><b>🧭 居家/辦公能量方位：</b>建議擺放於 <b>{res['pos']}</b></p>
        <p style="font-size:0.9rem; color:#555;">透過每天的觀照與觸摸植物的「指尖定力」，讓大自然的穩定頻率安撫大腦的雜訊。</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card">
        <span class="badge">今日靜心書寫練習</span>
        <p><b>📝 引導提問：</b>「{res['prompt']}」</p>
        <p style="font-size:0.85rem; color:#777;">拿出筆記本，花 5 分鐘寫下來。書寫是思緒的垃圾桶，倒空了，光才能照進來。</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="support-card">
        <h4 style="color:#2D4F38; margin-top:0;">🌱 一份來自心靈的共鳴與支持</h4>
        <p style="color:#444; font-size:0.95rem; line-height:1.6; margin-bottom:12px;">
            如果這份小小的測算工具，曾為此刻的你帶來一點清晰與安頓，<br>
            歡迎前往<b>官方 LINE</b>留下你的感受與好評，讓老臣知道這份陪伴傳遞到了你心裡。<br><br>
            若你認同這份理念，也歡迎<b>隨緣贊助支持</b>，陪伴老臣持續灌溉、開發更多有益於大眾的心靈陪伴工具！
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.link_button("💬 前往官方 LINE 留下好評", LINE_OFFICIAL_URL, use_container_width=True)
    with col_s2:
        st.link_button("☕ 隨緣贊助支持老臣開發", LINE_OFFICIAL_URL, use_container_width=True)

    st.markdown("---")
    st.markdown("### 🧭 渴望更完整的生命地圖與深度陪伴？")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        #### 方案一：【靈魂初見】生命密碼核心特質簡析（體驗版）
        * **適合對象：** 初次接觸、想快速了解核心天賦，或想知道自己為什麼常常內耗的你。
        * **我想對你說：** 這是一場你與內在靈魂的第一次正式見面，我會引導你撥開迷霧，看看自己最真實的本質色調。
        
        **✨ 三大核心簡析：**
        * **命宮守護星（天賦與盲點）：** 找到靈魂主角，看見默默守護你的穩定力量。
        * **內外在特質（性格優缺點）：** 看懂外在展現的堅強，也溫柔擁抱內心深處的柔軟。
        * **內在格局（社會定位）：** 讀懂與世界相處的節奏，找到最自在、不委屈的位置。
        """)
        st.link_button("👉 預約【靈魂初見】體驗版", "https://vocus.cc/salon/LUYILIFE/products/luyilife02", use_container_width=True)
        
    with col_b:
        st.markdown("""
        #### 方案二：【人生導航】你的專屬生命使用手冊（完整版）
        * **適合對象：** 面對人生十字路口、職場迷惘、感情卡關、家庭和諧，或渴望得到具體調頻處方的你。
        * **我想對你說：** 這是一場全方位的生命校準大工程。除了認識設定，我更會為你開立一份結合「動、靜、時、位」的專屬能量處方。
        
        **📜 五大核心導航指南：**
        1. 🧩 **全盤性格解密** ｜ 命宮守護星 ✕ 內外性格 ✕ 格局合盤，看懂天賦與盲點，不再自己打架
        2. 🌿 **健康體質覺察** ｜ 從先天五行精準解析，提早看懂需要溫柔關注的身心部位
        3. 🚀 **職涯潛能激發** ｜ 解讀靈魂原廠設定，找到最順應天賦、不委屈自己的事業發揮舞台
        4. 🧭 **本命氣場導航** ｜ 鎖定專屬招財與文昌方位，讓你的努力與心力精準對焦
        5. 🪴 **綠植動靜處方** ｜ 整合靜心書寫與五行植物能量，打造屬於你的居家心靈森林
        """)
        st.link_button("👉 預約【人生導航】完整版", "https://vocus.cc/salon/LUYILIFE/products/luyilife03", use_container_width=True)
    
    st.markdown("---")
    st.markdown("""
    #### 🌱 【30天找回自己】深度陪跑諮詢計畫
    > 老臣親自 1 對 1 陪跑、靜心書寫引導、客製專屬綠植調頻及完整生命使用手冊、出版書籍陪伴輔助等心靈工具。（*為確保陪伴品質，採審查制，請先填寫評估問卷看是否適合由老臣來陪跑*）
    """)
    st.link_button("📝 加入官方LINE填寫 30 天陪跑評估問卷", LINE_OFFICIAL_URL, use_container_width=True)

st.markdown("---")
st.caption("綠藝國際學苑 ╳ 老臣聊心室 LUYILIFE © 2026 ｜ 聽你的心，陪你調頻｜ 設計者：陳信忠(老臣/Alan)")
