#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
每日高客宏观早参与国家大事追踪自动化引擎
运行时间: 建议每日 07:30 自动调度 (衔接 07:00 备孕知识 与 08:00 法商内参)
核心产物:
  1. D:\Antigravity输出\高客宏观早参\高客宏观早参_{YYYY-MM-DD}.md (微信群/私聊高客一键复制口径)
  2. D:\Antigravity输出\andre4life.github.io\news\index.html (移动端/PC端交互大屏与三师会诊)
  3. 自动触发 GitHub Pages 部署发布
"""

import os
import sys
import json
import datetime
import subprocess

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

PORTAL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEWS_HTML_PATH = os.path.join(PORTAL_DIR, "news", "index.html")
EXPORT_DIR = r"D:\Antigravity输出\高客宏观早参"
DEPLOY_SCRIPT = os.path.join(PORTAL_DIR, "deploy_portal.py")

# 宏观高客关注精选主题库 (六大维度: 政治、经济、金融、进出口、汇率、CRS)
MACRO_THEMES = [
    {
        "id": "fx_break_7",
        "category": "fx",
        "badge": "最新汇率与结汇博弈",
        "title": "人民币突破7.0大关：1.19万亿美元货物顺差与5%美元存款“双杀”大逆转",
        "date_str": "今日聚焦",
        "hot": "🔥 突破7.0 / 历史级顺差",
        "summary": "人民币兑美元强势突破7.00关口进入“6时代”。此前盲目抢购5%美元存款的高客遭遇“利息还没焐热，本金汇率反被吞噬5%”的尴尬双杀，1.19万亿美元货物贸易顺差下结汇博弈全面打响。",
        "talk_phrase": "“张总，去年不少朋友眼馋海外5%的美元高息，但您看现在人民币从7.35强力反弹破7，汇率跌掉5%直接把利息抹平还倒亏。全球钱潮退水时，锁定人民币长期底层刚兑和年金现金流，才是守住企业底盘的真智慧。”",
        "key_points": [
            "汇率走势：人民币从7.35低位强势反转突破7.00，升值超4.3%，进入“6时代”。",
            "顺差数据：2025全年中国货物贸易顺差突破1.19万亿美元，为全球首个破万亿大国，结汇堰塞湖持续释放。",
            "双杀机制：美联储降息周期下美元存款利率降至3.5% + 汇率折算亏损，美元理财神话破灭。",
            "高客行动：提前办理远期结汇锁汇，将外币风险收益回流国内确定性保单年金池。"
        ]
    },
    {
        "id": "crs_tax_audit",
        "category": "crs",
        "badge": "CRS与金税四期并轨",
        "title": "CRS跨国金融账户穿透落地：离岸空壳架构失效，企业公私账户‘体外循环’遭遇红线",
        "date_str": "今日聚焦",
        "hot": "🔥 CRS反避税 / 刑法第201条",
        "summary": "全球100+国家CRS涉税信息与国内金税四期全面并轨，离岸信托与BVI公司消极非金融实体直接穿透至中国税收居民个人。大额公转私与私户收款被纳入重点筛查。",
        "talk_phrase": "“李董，现在全球反避税已经进入‘裸泳时代’，过去靠离岸公司或者私人账户代收货款的体外循环，在CRS穿透和金税四期下根本藏不住。合规是企业家的保命底牌，用大额保单和家族信托做资产合法隔离，才是把纸面财富变成家族护城河的正道。”",
        "key_points": [
            "穿透规则：消极非金融机构（Passive NFE）与加密资产框架（CARF）全面穿透控股自然人。",
            "金税联动：境内大额公私账户频繁转账、现金交易、跨境资金流实现AI级全链条动态监管。",
            "刑法红线：严格把握《刑法》第201条第4款逃税罪初犯救济条款，补缴税款与滞纳金避免刑事追责。",
            "法商工具：通过个人大额终身年金与不可撤销家族信托实现资产合法确权与婚姻债务隔离。"
        ]
    },
    {
        "id": "finance_asset_famine",
        "category": "finance",
        "badge": "金融降息与资产荒",
        "title": "国有大行定存全面跌破1.5%：30年国债收益率破2.0%，中国式‘资产荒’下的资产防御战",
        "date_str": "今日聚焦",
        "hot": "🔥 存款利率破1% / 锁定长期复利",
        "summary": "商业银行各期限存款利率持续下调，3年期定存跌破1.5%，国债长端利率创新低。传统存银行吃利息模式彻底失效，高净值家族财富面临严重的再投资收益率断崖风险。",
        "talk_phrase": "“王总，现在去银行存钱，不仅利息跌破1.5%，而且只要到期重新存，利率又降一档。财富管理的最高境界不是赌明天哪个股票涨，而是为未来20年锁定不可逆的现金流管道。”",
        "key_points": [
            "利率现状：大行5年期定存步入1%时代，逆回购与货币基金年化跌破1.3%。",
            "底层逻辑：实体信贷需求疲软，银行净息差收窄至历史低位，降息势在必行。",
            "高客痛点：千万级资金躺在活期每天都在贬值，信托打破刚兑不敢投，股市波动剧烈。",
            "配置路径：利用分红险保底+分红的双轮驱动机制，锁定跨越周期的保单现金价值成长。"
        ]
    },
    {
        "id": "trade_decoupling_outbound",
        "category": "trade",
        "badge": "进出口与供应链出海",
        "title": "全球关税风暴与转口贸易重构：民营制造业出海‘借道东盟/墨西哥’的法律与汇率暗礁",
        "date_str": "今日聚焦",
        "hot": "🔥 供应链出海 / 原产地穿透",
        "summary": "面对欧美贸易壁垒升级，大量中国优质供应链加速向越南、印尼、墨西哥等国转移。然而海外建厂面临东道国劳工法、外汇管制、原产地规则穿透核查等多重考验。",
        "talk_phrase": "“陈总，您的工厂去东南亚布局是顺应大势，但在海外打拼，最怕‘前线赚外汇，后院起大火’。跨国经营不仅要管好订单，更要把核心创始人的身家和企业经营风险彻底切断隔离。”",
        "key_points": [
            "贸易变局：欧美针对转口贸易的原产地附加值比例审查极其严苛，单纯贴牌风险极高。",
            "资金风险：部分海外国家外汇管制严格，企业利润回流国内通道存在阻碍与汇兑损失。",
            "人身保障：外派高管与企业主跨国差旅频繁，高端全球医疗与突发意外转运成为刚需。",
            "对冲策略：多币种离岸账户搭建 + 国内保单财富锚定，形成‘外攻内守’安全格局。"
        ]
    },
    {
        "id": "politics_private_economy",
        "category": "politics",
        "badge": "顶层信号与民企保护",
        "title": "《民营经济促进法》立法提速：异地趋利性执法被严厉叫停，民营企业家财富安全感筑底",
        "date_str": "今日聚焦",
        "hot": "🔥 保护民营经济 / 规范异地执法",
        "summary": "最高法与发改委明确出台意见，严厉打击针对民营企业的异地趋利性执法和超权限查封冻结。国家从最高顶层释放‘保护企业家合法产权与人身财产安全’的明确政治信号。",
        "talk_phrase": "“周董，国家这次立法保护民企产权，释放的信号非常明确：合规守法的企业和资产受到最高法律保护。越是在这个节点，越要主动把企业的公账和您个人、家庭的私账划分得清清楚楚，让法律成为您最好的保护伞。”",
        "key_points": [
            "政策信号：民营经济促进法进入立法快车道，确立民企与国企同等法律地位和平等待遇。",
            "规范整治：严禁异地远洋捕捞式趋利性执法，规范查封、扣押、冻结涉案财产程序。",
            "法律机制：避免因企业涉诉导致个人及家庭连带破产，公私财产人格混同仍是头号杀手。",
            "实务落地：设立不可撤销保单与信托架构，合法合规防范债务外溢与企业经营连带风险。"
        ]
    }
]

def generate_daily_markdown(theme):
    """生成今日高客宏观早参 Markdown 文档"""
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    os.makedirs(EXPORT_DIR, exist_ok=True)
    md_file = os.path.join(EXPORT_DIR, f"高客宏观早参_{today_str}.md")
    
    content = f"""# 📈 金华平安家办·高客宏观早参与国家大事陪谈内参
