import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# 設定頁面
st.set_page_config(
    page_title="雜貨店轉型方案",
    page_icon="🏪",
    layout="wide"
)

# 樣式增強
st.markdown("""
<style>
    .big-title { 
        font-size: 2.5rem; 
        color: #8B4513; 
        text-align: center;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .sub-title { 
        font-size: 1.2rem; 
        color: #666; 
        text-align: center;
        margin-bottom: 30px;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #8B4513;
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .cloud-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 3px 10px;
        border-radius: 15px;
        font-size: 0.8rem;
        display: inline-block;
        margin-right: 5px;
        margin-bottom: 5px;
    }
    .tech-demo {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        font-family: monospace;
        font-size: 0.9rem;
    }
    .highlight {
        background: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# 標題區
st.markdown('<div class="big-title">🏪雜貨店轉型方案</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">50年老店</div>', unsafe_allow_html=True)


# 雲端狀態顯示
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("雲端儲存使用", "15GB", "2GB 新增")
with col2:
    st.metric("線上訂單", "127 筆", "23% 成長")
with col3:
    st.metric("雲端節省時間", "18 小時/週", "相比紙本")

st.divider()

# 第一部分：雲端轉型優勢
st.header("☁️ 為什麼要用雲端？")
st.markdown('雲端科技可以讓小店也能像大公司一樣聰明經營！', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h4>💾 資料永不遺失</h4>
        <span class="cloud-badge">Google雲端</span>
        <span class="cloud-badge">自動備份</span>
        <p>• 帳本、客戶資料安全保存</p>
        <p>• 手機電腦都能看</p>
        <p>• 不怕火災水災</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>📊 自動分析報表</h4>
        <span class="cloud-badge">數據分析</span>
        <span class="cloud-badge">AI預測</span>
        <p>• 自動算哪個商品好賣</p>
        <p>• 提醒何時要補貨</p>
        <p>• 天氣熱自動推冰品</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4>🤖 智慧幫手</h4>
        <span class="cloud-badge">Chatbot</span>
        <span class="cloud-badge">自動回覆</span>
        <p>• Line機器人接訂單</p>
        <p>• 自動回客人問題</p>
        <p>• 24小時不打烊</p>
    </div>
    """, unsafe_allow_html=True)

# 第二部分：雲端工具示範
st.divider()
st.header("🛠️ 實際雲端應用示範")

tab1, tab2, tab3, tab4 = st.tabs(["庫存管理", "客戶服務", "線上銷售", "數據分析"])

with tab1:
    st.markdown("### 📦 智慧庫存管理系統")
    
    # 模擬庫存數據
    inventory_data = {
        '商品': ['手工醬油', '有機白米', '古早味餅乾', '在地蜂蜜', '健康堅果'],
        '當前庫存': [45, 120, 85, 32, 67],
        '安全庫存': [30, 100, 50, 20, 40],
        '本週銷售': [23, 45, 38, 15, 28],
        '建議補貨': ['✓ 建議補貨', '充足', '充足', '✓ 建議補貨', '充足']
    }
    
    df_inventory = pd.DataFrame(inventory_data)
    
    
    st.dataframe(df_inventory.style.applymap(
            lambda x: 'background-color: #ffcccc' if '建議補貨' in str(x) else '',
            subset=['建議補貨']
        ), use_container_width=True)
    
    

