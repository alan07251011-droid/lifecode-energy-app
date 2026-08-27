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
    /* 引言卡片 */
    .quote-card {
        background-color: #FFFFFF;
        border-left: 5px solid #C49A45;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
        line-height: 1.7;
        font-size: 0.95rem;
        color: #3B4B3D;
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

# --- 一、頂部品牌識別與能量調頻視覺 ---
st.markdown("""
<div style="background-color: #2D5A3F; border-radius: 16px; padding: 24px 20px; text-align: center; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); margin-bottom: 20px;">
    <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 12px;">
        <svg width="52" height="52" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0 2px 6px rgba(0,0,0,0.3));">
            <circle cx="50" cy="50" r="46" fill="#1C3826" opacity="0.6"/>
            <circle cx="50" cy="50" r="39" stroke="#F5DF9E" stroke-width="1.5" stroke-dasharray="3 3" opacity="0.6"/>
            <path d="M50 16 L54 44 L68 40 L56 50 L68 60 L54 56 L50 84 L46 56 L32 60 L44 50 L32 40 L46 44 Z" fill="#6EE7B7" opacity="0.9"/>
            <path d="M50 12 L55 50 L50 54 L45 50 Z" fill="#F5DF9E"/>
            <path d="M50 88 L55 50 L50 46 L45 50 Z" fill="#A7F3D0"/>
            <circle cx="50" cy="50" r="10" fill="#2D5A3F" stroke="#F5DF9E" stroke-width="2"/>
            <circle cx="50" cy="50" r="4" fill="#FDE68A"/>
        </svg>
    </div>
    <h1 style="font-size: 1.65rem; font-weight: bold; letter-spacing: 1.5px; color: #F5DF9E; margin: 0 0 0.5rem 0; text-shadow: 0 2px 4px rgba(0,0,0,0.15);">
        生命密碼 能量調頻
    </h1>
    <p style="font-size: 0.95rem; color: #E8F5ED; letter-spacing: 0.8px; font-weight: 300; margin: 0 0 0.8rem 0; opacity: 0.95; line-height: 1.6;">
        以先天密碼洞悉本質 ✕ 以靜心書寫對齊頻率 ✕ 以自然綠植補足能量
    </p>
    <div style="width: 100px; height: 1px; background: rgba(210, 235, 218, 0.35); margin: 0.7rem auto;"></div>
    <p style="font-size: 0.75rem; color: rgba(255, 255, 255, 0.6); letter-spacing: 1.2px; font-family: monospace, sans-serif; margin: 0; user-select: none;">
        綠藝國際學苑 ✕ 老臣聊心室 LUYILIFE ｜ 聽你的心，陪你調頻 ｜ 設計者：陳信忠 (老臣/Alan)
    </p>
</div>
""", unsafe_allow_html=True)

# 老臣心靈引言卡片
st.markdown("""
<div class="quote-card">
    <b>老臣聊心室 心靈引言：</b><br>
    『命宮星曜只是靈魂的「GPS 起點」，看懂外在元神、內在靈魂本能與社會格局的合盤交織，才是你完整的「生命地圖」。真正的調頻，在於透過靜心書寫覺察盲點、藉由綠植五行能量安頓身心，由內而外活出靈魂的原廠設定。』
</div>
""", unsafe_allow_html=True)

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

# 1. 按鈕上方引導提示
st.markdown("""
<p style="font-size: 0.88rem; color: #4B6351; margin-top: 0.9rem; margin-bottom: 0.6rem; text-align: center; line-height: 1.5;">
    ✨ 準備好探索專屬於你的靈魂原廠設定了嗎？點擊下方按鈕，老臣將為你解鎖守護星曜的天賦、思維盲點與安定能量方位。
</p>
""", unsafe_allow_html=True)

# 2. 判斷使用者是否點擊按鈕或已觸發計算
if "calculated" not in st.session_state:
    st.session_state.calculated = False

submit_btn = st.button("✨ 立即解鎖我的命宮星曜")
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
    # 3. 計算完成後的引言標題
    st.markdown(f"### 💌 嗨，{display_name}！這是老臣為你解讀的命宮星曜本質：")
    
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
    
    # 底部心靈共振與行動呼籲模組（四維整合統一版）
    st.markdown("""
    <div style="margin-top: 3.5rem; padding: 2rem 1.5rem; background-color: rgba(35, 71, 50, 0.95); border-radius: 18px; border: 1px solid rgba(16, 185, 129, 0.25); color: #F5F5F4; box-shadow: 0 12px 28px -6px rgba(0, 0, 0, 0.25); max-width: 680px; margin-left: auto; margin-right: auto; text-align: center;">

      <div style="margin-bottom: 1.5rem;">
        <div style="font-size: 1.75rem; margin-bottom: 0.35rem;">🌿</div>
        <h3 style="font-size: 1.25rem; font-weight: bold; color: #FDE68A; letter-spacing: 0.5px; margin: 0 0 0.6rem 0; line-height: 1.4;">
          受過傷的地方，細心灌溉，依然能長出翠綠的風景
        </h3>
        <p style="font-size: 0.95rem; color: rgba(209, 250, 229, 0.9); line-height: 1.65; font-weight: 300; margin: 0;">
          心靈陪伴指引只是看見內在設定的起點，<br>
          真正的智慧在於回到日常生活，溫柔地接住自己。
        </p>
      </div>

      <div style="width: 70px; height: 1px; background: rgba(52, 211, 153, 0.4); margin: 1.5rem auto;"></div>

      <div style="background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(52, 211, 153, 0.2); border-radius: 14px; padding: 1.25rem; margin-bottom: 1.5rem; text-align: left; display: flex; flex-direction: column; gap: 0.85rem;">
        <div style="display: flex; align-items: flex-start; gap: 0.85rem;">
          <div style="width: 48px; height: 48px; border-radius: 50%; background: #132E1E; border: 1px solid rgba(253, 230, 138, 0.5); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; flex-shrink: 0; margin-top: 2px;">
            🌿
          </div>
          <div>
            <div style="display: flex; align-items: center; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 0.4rem;">
              <span style="font-size: 1.05rem; font-weight: bold; color: #FDE68A;">陳信忠（老臣 / Alan）</span>
              <span style="font-size: 0.75rem; padding: 2px 10px; border-radius: 9999px; background: rgba(6, 78, 59, 0.85); color: #A7F3D0; border: 1px solid rgba(5, 150, 105, 0.4); font-weight: 500;">心靈陪伴者</span>
              <span style="font-size: 0.75rem; padding: 2px 10px; border-radius: 9999px; background: rgba(6, 78, 59, 0.85); color: #A7F3D0; border: 1px solid rgba(5, 150, 105, 0.4); font-weight: 500;">國際園藝治療師</span>
            </div>
            <p style="font-size: 0.88rem; color: rgba(231, 229, 228, 0.95); line-height: 1.65; font-weight: 300; margin: 0;">
              綠藝國際學苑創辦人暨「老臣聊心室」心靈陪伴者；老臣於觀音成道日出生，幼年深結佛緣，長期研討宗教信仰與生命密碼；曾任科技企業工程主管與國際園藝治療師。深信修行在日常柴米油鹽中，以「觀音心法 × 靜心書寫 × 生命密碼 × 園藝療法」結合理性邏輯與自然調頻，陪你找回靈魂的原廠設定。
            </p>
          </div>
        </div>
      </div>

      <a href="https://line.me/R/ti/p/@mir4855b" target="_blank" style="display: block; text-decoration: none; padding: 1.15rem 1rem; border-radius: 14px; background: rgba(6, 95, 70, 0.6); border: 1px solid rgba(52, 211, 153, 0.35); margin-bottom: 1.5rem; transition: background 0.2s ease;">
        <div style="font-size: 0.82rem; font-weight: 600; color: #6EE7B7; margin-bottom: 0.3rem;">
          💬 綠藝漫活居 官方 LINE@
        </div>
        <div style="font-size: 1.05rem; font-weight: bold; color: #FFFFFF; margin-bottom: 0.35rem; line-height: 1.4;">
          點此進入心靈導航站｜領取深度指引・預約諮詢・探索新書作品
        </div>
        <div style="font-size: 0.82rem; color: rgba(214, 211, 209, 0.9); font-weight: 300;">
          加入後輸入對應關鍵字即可取得所需資源
        </div>
      </a>

      <div style="padding-top: 0.75rem; border-top: 1px solid rgba(16, 185, 129, 0.25);">
        <p style="font-size: 0.85rem; color: rgba(209, 250, 229, 0.85); line-height: 1.6; font-weight: 300; margin: 0 0 0.85rem 0;">
          這套心靈數位工具由老臣持續自主研發與維運。<br>
          若這份陪伴為你帶來安頓，歡迎隨喜贊助，護持更多心靈工具持續誕生。
        </p>
        <a href="https://line.me/R/ti/p/@mir4855b" target="_blank" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.6rem 1.4rem; border-radius: 9999px; background: rgba(253, 230, 138, 0.12); color: #FDE68A; border: 1px solid rgba(253, 230, 138, 0.4); font-size: 0.85rem; font-weight: 500; text-decoration: none; transition: background 0.2s ease;">
          <span>🍵</span> 隨喜支持・前往 LINE@ 輸入「3」贊助老臣持續研發
        </a>
      </div>

    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("綠藝國際學苑 ╳ 老臣聊心室 LUYILIFE © 2026 ｜ 聽你的心，陪你調頻 ｜ 設計者：陳信忠 (老臣/Alan)")