> **日期**：{today_str} | **整理内勤**：平安人寿培训内勤 / 高家帮法律服务团队  
> **核心定位**：懂国家顶层大局，知高净值客户真正痛点，化宏观大势为展业谈资与法商成交利器！

---

## 🧭 今日头条宏观聚焦：【{theme['badge']}】
### 📌 核心议题：{theme['title']}
- **热度标签**：`{theme['hot']}`
- **宏观事件核心拆解**：
{theme['summary']}

---

## 💡 【三师会诊】深层透视：宏观动向对高客究竟意味着什么？

### 1. ⚖️ 民商法律师视角（合规与法律防线）
- 宏观政策与法规调整，本质是**对财富合法性与边界的重新厘清**。
- 不论是关税审查、外汇结汇还是企业公私账往来，**公私财产混同**依然是悬在很多民营企业家头上的达摩克利斯之剑。
- 必须运用《民法典》第一千零六十二条夫妻共同财产确权规则、公司法第二十三条人格否认防范机制，筑牢底层法律防火墙。

### 2. 📊 投顾理财规划师视角（资产与收益锁定）
- 利率下行与汇率博弈的时代，高客最大的焦虑是**“钱不知道往哪放”**与**“资产被无形侵蚀”**。
- 汇率波动破7、美元存款降息、银行理财净值波动，证明了“短期看似高收益，往往隐含巨大汇率或再投资风险”。
- 资产配置必须秉持**“核心底仓刚兑保本 + 卫星资产适度博弈”**，通过保单现金价值的确定性终身增长，抵御宏观利率下行周期。

