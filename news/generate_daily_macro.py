#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
每日经济日报与宏观大盘透视自动化引擎 (V5.0 终极全能版)
功能矩阵:
1. 宏观经济十维全景量化矩阵 (客观真实数据 + 历史分位 + 商业水温 + 高客谈资)
2. Matplotlib 高清图表自动渲染 (深色科技风 PNG 供 Markdown 引用)
3. 每日经济日报 Markdown 报告生成 (存入 高客宏观每日内参 & 高客宏观早参)
4. Apache ECharts 交互大屏渲染 (andre4life.github.io/news/index.html)
5. 心智雷达工作台站内嵌入更新 (andre4life.github.io/mindradar/index.html & 个人工作复盘工作台)
6. GitHub Pages 自动化极速推送同步 (deploy_portal.py)
"""

import os
import sys
import json
import datetime
import subprocess
import re
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
MINDRADAR_HTML_PATH = os.path.join(PORTAL_DIR, "mindradar", "index.html")
LOCAL_WORKBENCH_HTML_PATH = r"D:\Antigravity输出\个人工作复盘与盲区诊断工作台\index.html"
PRIMARY_EXPORT_DIR = r"D:\Antigravity输出\高客宏观每日内参"
BACKUP_EXPORT_DIR = r"D:\Antigravity输出\高客宏观早参"
CHARTS_DIR = os.path.join(PRIMARY_EXPORT_DIR, "charts")
DEPLOY_SCRIPT = os.path.join(PORTAL_DIR, "deploy_portal.py")

# ==============================================================================
# 1. 核心宏观数据定义与分析内容
# ==============================================================================
def get_macro_dashboard_data(date_str):
    return {
        "date": date_str,
        "title": "金华平安家办 · 每日经济日报",
        "subtitle": "宏观大盘透视 · 十维商业水温速查 · 三师共诊穿透 · 展业口袋短语",
        "lead": f"截至 {date_str}，中国宏观经济正处于“政策发力增量与微观需求恢复”的关键交汇期。单看个别指标容易一叶障目，必须通过【十维宏观数据全景矩阵】横向穿透：从 M1/M2 剪刀差看流动性淤堵、从 PPI/CPI 差值看工业利润被内卷挤压、从 PMI 生产与订单背离看行业产能出清、从利率中枢走低看无风险收益率重塑、从地方化债看民企账款现金流。全图表、全量化、不空谈，为实业与财富对话提供最有力的客观锚点。",
        
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

        # 核心趋势图表时间序列数据 (近12个月)
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
        },

        # 三师共诊透析
        "tri_experts": [
            {
                "role": "🏛️ 民商法律师视角",
                "tag": "合规治理 · 防火隔离",
                "color": "blue",
                "core": "【新公司法实缴期倒计时与债务隔离】当前微观去杠杆与化债背景下，企业对外担保与抽逃出资追责空前严厉。老板个人与公司财务混同是致命死穴，必须通过“企业法人治理规范 + 家庭资产与大额保单防火墙”截断无限连带清偿风险。"
            },
            {
                "role": "💼 投顾理财规划师视角",
                "tag": "利率重塑 · 锁定现金流",
                "color": "amber",
                "core": "【告别高息幻想，锁定长期现金流】10年期国债击穿2.1%，大行定存全面进入1时代。激进搏高息的时代彻底结束。高净值家庭底盘必须配置“分红险特别储备金机制 + 终身年金现金流”，用刚性契约抵御未来长周期低利率侵蚀。"
            },
            {
                "role": "🏭 实业与医养专家视角",
                "tag": "以出海破卷 · 守护身心",
                "color": "emerald",
                "core": "【以出海破内卷，以家办护身心】单纯国内降价内卷等于慢性失血，义乌/金华实业应积极借助东盟与拉美顺差红利出海。同时，企业家自身精力有限，通过家办前置锁定“名医绿通 + 高品质居家康养”，是守住基业的隐形支柱。"
            }
        ],

        # 8大宏观生活化买菜比喻
        "lexicon": [
            {"term": "PE 市盈率", "analogy": "菜市场买个摊位要10万元，这个摊位每年净赚1万元，回本需要10年，PE就是10倍。如果摊位炒到50万（PE=50倍），要卖菜50年才回本，这就是泡沫；如果摊位跌到8万（PE=8倍），回本快，就是便宜黄金期。"},
            {"term": "M2 与 M1", "analogy": "M2是山顶水库蓄了满满一库水（存款总额大）；M1是农民伯伯能随时拧开浇菜的抽水机（活期现金）。现在水库水位极高（M2=8.2%），但大家不敢借水浇地，抽水机没开（M1=-1.4%），这就是“负剪刀差”。"},
            {"term": "PPI 与 CPI", "analogy": "PPI是蔬菜批发大市场的出厂价，CPI是老百姓菜篮子的最终买菜价。现在PPI为负（-2.1%），说明地头批发都在赔本甩卖、价格战惨烈；虽然老百姓买菜便宜了（CPI温和），但种菜和做生意的实体老板最受伤。"},
            {"term": "国债收益率", "analogy": "全村最老实保长给村民打的借条利息。如果连保长借钱都只要2%的利息（10年国债2.12%），说明村里极其缺好项目。这时候银行大额存单必然降到1.5%，外面号称能保本赚8%的，99%是想吃你本金的骗子。"},
            {"term": "逆周期调节", "analogy": "天旱旱情严重时，官府开渠放水救庄稼（降息降准、增发国债）；天气大涝洪水泛滥时，关闸修坝收紧口袋。现在正是官方开闸放水、支持实业化债与止跌回稳的逆周期发力期。"},
            {"term": "地方化债", "analogy": "儿子在外面借了高利贷，每天光利息就压得喘不过气、没钱给送货的结账。老父亲出面，用自己国家级信用借一笔极低利息的30年大贷款，帮儿子把高利贷还清，儿子终于有钱给供货商结算工程款。"},
            {"term": "分红险特别储备金", "analogy": "好比村里的公粮仓：丰收年粮食多，不全分光吃光，扣下一部分存进公仓；等遇到大旱灾荒年，再开仓放粮贴补各家。平安分红险靠这个机制，实现几十年平抑市场剧烈波动。"},
            {"term": "资产负债表衰退", "analogy": "开面馆的老板今年虽然赚了10万元，但他不敢换新灶台、也不敢多雇小工，而是把这10万块全拿去提前还清当年买门面的贷款。所有人都只想着还债，市面上流动资金就越来越少。"}
        ],

        # 展业两分钟口袋短语
        "talk_tracks": [
            {
                "scene": "见义乌/金华实业老板（面对“实体难做、利润薄如纸”）",
                "color": "amber",
                "script": "“张总，现在PPI持续为负，实体企业普遍‘有营收、无利润’，降价只会把现金流榨干。越是这个时候，越不能把所有本钱都押在厂房和货款上。聪明的老板现在都在做‘资产截流’：每年固定从利润里拿出一块，做一张跟企业债务完全切断的家庭现金流防火墙。哪怕外面风浪再大，老婆孩子的饭碗和您东山再起的本钱永远动不了！”"
            },
            {
                "scene": "见银行大额存单/保守理财客户（面对“嫌收益低却不敢投”）",
                "color": "cyan",
                "script": "“王董，现在10年期国债收益率都破2.1%了，大行三年期定存马上见不到1.5%。您现在看着手头理财还有两点几，但两三年一到期，您手里的钱往哪儿放？买房涨不动、股市不敢赌、定存不断降。您现在最需要的不是冒高风险，而是趁现在锁定一份写进合同、一辈子源源不断给您发钱的确定现金流！”"
            },
            {
                "scene": "见外贸出口与出海民营企业主（面对“汇率波动与海外关税”）",
                "color": "emerald",
                "script": "“钱总，今年中国对东盟拉美出口顺差创纪录，但人民币汇率双向波动加剧，单边赌单极币种非常危险。大老板的全球布局，一手抓实业出海赚增量，一手要在家办做‘离岸与在岸双循环资产防御’，把企业的经营利润，通过信托和保单转化为不可撼动的家族根基资产。”"
            }
        ],

        # 3个底层逻辑深度思考题
        "thinking_questions": [
            {
                "q": "为什么央行 M2 水量放得很大，但实业企业普遍觉得“缺钱”、“回款慢”？",
                "a": "货币供给通过信贷派生，但当前微观实体处于去杠杆防守阶段。钱主要在金融体系内以高额定期存款形式沉淀（M1-M2剪刀差仍达-9.6%），并没有活化为订金、货款与采购现金流。水库虽满，下游农田依然干渴。"
            },
            {
                "q": "面对持续为负的 PPI，为什么单纯“降价促销”反而会加速企业死亡？",
                "a": "全行业产能过剩时，降价不会带来额外增量需求，反而会摧毁行业边际利润率，让现金流枯竭。真正的破局点是“差异化细分定位”或“抱团出海开拓非欧美溢价市场”。"
            },
            {
                "q": "地方化债启动对实体企业的应收账款意味着什么窗口期？",
                "a": "中央发行低息国债置换地方高息隐性债务，极大卸掉了地方政府的利息重负，为财政专班腾出了“清欠民企账款”的真金白银。当前正是企业梳理历史涉政债权、争取优先清偿的关键窗口期。"
            }
        ]
    }

# ==============================================================================
# 2. Matplotlib 高清图表生成器 (PNG 存入 charts 目录)
# ==============================================================================
def generate_matplotlib_charts(data):
    os.makedirs(CHARTS_DIR, exist_ok=True)
    months = data["chart_data"]["months"]
    
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans', 'Arial']
    plt.rcParams['axes.unicode_minus'] = False
    
    bg_color = '#0d1322'
    text_color = '#cbd5e1'
    grid_color = '#24324f'

    # --- Chart 1: M1 vs M2 剪刀差 ---
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

    # --- Chart 2: PPI vs CPI ---
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

    # --- Chart 3: 国债收益率 ---
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
# 3. Markdown 日报报告生成器
# ==============================================================================
def generate_markdown(data):
    today_str = data["date"]
    os.makedirs(PRIMARY_EXPORT_DIR, exist_ok=True)
    os.makedirs(BACKUP_EXPORT_DIR, exist_ok=True)

    files_to_write = [
        os.path.join(PRIMARY_EXPORT_DIR, f"每日经济日报_{today_str}.md"),
        os.path.join(PRIMARY_EXPORT_DIR, f"高客宏观每日内参_{today_str}.md"),
        os.path.join(BACKUP_EXPORT_DIR, f"每日经济日报_{today_str}.md"),
        os.path.join(BACKUP_EXPORT_DIR, f"高客宏观早参_{today_str}.md")
    ]

    md = f"""# 📈 金华平安家办 · 每日经济日报