with tab2:
    st.markdown("### 💬 雲端客戶服務系統")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
        <h4>Line智慧客服機器人</h4>
        <span class="cloud-badge">24小時服務</span>
        
        **常用功能：**
        1. 📋 查商品價錢
        2. 🛒 直接下訂單
        3. 📍 查營業時間
        4. 🚚 追蹤訂單
        5. 💰 查會員點數
        
        **設定流程：**
        1. 申請Line商家帳號
        2. 設定自動回覆規則
        3. 綁定Google表單
        4. 啟用訂單通知
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # 模擬客服對話
        st.markdown("### 💬 客服機器人對話模擬")
        
        messages = [
            {"role": "user", "content": "請問手工醬油多少錢？", "time": "10:30"},
            {"role": "bot", "content": "手工醬油一瓶$250，買三瓶特價$700哦！", "time": "10:30"},
            {"role": "user", "content": "我要訂兩瓶，可以送貨嗎？", "time": "10:31"},
            {"role": "bot", "content": "可以的！滿$500免運費，請點連結填地址：https://forms.gle/xxxx", "time": "10:31"}
        ]
        
        for msg in messages:
            if msg["role"] == "user":
                st.markdown(f"""
                <div style='text-align: right; margin: 5px;'>
                    <div style='background-color: #e3f2fd; padding: 10px; border-radius: 10px; display: inline-block;'>
                        {msg["content"]}
                        <div style='font-size: 0.8em; color: #666;'>{msg["time"]}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style='margin: 5px;'>
                    <div style='background-color: #f5f5f5; padding: 10px; border-radius: 10px; display: inline-block;'>
                        <strong>🤖 雜貨店小幫手：</strong>{msg["content"]}
                        <div style='font-size: 0.8em; color: #666;'>{msg["time"]}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

with tab3:
    st.markdown("### 🛍️ 多平台線上銷售")
    
    platforms = {
        "Line購物": {"訂單": 45, "成長": "+15%", "特色": "熟客最愛"},
        "Facebook商店": {"訂單": 32, "成長": "+25%", "特色": "分享擴散快"},
        "Google商家": {"訂單": 28, "成長": "+18%", "特色": "在地客搜尋"},
        "簡單官網": {"訂單": 22, "成長": "+30%", "特色": "24小時接單"}
    }
    
    # 田字型顯示 - 最簡單的2x2網格
    col1, col2 = st.columns(2)
    
    with col1:
        # Line購物
        st.markdown("""
        <div class="card">
            <h5>💬 Line購物</h5>
            <h3>45 筆</h3>
            <p>📈 +15% 成長</p>
            <small>熟客最愛</small>
        </div>
        """, unsafe_allow_html=True)
        
        # Google商家
        st.markdown("""
        <div class="card">
            <h5>🔍 Google商家</h5>
            <h3>28 筆</h3>
            <p>📈 +18% 成長</p>
            <small>在地客搜尋</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Facebook商店
        st.markdown("""
        <div class="card">
            <h5>📘 Facebook商店</h5>
            <h3>32 筆</h3>
            <p>📈 +25% 成長</p>
            <small>分享擴散快</small>
        </div>
        """, unsafe_allow_html=True)
        
        # 簡單官網
        st.markdown("""
        <div class="card">
            <h5>🌐 簡單官網</h5>
            <h3>22 筆</h3>
            <p>📈 +30% 成長</p>
            <small>24小時接單</small>
        </div>
        """, unsafe_allow_html=True)
    

with tab4:
    st.markdown("### 📈 雲端數據分析儀表板")
    
    # 直接使用Streamlit內建圖表，最簡單可靠
    st.markdown("#### 📊 營業額趨勢")
    
    # 生成數據
    dates = pd.date_range(start='2024-01-01', periods=31, freq='D')
    sales = np.random.randint(8000, 20000, size=31)
    
    # Streamlit內建圖表
    chart_data = pd.DataFrame({
        '營業額': sales
    }, index=dates)
    
    st.line_chart(chart_data)
    
    st.markdown("#### 🏷️ 商品類別銷售比例")
    
    # 簡單顯示比例
    data = {
        '商品類別': ['食品', '調味料', '飲料', '日用品', '其他'],
        '銷售比例%': [35, 25, 20, 15, 5]
    }
    
    df_categories = pd.DataFrame(data)
    
    # 或者用長條圖
    st.bar_chart(df_categories.set_index('商品類別'))
    
    # 雲端分析洞察
    st.markdown("### 💡 雲端AI建議")
    
    insights = [
        {
            "發現": "週末手工醬油銷售比平日多40%",
            "建議": "週五發送醬油優惠券"
        },
        {
            "發現": "下雨天線上訂單增加60%",
            "建議": "雨天自動推免運優惠"
        },
        {
            "發現": "王阿姨每月15號買米",
            "建議": "自動提醒並預留商品"
        },
        {
            "發現": "年輕人喜歡小包裝組合",
            "建議": "推出嘗鮮組合包"
        }
    ]
    
    for insight in insights:
        st.markdown(f"""
        <div style="padding: 15px; margin: 10px 0; background-color: #f8f9fa; border-radius: 8px; border-left: 4px solid #8B4513; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <div style="display: flex; align-items: flex-start;">
                <div>
                    <div style="font-weight: bold; color: #333; margin-bottom: 5px;">
                        {insight['發現']}
                    </div>
                    <div style="color: #666; display: flex; align-items: center;">
                        {insight['建議']}
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 第三部分：實施步驟
st.divider()
st.header("🚀 雲端轉型三步驟")

steps = [
    {
        "title": "第一週：基礎雲端設定",
        "tasks": [
            "申請Google帳號（免費）",
            "設定Google雲端硬碟",
            "建立商品相簿",
            "設定Line商家帳號"
        ],
        "time": "3-5小時",
        "cost": "免費"
    },
    {
        "title": "第一個月：數位工具上線",
        "tasks": [
            "建立Google表單訂單系統",
            "設定自動化記帳試算表",
            "開始用Line收訂單",
            "建立客戶資料庫"
        ],
        "time": "10-15小時",
        "cost": "免費"
    },
    {
        "title": "三個月：智慧化營運",
        "tasks": [
            "啟用AI庫存預測",
            "設定自動化行銷",
            "建立數據儀表板",
            "整合多平台訂單"
        ],
        "time": "20-30小時",
        "cost": "月付$300-500"
    }
]

for i, step in enumerate(steps, 1):
    with st.expander(f"步驟 {i}: {step['title']}"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**主要任務：**")
            for task in step['tasks']:
                st.markdown(f"✓ {task}")
        with col2:
            st.metric("所需時間", step['time'])
            st.metric("每月成本", step['cost'])

# 第四部分：成本效益分析
st.divider()
st.header("💰 成本效益分析")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h4>初期投資（第一年）</h4>
        <p>• 平板電腦：$8,000</p>
        <p>• 雲端服務：$6,000/年</p>
        <p>• 數位學習：$3,000</p>
        <p>• 包裝升級：$5,000</p>
        <p><strong>合計：$22,000</strong></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>每月雲端服務</h4>
        <p>• Google Workspace：$240</p>
        <p>• 智慧分析工具：$300</p>
        <p>• 電商平台費：$150</p>
        <p>• 網路費用：$699</p>
        <p><strong>月計：$1,389</strong></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4>預期效益</h4>
        <p>• 營業額增加：+30%</p>
        <p>• 新客人增加：+50人/月</p>
        <p>• 節省時間：20小時/週</p>
        <p>• 錯誤減少：80%</p>
        <p><strong>投資回收：6-8個月</strong></p>
    </div>
    """, unsafe_allow_html=True)


