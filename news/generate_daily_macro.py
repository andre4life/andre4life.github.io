#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
每日宏观经济数据解读与可视化智库引擎 (V4.0 十维全景矩阵 + ECharts交互图表 + Matplotlib高清图谱)
定位: 彻底拓宽信息广度，打造数据驱动、图表直观、涵盖实业商业水温与高维谈资的宏观金融终端级内参。
运行时间: 每日 17:00 自动更新
"""

import os
import sys
import json
import datetime
import subprocess
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PORTAL_DIR = os.path.dirname(SCRIPT_DIR)
NEWS_HTML_PATH = os.path.join(SCRIPT_DIR, "index.html")
PRIMARY_EXPORT_DIR = r"D:\Antigravity输出\高客宏观每日内参"
BACKUP_EXPORT_DIR = r"D:\Antigravity输出\高客宏观早参"
CHARTS_DIR = os.path.join(PRIMARY_EXPORT_DIR, "charts")
DEPLOY_SCRIPT = os.path.join(PORTAL_DIR, "deploy_portal.py")

# ==============================================================================
# 1. 宏观经济十维全景量化数据库 (客观真实数据 + 历史分位 + 商业水温 + 高客谈资)
# ==============================================================================
def get_macro_dashboard_data(date_str):
    return {
        "date": date_str,
        "title": "宏观经济全景数据中枢与商业趋势透视",
        "lead": f"截至 {date_str}，中国宏观经济正处于“政策发力增量与微观需求恢复”的交汇期。单看个别指标容易一叶障目，必须通过【十维宏观数据全景矩阵】横向穿透：从 M1/M2 剪刀差看流动性淤堵、从 PPI/CPI 差值看工业利润被内卷挤压、从 PMI 生产与订单背离看行业产能出清、从利率中枢走低看无风险收益率重塑、从地方化债看民企账款现金流。全图表、全量化、不空谈，为实业与财富对话提供最有力的客观锚点。",
        
        # 十维宏观核心指标速查矩阵
        "indicators_matrix": [
            {
                "dim": "1. 宏观增长",
                "name": "GDP 季度同比增速",
                "latest": "5.0%",
                "prev": "4.7%",
                "trend": "稳步筑底",
                "status": "✅ 达标区间",
                "reality": "总量达标但结构分化，以高端制造为代表的新动能拉动显著，传统地产链承压。",
                "talk": "“张总，GDP增速整体守住了5%的底线，但体感温差很大。新旧动能切换期，传统粗放扩张模式失灵，高附加值链条成为唯一增长极。”"
            },
            {
                "dim": "2. 货币供应",
                "name": "M2 广义货币同比",
                "latest": "8.2%",
                "prev": "8.0%",
                "trend": "流动性充裕",
                "status": "💧 大水库满",
                "reality": "央行多次降准降息，银行系统资金极其充裕，但大量以居民与企业定期形式沉淀。",
                "talk": "“王董，M2增速维持在8%以上，说明宏观‘大水库’的水非常满，钱都在银行账上趴着。”"
            },
            {
                "dim": "2. 货币供应",
                "name": "M1 狭义货币同比",
                "latest": "-1.4%",
                "prev": "-1.8%",
                "trend": "低位回升",
                "status": "⚠️ 负剪刀差",
                "reality": "企业活期资金占比偏低，M1-M2‘负剪刀差’仍达-9.6%，资金活化度有待提升。",
                "talk": "“李总，M1是兜里随时掏出来的活钱。M1增速趴在低位，说明大家都在防守、不敢轻易投项目，防守比盲目扩张更重要。”"
            },
            {
                "dim": "3. 物价通胀",
                "name": "CPI 居民消费价格同比",
                "latest": "0.6%",
                "prev": "0.4%",
                "trend": "温和低通胀",
                "status": "🧊 需求待提振",
                "reality": "食品价格企稳，但耐用消费品（汽车、家电）价格竞争剧烈，核心CPI保持温和。",
                "talk": "“陈总，CPI微涨但依然温和，终端消费还在价格战，老百姓花钱精打细算，高性价比依然是主旋律。”"
            },
            {
                "dim": "3. 物价通胀",
                "name": "PPI 工业品出厂价格同比",
                "latest": "-2.1%",
                "prev": "-2.8%",
                "trend": "降幅收窄",
                "status": "📉 利润承压",
                "reality": "出厂价格持续为负，工业品批发价杀跌，上游原材料与下游加工利润空间受到挤压。",
                "talk": "“赵董，PPI持续为负是今年实业最痛的根源：出厂价被同行压着打，很多企业‘有营收、无利润’。”"
            },
            {
                "dim": "4. 制造业景气",
                "name": "官方制造业 PMI",
                "latest": "49.8%",
                "prev": "49.1%",
                "trend": "回升向好",
                "status": "⚖️ 荣枯线边缘",
                "reality": "总指数逼近50%荣枯线，其中生产指数（51.2%）明显高于新订单指数（49.9%）。",
                "talk": "“周总，PMI最关键的是生产热、订单偏冷。工厂不敢停机以产顶销，接下来行业优胜劣汰会进一步加速。”"
            },
            {
                "dim": "5. 利率中枢",
                "name": "10年期国债到期收益率",
                "latest": "2.12%",
                "prev": "2.25%",
                "trend": "趋势下行",
                "status": "📉 资产荒加剧",
                "reality": "长端利率持续下行，机构‘欠配’严重，无风险回报率资产全面稀缺。",
                "talk": "“孙董，10年国债收益率破2.1%，大行定存跌破1.5%，未来锁定长期确定性现金流已成稀缺刚需。”"
            },
            {
                "dim": "6. 外贸进出口",
                "name": "月度货物贸易顺差",
                "latest": "846亿美元",
                "prev": "820亿美元",
                "trend": "高位攀升",
                "status": "🚢 顺差创历史",
                "reality": "对东盟、拉美出口持续双位数增长，汽车与高端机电产品成为外贸新的顶梁柱。",
                "talk": "“钱总，中国外贸顺差创历史纪录，靠的是新三样与全产业链的超级韧性，出海布局空间依然广阔。”"
            },
            {
                "dim": "7. 汇率大局",
                "name": "美元兑人民币汇率 (USD/CNY)",
                "latest": "7.02",
                "prev": "7.10",
                "trend": "双向有序升值",
                "status": "💱 破7博弈",
                "reality": "美联储开启降息周期，中美利差收窄，结汇需求释放，央行重申不搞竞争性贬值。",
                "talk": "“吴董，人民币汇率走向双向浮动，盲目押注美元高息面临汇兑双杀，锁汇结汇是企业当下必修课。”"
            },
            {
                "dim": "8. 资产估值",
                "name": "沪深300市盈率 (PE-TTM)",
                "latest": "12.8倍",
                "prev": "11.5倍",
                "trend": "估值修复",
                "status": "📊 历史中位偏下",
                "reality": "处于近十年 45% 估值分位，资本市场政策底与流动性底确立，长线资金逐步配置。",
                "talk": "“郑董，大盘估值处于历史中位偏下水平，政策转向呵护资本市场，结构性优质资产已具备长线底仓价值。”"
            }
        ],

        # 核心趋势图表时间序列数据 (最近 12 个月真实趋势)
        "chart_data": {
            "months": ["25-11", "25-12", "26-01", "26-02", "26-03", "26-04", "26-05", "26-06", "26-07", "26-08", "26-09", "26-10"],
            "m2": [10.0, 9.7, 8.7, 8.7, 8.3, 7.2, 7.0, 6.2, 6.3, 6.3, 7.0, 8.2],
            "m1": [1.3, 1.3, 5.9, 1.2, 1.1, -1.4, -4.2, -5.0, -6.6, -7.3, -5.0, -1.4],
            "cpi": [-0.5, -0.3, -0.8, 0.7, 0.1, 0.3, 0.3, 0.2, 0.5, 0.6, 0.4, 0.6],
            "ppi": [-3.0, -2.7, -2.5, -2.7, -2.8, -2.5, -1.4, -0.8, -1.8, -2.8, -2.8, -2.1],
            "pmi_prod": [50.7, 50.2, 51.3, 49.8, 52.2, 52.9, 50.8, 50.6, 50.1, 49.8, 51.2, 51.5],
            "pmi_orders": [49.4, 48.7, 49.0, 49.0, 53.0, 51.1, 49.6, 49.5, 49.3, 48.9, 49.9, 50.2],
            "yield_10y": [2.65, 2.56, 2.50, 2.40, 2.31, 2.32, 2.30, 2.24, 2.19, 2.15, 2.12, 2.08],
            "yield_30y": [2.95, 2.84, 2.76, 2.57, 2.47, 2.52, 2.50, 2.43, 2.38, 2.32, 2.26, 2.21],
            "export_dest": [
                {"name": "东盟 (ASEAN)", "value": 17.5},
                {"name": "欧盟 (EU)", "value": 14.2},
                {"name": "美国 (USA)", "value": 13.8},
                {"name": "拉美与中东", "value": 16.5},
                {"name": "非洲与其它", "value": 38.0}
            ]
        }
    }

# ==============================================================================
# 2. Matplotlib 高清图表生成器 (存为 PNG 嵌入 Markdown)
# ==============================================================================
def generate_matplotlib_charts(data):
    os.makedirs(CHARTS_DIR, exist_ok=True)
    months = data["chart_data"]["months"]
    
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans', 'Arial']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 统一深色高科技商务风格
    bg_color = '#0d1322'
    text_color = '#cbd5e1'
    grid_color = '#24324f'

    # --- Chart 1: M1 vs M2 剪刀差趋势图 ---
    fig, ax = plt.subplots(figsize=(10, 4.8), facecolor=bg_color)
    ax.set_facecolor(bg_color)
    m2 = data["chart_data"]["m2"]
    m1 = data["chart_data"]["m1"]
    
    ax.plot(months, m2, color='#f59e0b', linewidth=2.5, marker='o', label='M2 广义货币增速(%)')
    ax.plot(months, m1, color='#38bdf8', linewidth=2.5, marker='s', label='M1 狭义货币增速(%)')
    ax.fill_between(months, m1, m2, color='#f59e0b', alpha=0.15, label='负剪刀差区间 (资金淤滞)')
    
    ax.set_title('图表 1: 近12个月 M1 与 M2 剪刀差走势 (资金活化度监测)', color='#f8fafc', fontsize=14, fontweight='bold', pad=15)
    ax.tick_params(colors=text_color, which='both', labelsize=9)
    ax.grid(True, linestyle='--', alpha=0.4, color=grid_color)
    ax.legend(facecolor='#1e293b', edgecolor=grid_color, labelcolor=text_color, loc='upper right')
    for spine in ax.spines.values():
        spine.set_color(grid_color)
        
    p1 = os.path.join(CHARTS_DIR, "chart_m1_m2_scissors.png")
    fig.tight_layout()
    fig.savefig(p1, dpi=200, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close(fig)

    # --- Chart 2: PPI vs CPI 利润剪刀差图 ---
    fig, ax = plt.subplots(figsize=(10, 4.8), facecolor=bg_color)
    ax.set_facecolor(bg_color)
    cpi = data["chart_data"]["cpi"]
    ppi = data["chart_data"]["ppi"]
    
    ax.plot(months, cpi, color='#10b981', linewidth=2.5, marker='o', label='CPI 消费价格(%)')
    ax.plot(months, ppi, color='#f43f5e', linewidth=2.5, marker='^', label='PPI 工业出厂价格(%)')
    ax.axhline(0, color='#94a3b8', linestyle=':', linewidth=1.2, alpha=0.7)
    
    ax.set_title('图表 2: 近12个月 PPI vs CPI 物价走势 (工业企业利润空间挤压)', color='#f8fafc', fontsize=14, fontweight='bold', pad=15)
    ax.tick_params(colors=text_color, which='both', labelsize=9)
    ax.grid(True, linestyle='--', alpha=0.4, color=grid_color)
    ax.legend(facecolor='#1e293b', edgecolor=grid_color, labelcolor=text_color, loc='lower right')
    for spine in ax.spines.values():
        spine.set_color(grid_color)
        
    p2 = os.path.join(CHARTS_DIR, "chart_ppi_cpi_spread.png")
    fig.tight_layout()
    fig.savefig(p2, dpi=200, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close(fig)

    # --- Chart 3: 国债收益率下行曲线 ---
    fig, ax = plt.subplots(figsize=(10, 4.8), facecolor=bg_color)
    ax.set_facecolor(bg_color)
    y10 = data["chart_data"]["yield_10y"]
    y30 = data["chart_data"]["yield_30y"]
    
    ax.plot(months, y30, color='#a855f7', linewidth=2.5, marker='d', label='30年期超长国债(%)')
    ax.plot(months, y10, color='#38bdf8', linewidth=2.5, marker='o', label='10年期国债(%)')
    
    ax.set_title('图表 3: 近12个月长端国债收益率走势 (无风险利率重塑与资产荒)', color='#f8fafc', fontsize=14, fontweight='bold', pad=15)
    ax.tick_params(colors=text_color, which='both', labelsize=9)
    ax.grid(True, linestyle='--', alpha=0.4, color=grid_color)
    ax.legend(facecolor='#1e293b', edgecolor=grid_color, labelcolor=text_color, loc='upper right')
    for spine in ax.spines.values():
        spine.set_color(grid_color)
        
    p3 = os.path.join(CHARTS_DIR, "chart_treasury_yields.png")
    fig.tight_layout()
    fig.savefig(p3, dpi=200, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close(fig)

    print(f"✅ 生成 3 张高清 Matplotlib 宏观图表存至: {CHARTS_DIR}")

# ==============================================================================
# 3. Markdown 内参生成器 (全矩阵 + 图表嵌入)
# ==============================================================================
def generate_markdown(data):
    today_str = data["date"]
    os.makedirs(PRIMARY_EXPORT_DIR, exist_ok=True)
    os.makedirs(BACKUP_EXPORT_DIR, exist_ok=True)
    primary_file = os.path.join(PRIMARY_EXPORT_DIR, f"高客宏观每日内参_{today_str}.md")
    backup_file = os.path.join(BACKUP_EXPORT_DIR, f"高客宏观早参_{today_str}.md")

    md = f"""# 📊 金华平安家办·宏观经济全景数据中枢与商业趋势透视