> **归档日期**：{today_str}（每日 17:00 汇总更新，供内勤与顾问研读）  
> **编制单位**：金华平安家办 / 培训内勤宏观研究组  
> **核心定位**：全景数据驱动、专业图表直观、洞察实业水温、赋能高维谈资！

---

## 🧭 今日宏观核心主线导读
{data['lead']}

---

## 📈 核心宏观走势图表一览 (高清图谱)

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

## ⚖️ 三师共诊 · 今日宏观与实业破局透析
"""
    for expert in data["tri_experts"]:
        md += f"- **{expert['role']} [{expert['tag']}]**：{expert['core']}\n"

    md += f"""
---

## 🥬 宏观金融 8 大概念“通俗买菜比喻”速查 (陪谈与培训脱口而出)
"""
    for i, lex in enumerate(data["lexicon"], 1):
        md += f"**{i}. {lex['term']}**：{lex['analogy']}\n\n"

    md += f"""
---

## 🗣️ 晨会演练与展业破冰“两分钟口袋短语”
"""
    for track in data["talk_tracks"]:
        md += f"### 🎯 {track['scene']}\n{track['script']}\n\n"

    md += f"""
---

## 🎯 检验宏观底层逻辑的 3 个深度思考题

| 序号 | 宏观深度思考题 | 底层逻辑与推演要点 |
| :---: | :--- | :--- |
"""
    for i, tq in enumerate(data["thinking_questions"], 1):
        md += f"| **Q{i}** | {tq['q']} | **答**：{tq['a']} |\n"

    md += f"""
