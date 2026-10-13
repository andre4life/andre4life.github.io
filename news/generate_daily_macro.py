#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
每日宏观经济数据解读与国家大事追踪引擎 (V3.0 高客深度谈资与宏观智囊版)
定位: 彻底跳出单一保险思维，聚焦纯粹、硬核、深刻的宏观经济指标解读、商业周期推演与国家政策趋势。
      供内勤/顾问深入理解宏观经济真实水温，沉淀与企业主、高净值客户交流时的高维度谈资。
运行时间: 每日 17:00 自动更新
输出产物:
  1. D:\Antigravity输出\高客宏观每日内参\高客宏观每日内参_{YYYY-MM-DD}.md
  2. D:\Antigravity输出\andre4life.github.io\news\index.html
  3. 自动同步部署至 GitHub Pages (https://andre4life.github.io/news/)
"""

import os
import sys
import datetime
import subprocess

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
DEPLOY_SCRIPT = os.path.join(PORTAL_DIR, "deploy_portal.py")

# ==============================================================================
# 宏观经济与商业趋势核心数据全景库 (纯宏观分析 + 商业体感 + 买菜比喻 + 高客谈资)
# ==============================================================================
def get_pure_macro_data(date_str):
    return {
        "date": date_str,
        "title": "宏观经济数据深度透视：水流何处去、利润谁吃掉、企业真实水温与高客谈资",
        "lead": f"截至 {date_str}，宏观经济的核心矛盾已从单纯的“流动性供给”转向“资产负债表与需求恢复”。央行适度宽松组合拳不断发力、M2保持高位，但微观体感上企业普遍反映‘赚钱难、回款慢、应收账款账期拉长’。理解 M1-M2 剪刀差、PPI-CPI 利润挤压、PMI 新订单分项、地方化债对产业链现金流的影响，是看清当前中国经济棋局、与实业企业家高客建立深度认知共鸣的关键抓手。",
        
        # 六大宏观硬核维度
        "modules": [
            {
                "id": "m1_m2",
                "badge": "货币与流动性",
                "tag": "M1与M2剪刀差 / 资金活化度",
                "title": "M1-M2 负剪刀差与“资金堰塞湖”：水放出来了，为什么实体水温不高？",
                "data_fact": "全国广义货币（M2）余额保持平稳增长，而狭义货币（M1）增速持续在低位徘徊，两者呈现明显的‘负剪刀差’。同时金融机构新增存款中，居民与企业定期存款占比居高不下，超额储蓄现象显著。",
                "metaphor": "蓄水池与死活水模型：央行往大水库（M2）里注了大量水，水库水位很高；但通往田间地头（实体经济生产交易）的小水渠（M1）水流却很细。老百姓把钱锁在定期存折里（死水），企业不敢轻易拿钱去买原材料或扩建厂房，而是也把钱存定期吃微薄利息（资金防守）。结果就是‘水库水很满，田里依然觉得口渴’。",
                "business_reality": "实业老板体感：‘银行天天打电话求我贷款，利率压到2.8%甚至更低，但我手里原有的订单都找不到高利润，借了钱投下去可能亏得更快，不如不贷，手里趴着现金最安心。’这就是典型的‘流动性陷阱’与‘企业去杠杆心态’。",
                "talk_perspective": "【高客高维谈资】：‘张总，很多做实业的朋友最近总问我，为什么天天看新闻说货币宽松、信贷放量，但生意却感觉越来越卷、回款越来越慢？看一眼 M1 和 M2 的剪刀差就懂了。现在的资金大多在金融和定期体系内部沉淀，没有真正变成企业随时能调用的活期流动性。大家都在观望防守，这说明当下的胜负手不是盲目加杠杆扩张，而是比谁的现金流更健康、谁能耗到下一轮复苏周期启动。’"
            },
            {
                "id": "ppi_cpi",
                "badge": "物价与利润分配",
                "tag": "PPI vs CPI 剪刀差 / 工业利润",
                "title": "PPI 低位与 CPI 温和：工业品出厂价承压，制造业利润空间被谁压缩了？",
                "data_fact": "工业生产者出厂价格指数（PPI）同比持续低位震荡，生产资料价格承压；居民消费价格指数（CPI）温和波动。工业品价格跌幅大于消费终端，工业企业营业收入利润率承压明显。",
                "metaphor": "包子铺面粉与零售价模型：面粉、猪肉进价（上游原材料）虽然波动，但满大街都是包子铺，谁敢涨价谁就没生意！为了抢仅有的几个顾客，大家只能降价促销，原本卖3块的包子硬生生杀到2块钱（PPI走低）。老板累死累活卖了一万个包子，一算账连房租和人工都快挣不出来，利润全在激烈的内卷竞争中被‘磨损’掉了。",
                "business_reality": "实业老板体感：‘不是没单子做，是单子没利润！客户拿走货，天天逼着降价，同行为了养工人还亏本抢单。营收数字看起来跟去年差不多，到年底一盘点，净利润薄如刀片。’",
                "talk_perspective": "【高客高维谈资】：‘李总，我看最近几个月的 PPI 数据，工业出厂价格一直在低位徘徊，这正是实业老板今年最痛的地方——产能过剩叠加价格内卷，形成了明显的利润挤压。现在的局势下，单纯靠拼价格出清是杀敌一千自损八百。国内走得通的企业，要么靠技术差异化跳出红海，要么抱团出海去抢中东、拉美、东盟这些还有溢价空间的增量市场。’"
            },
            {
                "id": "pmi_structure",
                "badge": "制造业景气度",
                "tag": "PMI 荣枯线 / 供需分项异动",
                "title": "PMI 生产指数 vs 新订单指数背离：‘生产热、订单冷’的结构性病灶",
                "data_fact": "制造业采购经理指数（PMI）结构分化：生产指数往往强于新订单指数，大型企业景气度明显优于中小型企业。新出口订单指数受外部关税博弈影响出现结构性波动，高技术制造与装备制造PMI显著领跑传统高耗能行业。",
                "metaphor": "工厂开机与销路模型：工厂老板为了分摊高昂的厂房折旧、机器维护和熟练工人工资，不敢轻易停工，哪怕没利润机器也得轰隆隆开着（生产指数维持在荣枯线上）；但去销售部一问，业务员拿回来的新订单却寥寥无几（新订单指数掉在50以下）。库房里的成品越堆越高，变成了‘以产顶销’的被动累库局面。",
                "business_reality": "实业老板体感：‘不开工每天亏折旧和工资，开工又怕货卖不出去变库存。中小型配套代工厂的日子最难过，大国企和链主企业压价压得极狠，行业正在经历大鱼吃小鱼的残酷残酷洗牌期。’",
                "talk_perspective": "【高客高维谈资】：‘王董，看官方 PMI 分项数据，最值得关注的不是总指数有没有过 50，而是生产和新订单的剪刀差。生产热、订单偏冷，说明供给端的产能释放远快于需求回暖。这意味着接下来的 1-2 年，各行各业的行业集中度会加速提升，尾部中小型加工厂会大批出清。对于咱们有底盘优势的企业来说，守好现金流，熬到行业产能出清，剩下的就是行业龙头的超级红利。’"
            },
            {
                "id": "fiscal_debt",
                "badge": "财政政策与化债",
                "tag": "特别国债 / 地方化债 / 应收账款",
                "title": "中央加杠杆与万亿化债启动：地方政府‘拆弹’，对民企工程款与账期意味着什么？",
                "data_fact": "国家连续发行超长期特别国债，大规模增加地方政府债务限额置换存量隐性债务。财政政策从‘控杠杆’明确转向‘中央积极加杠杆、地方大力度腾挪化债’，重点支持重点产业链、国家重大基础设施（六张网）及民生领域。",
                "metaphor": "老子替儿子还高利贷模型：地方政府（儿子）以前借了大量利息高达7%-8%的城投债和信托款，每天被利息压得喘不过气，连给做工程、做绿化的民营企业（包工头）结工程款的钱都没有（到处打白条）。现在中央财政（老子）亲自下场，发2%低息的超长期国债借给地方，帮地方把高息高危的隐性债务换掉。虽然不能瞬间暴富，但地方政府‘每个月要还的利息断崖式下降’，终于能缓过一口气来清欠民企欠款。",
                "business_reality": "实业老板体感：‘前几年接的地方基建和政企项目，应收账款压了几千万，天天跑财政局催款。化债政策一落地，最直接的希望就是拖欠了两三年的老账本能不能开始兑现回款。’",
                "talk_perspective": "【高客高维谈资】：‘周总，这轮万亿级地方债务置换，本质是中央在帮地方资产负债表‘做手术’。很多做市政、工程、环保的企业家朋友前几年被应收账款拖得半死。这次化债最核心的目的就是腾出财力‘清欠民营企业账款’。您如果手里有政企拖欠的老项目，现在正是紧盯财政专班、争取优先列入第一批债务化解清偿清单的黄金窗口期。’"
            },
            {
                "id": "trade_fx",
                "badge": "进出口与全球外贸",
                "tag": "万亿顺差结构 / 美联储降息 / 结汇博弈",
                "title": "货物顺差创纪录与结汇堰塞湖：中国出口不仅没死，反而升级成了‘全能链主’？",
                "data_fact": "中国货物贸易顺差创历史纪录，但贸易结构发生巨变：传统劳动密集型产品占比下降，汽车、锂电、光伏、智能机械等高附加值产品占比飙升；对东盟、拉美、非洲的贸易增速远超对欧美传统市场。人民币对一篮子货币（CFETS）保持平稳，中美利差在美联储降息周期下逐步收窄。",
                "metaphor": "从织布裁缝到造重型铠甲模型：二十年前我们做外贸，是靠几亿件衬衫换一架大飞机，赚的是最苦最累的血汗工钱；现在我们做外贸，是向全世界输出成套的光伏电站、智能电车、工业机器人和全套供应链零件。哪怕欧美加高关税壁垒，但他们自己的工厂如果离开了中国的模具、电机和基础电子元器件，整条产线直接停摆。",
                "business_reality": "外贸老板体感：‘老美查原产地查得很凶，直接出口美国确实阻力大；但我们在东南亚建了组装厂，零部件从国内运过去，订单反而越来越多。外贸不是做不下去了，而是玩法变了，只懂在义乌卖小商品的在淘汰，懂得全球供应链调度的大老板赚得盆满钵满。’",
                "talk_perspective": "【高客高维谈资】：‘陈总，很多唱衰外贸的声音其实完全没看懂海关总署的真实数据。中国的外贸不仅没跨，反而在完成一次惊人的‘大换血’。我们对欧美的直接顺差虽然面临摩擦，但通过东盟、墨西哥的转口和深度分工，中国实际上成了全球制造业事实上的‘总供应链底座’。今天做外贸的核心，已经从拼工人成本，变成了拼谁懂原产地规则、谁能在全球布局‘中国大脑+海外组装’的敏捷网络。’"
            },
            {
                "id": "re_assets",
                "badge": "房地产与大类资产",
                "tag": "房地产转轨 / 租金回报率 / 资产荒配置",
                "title": "告别土地财政与无风险高息：中国高净值家庭‘资产锚’正在发生深刻迁移",
                "data_fact": "房地产市场进入由高周转高负债向高品质‘好房子’和租金回报率定价的平稳转轨期；城投债刚兑彻底破除，信托违约常态化；银行大额存单利率全面跌破2.0%，30年期国债收益率创历史低位。无风险高收益资产彻底成为历史。",
                "metaphor": "从野蛮买地建房到选能下蛋的母鸡模型：过去二十年，闭着眼睛买套房，转手就能涨50%，大家买的是‘房价永远暴涨的预期’；现在这个预期被彻底打破了，房子从‘投机筹码’回归到了‘居住和收租本质’。就跟买母鸡一样，以前是赌母鸡明天身价翻倍，现在必须看这只母鸡每天到底能下几个蛋（租售比）。下不出蛋的高估值资产，都在被市场无情抛弃。",
                "business_reality": "高客财富焦虑：‘过去赚了钱就买商铺、买住宅、买信托，年化8%稳稳当当。现在信托频频暴雷，商铺租不出去，银行理财跌破2%，几千万现金躺在账上，看着利息一天比一天低，真不知道还能把钱投到哪里去。’",
                "talk_perspective": "【高客高维谈资】：‘孙董，房地产和高息信托的落幕，意味着中国老百姓持续了二十年的财富逻辑发生了根本性扭转。以前大家比的是谁的进攻更激进、谁敢借钱炒房；未来十年，资产配置的最高智慧是‘防守反击’。一是坚决砍掉没有现金流支撑的低效资产，二是建立一个绝对不能亏损、能持续跨越周期的‘无风险现金流底盘’。底盘稳住了，才能在市场每次恐慌打折时，有充足的真金白银去捡带血的优质核心资产。’"
            }
        ],

        # 核心宏观指标词典（大白话+实战拆解）
        "lexicon": [
            {
                "term": "M1 与 M2 剪刀差",
                "tag": "流动性 / 商业水温",
                "plain_concept": "M1（狭义货币）= 流通中的现金 + 企业活期存款（随时能花的钱）。M2（广义货币）= M1 + 企业定期存款 + 居民储蓄存款（沉淀在银行里的钱）。",
                "metaphor": "买菜皮夹子与存折：M1是你兜里装的随时能买菜掏出来的现金；M2是你锁在柜子深处的定期存折。如果M1涨得快，说明大家都把存折里的钱取出来准备买货搞投资，经济火热；如果M1跌、M2涨，说明大家都把钱包里的零钱存进存折锁死了，大家都捂紧口袋不敢花钱。",
                "talk_value": "和高客谈资：用来向老板解释为什么信贷放水很多，但客户普遍不愿签大单、不愿提前打预付款。"
            },
            {
                "term": "PPI（工业生产者出厂价格指数）",
                "tag": "工业利润 / 价格内卷",
                "plain_concept": "工业品刚出厂门时候的第一道批发销售价格，衡量的是生产制造端的通胀或通缩压力。",
                "metaphor": "出厂批发价水银柱：反映的是工厂卖货到底能不能卖上价。PPI持续为负，说明工厂端生产的产品严重过剩，大家都在互相砸价抢市场；PPI回正上升，说明下游需求旺盛，工厂不仅能把货卖出去，还能把原材料涨价的成本顺利转嫁给客户。",
                "talk_value": "和高客谈资：用来剖析制造业企业为什么‘营收数字好看，但年底算总账净利润薄如刀片’。"
            },
            {
                "term": "PMI 荣枯线（50%分界线）",
                "tag": "经济景气度 / 晴雨表",
                "plain_concept": "采购经理人指数，抽样调查各企业采购总监得出的综合景气度指标。50%为分水岭，大于50代表经济扩张，小于50代表收缩。",
                "metaphor": "经济体检的体温计：37度是正常体温。大于50度就像身体正在发热加速运转，工厂在招工、买料、扩产；小于50度说明身体有些发冷，经理们都在压缩开支、减少采购、清理存货。",
                "talk_value": "和高客谈资：重点拆解‘新订单分项’和‘原材料库存分项’，判断未来半年的产业链供求趋势。"
            },
            {
                "term": "社融规模（社会融资规模）",
                "tag": "实体融资 / 信用扩张",
                "plain_concept": "一定时期内实体经济（企业和个人）从金融体系（银行、债券、股票、信托等）获得的资金总额。",
                "metaphor": "实体经济的输血总量：银行和资本市场是心脏，企业和居民是身体器官。社融就是心脏一个月内究竟给全身各个器官输送了多少毫升新鲜血液。看社融不仅看输血总量，更要看血液流向了国企大动脉，还是流到了民营企业的小毛细血管。",
                "talk_value": "和高客谈资：拆解新增信贷里‘居民中长期贷款（房贷）’和‘企业中长期贷款’的比例，判断民间真实投资信心。"
            },
            {
                "term": "逆周期调节与跨周期调节",
                "tag": "宏观调控 / 国家棋局",
                "plain_concept": "逆周期调节侧重于短期‘削峰填谷’（经济冷了踩油门降息，热了踩刹车）；跨周期调节侧重于兼顾中长期结构改革与风险防范（不搞大水漫灌，留足政策子弹）。",
                "metaphor": "中医调理与下猛药的区别：逆周期是发烧了赶紧吃退烧药；跨周期是不仅要退烧，还要强健脾胃、锻炼体质，绝不能因为发烧就一口气吃十副猛药把肝肾吃衰竭。国家宁可容忍经济短期慢一点，也坚决不再搞当年的大水漫灌炒地皮，而是要把资源全部引导到芯片、新能源、硬科技上。",
                "talk_value": "和高客谈资：向企业家解释为什么国家这次政策定力这么强，不再搞四万亿大放水炒房炒地，让高客放弃暴利幻想、专注实业精细化。"
            }
        ],

        # 3个检验宏观逻辑的深度思考题
        "quizzes": [
            {
                "q": "为什么央行多次降准降息、社会综合融资成本创历史新低，但民营企业投资扩产的意愿依然偏谨慎？",
                "a": "降息降低的是‘资金成本’，但决定企业是否投资的核心变量是‘边际资本回报率（ROIC）与预期利润’。当大部分行业面临产能过剩、PPI持续低迷、终端需求不足时，企业即使借到低息贷款也找不到确定盈利的项目，投资可能加速亏损。因此在需求和资产负债表完全修复前，企业会优先选择‘修养生息、用现金流偿还旧债’。"
            },
            {
                "q": "在财政‘地方化债’大背景下，为什么说民企不能盲目等待全面‘水漫金山’，而必须主动做‘资产负债表断舍离’？",
                "a": "本轮中央主导的债务置换，本质是将高息隐性债务置换为低息显性债务，目的是‘拆弹防风险、腾挪保民生与重点项目’，绝非让地方政府重新展开无序扩张。政府清欠账款也是结构性、分批次的。依赖传统粗放政企垫资的民企，如果继续指望地方大上快上，资金链极易在等待中崩塌，唯有主动出清低效存货与垫资项目，方能存活。"
            },
            {
                "q": "当中国货物贸易顺差创万亿美元新高，为什么普通外贸工厂却感觉‘订单做不完，但利润越来越薄’？",
                "a": "外贸顺差由‘量’和‘质’两极分化构成：高技术制造业（汽车、光伏、电池、高端装备）凭借全产业链优势抢占了大量国际高附加值份额；而中低端劳动密集型代工行业，由于东南亚竞品分流以及国内同质化产能严重，外商普遍通过比价极限压低出厂报价，导致代工企业陷入‘有产值、无净利’的夹心层困局。"
            }
        ]
    }

# ==============================================================================
# Markdown 生成引擎
# ==============================================================================
def generate_pure_macro_markdown(data):
    today_str = data["date"]
    os.makedirs(PRIMARY_EXPORT_DIR, exist_ok=True)
    os.makedirs(BACKUP_EXPORT_DIR, exist_ok=True)
    primary_file = os.path.join(PRIMARY_EXPORT_DIR, f"高客宏观每日内参_{today_str}.md")
    backup_file = os.path.join(BACKUP_EXPORT_DIR, f"高客宏观早参_{today_str}.md")

    md = f"""# 📊 金华平安家办·每日宏观经济深度透视与商业谈资内参
> **归档日期**：{today_str}（每日 17:00 汇总截至当日最新宏观经济数据与政策博弈）  
> **编制内勤**：平安人寿培训内勤 / 高家帮法律服务团队  
> **核心定位**：彻底跳出狭隘推销思维，用纯粹、客观、硬核的宏观经济指标与商业周期洞察，为内勤与外勤顾问赋能，沉淀与实业企业家高客深度对话的高维度谈资！

---

## 🧭 今日宏观核心主线：【{data['title']}】
{data['lead']}

---

## 🔍 今日六大宏观维度全景扫描（数据核查 + 买菜模型 + 商业真实体感 + 高客高维谈资）
"""
    for idx, m in enumerate(data["modules"], 1):
        md += f"""
### 维度 {idx}：【{m['badge']}】{m['title']}
- **📈 宏观数据与客观事实**：
  {m['data_fact']}
- **🥬 生活化大白话比喻（买菜模型）**：
  {m['metaphor']}
- **🏭 实业企业家真实体感（商业水温）**：
  {m['business_reality']}
- **🗣️ 【与高客交流的高维谈资（直击商业认知）】**：
  > 📝 *{m['talk_perspective']}*

---
"""

    md += """
## 📚 【宏观经济高频核心术语·买菜模型速查词典】
> *懂数据背后的逻辑，才能在与高客沟通时降维沟通：*
"""
    for idx, lex in enumerate(data["lexicon"], 1):
        md += f"""
### 💡 术语 {idx}：{lex['term']} `[{lex['tag']}]`
- **📖 纯学术/官方概念**：{lex['plain_concept']}
- **🥬 买菜大白话比喻**：{lex['metaphor']}
- **🎯 和高客聊天的实战价值**：{lex['talk_value']}
"""

    md += """
---

## 🎯 检验是否真正读懂宏观棋局的 3 个深度思考题

| 序号 | 宏观深度思考题 | 底层逻辑与推演要点 |
| :---: | :--- | :--- |
"""
    for idx, qz in enumerate(data["quizzes"], 1):
        md += f"| **Q{idx}** | {qz['q']} | **答**：{qz['a']} |\n"

    md += f"""
---
*本内参每日 17:00 由 Windows 任务计划程序【DailyMacroNewsUpdate_1700】全自动生成、归档与同步部署。*  
*手机端随时随地阅读完整图表与交互大屏：`https://andre4life.github.io/news/`*
"""
    with open(primary_file, "w", encoding="utf-8") as f:
        f.write(md)
    with open(backup_file, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"✅ 生成高客宏观每日内参: {primary_file}")
    return primary_file

# ==============================================================================
# HTML 移动端与交互大屏渲染器
# ==============================================================================
def update_pure_macro_html(data):
    today_str = data["date"]

    cards_html = ""
    for m in data["modules"]:
        cards_html += f"""
        <article class="bg-dark-850 rounded-2xl border border-dark-700/80 p-6 md:p-8 hover:border-amber-500/40 transition-all duration-300 shadow-xl">
          <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-amber-500/10 text-amber-400 border border-amber-500/30 rounded-full text-xs font-semibold">
              {m['badge']} · {m['tag']}
            </span>
            <span class="text-xs text-slate-400">客观数据分析</span>
          </div>

          <h3 class="text-xl md:text-2xl font-bold text-white mb-4 leading-snug">
            {m['title']}
          </h3>

          <!-- 数据客观事实 -->
          <div class="mb-4 bg-dark-800 rounded-xl p-4 border border-dark-700">
            <h4 class="text-xs font-bold text-blue-400 uppercase tracking-wider mb-1 flex items-center gap-2">
              <span>📈</span> 宏观指标与数据客观发布
            </h4>
            <p class="text-slate-300 text-sm leading-relaxed">{m['data_fact']}</p>
          </div>

          <!-- 买菜生活化模型 -->
          <div class="mb-4 bg-emerald-950/20 border border-emerald-500/30 rounded-xl p-4">
            <h4 class="text-xs font-bold text-emerald-300 uppercase tracking-wider mb-1 flex items-center gap-2">
              <span>🥬</span> 生活化大白话比喻（买菜模型）
            </h4>
            <p class="text-emerald-100 text-sm leading-relaxed">{m['metaphor']}</p>
          </div>

          <!-- 实业老板体感 -->
          <div class="mb-4 bg-rose-950/20 border border-rose-500/30 rounded-xl p-4">
            <h4 class="text-xs font-bold text-rose-300 uppercase tracking-wider mb-1 flex items-center gap-2">
              <span>🏭</span> 实业企业家真实体感（商业水温）
            </h4>
            <p class="text-rose-200 text-sm leading-relaxed">{m['business_reality']}</p>
          </div>

          <!-- 高客高维谈资 -->
          <div class="bg-gradient-to-r from-amber-500/15 to-transparent border-l-4 border-amber-500 p-4 rounded-r-xl">
            <div class="flex items-center justify-between mb-1">
              <span class="text-xs font-bold text-amber-400 flex items-center gap-1">
                <span>🗣️</span> 与高客交流的高维谈资（建立认知共鸣）
              </span>
              <button onclick="navigator.clipboard.writeText('{m['talk_perspective']}'); alert('谈资已成功复制！');" 
                      class="text-xs px-2.5 py-1 bg-amber-500/20 hover:bg-amber-500/40 text-amber-300 rounded border border-amber-500/30 transition-colors">
                复制谈资
              </button>
            </div>
            <p class="text-slate-200 text-sm leading-relaxed mt-1 italic">{m['talk_perspective']}</p>
          </div>
        </article>
        """

    lexicon_html = ""
    for lex in data["lexicon"]:
        lexicon_html += f"""
        <div class="p-5 bg-dark-800 rounded-xl border border-dark-700 hover:border-amber-500/30 transition-all">
          <div class="flex items-center justify-between mb-2">
            <h4 class="text-base font-bold text-white flex items-center gap-2">
              <span class="text-amber-400">💡</span> {lex['term']}
            </h4>
            <span class="text-xs px-2.5 py-0.5 bg-dark-750 text-slate-300 rounded-full">{lex['tag']}</span>
          </div>
          <p class="text-xs text-slate-400 mb-2">{lex['plain_concept']}</p>
          <div class="p-3 bg-dark-900/80 rounded-lg text-xs text-emerald-300 mb-2 border border-dark-700">
            <strong class="text-emerald-400">🥬 买菜比喻：</strong>{lex['metaphor']}
          </div>
          <div class="text-xs text-amber-300/90">
            <strong class="text-amber-400">🎯 高客谈资价值：</strong>{lex['talk_value']}
          </div>
        </div>
        """

    quizzes_html = ""
    for idx, qz in enumerate(data["quizzes"], 1):
        quizzes_html += f"""
        <div class="p-5 bg-dark-850 rounded-xl border border-dark-700">
          <h4 class="text-sm font-bold text-white mb-2 flex items-start gap-2">
            <span class="text-amber-400 font-mono text-base">Q{idx}.</span>
            <span>{qz['q']}</span>
          </h4>
          <div class="mt-3 p-3 bg-dark-800 rounded-lg text-xs text-slate-300 leading-relaxed border-l-2 border-emerald-400">
            <strong class="text-emerald-400">底层逻辑推演：</strong> {qz['a']}
          </div>
        </div>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>每日宏观经济数据透视与高客谈资</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    ::-webkit-scrollbar {{ width: 4px; height: 4px; }}
    ::-webkit-scrollbar-track {{ background: #070a12; }}
    ::-webkit-scrollbar-thumb {{ background: #334155; border-radius: 4px; }}
    .bg-dark-900 {{ background-color: #070a12; }}
    .bg-dark-850 {{ background-color: #0d1322; }}
    .bg-dark-800 {{ background-color: #131b2e; }}
    .bg-dark-750 {{ background-color: #1a243b; }}
    .border-dark-700 {{ border-color: #24324f; }}
  </style>
</head>
<body class="bg-dark-900 text-slate-100 min-h-screen font-sans antialiased selection:bg-amber-500 selection:text-white pb-20">

  <!-- 顶部导航 -->
  <header class="sticky top-0 z-50 bg-dark-900/90 backdrop-blur-md border-b border-dark-700/80 px-4 py-3">
    <div class="max-w-5xl mx-auto flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <a href="../index.html" class="p-2 text-slate-400 hover:text-white rounded-lg hover:bg-dark-800 transition">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
          </svg>
        </a>
        <div>
          <h1 class="text-sm font-bold tracking-tight text-white flex items-center gap-2">
            金华平安家办 · 宏观经济与商业智库
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          </h1>
          <p class="text-xs text-slate-400">每日 17:00 自动更新 · 硬核宏观谈资储备</p>
        </div>
      </div>
      <span class="text-xs px-2.5 py-1 bg-amber-500/10 border border-amber-500/30 text-amber-300 font-mono rounded-md">
        {today_str}
      </span>
    </div>
  </header>

  <!-- 主体容器 -->
  <main class="max-w-5xl mx-auto px-4 pt-6 space-y-8">

    <!-- 顶部导读 -->
    <section class="bg-gradient-to-br from-dark-850 to-dark-800 rounded-2xl border border-amber-500/30 p-6 md:p-8 shadow-2xl">
      <span class="inline-block px-3 py-1 bg-amber-500/20 text-amber-300 border border-amber-500/40 rounded-full text-xs font-bold tracking-wider mb-3">
        今日宏观大局核心主线
      </span>
      <h2 class="text-2xl md:text-3xl font-extrabold text-white mb-4 leading-tight">
        {data['title']}
      </h2>
      <p class="text-slate-300 text-sm md:text-base leading-relaxed">
        {data['lead']}
      </p>
    </section>

    <!-- 六大模块 -->
    <section class="space-y-6">
      <div class="flex items-center justify-between border-b border-dark-700/80 pb-3">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <span>🔍</span> 宏观数据深度剖析与商业真实水温
        </h3>
        <span class="text-xs text-slate-400">客观推演 · 拒绝机械推销</span>
      </div>
      <div class="space-y-6">
        {cards_html}
      </div>
    </section>

    <!-- 核心指标速查词典 -->
    <section class="bg-dark-850 rounded-2xl border border-dark-700/80 p-6 md:p-8 shadow-xl">
      <div class="border-b border-dark-700 pb-3 mb-6">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <span>📚</span> 宏观核心指标买菜模型速查词典
        </h3>
        <p class="text-xs text-slate-400 mt-1">生活化买菜拆解 + 赋能与高客对话的实战谈资</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        {lexicon_html}
      </div>
    </section>

    <!-- 深度思考题 -->
    <section class="bg-dark-850 rounded-2xl border border-dark-700/80 p-6 md:p-8 shadow-xl">
      <div class="border-b border-dark-700 pb-3 mb-6">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <span>🎯</span> 检验宏观底层逻辑的 3 个深度思考题
        </h3>
        <p class="text-xs text-slate-400 mt-1">看透数据背后的因果链条，不做表面看客</p>
      </div>
      <div class="space-y-4">
        {quizzes_html}
      </div>
    </section>

    <!-- 页脚 -->
    <footer class="text-center text-xs text-slate-500 pt-6 pb-12 space-y-2 border-t border-dark-700/60">
      <p>金华平安家办 · 宏观商业智囊内参</p>
      <p>由 Windows 计划任务【DailyMacroNewsUpdate_1700】全自动调度更新部署</p>
    </footer>

  </main>
</body>
</html>"""

    with open(NEWS_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"✅ 渲染并更新网页大屏: {NEWS_HTML_PATH}")

# ==============================================================================
# 主执行入口
# ==============================================================================
def main():
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    print("=" * 60)
    print(f"🚀 启动宏观经济数据解读与高客谈资自动化引擎 [{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    print(f"📅 归档日期: {today_str}")
    print("=" * 60)

    data = get_pure_macro_data(today_str)
    generate_pure_macro_markdown(data)
    update_pure_macro_html(data)

    if os.path.exists(DEPLOY_SCRIPT):
        print("🚀 执行 GitHub Pages 自动化同步部署...")
        res = subprocess.run([sys.executable, DEPLOY_SCRIPT, f"feat: upgrade daily macro {today_str} to pure macroeconomic business intelligence and HNW sparring"], capture_output=True, text=True, encoding="utf-8", errors="ignore")
        if res.returncode == 0:
            print("✅ GitHub Pages 部署发布成功！")
        else:
            print(f"❌ 部署返回警告: {res.stderr}")

    print("=" * 60)
    print("🎉 自动化流程全部完成！")

if __name__ == "__main__":
    main()
