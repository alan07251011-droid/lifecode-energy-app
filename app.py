# -*- coding: utf-8 -*-
"""
綠藝國際學苑 ╳ 老臣聊心室
生命密碼能量調頻 App - 先天本質與思維盲點深度解析
"""
import streamlit as st
from datetime import datetime, date

# 1. 頁面基本配置（必須是第一個 Streamlit 指令）
st.set_page_config(
    page_title="探索你與生俱來的先天本質與盲點｜老臣聊心室",
    page_icon="🌿",
    layout="centered"
)

# 2. 自訂森林系療癒 CSS
st.markdown("""
<style>
    .stApp {
        background-color: #F7F4EE;
        color: #2C3E2E;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans TC", sans-serif;
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #2D4F38 0%, #3D6A4E 60%, #5B886B 100%);
        color: #FFFFFF;
        border-radius: 16px;
        padding: 2rem 1.5rem;
        text-align: center;
        margin-bottom: 1.2rem;
        box-shadow: 0 6px 20px rgba(45, 79, 56, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.15);
    }
    
    .stButton>button {
        background-color: #2D4F38;
        color: white !important;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-weight: bold;
        width: 100%;
        border: none;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        cursor: pointer;
        transition: all 0.2s ease;
    }
    .stButton>button:hover, .stButton>button:active {
        background-color: #1E3525 !important;
        color: #E8E3D9 !important;
    }
    
    .card {
        background-color: #FFFFFF;
        padding: 1.4rem;
        border-radius: 14px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.05);
        margin-bottom: 1.2rem;
        border-left: 5px solid #2D4F38;
        border-top: 1px solid #E6ECE8;
        border-right: 1px solid #E6ECE8;
        border-bottom: 1px solid #E6ECE8;
    }
    .badge {
        background-color: #E2ECE5;
        color: #2D4F38;
        padding: 4px 14px;
        border-radius: 16px;
        font-weight: bold;
        font-size: 0.9rem;
        display: inline-block;
        margin-bottom: 8px;
    }

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
        padding: 0.65rem 1rem !important;
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        cursor: pointer !important;
        text-decoration: none !important;
    }
    .stLinkButton > a:hover, .stLinkButton > a:active {
        background-color: #1E3525 !important;
        color: #E8E3D9 !important;
        border-color: #1E3525 !important;
    }
</style>
""", unsafe_allow_html=True)

# 官方 LINE 原生 URL
LINE_OFFICIAL_URL = "https://line.me/R/ti/p/@mir4855b"

def calculate_ming_gong(year, gender):
    """
    計算九星命宮守護星、先天特質、思維盲點與調頻綠植
    """
    try:
        y_int = int(year)
        digits_sum = sum(int(d) for d in str(y_int))
        while digits_sum > 9:
            digits_sum = sum(int(d) for d in str(digits_sum))
        
        if "男" in str(gender):
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
    except Exception:
        return {
            "title": "命宮守護星・調和能量",
            "trait": "具備深層感知力與自我覺察潛能，順應自然節奏蓄積能量。",
            "blind": "容易受外界雜音干擾，宜時常回歸內在清明。",
            "plant": "圓葉椒草、虎尾蘭、開運竹",
            "pos": "書房或辦公桌明亮處",
            "prompt": "今天你最想給自己的一句溫柔話語是什麼？寫下三個字詞。"
        }

# 頂部視覺橫幅
st.markdown("""
<div class="hero-banner">
    <div style="font-size: 2.2rem; margin-bottom: 8px;">🌿</div>
    <h1 style="font-size: 1.55rem; font-weight: bold; letter-spacing: 1px; color: #F5DF9E; margin: 0 0 0.5rem 0;">
        探索你與生俱來的先天本質與盲點
    </h1>
    <p style="font-size: 0.92rem; color: #E8F5ED; margin: 0; line-height: 1.6;">
        綠藝國際學苑 ╳ 老臣聊心室 ╳ 生命密碼能量調頻
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
> 「八字與數字只是指引天賦與盲點的『地圖』，而非限制生命的『框架』。真正的智慧在於調和能量與修煉心性。」
""")