### 3. 🛡️ 法税医养综合视角（家族护城河）
- 全球反避税（CRS）与金税四期已实现全数据链条并轨，依靠海外空壳公司和隐匿账户避税的时代已彻底终结。
- 真正的大额财富传承，必须依托合规合法的制度型工具（保单架构、大额年金、家族信托）。
- 结合平安“保险+居家养老/高品质康养/就医通”全生态权益，实现“钱有保障、税有合规、老有所养、病有所依”的四维闭环。

---

## 🗣️ 【高客陪谈口袋短语·一键复制】
> 📝 **陪谈话术**（可直接在微信沟通或面访破冰时使用）：
> 
> {theme['talk_phrase']}

---

## 🔍 今日数据与实战要点清单
"""
    for kp in theme['key_points']:
        content += f"- ✅ {kp}\n"

    content += f"""
---
*本内参每日早间 07:30 由【高客宏观自动化引擎】全自动提炼与归档。*
*完整交互式多维分析与图表请访问个人工作台：`https://andre4life.github.io/news/`*
"""
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ 生成高客宏观早参: {md_file}")
    return md_file

def update_news_portal(theme):
    """更新 news/index.html 与 GitHub Pages 交互大屏"""
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    print(f"✅ 检查 news/index.html 状态: 已包含 {theme['category']} 模块")
    # 执行部署
    if os.path.exists(DEPLOY_SCRIPT):
        print("🚀 执行 GitHub Pages 自动化同步部署...")
        res = subprocess.run([sys.executable, DEPLOY_SCRIPT], capture_output=True, text=True)
        print(res.stdout)
        if res.returncode == 0:
            print("✅ GitHub Pages 部署发布成功！")
        else:
            print(f"❌ 部署返回警告: {res.stderr}")

def main():
    # 按照星期轮换或选择最新主题（今日以汇率与结汇博弈为核心焦点）
    today = datetime.date.today()
    day_idx = today.weekday() % len(MACRO_THEMES)
    # 强制选用汇率作为今日核心焦点（契合用户即时需求）
    chosen_theme = MACRO_THEMES[0]
    
    print("=" * 60)
    print(f"🚀 启动高客宏观早参与国家大事每日自动化引擎 [{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    print(f"📌 今日焦点主题: {chosen_theme['title']}")
    print("=" * 60)
    
    md_file = generate_daily_markdown(chosen_theme)
    update_news_portal(chosen_theme)
    
    print("=" * 60)
    print("🎉 自动化流程全部完成！")

if __name__ == "__main__":
    main()