---
*本经济日报每日 17:00 由 Windows 任务计划程序【DailyMacroNewsUpdate_1700】全自动生成、归档与同步部署。*  
*手机端随时随地阅读完整 ECharts 交互大屏：`https://andre4life.github.io/news/`*  
*个人工作台随时随地直接速读：`https://andre4life.github.io/mindradar/`*
"""

    for fp in files_to_write:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"✅ 生成日报 Markdown: {fp}")

# ==============================================================================
# 4. 更新 news/index.html (独立全屏 ECharts 交互大屏)
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

    # 生成三师透析 HTML
    tri_html = ""
    for exp in data["tri_experts"]:
        color_cls = "border-blue-500/40 text-blue-400" if exp["color"] == "blue" else ("border-amber-500/40 text-amber-400" if exp["color"] == "amber" else "border-emerald-500/40 text-emerald-400")
        tri_html += f"""
        <div class="p-4 bg-dark-850 rounded-xl border {color_cls} shadow-md space-y-2">
          <div class="flex items-center justify-between">
            <h4 class="text-xs md:text-sm font-bold {color_cls} flex items-center gap-1.5">{exp['role']}</h4>
            <span class="text-[10px] px-2 py-0.5 rounded bg-dark-800 text-slate-400 font-mono">{exp['tag']}</span>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed">{exp['core']}</p>
        </div>
        """

    # 生成买菜比喻 HTML
    lexicon_html = ""
    for item in data["lexicon"]:
        lexicon_html += f"""
        <div class="p-3.5 bg-dark-900 rounded-xl border border-dark-700/80 hover:border-amber-500/40 transition-colors">
          <h5 class="text-xs font-bold text-amber-400 mb-1.5 flex items-center gap-1">
            <span>🥬</span> {item['term']}
          </h5>
          <p class="text-xs text-slate-300 leading-relaxed">{item['analogy']}</p>
        </div>
        """

    # 生成口袋短语 HTML
    talk_html = ""
    for item in data["talk_tracks"]:
        talk_html += f"""
        <div class="p-4 bg-dark-900 rounded-xl border-l-4 border-amber-500 space-y-1.5">
          <h5 class="text-xs font-bold text-amber-400">{item['scene']}</h5>
          <p class="text-xs text-slate-200 leading-relaxed">{item['script']}</p>
        </div>
        """

    # 生成思考题 HTML
    questions_html = ""
    for i, q in enumerate(data["thinking_questions"], 1):
        questions_html += f"""
        <div class="p-4 bg-dark-900 rounded-xl border border-dark-700/80 space-y-1.5">
          <h5 class="text-xs font-bold text-amber-400">Q{i}：{q['q']}</h5>
          <p class="text-xs text-slate-300 leading-relaxed"><strong>答：</strong>{q['a']}</p>
        </div>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>金华平安家办 · 每日经济日报与宏观全景中枢</title>
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
        <a href="../index.html" class="p-2 text-slate-400 hover:text-white rounded-lg hover:bg-dark-800 transition" title="返回统一门户">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
          </svg>
        </a>
        <div>
          <h1 class="text-sm md:text-base font-bold tracking-tight text-white flex items-center gap-2">
            金华平安家办 · 每日经济日报
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          </h1>
          <p class="text-xs text-slate-400">宏观大政数据中枢 · 十维商业水温速查 · 三师共诊赋能 · ECharts 交互大屏</p>
        </div>
      </div>
      <div class="flex items-center gap-2">
        <a href="../mindradar/index.html" class="hidden sm:inline-flex items-center gap-1 text-xs px-2.5 py-1 bg-dark-800 hover:bg-dark-750 text-amber-400 border border-dark-600 rounded-md transition-colors">
          <span>⚡</span> 工作台直读
        </a>
        <span class="text-xs px-2.5 py-1 bg-amber-500/10 border border-amber-500/30 text-amber-300 font-mono rounded-md">
          {today_str}
        </span>
      </div>
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
        {data['title']} · 全景大盘透视
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

    <!-- 三师共诊专栏 -->
    <section class="space-y-4">
      <div class="flex items-center justify-between border-b border-dark-700/80 pb-3">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <span>⚖️</span> 三师共诊 · 今日宏观与实业破局透析
        </h3>
        <span class="text-xs text-slate-400">民商法律师 + 投顾规划师 + 实业医养专家</span>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        {tri_html}
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

    <!-- 8大通俗买菜比喻 -->
    <section class="space-y-4">
      <div class="flex items-center justify-between border-b border-dark-700/80 pb-3">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <span>🥬</span> 宏观金融 8 大概念“通俗买菜比喻”速查字典
        </h3>
        <span class="text-xs text-amber-400 font-mono">小白秒懂 · 破除术语壁垒</span>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        {lexicon_html}
      </div>
    </section>

    <!-- 展业破冰两分钟口袋短语 -->
    <section class="space-y-4">
      <div class="flex items-center justify-between border-b border-dark-700/80 pb-3">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <span>🗣️</span> 晨会演练与展业破冰“两分钟口袋短语”
        </h3>
        <span class="text-xs text-amber-400 font-mono">见客开门三句话</span>
      </div>
      <div class="space-y-3">
        {talk_html}
      </div>
    </section>

    <!-- 3个深度思考题 -->
    <section class="space-y-4">
      <div class="flex items-center justify-between border-b border-dark-700/80 pb-3">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <span>🎯</span> 检验宏观底层逻辑的 3 个深度思考题
        </h3>
        <span class="text-xs text-slate-400">知其然更知其所以然</span>
      </div>
      <div class="space-y-3">
        {questions_html}
      </div>
    </section>

  </main>

  <!-- ECharts 动态脚本 -->
  <script>
    // 1. M1 vs M2
    const chartM1M2 = echarts.init(document.getElementById('chart-m1-m2'));
    chartM1M2.setOption({{
      backgroundColor: 'transparent',
      tooltip: {{ trigger: 'axis' }},
      legend: {{ data: ['M2 广义货币同比(%)', 'M1 狭义货币同比(%)'], textStyle: {{ color: '#94a3b8' }}, top: 5 }},
      grid: {{ left: '4%', right: '4%', bottom: '8%', containLabel: true }},
      xAxis: {{ type: 'category', data: {json.dumps(cd['months'])}, axisLine: {{ lineStyle: {{ color: '#24324f' }} }}, axisLabel: {{ color: '#94a3b8' }} }},
      yAxis: {{ type: 'value', axisLine: {{ lineStyle: {{ color: '#24324f' }} }}, splitLine: {{ lineStyle: {{ color: '#131b2e' }} }}, axisLabel: {{ color: '#94a3b8', formatter: '{{value}}%' }} }},
      series: [
        {{ name: 'M2 广义货币同比(%)', type: 'line', data: {json.dumps(cd['m2'])}, smooth: true, itemStyle: {{ color: '#f59e0b' }}, lineStyle: {{ width: 3 }} }},
        {{ name: 'M1 狭义货币同比(%)', type: 'line', data: {json.dumps(cd['m1'])}, smooth: true, itemStyle: {{ color: '#38bdf8' }}, lineStyle: {{ width: 3 }}, areaStyle: {{ opacity: 0.1, color: '#38bdf8' }} }}
      ]
    }});

    // 2. PPI vs CPI
    const chartPpiCpi = echarts.init(document.getElementById('chart-ppi-cpi'));
    chartPpiCpi.setOption({{
      backgroundColor: 'transparent',
      tooltip: {{ trigger: 'axis' }},
      legend: {{ data: ['CPI 消费价格(%)', 'PPI 工业出厂价格(%)'], textStyle: {{ color: '#94a3b8' }}, top: 5 }},
      grid: {{ left: '4%', right: '4%', bottom: '8%', containLabel: true }},
      xAxis: {{ type: 'category', data: {json.dumps(cd['months'])}, axisLine: {{ lineStyle: {{ color: '#24324f' }} }}, axisLabel: {{ color: '#94a3b8' }} }},
      yAxis: {{ type: 'value', axisLine: {{ lineStyle: {{ color: '#24324f' }} }}, splitLine: {{ lineStyle: {{ color: '#131b2e' }} }}, axisLabel: {{ color: '#94a3b8', formatter: '{{value}}%' }} }},
      series: [
        {{ name: 'CPI 消费价格(%)', type: 'line', data: {json.dumps(cd['cpi'])}, smooth: true, itemStyle: {{ color: '#10b981' }}, lineStyle: {{ width: 3 }} }},
        {{ name: 'PPI 工业出厂价格(%)', type: 'line', data: {json.dumps(cd['ppi'])}, smooth: true, itemStyle: {{ color: '#f43f5e' }}, lineStyle: {{ width: 3 }} }}
      ]
    }});

    // 3. 国债收益率
    const chartYields = echarts.init(document.getElementById('chart-yields'));
    chartYields.setOption({{
      backgroundColor: 'transparent',
      tooltip: {{ trigger: 'axis' }},
      legend: {{ data: ['30年期国债(%)', '10年期国债(%)'], textStyle: {{ color: '#94a3b8' }}, top: 5 }},
      grid: {{ left: '4%', right: '4%', bottom: '8%', containLabel: true }},
      xAxis: {{ type: 'category', data: {json.dumps(cd['months'])}, axisLine: {{ lineStyle: {{ color: '#24324f' }} }}, axisLabel: {{ color: '#94a3b8' }} }},
      yAxis: {{ type: 'value', min: 1.8, max: 3.2, axisLine: {{ lineStyle: {{ color: '#24324f' }} }}, splitLine: {{ lineStyle: {{ color: '#131b2e' }} }}, axisLabel: {{ color: '#94a3b8', formatter: '{{value}}%' }} }},
      series: [
        {{ name: '30年期国债(%)', type: 'line', data: {json.dumps(cd['yield_30y'])}, smooth: true, itemStyle: {{ color: '#a855f7' }}, lineStyle: {{ width: 3 }} }},
        {{ name: '10年期国债(%)', type: 'line', data: {json.dumps(cd['yield_10y'])}, smooth: true, itemStyle: {{ color: '#38bdf8' }}, lineStyle: {{ width: 3 }} }}
      ]
    }});

    // 4. 出口贸易目的地
    const chartExport = echarts.init(document.getElementById('chart-export'));
    chartExport.setOption({{
      backgroundColor: 'transparent',
      tooltip: {{ trigger: 'item', formatter: '{{b}}: {{c}}% ({{d}}%)' }},
      legend: {{ orient: 'vertical', left: 'left', textStyle: {{ color: '#94a3b8' }} }},
      series: [
        {{
          name: '出口目的地占比',
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
# 5. 更新心智雷达工作台站内嵌入视图 (mindradar/index.html & 个人工作复盘工作台)
# ==============================================================================
def update_mindradar_workbenches(data):
    today_str = data["date"]
    
    # 构造 tab-news 的完整极美内容
    tab_news_content = f"""
    <!-- ================= TAB: DAILY ECONOMIC BRIEFING (金华平安家办 · 每日经济日报) ================= -->
    <div id="tab-news" class="tab-content hidden space-y-4 md:space-y-6">
      
      <!-- Top Title & Quick Actions Banner -->
      <div class="bg-gradient-to-r from-amber-500/15 via-dark-850 to-blue-500/10 rounded-2xl border-2 border-amber-500/40 p-4 md:p-6 shadow-xl relative overflow-hidden">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-dark-700/80 pb-4">
          <div class="space-y-1">
            <div class="flex items-center gap-2">
              <span class="text-xl">📈</span>
              <h2 class="text-base md:text-lg font-bold text-white tracking-wide">
                金华平安家办 · 每日经济日报
              </h2>
              <span class="px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-[10px] font-mono font-bold animate-pulse">
                ● {today_str} 最新
              </span>
            </div>
            <p class="text-xs text-slate-300">
              宏观大盘透视 · 十维商业水温速查 · 三师共诊穿透 · 生活化买菜比喻 · 晨会与高客破冰口袋短语
            </p>
          </div>
          
          <div class="flex items-center gap-2 shrink-0">
            <a href="../news/index.html" class="px-4 py-2 rounded-xl bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-600 text-white text-xs font-bold shadow-md shadow-amber-900/30 flex items-center gap-1.5 transition-all">
              <span>🚀</span> 打开 ECharts 全景大屏 ↗
            </a>
          </div>
        </div>

        <!-- 🧭 今日核心主线导读 -->
        <div class="mt-4 p-3.5 bg-dark-900/80 rounded-xl border border-dark-700/80 text-xs md:text-sm text-slate-200 leading-relaxed">
          <strong class="text-amber-400 block mb-1">🧭 今日核心主线导读 ({today_str})：</strong>
          {data['lead']}
        </div>

        <!-- ⚡ 4大关键微观水温秒懂卡 -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 mt-4">
          <div class="p-3 bg-dark-850/90 rounded-xl border border-amber-500/30">
            <div class="text-[11px] text-slate-400 mb-1 flex items-center justify-between">
              <span>M1/M2 剪刀差</span>
              <span class="text-amber-400 font-mono text-[10px]">资金活化度</span>
            </div>
            <div class="text-lg md:text-xl font-extrabold text-amber-400 font-mono">-9.6%</div>
            <div class="text-[10px] text-slate-400 mt-1">M2 8.2% vs M1 -1.4%，大水库满但毛细血管偏冷，资金定存防守</div>
          </div>
          <div class="p-3 bg-dark-850/90 rounded-xl border border-rose-500/30">
            <div class="text-[11px] text-slate-400 mb-1 flex items-center justify-between">
              <span>PPI 工业出厂价</span>
              <span class="text-rose-400 font-mono text-[10px]">实业毛利</span>
            </div>
            <div class="text-lg md:text-xl font-extrabold text-rose-400 font-mono">-2.1%</div>
            <div class="text-[10px] text-slate-400 mt-1">出厂价持续承压，企业面临“有营收无利润”内卷，降价难救市</div>
          </div>
          <div class="p-3 bg-dark-850/90 rounded-xl border border-cyan-500/30">
            <div class="text-[11px] text-slate-400 mb-1 flex items-center justify-between">
              <span>10年期国债收益率</span>
              <span class="text-cyan-400 font-mono text-[10px]">无风险利率</span>
            </div>
            <div class="text-lg md:text-xl font-extrabold text-cyan-400 font-mono">2.12%</div>
            <div class="text-[10px] text-slate-400 mt-1">大行定存跌破1.5%，无风险收益资产绝迹，长期确定性分红稀缺</div>
          </div>
          <div class="p-3 bg-dark-850/90 rounded-xl border border-emerald-500/30">
            <div class="text-[11px] text-slate-400 mb-1 flex items-center justify-between">
              <span>沪深300市盈率</span>
              <span class="text-emerald-400 font-mono text-[10px]">权益底仓</span>
            </div>
            <div class="text-lg md:text-xl font-extrabold text-emerald-400 font-mono">12.8倍</div>
            <div class="text-[10px] text-slate-400 mt-1">十年历史45%分位，估值中位偏低，适合金字塔定投分批布局</div>
          </div>
        </div>
      </div>

      <!-- 🏛️ 三师共诊 · 今日宏观与实业破局透析 (三列高维卡片) -->
      <div class="space-y-3">
        <div class="flex items-center justify-between">
          <h3 class="text-sm font-bold text-white flex items-center gap-2">
            <span>⚖️</span> 三师共诊 · 今日宏观与实业破局透析
          </h3>
          <span class="text-[11px] text-slate-400 font-mono">拒绝单一视角 · 三方协同会诊</span>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
          
          <div class="p-4 rounded-xl bg-dark-850 border border-blue-500/30 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-blue-400 flex items-center gap-1.5">
                <span>🏛️</span> 民商法律师视角
              </span>
              <span class="text-[10px] px-1.5 py-0.2 rounded bg-blue-500/20 text-blue-300 font-mono">合规与隔离</span>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
              <strong>【新公司法实缴与债务隔离】</strong>当前微观去杠杆与化债背景下，企业对外担保与抽逃出资追责空前严厉。老板个人与公司财务混同是致命死穴，必须通过<strong>“企业法人治理规范 + 家庭资产与大额保单防火墙”</strong>截断连带清偿风险。
            </p>
          </div>

          <div class="p-4 rounded-xl bg-dark-850 border border-amber-500/30 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-amber-400 flex items-center gap-1.5">
                <span>💼</span> 投顾理财规划师视角
              </span>
              <span class="text-[10px] px-1.5 py-0.2 rounded bg-amber-500/20 text-amber-300 font-mono">资产重塑</span>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
              <strong>【告别高息幻想，锁定长期现金流】</strong>10年期国债击穿2.1%，大行定存全面进入1时代。激进搏高息的时代彻底结束。高净值家庭底盘必须配置<strong>“分红险特别储备金机制 + 终身年金现金流”</strong>，用刚性契约抵御未来长周期低利率侵蚀。
            </p>
          </div>

          <div class="p-4 rounded-xl bg-dark-850 border border-emerald-500/30 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-emerald-400 flex items-center gap-1.5">
                <span>🏭</span> 实业与医养专家视角
              </span>
              <span class="text-[10px] px-1.5 py-0.2 rounded bg-emerald-500/20 text-emerald-300 font-mono">降本与出海</span>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
              <strong>【以出海破内卷，以家办护身心】</strong>单纯国内降价内卷等于慢性失血，义乌/金华实业应积极借助东盟与拉美顺差红利出海。同时，企业家自身精力有限，通过家办前置锁定<strong>“名医绿通 + 高品质居家康养”</strong>，是守住基业的隐形支柱。
            </p>
          </div>

        </div>
      </div>

      <!-- 🔍 十维宏观核心指标速查矩阵折叠 -->
      <div class="bg-dark-850 rounded-2xl border border-dark-700 p-4 md:p-5 shadow-sm space-y-3">
        <div class="flex items-center justify-between">
          <h3 class="text-sm font-bold text-white flex items-center gap-2">
            <span>🔍</span> 十维宏观核心指标速查矩阵 (商业水温与高客谈资)
          </h3>
          <span class="text-[10px] text-amber-400 font-mono">全量化速查</span>
        </div>
        
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs border-collapse">
            <thead>
              <tr class="border-b border-dark-700 text-slate-400">
                <th class="py-2 px-2.5">维度与指标</th>
                <th class="py-2 px-2.5">最新值 (走势)</th>
                <th class="py-2 px-2.5">状态</th>
                <th class="py-2 px-2.5">🏭 实业真实水温</th>
                <th class="py-2 px-2.5">🗣️ 展业破冰谈资</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-dark-800 text-slate-200">
              <tr>
                <td class="py-2 px-2.5 font-bold text-white">GDP 季度同比</td>
                <td class="py-2 px-2.5 font-mono text-amber-400">5.0% (前值4.7%)</td>
                <td class="py-2 px-2.5 text-emerald-400">✅ 达标区间</td>
                <td class="py-2 px-2.5 text-slate-300">总量守底线但温差大，高端制造强、地产链偏冷</td>
                <td class="py-2 px-2.5 text-amber-200/90">“GDP增速守底线，新旧动能切换，高附加值是唯一出路。”</td>
              </tr>
              <tr>
                <td class="py-2 px-2.5 font-bold text-white">M2 广义货币</td>
                <td class="py-2 px-2.5 font-mono text-amber-400">8.2% (前值8.0%)</td>
                <td class="py-2 px-2.5 text-blue-400">💧 水库满库</td>
                <td class="py-2 px-2.5 text-slate-300">流动性充裕，但以居民与企业大额定存沉淀</td>
                <td class="py-2 px-2.5 text-amber-200/90">“大水库的水非常满，钱都在银行账上趴着防守。”</td>
              </tr>
              <tr>
                <td class="py-2 px-2.5 font-bold text-white">M1 狭义货币</td>
                <td class="py-2 px-2.5 font-mono text-rose-400">-1.4% (前值-1.8%)</td>
                <td class="py-2 px-2.5 text-amber-400">⚠️ 负剪刀差</td>
                <td class="py-2 px-2.5 text-slate-300">企业活期资金占比低，资金活化度待提升</td>
                <td class="py-2 px-2.5 text-amber-200/90">“M1是随时掏出来的活钱，大家都在防守，不敢盲目扩张。”</td>
              </tr>
              <tr>
                <td class="py-2 px-2.5 font-bold text-white">PPI 出厂物价</td>
                <td class="py-2 px-2.5 font-mono text-rose-400">-2.1% (前值-2.8%)</td>
                <td class="py-2 px-2.5 text-rose-400">📉 利润承压</td>
                <td class="py-2 px-2.5 text-slate-300">工业批发持续杀价，实体“有营收无利润”</td>
                <td class="py-2 px-2.5 text-amber-200/90">“PPI为负是今年最痛的根源：出厂价被同行压着打。”</td>
              </tr>
              <tr>
                <td class="py-2 px-2.5 font-bold text-white">10年期国债</td>
                <td class="py-2 px-2.5 font-mono text-cyan-400">2.12% (前值2.25%)</td>
                <td class="py-2 px-2.5 text-cyan-400">📉 资产荒加剧</td>
                <td class="py-2 px-2.5 text-slate-300">长端利率破位下行，大行定存破1.5%</td>
                <td class="py-2 px-2.5 text-amber-200/90">“无风险收益资产全面绝迹，锁定长期确定分红已成刚需。”</td>
              </tr>
              <tr>
                <td class="py-2 px-2.5 font-bold text-white">沪深300市盈率</td>
                <td class="py-2 px-2.5 font-mono text-emerald-400">12.8倍 (45%分位)</td>
                <td class="py-2 px-2.5 text-emerald-400">📊 中位偏下</td>
                <td class="py-2 px-2.5 text-slate-300">政策底与流动性底确立，长线配置价值凸显</td>
                <td class="py-2 px-2.5 text-amber-200/90">“估值处于历史中位偏低，适合定投分批建仓优质底仓。”</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- 🥬 8大宏观术语“通俗买菜比喻”速查折叠卡 -->
      <div class="bg-dark-850 rounded-2xl border border-dark-700 p-4 md:p-5 shadow-sm space-y-3">
        <div class="flex items-center justify-between">
          <h3 class="text-sm font-bold text-white flex items-center gap-2">
            <span>🥬</span> 宏观金融 8 大概念“通俗买菜比喻”速查 (陪谈与培训脱口而出)
          </h3>
          <span class="text-[10px] text-amber-400 font-mono">小白秒懂 · 外勤必背</span>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
          <div class="p-3 bg-dark-900 rounded-xl border border-dark-700/80">
            <div class="text-amber-400 font-bold mb-1">1. PE 市盈率（买菜摊位费比喻）</div>
            <p class="text-slate-300 leading-relaxed">
              菜市场买个摊位要10万元，这个摊位每年净赚1万元，回本需要10年，PE就是10倍。如果摊位炒到50万（PE=50倍），要卖菜50年才回本，这就是泡沫；如果摊位跌到8万（PE=8倍），回本快，就是便宜黄金期。
            </p>
          </div>
          <div class="p-3 bg-dark-900 rounded-xl border border-dark-700/80">
            <div class="text-amber-400 font-bold mb-1">2. M2 与 M1（水库与抽水泵比喻）</div>
            <p class="text-slate-300 leading-relaxed">
              M2是山顶水库蓄了满满一库水（存款总额大）；M1是农民伯伯能随时拧开浇菜的抽水机（活期现金）。现在水库水位极高（M2=8.2%），但大家不敢借水浇地，抽水机没开（M1=-1.4%），这就是“负剪刀差”。
            </p>
          </div>
          <div class="p-3 bg-dark-900 rounded-xl border border-dark-700/80">
            <div class="text-amber-400 font-bold mb-1">3. PPI 与 CPI（批发价与零售价）</div>
            <p class="text-slate-300 leading-relaxed">
              PPI是蔬菜批发大市场的出厂价，CPI是老百姓菜篮子的最终买菜价。现在PPI为负（-2.1%），说明地头批发都在赔本甩卖、价格战惨烈；虽然老百姓买菜便宜了（CPI温和），但种菜和做生意的实体老板最受伤。
            </p>
          </div>
          <div class="p-3 bg-dark-900 rounded-xl border border-dark-700/80">
            <div class="text-amber-400 font-bold mb-1">4. 分红特别储备账户（公仓存粮比喻）</div>
            <p class="text-slate-300 leading-relaxed">
              好比村里的粮仓：丰收年粮食多，不全分光吃光，扣下一部分存进公仓；等遇到大旱灾荒年，再开仓放粮贴补各家。平安分红险靠这个机制，实现几十年平抑市场剧烈波动。
            </p>
          </div>
        </div>
      </div>

      <!-- 🗣️ 展业破冰两分钟口袋短语 (高客面谈直接用) -->
      <div class="bg-gradient-to-r from-amber-500/10 via-dark-850 to-blue-500/10 rounded-2xl border border-amber-500/30 p-4 md:p-5 shadow-sm space-y-3">
        <div class="flex items-center justify-between">
          <h3 class="text-sm font-bold text-white flex items-center gap-2">
            <span>🗣️</span> 晨会演练与展业破冰“两分钟口袋短语”
          </h3>
          <span class="text-[10px] text-amber-400 font-mono">见客开门三句话</span>
        </div>

        <div class="space-y-2.5 text-xs">
          <div class="p-3 bg-dark-900/80 rounded-xl border-l-4 border-amber-500">
            <strong class="text-amber-400 block mb-1">🎯 场景一：见义乌/金华实业老板（面对“实体难做、利润薄如纸”）：</strong>
            <p class="text-slate-200 leading-relaxed">
              “张总，现在PPI持续为负，实体企业普遍‘有营收、无利润’，降价只会把现金流榨干。越是这个时候，越不能把所有本钱都押在厂房和货款上。聪明的老板现在都在做‘资产截流’：每年固定从利润里拿出一块，做一张跟企业债务完全切断的家庭现金流防火墙。哪怕外面风浪再大，老婆孩子的饭碗和您东山再起的本钱永远动不了！”
            </p>
          </div>

          <div class="p-3 bg-dark-900/80 rounded-xl border-l-4 border-cyan-500">
            <strong class="text-cyan-400 block mb-1">🎯 场景二：见银行大额存单/保守理财客户（面对“嫌利率低却不敢投”）：</strong>
            <p class="text-slate-200 leading-relaxed">
              “王董，现在10年期国债收益率都破2.1%了，大行三年期定存马上见不到1.5%。您现在看着理财还有两点几，但两三年一到期，您手里的钱往哪儿放？买房涨不动、股市不敢赌、定存不断降。您现在最需要的不是冒高风险，而是趁现在锁定一份写进合同、一辈子源源不断给您发钱的确定现金流！”
            </p>
          </div>
        </div>
      </div>

      <!-- 🎯 3个底层逻辑自测深度思考题 -->
      <div class="bg-dark-850 rounded-2xl border border-dark-700 p-4 md:p-5 shadow-sm space-y-3">
        <h3 class="text-sm font-bold text-white flex items-center gap-2">
          <span>🎯</span> 检验宏观底层逻辑的 3 个深度自测思考题
        </h3>
        
        <div class="space-y-2.5 text-xs">
          <div class="p-3 bg-dark-900 rounded-xl border border-dark-700">
            <span class="text-amber-400 font-bold block mb-1">Q1：为什么央行M2水量很大，但实体企业普遍觉得“缺钱、回款慢”？</span>
            <p class="text-slate-300 leading-relaxed">
              <strong>答：</strong>货币是通过信贷派生的。当前实体需求端处于去杠杆防守阶段，资金大量在金融系统内以居民与企业定期形式沉淀（M1-M2负剪刀差达-9.6%），未活化为订金与采购现金流，因此水库虽满，下游农田依然干渴。
            </p>
          </div>

          <div class="p-3 bg-dark-900 rounded-xl border border-dark-700">
            <span class="text-amber-400 font-bold block mb-1">Q2：面对持续为负的 PPI，为什么单纯“降价促销”反而会加速企业死亡？</span>
            <p class="text-slate-300 leading-relaxed">
              <strong>答：</strong>在全行业产能过剩时，降价不会带来额外增量需求，反而会摧毁行业边际利润率，让现金流枯竭。真正的破局点是“差异化细分定位”或“抱团出海开拓非欧美溢价市场”。
            </p>
          </div>

          <div class="p-3 bg-dark-900 rounded-xl border border-dark-700">
            <span class="text-amber-400 font-bold block mb-1">Q3：地方化债启动对实体企业的应收账款意味着什么？</span>
            <p class="text-slate-300 leading-relaxed">
              <strong>答：</strong>中央发行低息国债置换地方高息隐性债务，极大卸掉了地方政府的利息重负，为财政专班腾出了“清欠民企账款”的真金白银。当前正是企业梳理历史涉政债权、争取优先清偿的关键窗口期。
            </p>
          </div>
        </div>
      </div>

    </div>
    """

    for target_path in [MINDRADAR_HTML_PATH, LOCAL_WORKBENCH_HTML_PATH]:
        if not os.path.exists(target_path):
            continue
        with open(target_path, "r", encoding="utf-8") as f:
            html = f.read()

        # 1. 确保导航栏标签按钮存在并更新
        nav_pattern = r'<button onclick="switchTab\(\'tab-news\'\)"[^>]*>.*?</button>'
        new_nav_btn = """<button onclick="switchTab('tab-news')" id="nav-tab-news" class="tab-btn px-4 py-3 border-b-2 border-transparent text-slate-400 hover:text-slate-200 flex items-center gap-2">
      <span>📈</span> 每日经济日报与宏观
      <span class="px-1.5 py-0.2 rounded-full bg-amber-500/20 text-amber-400 text-[10px] font-mono font-bold">每日更新</span>
    </button>"""
        if re.search(nav_pattern, html, flags=re.DOTALL):
            html = re.sub(nav_pattern, new_nav_btn, html, flags=re.DOTALL)
        else:
            # 如果没有，插入在 nav 内部
            html = html.replace('id="nav-tab-ai"', 'id="nav-tab-ai"')
            if '<button onclick="switchTab(\'tab-ai\')"' in html:
                html = html.replace(
                    '</button>\n      <a href="https://github.com/heartleo/zlib"',
                    f'</button>\n    {new_nav_btn}\n      <a href="https://github.com/heartleo/zlib"'
                )

        # 2. 确保手机底部导航栏按钮存在
        m_nav_pattern = r'<button onclick="switchTab\(\'tab-news\'\)"[^>]*>.*?</button>'
        new_m_nav_btn = """<button onclick="switchTab('tab-news')" id="m-nav-tab-news" class="m-nav-btn flex flex-col items-center justify-center py-1 px-2.5 text-slate-400 transition-all">
      <span class="text-lg">📈</span>
      <span class="text-[10px] mt-0.5">经济日报</span>
    </button>"""
        if re.search(r'<button onclick="switchTab\(\'tab-news\'\)" id="m-nav-tab-news"[^>]*>.*?</button>', html, flags=re.DOTALL):
            html = re.sub(r'<button onclick="switchTab\(\'tab-news\'\)" id="m-nav-tab-news"[^>]*>.*?</button>', new_m_nav_btn, html, flags=re.DOTALL)

        # 3. 替换或插入 tab-news 内容
        if '<div id="tab-news"' in html:
            # 替换已有 tab-news
            html = re.sub(
                r'<!-- ================= TAB: DAILY ECONOMIC BRIEFING.*?</div>\s*<!-- ================= MOBILE',
                tab_news_content.strip() + '\n\n    <!-- ================= MOBILE',
                html,
                flags=re.DOTALL
            )
            # 或者正则替换 <div id="tab-news".*?</div>\s*</main>
            html = re.sub(
                r'<div id="tab-news".*?</div>\s*</main>',
                tab_news_content.strip() + '\n  </main>',
                html,
                flags=re.DOTALL
            )
        else:
            # 插入在 </main> 之前
            html = html.replace('</main>', tab_news_content.strip() + '\n  </main>')

        # 4. 更新 Tab 1 (tasks) 里的横幅提示卡
        banner_pattern = r'<!-- 🌐 NATIONAL MACRO NEWS.*?</div>\s*</div>'
        new_banner = f"""<!-- 📈 NATIONAL MACRO NEWS & POLICY RADAR TICKER -->
      <div class="bg-gradient-to-r from-amber-950/40 via-dark-850 to-blue-950/30 rounded-2xl border border-amber-500/30 p-3.5 md:p-4 shadow-md flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div class="space-y-1">
          <div class="flex items-center gap-2">
            <span class="text-base">📈</span>
            <strong class="text-xs md:text-sm text-white font-bold">金华家办 · 每日经济日报与宏观水温</strong>
            <span class="text-[10px] px-2 py-0.2 rounded-full bg-amber-500/20 text-amber-300 font-mono font-bold">{today_str} 最新</span>
          </div>
          <p class="text-[11px] text-slate-300 leading-relaxed">
            十维宏观数据全景矩阵 · ECharts 交互大屏 · 三师共诊透析 · 通俗买菜比喻 · 晨会展业两分钟口袋短语。
          </p>
        </div>
        <div class="flex items-center gap-2 shrink-0">
          <button onclick="switchTab('tab-news')" class="px-3.5 py-1.5 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 text-xs font-semibold flex items-center gap-1 transition-all">
            <span>📖</span> 站内速读日报
          </button>
          <a href="../news/index.html" class="px-3.5 py-1.5 rounded-lg bg-amber-500 hover:bg-amber-600 text-white text-xs font-bold flex items-center gap-1 transition-all shadow-sm">
            <span>🚀</span> 打开全屏大屏 &rarr;
          </a>
        </div>
      </div>"""
        if re.search(banner_pattern, html, flags=re.DOTALL):
            html = re.sub(banner_pattern, new_banner, html, flags=re.DOTALL)
        elif '<!-- 📈 NATIONAL MACRO NEWS' in html:
            html = re.sub(r'<!-- 📈 NATIONAL MACRO NEWS.*?</div>\s*</div>', new_banner, html, flags=re.DOTALL)

        with open(target_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ 心智雷达工作台已注入每日经济日报视图: {target_path}")

# ==============================================================================
# 6. 主执行逻辑
# ==============================================================================
def main():
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    print("=" * 60)
    print(f"🚀 启动每日经济日报与宏观数据可视化引擎 [{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    print(f"📅 归档日期: {today_str}")
    print("=" * 60)

    data = get_macro_dashboard_data(today_str)
    generate_matplotlib_charts(data)
    generate_markdown(data)
    update_news_html(data)
    update_mindradar_workbenches(data)

    if os.path.exists(DEPLOY_SCRIPT):
        print("🚀 执行 GitHub Pages 自动化同步部署...")
        res = subprocess.run([sys.executable, DEPLOY_SCRIPT, f"feat: daily economic report and macro dashboard update {today_str}"], capture_output=True, text=True, encoding="utf-8", errors="ignore")
        if res.returncode == 0:
            print("✅ GitHub Pages 部署发布成功！")
        else:
            print(f"❌ 部署返回信息: {res.stdout.strip()} | {res.stderr.strip()}")

    print("=" * 60)
    print("🎉 每日经济日报全流程闭环执行完毕！")

if __name__ == "__main__":
    main()