# 表單容器
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("如何稱呼您？", placeholder="例如：Alan 或 小晴")
    with col2:
        gender = st.selectbox("性別", ["女 (坤命)", "男 (乾命)"])
    
    # 支援 date 物件與安全預設值
    birth_date = st.date_input(
        "西元出生年月日",
        min_value=date(1940, 1, 1),
        max_value=date(2026, 12, 31),
        value=date(1990, 1, 1)
    )

# 判斷使用者是否點擊按鈕或已觸發計算
if "calculated" not in st.session_state:
    st.session_state.calculated = False

submit_btn = st.button("✨ 立即解鎖我的天賦地圖")
if submit_btn:
    st.session_state.calculated = True

if st.session_state.calculated:
    # 提取年份
    if isinstance(birth_date, (list, tuple)):
        chosen_date = birth_date[0] if len(birth_date) > 0 else date(1990, 1, 1)
    else:
        chosen_date = birth_date or date(1990, 1, 1)
    
    res = calculate_ming_gong(chosen_date.year, gender)
    display_name = name.strip() if name and name.strip() else "朋友"
    
    st.markdown("---")
    st.markdown(f"### 💌 嗨，{display_name}！這是老臣為你解讀的原廠天性：")
    
    st.markdown(f"""
    <div class="card">
        <span class="badge">命宮守護星</span>
        <h3 style="color:#2D4F38; margin:0 0 8px 0;">{res['title']}</h3>
        <p style="margin: 6px 0;"><b>🌟 天賦（天性本質）：</b>{res['trait']}</p>
        <p style="margin: 6px 0; color:#8C4A32;"><b>⚠️ 思維盲點：</b>{res['blind']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card">
        <span class="badge">自然綠植調頻</span>
        <h4 style="margin:0 0 6px 0; color:#2D4F38;">🌿 專屬自然綠植：{res['plant']}</h4>
        <p style="margin: 6px 0;"><b>🧭 居家/辦公能量方位：</b>建議擺放於 <b>{res['pos']}</b></p>
        <p style="font-size:0.9rem; color:#555; margin: 4px 0 0 0;">透過每天的觀照與觸摸植物的「指尖定力」，讓大自然的穩定頻率安撫大腦的雜訊。</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card">
        <span class="badge">今日靜心書寫練習</span>
        <p style="margin: 6px 0;"><b>📝 引導提問：</b>「{res['prompt']}」</p>
        <p style="font-size:0.85rem; color:#777; margin: 4px 0 0 0;">拿出筆記本，花 5 分鐘寫下來。書寫是思緒的垃圾桶，倒空了，光才能照進來。</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 底部心靈共振與行動呼籲模組
    st.markdown("""
    <div style="margin-top: 3rem; padding: 2rem 1.5rem; background-color: rgba(35, 71, 50, 0.95); border-radius: 18px; border: 1px solid rgba(16, 185, 129, 0.25); color: #F5F5F4; box-shadow: 0 12px 28px -6px rgba(0, 0, 0, 0.25); max-width: 680px; margin-left: auto; margin-right: auto; text-align: center;">
      <div style="margin-bottom: 1.5rem;">
        <div style="font-size: 1.75rem; margin-bottom: 0.35rem;">🌱</div>
        <h3 style="font-size: 1.25rem; font-weight: bold; color: #FDE68A; letter-spacing: 0.5px; margin: 0 0 0.6rem 0; line-height: 1.4;">
          受過傷的地方，細心灌溉，依然能長出翠綠的風景
        </h3>
        <p style="font-size: 0.95rem; color: rgba(209, 250, 229, 0.9); line-height: 1.65; font-weight: 300; margin: 0;">
          在這個快節奏的時代，拼命追趕世界太累了。<br>
          如果今天的生命密碼指引曾為你帶來一絲安頓，請記得：今天，先溫柔地接住你自己。
        </p>
      </div>

      <div style="width: 70px; height: 1px; background: rgba(52, 211, 153, 0.4); margin: 1.5rem auto;"></div>

      <div style="background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(52, 211, 153, 0.2); border-radius: 14px; padding: 1.25rem; margin-bottom: 1.5rem; text-align: left; display: flex; flex-direction: column; gap: 0.85rem;">
        <div style="display: flex; align-items: flex-start; gap: 0.85rem;">
          <div style="width: 48px; height: 48px; border-radius: 50%; background: #132E1E; border: 1px solid rgba(253, 230, 138, 0.5); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; flex-shrink: 0; margin-top: 2px;">
            🌿
          </div>
          <div>
            <div style="display: flex; align-items: center; gap: 0.6rem; flex-wrap: wrap; margin-bottom: 0.35rem;">
              <span style="font-size: 1.05rem; font-weight: bold; color: #FDE68A;">陳信忠（老臣 / Alan）</span>
              <span style="font-size: 0.75rem; padding: 2px 10px; border-radius: 9999px; background: rgba(6, 78, 59, 0.85); color: #A7F3D0; border: 1px solid rgba(5, 150, 105, 0.4); font-weight: 500;">心靈陪伴者</span>
            </div>
            <p style="font-size: 0.88rem; color: rgba(231, 229, 228, 0.95); line-height: 1.65; font-weight: 300; margin: 0;">
              綠藝國際學苑創辦人。於觀音成道日出生，幼年深結佛緣，長期研討宗教信仰與生命密碼；曾任科技企業工程主管與國際園藝治療師，走過生死無常與至親病榻感悟，深信修行在日常柴米油鹽中，以觀音慈悲心法結合理性邏輯與自然調頻，陪你找回靈魂的原廠設定。
            </p>
          </div>
        </div>
      </div>

      <a href="https://line.me/R/ti/p/@mir4855b" target="_blank" style="display: block; text-decoration: none; padding: 1.15rem 1rem; border-radius: 14px; background: rgba(6, 95, 70, 0.6); border: 1px solid rgba(52, 211, 153, 0.35); margin-bottom: 1.5rem; transition: background 0.2s ease;">
        <div style="font-size: 0.82rem; font-weight: 600; color: #6EE7B7; margin-bottom: 0.3rem;">
          💬 綠藝漫活居 官方 LINE@
        </div>
        <div style="font-size: 1.05rem; font-weight: bold; color: #FFFFFF; margin-bottom: 0.35rem; line-height: 1.4;">
          點此進入心靈導航站｜領取免費測算・預約諮詢・探索新書作品
        </div>
        <div style="font-size: 0.82rem; color: rgba(214, 211, 209, 0.9); font-weight: 300;">
          加入後輸入對應關鍵字即可取得你所需要的資訊
        </div>
      </a>

      <div style="padding-top: 0.75rem; border-top: 1px solid rgba(16, 185, 129, 0.25);">
        <p style="font-size: 0.85rem; color: rgba(209, 250, 229, 0.85); line-height: 1.6; font-weight: 300; margin: 0 0 0.85rem 0;">
          這款免費靈籤與心靈工具由老臣持續自主研發與維運。<br>
          若這份陪伴對你有所啟發，歡迎隨緣贊助，護持更多心靈工具持續誕生。
        </p>
        <a href="https://line.me/R/ti/p/@mir4855b" target="_blank" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.6rem 1.4rem; border-radius: 9999px; background: rgba(253, 230, 138, 0.12); color: #FDE68A; border: 1px solid rgba(253, 230, 138, 0.4); font-size: 0.85rem; font-weight: 500; text-decoration: none; transition: background 0.2s ease;">
          <span>☕</span> 隨喜支持・前往 LINE@ 輸入「3」贊助老臣持續研發
        </a>
      </div>
    </div>
    """, unsafe_allow_html=True)

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
st.caption("綠藝國際學苑 ╳ 老臣聊心室 LUYILIFE © 2026 ｜ 聽你的心，陪你調頻 ｜ 設計者：陳信忠 (老臣/Alan)")