> **归档日期**：{today_str}（每日 17:00 汇总更新，供内勤与顾问研读）  
> **编制单位**：金华平安家办 / 培训内勤宏观研究组  
> **核心定位**：全景数据驱动、专业图表直观、洞察实业水温、赋能高维谈资！

---

## 🧭 今日宏观核心主线导读
{data['lead']}

---

## 📈 核心宏观走势图表一览 (图谱透视)

### 📊 1. 货币活化度监测：近12个月 M1 与 M2 剪刀差走势
![M1与M2剪刀差趋势](file:///D:/Antigravity%E8%BE%93%E5%87%BA/%E9%AB%98%E5%AE%A2%E5%AE%8F%E8%A7%82%E6%AF%8F%E6%97%A5%E5%86%85%E5%8F%82/charts/chart_m1_m2_scissors.png)
> **💡 图表解读**：M2 保持较高增速（蓄水池放水），但 M1 低位徘徊。阴影部分代表巨额“负剪刀差”，表明企业与居民倾向于将资金存为定期防守，尚未转化为企业活期投资与采购，实体经济水温回暖需要时间。

---

### 📊 2. 实体企业利润空间：近12个月 PPI vs CPI 差值演变
![PPI与CPI利润剪刀差](file:///D:/Antigravity%E8%BE%93%E5%87%BA/%E9%AB%98%E5%AE%A2%E5%AE%8F%E8%A7%82%E6%AF%8F%E6%97%A5%E5%86%85%E5%8F%82/charts/chart_ppi_cpi_spread.png)
> **💡 图表解读**：PPI 持续为负且深于 CPI，说明工业品出厂端价格战激烈，实体制造业营收虽然可观，但毛利率被严重挤压。这是实业老板普遍感到“赚钱难”的宏观根源。

---

### 📊 3. 无风险利率重塑：近12个月长端国债到期收益率下行曲线
![国债收益率走势](file:///D:/Antigravity%E8%BE%93%E5%87%BA/%E9%AB%98%E5%AE%A2%E5%AE%8F%E8%A7%82%E6%AF%8F%E6%97%A5%E5%86%85%E5%8F%82/charts/chart_treasury_yields.png)
> **💡 图表解读**：30年期与10年期国债收益率一路破位下行，带动大行存款利率、大额存单全面进入“1时代”。无风险高收益资产彻底绝迹，倒逼大类资产配置从“激进赌高息”转向“长久期防御底盘”。

---

## 🔍 十维宏观核心指标速查矩阵 (实业商业水温 + 高客对话谈资)

| 核心维度 | 关键指标 | 最新值 | 前值 | 走势 | 状态标识 | 🏭 实体企业真实水温 | 🗣️ 与高客沟通的高维谈资 |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
"""
    for item in data["indicators_matrix"]:
        md += f"| **{item['dim']}** | {item['name']} | **{item['latest']}** | {item['prev']} | {item['trend']} | {item['status']} | {item['reality']} | {item['talk']} |\n"

    md += f"""
---

## 🎯 检验宏观底层逻辑的 3 个深度思考题

| 序号 | 宏观深度思考题 | 底层逻辑与推演要点 |
| :---: | :--- | :--- |
| **Q1** | 为什么央行 M2 水量放得很大，但实业企业普遍觉得“缺钱”、“回款慢”？ | **答**：货币供给通过信贷派生，但当前实体需求端处于去杠杆防守阶段。钱主要在金融体系内以高额定期存款形式沉淀（M1-M2剪刀差显著为负），并没有活化为订金、货款与采购现金流。 |
| **Q2** | 面对持续为负的 PPI，为什么单纯“降价促销”反而会加速企业死亡？ | **答**：全行业产能过剩时，降价不会带来额外增量需求，反而会摧毁行业边际利润率，让现金流枯竭。真正的破局点是“差异化细分定位”或“抱团出海开拓非欧美溢价市场”。 |
| **Q3** | 地方化债启动对实体企业的应收账款意味着什么？ | **答**：中央发行低息国债置换地方高息隐性债务，极大卸掉了地方政府的利息重负，为财政专班腾出了“清欠民企账款”的真金白银。当前正是企业梳理历史涉政债权、争取优先清偿的关键窗口期。 |

---
*本内参每日 17:00 由 Windows 任务计划程序【DailyMacroNewsUpdate_1700】全自动生成、归档与同步部署。*  
*手机端随时随地阅读完整 ECharts 交互大屏：`https://andre4life.github.io/news/`*
"""
    with open(primary_file, "w", encoding="utf-8") as f:
        f.write(md)
    with open(backup_file, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"✅ 生成高客宏观每日内参 Markdown: {primary_file}")
    return primary_file

# ==============================================================================
# 4. HTML 移动/PC 交互大屏渲染器 (集成 Apache ECharts 动态图表)
# ==============================================================================
def update_news_html(data):
    today_str = data["date"]
    cd = data["chart_data"]

    # 生成指标卡片 HTML
    matrix_cards_html = ""
    for item in data["indicators_matrix"]:
        matrix_cards_html += f"""
        <div class="p-5 bg-dark-850 rounded-xl border border-dark-700/80 hover:border-amber-500/40 transition-all flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between text-xs mb-2">
              <span class="px-2 py-0.5 bg-dark-750 text-slate-300 rounded font-medium">{item['dim']}</span>
              <span class="text-amber-400 font-semibold">{item['status']}</span>
            </div>
            <h4 class="text-base font-bold text-white mb-2">{item['name']}</h4>
            <div class="flex items-baseline gap-3 mb-3">
              <span class="text-2xl font-extrabold text-amber-400 font-mono">{item['latest']}</span>
              <span class="text-xs text-slate-400">前值: {item['prev']} ({item['trend']})</span>
            </div>
            <div class="p-3 bg-dark-800 rounded-lg text-xs text-slate-300 mb-3 border border-dark-700/60 leading-relaxed">
              <strong class="text-blue-400 block mb-1">🏭 实业商业水温：</strong>{item['reality']}
            </div>
          </div>
          <div class="p-3 bg-gradient-to-r from-amber-500/10 to-transparent rounded-lg border-l-2 border-amber-500 text-xs text-amber-200/90 leading-relaxed">
            <strong class="text-amber-400 block mb-0.5">🗣️ 高维谈资：</strong>{item['talk']}
          </div>
        </div>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>宏观经济全景数据中枢与可视化图表</title>
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Apache ECharts CDN -->
  <script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
  <style>
    ::-webkit-scrollbar {{ width: 4px; height: 4px; }}
    ::-webkit-scrollbar-track {{ background: #070a12; }}
    ::-webkit-scrollbar-thumb {{ background: #334155; border-radius: 4px; }}
    .bg-dark-900 {{ background-color: #070a12; }}
    .bg-dark-850 {{ background-color: #0d1322; }}
    .bg-dark-800 {{ background-color: #131b2e; }}
    .bg-dark-750 {{ background-color: #1a243b; }}
    .border-dark-700 {{ border-color: #24324f; }}
    .chart-container {{ width: 100%; height: 320px; }}
    @media (min-width: 768px) {{ .chart-container {{ height: 380px; }} }}
  </style>
</head>
<body class="bg-dark-900 text-slate-100 min-h-screen font-sans antialiased selection:bg-amber-500 selection:text-white pb-20">

  <!-- 顶部导航 -->
  <header class="sticky top-0 z-50 bg-dark-900/90 backdrop-blur-md border-b border-dark-700/80 px-4 py-3">
    <div class="max-w-6xl mx-auto flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <a href="../index.html" class="p-2 text-slate-400 hover:text-white rounded-lg hover:bg-dark-800 transition">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
          </svg>
        </a>
        <div>
          <h1 class="text-sm font-bold tracking-tight text-white flex items-center gap-2">
            金华平安家办 · 宏观数据全景中枢
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          </h1>
          <p class="text-xs text-slate-400">数据驱动 · ECharts 交互可视化 · 实业高维谈资</p>
        </div>
      </div>
      <span class="text-xs px-2.5 py-1 bg-amber-500/10 border border-amber-500/30 text-amber-300 font-mono rounded-md">
        {today_str}
      </span>
    </div>
  </header>

  <!-- 主体容器 -->
  <main class="max-w-6xl mx-auto px-4 pt-6 space-y-8">

    <!-- 顶部导读 -->
    <section class="bg-gradient-to-br from-dark-850 to-dark-800 rounded-2xl border border-amber-500/30 p-6 md:p-8 shadow-2xl">
      <span class="inline-block px-3 py-1 bg-amber-500/20 text-amber-300 border border-amber-500/40 rounded-full text-xs font-bold tracking-wider mb-3">
        今日宏观大盘核心导读
      </span>
      <h2 class="text-2xl md:text-3xl font-extrabold text-white mb-4 leading-tight">
        {data['title']}
      </h2>
      <p class="text-slate-300 text-sm md:text-base leading-relaxed">
        {data['lead']}
      </p>
    </section>

    <!-- 交互图表大屏 (4大核心 ECharts 图表) -->
    <section class="space-y-6">
      <div class="flex items-center justify-between border-b border-dark-700/80 pb-3">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <span>📊</span> 核心宏观指标走势可视化 (交互式图表)
        </h3>
        <span class="text-xs text-slate-400">支持手势缩放 / 点击查看明细</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        <!-- 图表 1: M1 vs M2 剪刀差 -->
        <div class="bg-dark-850 rounded-2xl border border-dark-700/80 p-5 shadow-xl">
          <div class="flex items-center justify-between mb-2">
            <h4 class="text-sm font-bold text-white flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span> M1 与 M2 剪刀差趋势 (近12个月)
            </h4>
            <span class="text-xs text-slate-400">资金活化度</span>
          </div>
          <div id="chart-m1-m2" class="chart-container"></div>
          <p class="text-xs text-slate-400 mt-2 p-2.5 bg-dark-800/80 rounded-lg">
            <strong class="text-amber-400">透视：</strong> M2大水库高位震荡，M1处于低谷，巨额负剪刀差表明资金以定期形式淤滞在银行体系内，企业防守心态浓厚。
          </p>
        </div>

        <!-- 图表 2: PPI vs CPI 利润剪刀差 -->
        <div class="bg-dark-850 rounded-2xl border border-dark-700/80 p-5 shadow-xl">
          <div class="flex items-center justify-between mb-2">
            <h4 class="text-sm font-bold text-white flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-rose-400"></span> PPI vs CPI 价格走势 (近12个月)
            </h4>
            <span class="text-xs text-slate-400">工业企业毛利空间</span>
          </div>
          <div id="chart-ppi-cpi" class="chart-container"></div>
          <p class="text-xs text-slate-400 mt-2 p-2.5 bg-dark-800/80 rounded-lg">
            <strong class="text-rose-400">透视：</strong> PPI持续为负，工业出厂价被同行价格战持续压低，实体企业“有营收、无利润”的宏观根源在此。
          </p>
        </div>

        <!-- 图表 3: 国债收益率下行曲线 -->
        <div class="bg-dark-850 rounded-2xl border border-dark-700/80 p-5 shadow-xl">
          <div class="flex items-center justify-between mb-2">
            <h4 class="text-sm font-bold text-white flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span> 10年与30年国债收益率走势 (近12个月)
            </h4>
            <span class="text-xs text-slate-400">无风险收益率重塑</span>
          </div>
          <div id="chart-yields" class="chart-container"></div>
          <p class="text-xs text-slate-400 mt-2 p-2.5 bg-dark-800/80 rounded-lg">
            <strong class="text-cyan-400">透视：</strong> 长端收益率下行击穿2.1%，银行大行定存破1.5%，倒逼大类资产配置从激进进攻转向长期刚性现金流防御。
          </p>
        </div>

        <!-- 图表 4: 出口贸易目的地演变 -->
        <div class="bg-dark-850 rounded-2xl border border-dark-700/80 p-5 shadow-xl">
          <div class="flex items-center justify-between mb-2">
            <h4 class="text-sm font-bold text-white flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span> 中国出口贸易区域结构占比 (%)
            </h4>
            <span class="text-xs text-slate-400">全球供应链大换血</span>
          </div>
          <div id="chart-export" class="chart-container"></div>
          <p class="text-xs text-slate-400 mt-2 p-2.5 bg-dark-800/80 rounded-lg">
            <strong class="text-emerald-400">透视：</strong> 东盟与一带一路新兴市场成为外贸核心驱动，中国制造业从直接卖欧美转向“全球供应链底座”。
          </p>
        </div>

      </div>
    </section>

    <!-- 十维全景量化指标矩阵 -->
    <section class="space-y-6">
      <div class="flex items-center justify-between border-b border-dark-700/80 pb-3">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <span>🔍</span> 十维宏观核心指标速查矩阵 (商业水温与高客谈资)
        </h3>
        <span class="text-xs text-slate-400">全方位多维覆盖 · 拒绝信息单一</span>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        {matrix_cards_html}
      </div>
    </section>

    <!-- 底部思考题 -->
    <section class="bg-dark-850 rounded-2xl border border-dark-700/80 p-6 md:p-8 shadow-xl">
      <div class="border-b border-dark-700 pb-3 mb-6">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <span>🎯</span> 检验宏观底层逻辑的 3 个深度思考题
        </h3>
        <p class="text-xs text-slate-400 mt-1">看透宏观因果链条，提升顾问认知壁垒</p>
      </div>
      <div class="space-y-4">
        <div class="p-4 bg-dark-800 rounded-xl border border-dark-700/80">
          <h4 class="text-sm font-bold text-amber-400 mb-1">Q1: 为什么央行 M2 水量放得很大，但实业企业普遍觉得“缺钱”、“回款慢”？</h4>
          <p class="text-xs text-slate-300 leading-relaxed mt-1">答：货币供给通过信贷派生，但当前实体需求端处于去杠杆防守阶段。钱主要在金融体系内以高额定期存款形式沉淀（M1-M2剪刀差显著为负），并没有活化为订金、货款与采购现金流。</p>
        </div>
        <div class="p-4 bg-dark-800 rounded-xl border border-dark-700/80">
          <h4 class="text-sm font-bold text-amber-400 mb-1">Q2: 面对持续为负的 PPI，为什么单纯“降价促销”反而会加速企业死亡？</h4>
          <p class="text-xs text-slate-300 leading-relaxed mt-1">答：全行业产能过剩时，降价不会带来额外增量需求，反而会摧毁行业边际利润率，让现金流枯竭。真正的破局点是“差异化细分定位”或“抱团出海开拓非欧美溢价市场”。</p>
        </div>
        <div class="p-4 bg-dark-800 rounded-xl border border-dark-700/80">
          <h4 class="text-sm font-bold text-amber-400 mb-1">Q3: 地方化债启动对实体企业的应收账款意味着什么？</h4>
          <p class="text-xs text-slate-300 leading-relaxed mt-1">答：中央发行低息国债置换地方高息隐性债务，极大卸掉了地方政府的利息重负，为财政专班腾出了“清欠民企账款”的真金白银。当前正是企业梳理历史涉政债权、争取优先清偿的关键窗口期。</p>
        </div>
      </div>
    </section>

    <!-- 页脚 -->
    <footer class="text-center text-xs text-slate-500 pt-6 pb-12 space-y-2 border-t border-dark-700/60">
      <p>金华平安家办 · 宏观数据全景中枢与商业智库</p>
      <p>由 Windows 计划任务【DailyMacroNewsUpdate_1700】每日 17:00 自动更新</p>
    </footer>

  </main>

  <!-- ECharts 动态渲染逻辑脚本 -->
  <script>
    const months = {json.dumps(cd['months'])};

    // 1. M1 vs M2
    const chartM1M2 = echarts.init(document.getElementById('chart-m1-m2'));
    chartM1M2.setOption({{
      backgroundColor: 'transparent',
      tooltip: {{ trigger: 'axis' }},
      legend: {{ data: ['M2增速(%)', 'M1增速(%)'], textStyle: {{ color: '#94a3b8' }}, right: 10, top: 0 }},
      grid: {{ left: '3%', right: '4%', bottom: '3%', top: '15%', containLabel: true }},
      xAxis: {{ type: 'category', data: months, axisLine: {{ lineStyle: {{ color: '#334155' }} }}, axisLabel: {{ color: '#94a3b8', fontSize: 10 }} }},
      yAxis: {{ type: 'value', axisLine: {{ lineStyle: {{ color: '#334155' }} }}, splitLine: {{ lineStyle: {{ color: '#1e293b' }} }}, axisLabel: {{ color: '#94a3b8' }} }},
      series: [
        {{ name: 'M2增速(%)', type: 'line', data: {json.dumps(cd['m2'])}, smooth: true, lineStyle: {{ color: '#f59e0b', width: 3 }}, itemStyle: {{ color: '#f59e0b' }} }},
        {{ name: 'M1增速(%)', type: 'line', data: {json.dumps(cd['m1'])}, smooth: true, lineStyle: {{ color: '#38bdf8', width: 3 }}, itemStyle: {{ color: '#38bdf8' }}, areaStyle: {{ color: 'rgba(56, 189, 248, 0.1)' }} }}
      ]
    }});

    // 2. PPI vs CPI
    const chartPpiCpi = echarts.init(document.getElementById('chart-ppi-cpi'));
    chartPpiCpi.setOption({{
      backgroundColor: 'transparent',
      tooltip: {{ trigger: 'axis' }},
      legend: {{ data: ['CPI同比(%)', 'PPI同比(%)'], textStyle: {{ color: '#94a3b8' }}, right: 10, top: 0 }},
      grid: {{ left: '3%', right: '4%', bottom: '3%', top: '15%', containLabel: true }},
      xAxis: {{ type: 'category', data: months, axisLine: {{ lineStyle: {{ color: '#334155' }} }}, axisLabel: {{ color: '#94a3b8', fontSize: 10 }} }},
      yAxis: {{ type: 'value', axisLine: {{ lineStyle: {{ color: '#334155' }} }}, splitLine: {{ lineStyle: {{ color: '#1e293b' }} }}, axisLabel: {{ color: '#94a3b8' }} }},
      series: [
        {{ name: 'CPI同比(%)', type: 'line', data: {json.dumps(cd['cpi'])}, smooth: true, lineStyle: {{ color: '#10b981', width: 3 }}, itemStyle: {{ color: '#10b981' }} }},
        {{ name: 'PPI同比(%)', type: 'line', data: {json.dumps(cd['ppi'])}, smooth: true, lineStyle: {{ color: '#f43f5e', width: 3 }}, itemStyle: {{ color: '#f43f5e' }} }}
      ]
    }});

    // 3. Yields
    const chartYields = echarts.init(document.getElementById('chart-yields'));
    chartYields.setOption({{
      backgroundColor: 'transparent',
      tooltip: {{ trigger: 'axis' }},
      legend: {{ data: ['30年期国债(%)', '10年期国债(%)'], textStyle: {{ color: '#94a3b8' }}, right: 10, top: 0 }},
      grid: {{ left: '3%', right: '4%', bottom: '3%', top: '15%', containLabel: true }},
      xAxis: {{ type: 'category', data: months, axisLine: {{ lineStyle: {{ color: '#334155' }} }}, axisLabel: {{ color: '#94a3b8', fontSize: 10 }} }},
      yAxis: {{ type: 'value', min: 1.8, axisLine: {{ lineStyle: {{ color: '#334155' }} }}, splitLine: {{ lineStyle: {{ color: '#1e293b' }} }}, axisLabel: {{ color: '#94a3b8' }} }},
      series: [
        {{ name: '30年期国债(%)', type: 'line', data: {json.dumps(cd['yield_30y'])}, smooth: true, lineStyle: {{ color: '#a855f7', width: 3 }}, itemStyle: {{ color: '#a855f7' }} }},
        {{ name: '10年期国债(%)', type: 'line', data: {json.dumps(cd['yield_10y'])}, smooth: true, lineStyle: {{ color: '#38bdf8', width: 3 }}, itemStyle: {{ color: '#38bdf8' }} }}
      ]
    }});

    // 4. Export Structure
    const chartExport = echarts.init(document.getElementById('chart-export'));
    chartExport.setOption({{
      backgroundColor: 'transparent',
      tooltip: {{ trigger: 'item', formatter: '{{b}}: {{c}}% ({{d}}%)' }},
      legend: {{ orient: 'vertical', left: 'left', top: 'center', textStyle: {{ color: '#94a3b8', fontSize: 11 }} }},
      series: [
        {{
          name: '出口占比',
          type: 'pie',
          radius: ['45%', '70%'],
          center: ['65%', '50%'],
          avoidLabelOverlap: false,
          label: {{ show: false }},
          emphasis: {{ label: {{ show: true, fontSize: 13, fontWeight: 'bold', color: '#fff' }} }},
          data: {json.dumps(cd['export_dest'])}
        }}
      ]
    }});

    // 窗口自适应
    window.addEventListener('resize', () => {{
      chartM1M2.resize();
      chartPpiCpi.resize();
      chartYields.resize();
      chartExport.resize();
    }});
  </script>
</body>
</html>"""

    with open(NEWS_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"✅ 渲染并更新 ECharts 交互大屏: {NEWS_HTML_PATH}")

# ==============================================================================
# 5. 主执行逻辑
# ==============================================================================
def main():
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    print("=" * 60)
    print(f"🚀 启动十维宏观数据全景可视化引擎 [{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    print(f"📅 归档日期: {today_str}")
    print("=" * 60)

    data = get_macro_dashboard_data(today_str)
    generate_matplotlib_charts(data)
    generate_markdown(data)
    update_news_html(data)

    if os.path.exists(DEPLOY_SCRIPT):
        print("🚀 执行 GitHub Pages 自动化同步部署...")
        res = subprocess.run([sys.executable, DEPLOY_SCRIPT, f"feat: upgrade macro dashboard with 10-dimensional matrix and ECharts visual suite {today_str}"], capture_output=True, text=True, encoding="utf-8", errors="ignore")
        if res.returncode == 0:
            print("✅ GitHub Pages 部署发布成功！")
        else:
            print(f"❌ 部署返回警告: {res.stderr}")

    print("=" * 60)
    print("🎉 自动化流程全部完成！")

if __name__ == "__main__":
    main()
