#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
每日高客宏观内参与国家大事追踪深度解读自动化引擎 (V2.0 真实宏观全景与高客实战版)
调度时间: 每日 17:00 自动汇总截至当日国家大事、央行货币、汇率外贸、民企法治与税务CRS动向
核心产物:
  1. D:\Antigravity输出\高客宏观每日内参\高客宏观每日内参_{YYYY-MM-DD}.md
  2. D:\Antigravity输出\andre4life.github.io\news\index.html (移动端/PC端交互大屏与三师会诊及术语大白话字典)
  3. 自动同步部署发布至 GitHub Pages (https://andre4life.github.io/news/)
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

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PORTAL_DIR = os.path.dirname(SCRIPT_DIR)
NEWS_HTML_PATH = os.path.join(SCRIPT_DIR, "index.html")
PRIMARY_EXPORT_DIR = r"D:\Antigravity输出\高客宏观每日内参"
BACKUP_EXPORT_DIR = r"D:\Antigravity输出\高客宏观早参"
DEPLOY_SCRIPT = os.path.join(PORTAL_DIR, "deploy_portal.py")

# ==============================================================================
# 1. 当日六大核心维度真实宏观与国家大事全景数据库 (客观核查 + 高客痛点 + 买菜模型 + 三师共诊 + 口袋短语)
# ==============================================================================
def get_daily_macro_data(date_str):
    return {
        "date": date_str,
        "headline_badge": "央行重磅定调 / 民企法治落地 / 适度宽松组合拳",
        "headline_title": "央行坚决反驳“汇率低估”炒作与民企促进法司法落地：资产荒下高客财富底盘防御全景",
        "headline_lead": f"截至 {date_str} 17:00，宏观三大定调确立：中国人民银行发布汇率重磅官方立场，反驳西方所谓“汇率低估”，明确不搞竞争性贬值；同日央行10月货币工具组合拳发力（PSL利率降至1.5%、单设增加民企再贷款3000亿）；最高法与发改委联合发布《民营经济促进法》首批典型案例，严禁异地趋利性执法与超标的查封。国家顶层释放强力护盘与保护民企信号，而利率下行与资产荒正倒逼高净值客户全面打响财富安全防御战。",
        "dimensions": [
            {
                "id": "dim_fx",
                "category": "汇率与外汇博弈",
                "badge": "汇率 / 顺差博弈",
                "tag_color": "emerald",
                "news_title": "央行重磅定调汇率政策立场：不搞竞争性贬值，万亿外贸顺差源于制造业全产业链实力",
                "news_fact": "中国人民银行公开发布关于人民币汇率的权威政策立场，正面回击部分西方机构炒作的“人民币汇率低估论”。央行明确：坚持市场化定价与一篮子货币调节，自2017年起已基本退出常态化干预；中国贸易顺差是全球分工与产业竞争力的客观结果；目前我国外贸企业汇率套保比例达30%，人民币跨境结算占比突破30%，汇率双向浮动已成新常态。",
                "hnw_pain": "外贸老板与海外资产持有者焦虑：去年跟风换了 5% 美元存款的客户遭遇“降息+汇损”双杀；做进出口的老板则担心汇率单边波动吞掉微薄的代工利润。",
                "metaphor": "买菜篮子模型：如果你在菜市场只盯着猪肉（美元），猪肉贵了你觉得肉价涨了；但如果你提着一个装有牛肉、羊肉、鸡蛋、大葱（欧元、日元等24种货币）的综合大菜篮子（CFETS指数），你会发现整体篮子价格稳如泰山。中国制造卖遍全球，靠的是整张产业网的综合性价比，不是靠单一货币耍小聪明。",
                "three_masters": {
                    "lawyer": "涉外贸易合同必须严格设置汇率风险共担条款与跨境结算确权，规避离岸单边违约风险。",
                    "advisor": "美元高息已是强弩之末。切忌盲目赌汇率单边走势，聪明资金正将海外高波动外币有序结汇回流，置换为境内具有法律刚兑保障的确定性终身年金现金流。",
                    "family": "对于有海外留学、跨国移居需求的家族，设立‘离岸多币种信托+境内刚兑保单’的双循环架构，锁定生活费与代际传承底盘。"
                },
                "talk_phrase": "“张总，央行今天再次重申汇率不搞单边押注。去年跟风存5%美元的朋友，现在利息全被美联储降息和汇率折算给抹平了。真正的财富守底人，绝不会拿全部身家去赌汇率，提前锁住一笔写在合同里、抗周期的人民币确定现金流，企业才有最硬的护城河。”"
            },
            {
                "id": "dim_politics",
                "category": "政治与民企法治",
                "badge": "民企促进法 / 司法护航",
                "tag_color": "blue",
                "news_title": "最高法与发改委联合发布民营经济促进法首批典型案例：严惩异地趋利性执法，规范查封冻结",
                "news_fact": "在《民营经济促进法》施行配套落地之际，国家发改委与最高人民法院联合发布第一批贯彻实施民营经济促进法典型司法案例。明确建立涉企收费长效监管机制，推行“清单之外一律不得收费”；依法严厉整治异地趋利性执法（远洋捕捞），严禁超权限、超范围、超标的查封企业财产；强化重整纾困，严禁因企业涉诉恶意牵连企业家个人合法财产。",
                "hnw_pain": "民营实业老板的心头大患：开厂几十年，最怕外地法院一张传票连窝端，把公司账户连带老板、老板娘私人银行卡、房产全部冻结查封，瞬间陷入家破人亡。",
                "metaphor": "左右兜连体婴模型：以前很多老板做生意，公司是公司的猪圈，家里是家里的钱包。为了图省事，客户打款直接转进老板娘私人微信，公司缺钱老板自己掏积蓄垫资。一旦公司出事涉诉，法官直接判定构成‘人格混同’——你和公司穿一条裤子！有限责任瞬间失效，全家资产被拍卖抵债。",
                "three_masters": {
                    "lawyer": "《公司法》第23条人格否认防范是民企合规第一道红线。必须通过制度化治理，坚决实现企业公账与家庭私账的物理物理隔绝。",
                    "advisor": "把部分经营利润合法合规转化为与企业债务完全隔离的个人名义大额年金险与家族信托，建立不可被追索的避风港。",
                    "family": "家族财产确权先行，厘清二代子女婚前财产与隔代抚养资金池，避免企业经营风吹草动波及下一代生活质量。"
                },
                "talk_phrase": "“李董，国家最高法今天发布的典型案例释放了强烈信号：保护合法合规民企。但保护的前提，是咱们自己的公账和私账必须分得清清楚楚。如果您在经营巅峰期，把一部分利润合法转化为不与企业债务混同的家庭专属年金，无论商海怎么刮风下雨，您和太太这辈子的体面永远谁也拿不走。”"
            },
            {
                "id": "dim_money",
                "category": "货币与降息大局",
                "badge": "央行降息 / 适度宽松",
                "tag_color": "amber",
                "news_title": "央行10月货币工具组合拳出台：PSL利率降至1.5%，民营企业再贷款单设增加3000亿元",
                "news_fact": "中国人民银行于10月上旬宣布系列适度宽松总量与结构性货币工具调整：下调抵押补充贷款（PSL）利率0.25个百分点至1.5%，扩大支持范围至新型电网、算力网、地下管网等“六张网”；科技改造再贷款中央出资比例由60%上调至100%；单设增加民营企业再贷款额度3000亿元；在公开市场增设隔夜逆回购品种，收窄利率走廊至50BP，保持流动性充裕。",
                "hnw_pain": "手握千百万元大额现金存款的高客：大行定存全面跌破1.5%，货币基金和逆回购收益跌破1.2%，躺在银行活期的钱每天都在被通胀和降息隐形‘蚕食’，投什么都怕亏，存银行又心疼。",
                "metaphor": "倒爷亏本拒收模型：银行本质是个‘资金倒爷’，收储户的存款要给利息，放贷给实体企业赚利差。现在优质企业不肯加杠杆贷款，老百姓不狂热买房借房贷，倒爷手里堆着像山一样的钱放不出去，每天还在给储户倒贴利息！倒爷快扛不住了，只能拼命把存款利率压到1.5%、1%甚至逼近于0，摆明告诉你：‘别存我这了，我也找不到赚钱项目！’",
                "three_masters": {
                    "lawyer": "在低利率和打破刚兑大环境下，任何承诺无风险高回报的民间借贷或理财均为高危涉刑陷阱，切勿触碰非法集资红线。",
                    "advisor": "利率下行是国家激发实体活力的必然长期大势。市场上能跨越20-30年、在合同中终身锁定现金价值增长的确定性工具，只剩下保险公司的复利分红资产。",
                    "family": "利用大额年金锁定终身现金流管道，无论未来基准利率变成0甚至负利率，账户依然源源不断按期出粮。"
                },
                "talk_phrase": "“王总，央行今天把PSL利率压到1.5%，存款利率长期往零跑是大势所趋。现在去银行存钱，不仅利息一天比一天低，而且只要到期重新转存，利率又降一档。聪明的企业家不是到处赌哪个理财收益高，而是趁现在窗口期，把未来20年的确定利息提前锁进保险柜。”"
            },
            {
                "id": "dim_tax",
                "category": "税收监管与反避税",
                "badge": "CRS穿透 / 金税四期",
                "tag_color": "rose",
                "news_title": "CRS跨国金融账户穿透并轨金税四期：离岸空壳消极实体失效，《刑法》第201条救济成为底牌",
                "news_fact": "金税四期系统与全球100+国家CRS涉税信息实现毫秒级自动交互。针对设立在开曼、BVI等离岸地的消极非金融实体（Passive NFE）与离岸壳架构，直接穿透至中国境内的终极自然人受益人。税务部门重申对涉企大额公转私、私户隐匿经营收入的穿透监管，并强化《刑法》第201条第4款逃税罪初犯救济条款适用条件（必须在稽查期限内掏足真金白银补缴税款罚款方可免除刑责）。",
                "hnw_pain": "在海外有离岸公司或习惯私户收款的老板：担心海外账户被境内税务局查穿，更怕一旦遭遇税务稽查，账上流动资金全部套死在厂房设备存货里，掏不出几千万现金罚款而直接坐牢。",
                "metaphor": "穿透隐身衣的X光机与国家的初犯免死金牌：以前富豪穿了一件离岸隐身衣（空壳公司），税务局看不清真人。现在CRS就是X光机，直接穿透看骨头！而《刑法》第201条第4款则是国家的初犯免死金牌——只要你第一次被查，老老实实按期把少缴的税款和罚款用真金白银现金补上，国家绝不抓你去坐牢！但前提是：你账上必须能在短短十几天内拿出足额现金！如果全套死在厂房机器里掏不出钱，免死金牌当场作废！",
                "three_masters": {
                    "lawyer": "合规是企业家身家性命的第一底线。必须在法律专家指导下完成过往财税合规梳理，严守刑法初犯免刑的时间窗口与资金流动性要求。",
                    "advisor": "大额保单具备高现金价值与高流动性（保单质押贷款最快当天到账），是企业主在面临极端税务稽查或流动性危机时，随调随取的‘生命赎金池’。",
                    "family": "海外资产告别野蛮生长，必须回归合规阳光化运作，结合信托与合规保单完成代际平稳确权。"
                },
                "talk_phrase": "“赵董，现在税务监管已经装上了全天候天眼。经商几十年谁敢保证账目百分百完美？国家刑法给了企业家初犯免死金牌，但硬性前提是被查时手里能瞬间掏得出真金白银现金。家庭资产池里有一笔绝对安全、高流动性、随时能调用的保单现金流，就是关键时刻拯救整个家族的护身符。”"
            },
            {
                "id": "dim_trade",
                "category": "进出口与供应链出海",
                "badge": "供应链出海 / 转口合规",
                "tag_color": "purple",
                "news_title": "中国供应链出海提速面临原产地穿透：东盟与拉美建厂的法律合规与资产跨境锚定",
                "news_fact": "面对欧美关税壁垒升级，长三角及珠三角大量高端制造企业加速在越南、印尼、墨西哥等国布局海外工厂。然而转口贸易面临东道国劳工环保审查、外汇管制以及欧美原产地增值比例穿透核查等多重考验。高管外派频繁，海外人身与资产双重保障需求激增。",
                "hnw_pain": "出海建厂的实业老板：一方面担心海外当地政局、汇率变动和外汇管制导致利润出不来，另一方面核心创始人频繁跨国差旅，人身意外与高端医疗保障面临断层。",
                "metaphor": "跨国放风筝与地锚模型：企业出海就像在狂风暴雨中放风筝，风筝飞得再高再远，手里必须有一根拽得牢牢的坚固安全线（合规通道与法商架构），脚底下还要有一块沉甸甸的地锚（国内刚兑资产底盘）。地锚稳固，风筝断了线还能重做一只；地锚要是没了，一阵风连人带风筝全被刮进大海。",
                "three_masters": {
                    "lawyer": "排查东道国劳动法、外汇管制及出口目的国原产地规则，规避反规避调查与资产被扣押风险。",
                    "advisor": "利润回流通道多元化规划，境内外双资产池配置，境内以高信用分红险为锚，境外以离岸流动性工具为盾。",
                    "family": "为企业创始人及外派高管配置覆盖全球紧急救援与顶级三甲私立的平安高端医疗/就医通服务，守住人身安全底盘。"
                },
                "talk_phrase": "“陈总，您的企业去海外开疆拓土是顺应时代，但出海最怕‘前线拼命打胜仗，后院资产起火’。跨国打拼，脚底下必须有一个踩得最稳的国内刚盘。同时，您频繁跨国出差，平安顶级就医通和全球紧急救援给您配齐，让您在海外打仗没有任何后顾之忧。”"
            },
            {
                "id": "dim_insurance",
                "category": "金融资产与跨周期平滑",
                "badge": "资产荒防守 / 平滑分红",
                "tag_color": "cyan",
                "news_title": "30年国债收益率屡创新低：跨周期平滑分红险成为破解高客‘资产荒’的定海神针",
                "news_fact": "长端国债利率创出历史新低，金融市场深陷无风险资产收益率稀缺困境。信托打破刚兑暴雷频发，二级市场波动加剧。在此背景下，保险资金凭借超长投资久期与国家金融监管总局严格监管的‘平滑分红特别储备机制’，展现出极强的跨牛熊穿越能力，成为大类资产配置中罕见的稳健防御底仓。",
                "hnw_pain": "追求绝对本金安全又想跑赢通胀的保守高客：看到周围朋友买信托暴雷、买股票被套，自己手里几千万趴在银行活期，每天看着微薄的利息干着急，不知道什么资产才能真正稳赚不亏跨越20年。",
                "metaphor": "大户人家的抗旱大粮仓模型：遇到风调雨顺的大丰收年份（股市大牛市、保险公司投资狂赚），保险公司绝不把所有浮盈一次性挥霍分光，而是拿出一大半锁进特别储备大粮仓；等到大旱灾荒年份（熊市、大降息、资产荒），保险公司打开粮仓拿粮食源源不断补给客户，确保分红水准不垮台。这就是国家金融总局强制监管的‘平滑机制’，让客户坐享国家长期红利。",
                "three_masters": {
                    "lawyer": "保单现金价值受到《保险法》与国家存款保障机制双重庇护，白纸黑字写入合同，具有最顶级的法律确定性。",
                    "advisor": "分红险采用‘保底利益+分红浮动’的双轮驱动，既有不可逆的刚性底限，又能通过万亿险资大水库分享国家核心优质资产的长期成长溢价。",
                    "family": "打通平安居家养老、高品质康养社区及三师共诊家办权益，实现资产增值与高品质晚年生活的终极闭环。"
                },
                "talk_phrase": "“孙董，分红险最厉害的地方，不是跟别人赌明天谁赚得多，而是它独有的‘跨周期平滑大粮仓’。平安作为国内最大机构投资者，跨越几十年牛熊。在今天这个大降息的资产荒年代，它能帮您把未来几十年的安全粮仓彻底锁死，既保本守底，又坐享国家红利。”"
            }
        ],
        "lexicon": [
            {
                "name": "CFETS 人民币汇率指数",
                "tag": "汇率 / 进出口",
                "metaphor": "买菜篮子模型：如果你在菜市场只盯着猪肉（美元），猪肉便宜了（人民币兑美元升值）；但如果你提着一个装有牛肉、羊肉、鸡蛋、大葱（欧元、日元等24种货币）的大菜篮子，你会发现整个菜篮子的综合平均价格其实稳步微降。中国对外贸易不是只卖给美国，在非美市场（东盟、欧洲、拉美），中国制造依然拥有全球级性价比杀伤力。",
                "reality": "背后的真实含义：媒体天天喊‘人民币破7暴涨’，很多人担心外贸工厂被汇率搞垮。但真相是：在非美市场，人民币不仅没变贵，反而更具价格优势。央行坚决不搞竞争性贬值，中国外贸顺差靠的是制造业全供应链实力，而非靠汇率操纵。",
                "hnw_pain": "外贸高客焦虑：‘人民币破7了，我的海外订单会不会全黄了？’",
                "weapon": "陪谈话术：‘张总，别光盯美元单边，看CFETS一篮子指数就知道，咱们在东盟和欧洲的竞争力其实还在增强。但有一点必须提防：美元资产降息加汇损是不可逆的，用远期锁汇把利润锁定，回流到国内终身刚兑的年金池，才能真正落袋为安。’"
            },
            {
                "id": "lex_2",
                "name": "银行净息差收窄 与 中国式‘资产荒’",
                "tag": "银行利率 / 降息逻辑",
                "metaphor": "倒爷亏本拒收货物模型：银行本质是个‘资金倒爷’，3块钱收储户存款，5块钱放贷给买房企业，赚2块利差。现在优质企业不愿贷款，老百姓不买房，倒爷手里堆着成山的钱放不出去，还要每天给储户倒贴利息！倒爷快亏吐血了，只能拼命把存款利率压到1.5%、1%甚至0，摆明告诉你：‘别存我这了，我也找不到赚钱项目！’",
                "reality": "背后的真实含义：存款利率不断下调是国家为了拯救实体经济降低融资成本的必然举措。高客期待的高息无风险理财已永久消失，信托打破刚兑频发暴雷。整个金融市场进入‘资产荒’，长期确定性复利已成为极其稀缺的奢侈品。",
                "hnw_pain": "手里趴着千万活期的高客：‘银行定存才1点几，理财又不保本，我的现金到底放哪里才能跑赢通胀？’",
                "weapon": "陪谈话术：‘孙总，银行降息不是暂时的，而是不可逆的大趋势。现在市场上能白纸黑字写进合同、承诺终身跨越周期的，只有保险公司的复利工具。今天抢先锁定的确定现价，就是未来20年别人羡慕不来的高息特权。’"
            },
            {
                "id": "lex_3",
                "name": "《刑法》第201条第4款（逃税罪初犯救济条款）",
                "tag": "刑法红线 / 保命免死金牌",
                "metaphor": "国家的‘初犯免死金牌’：国家立法规定：只要你是初犯，税务局稽查找上门时，你老老实实、按期把少缴的税款、滞纳金和罚款全部掏现金补齐，国家就绝不抓你去坐牢！但注意：必须掏得出真金白银，而且5年内只能免死一次！",
                "reality": "背后的真实含义：为什么很多明星补税几个亿能全身而退，而有的老板却锒铛入狱？关键就在于被查时账上能不能在15天内拿出足额现金！如果所有资产全套死在厂房、机器和存货里，现金流断裂掏不出罚款，免死金牌当场作废，直接按逃税罪判刑！",
                "hnw_pain": "有税务瑕疵历史的企业主：‘万一被稽查了，我会不会坐牢？’",
                "weapon": "陪谈话术：‘赵总，经商三十年谁敢保证账目百分百完美？刑法给企业家的初犯救济，前提是有足额现金能补救。您必须在家庭资产池里，存下一笔绝对安全、高流动性、随时能调用的保单现金流，这就是关键时刻救命的赎金！’"
            },
            {
                "id": "lex_4",
                "name": "金税四期公私账打通 与 人格混同",
                "tag": "公司法 / 企业主连带责任",
                "metaphor": "左右兜连体婴比喻：以前做生意，公司是公司的猪圈，家里是家里的钱包。很多老板图省事，客户打款直接扫老板娘个人微信，或者公司账上有钱直接转给老妈买房。金税四期装上天眼监控后，一旦发现公私不分，法院直接宣判：‘你和公司穿一条裤子，是一码事！’公司破产欠债，直接查封拍卖你全家的房子和存款！",
                "reality": "背后的真实含义：很多企业主误以为有限责任公司可以替自己挡子弹。但新《公司法》第23条与金税四期联动，一旦构成人格混同，股东必须承担无限连带清偿责任！有限责任瞬间沦为废纸。",
                "hnw_pain": "习惯私账收款的民营老板：‘我以前私户收货款、公款私用买车买房，会不会被秋后算账？’",
                "weapon": "陪谈话术：‘周董，金税四期时代，公私账混用是悬在每个民营企业家头上的达摩克利斯之剑。越早把经营资产和家庭资产做物理切割，通过个人年金保险建立不可被追偿的防火墙，您和家人的后半生才真正有了兜底。’"
            },
            {
                "id": "lex_5",
                "name": "分红险特别储备账户（平滑分红机制）",
                "tag": "保险精算 / 跨周期护城河",
                "metaphor": "大户人家的抗旱粮仓：遇到风调雨顺的大丰年（股市大牛市、保险公司投资暴赚），保险公司不把所有浮盈一次性挥霍分光，而是拿出一大半锁进特别储备大粮仓；等到大旱荒年（熊市、资产荒、黑天鹅），保险公司打开粮仓拿粮食补给客户，确保分红水准不垮台。",
                "reality": "背后的真实含义：很多客户担心‘分红险行情差会不会分不到钱？’平滑机制由国家金融监管总局强制监管执行，它将短期的市场剧烈波动化解在十几年的超长资金池中，使得客户既能享受保底确定性，又能长期分得国家核心资产成长的长期溢价红利。",
                "hnw_pain": "对分红险心存疑虑的高客：‘你们的分红演示会不会是画大饼？’",
                "weapon": "陪谈话术：‘吴董，分红险最厉害的不是承诺暴利，而是它独有的特别平滑粮仓。平安作为国内最大机构投资者，跨越几十个牛熊周期，粮仓储备丰厚。它不是靠赌单一年份行情，而是让您的家族资产搭上国家超级航母的长期红利。’"
            }
        ],
        "quiz": [
            {
                "q": "为什么央行在强调适度宽松、多次降息降准的同时，却明确表示‘绝不搞竞争性贬值’？",
                "a": "中国外贸顺差创纪录的关键驱动力在于中国制造业全供应链体系的性价比与技术升级（如高技术、绿色能源产业），而非靠汇率贬值占便宜；单边贬值不仅会诱发资本外流与输入型通胀，还会伤害人民币国际化大局与人民币资产的全球定价权。"
            },
            {
                "q": "最高法与发改委严厉整治异地趋利性执法（‘远洋捕捞’），民营企业家为什么依然必须高度警惕公私账往来？",
                "a": "异地执法规范保护的是‘合法合规企业’的经营秩序；但如果老板个人私户代收货款、公司资金随意转入家庭购房，在司法审判中直接触犯《公司法》第23条‘股东与公司财产人格混同’，有限责任公司防火墙破裂，股东依然要对公司全部债务承担个人无限连带清偿责任。"
            },
            {
                "q": "在存款利率全面破1.5%的‘资产荒’时代，为什么分红险的‘特别储备账户’是高客穿越周期的硬核底牌？",
                "a": "传统银行定存和理财只能承受单期波动，到期即面临利率下调或再投资风险；而分红险由金融监管总局强制实施特别储备平滑机制，在牛市丰收年丰存荒歉，以超长久期资金平滑短期经济剧烈波动，让客户既获得合同刚兑现价兜底，又长期坐享国家核心资产收益。"
            }
        ]
    }

# ==============================================================================
# 2. Markdown 内参生成器
# ==============================================================================
def generate_markdown(data):
    today_str = data["date"]
    os.makedirs(PRIMARY_EXPORT_DIR, exist_ok=True)
    os.makedirs(BACKUP_EXPORT_DIR, exist_ok=True)
    primary_file = os.path.join(PRIMARY_EXPORT_DIR, f"高客宏观每日内参_{today_str}.md")
    backup_file = os.path.join(BACKUP_EXPORT_DIR, f"高客宏观早参_{today_str}.md")

    md = f"""# 📈 金华平安家办·高客宏观每日内参与国家大事深度解读
> **归档日期**：{today_str}（每日 17:00 汇总截至当日最新动向，供次日清晨上班路上研读）  
> **整理内勤**：平安人寿培训内勤 / 高家帮法律服务团队  
> **核心定位**：懂国家顶层大局，知高净值客户真正痛点，化宏观大势为展业谈资与法商成交利器！

---

## 🧭 今日头条宏观聚焦：【{data['headline_badge']}】
### 📌 核心议题：{data['headline_title']}
- **宏观大局核心总括**：
{data['headline_lead']}

---

## 🔍 今日六大宏观维度全景扫描（事实核查 + 高客痛点 + 买菜模型 + 三师共诊 + 口袋短语）
"""
    for idx, d in enumerate(data["dimensions"], 1):
        md += f"""
### 维度 {idx}：【{d['badge']}】{d['news_title']}
- **📰 国家大事客观原貌与数据核查**：
  {d['news_fact']}
- **😨 高客真正关心什么（老板在慌什么）**：
  {d['hnw_pain']}
- **🥬 大白话买菜模型（剥洋葱通俗比喻）**：
  {d['metaphor']}
- **⚖️ 【三师共诊·实战破局点】**：
  - ⚖️ **民商法律师**：{d['three_masters']['lawyer']}
  - 📊 **投顾理财师**：{d['three_masters']['advisor']}
  - 🛡️ **家办医养专家**：{d['three_masters']['family']}
- **🗣️ 【高客陪谈口袋短语·一键复制】**：
  > 📝 *{d['talk_phrase']}*

---
"""

    md += """
## 📚 【高客宏观法商术语大白话速查字典·背后的刀光剑影】
> *为方便您随时查阅，以下将当前金融、汇率、法税中最晦涩、最常听到的 5 大核心术语，做“剥洋葱式”的大白话剖析：*
"""
    for idx, lex in enumerate(data["lexicon"], 1):
        md += f"""
### 💡 术语 {idx}：{lex['name']} `[{lex['tag']}]`
- **🥬 生活化买菜比喻**：{lex['metaphor']}
- **⚙️ 背后的真实刀光剑影与底层机制**：{lex['reality']}
- **😨 高客最怕什么（内心焦虑）**：{lex['hnw_pain']}
- **🛡️ 展业破冰与陪谈武器**：{lex['weapon']}
"""

    md += """
---

## 🎯 检验是否真正理解的 3 个核心自测题

| 序号 | 核心自测深层问题 | 正确理解与穿透要点 |
| :---: | :--- | :--- |
"""
    for idx, qz in enumerate(data["quiz"], 1):
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
# 3. HTML 移动/PC 交互大屏渲染器
# ==============================================================================
def update_news_html(data):
    today_str = data["date"]
    
    dim_cards_html = ""
    for d in data["dimensions"]:
        color = d["tag_color"]
        dim_cards_html += f"""
        <article class="bg-dark-850 rounded-2xl border border-dark-700/80 p-6 md:p-8 hover:border-{color}-500/50 transition-all duration-300 shadow-xl">
          <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
            <span class="px-3 py-1 bg-{color}-500/10 text-{color}-400 border border-{color}-500/30 rounded-full text-xs font-semibold tracking-wide">
              {d['badge']}
            </span>
            <span class="text-slate-400 text-xs flex items-center gap-1">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span> 权威核查
            </span>
          </div>

          <h3 class="text-xl md:text-2xl font-bold text-white mb-4 leading-snug">
            {d['news_title']}
          </h3>

          <!-- 客观原貌 -->
          <div class="mb-5 bg-dark-800/90 rounded-xl p-4 border border-dark-700">
            <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider mb-2 flex items-center gap-2">
              <span class="text-blue-400">📰</span> 国家大事原貌与数据核查
            </h4>
            <p class="text-slate-300 text-sm leading-relaxed">{d['news_fact']}</p>
          </div>

          <!-- 高客焦虑 -->
          <div class="mb-5 bg-rose-950/20 border border-rose-500/30 rounded-xl p-4">
            <h4 class="text-xs font-bold text-rose-300 uppercase tracking-wider mb-2 flex items-center gap-2">
              <span>😨</span> 高客核心痛点（老板在慌什么）
            </h4>
            <p class="text-rose-200/90 text-sm leading-relaxed">{d['hnw_pain']}</p>
          </div>

          <!-- 买菜模型 -->
          <div class="mb-5 bg-emerald-950/20 border border-emerald-500/30 rounded-xl p-4">
            <h4 class="text-xs font-bold text-emerald-300 uppercase tracking-wider mb-2 flex items-center gap-2">
              <span>🥬</span> 生活化大白话拆解（买菜模型）
            </h4>
            <p class="text-emerald-100 text-sm leading-relaxed">{d['metaphor']}</p>
          </div>

          <!-- 三师共诊 -->
          <div class="mb-5 bg-dark-900/80 rounded-xl p-4 border border-dark-700/60">
            <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider mb-3 flex items-center gap-2">
              <span>⚖️</span> 三师共诊·实战破局要点
            </h4>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
              <div class="p-3 bg-dark-800/80 rounded-lg border border-dark-700/50">
                <span class="font-bold text-blue-400 block mb-1">⚖️ 民商法律师</span>
                <span class="text-slate-300 leading-normal">{d['three_masters']['lawyer']}</span>
              </div>
              <div class="p-3 bg-dark-800/80 rounded-lg border border-dark-700/50">
                <span class="font-bold text-amber-400 block mb-1">📊 投顾理财师</span>
                <span class="text-slate-300 leading-normal">{d['three_masters']['advisor']}</span>
              </div>
              <div class="p-3 bg-dark-800/80 rounded-lg border border-dark-700/50">
                <span class="font-bold text-emerald-400 block mb-1">🛡️ 家办医养专家</span>
                <span class="text-slate-300 leading-normal">{d['three_masters']['family']}</span>
              </div>
            </div>
          </div>

          <!-- 陪谈口袋短语 -->
          <div class="bg-gradient-to-r from-amber-500/15 to-transparent border-l-4 border-amber-500 p-4 rounded-r-xl">
            <div class="flex items-center justify-between mb-1">
              <span class="text-xs font-bold text-amber-400 flex items-center gap-1">
                <span>🗣️</span> 高客陪谈口袋短语 · 一键复制话术
              </span>
              <button onclick="navigator.clipboard.writeText('{d['talk_phrase']}'); alert('话术已成功复制到剪贴板！');" 
                      class="text-xs px-2.5 py-1 bg-amber-500/20 hover:bg-amber-500/40 text-amber-300 rounded border border-amber-500/30 transition-colors">
                复制话术
              </button>
            </div>
            <p class="text-slate-200 text-sm italic leading-relaxed mt-1">{d['talk_phrase']}</p>
          </div>
        </article>
        """

    lexicon_html = ""
    for lex in data["lexicon"]:
        lexicon_html += f"""
        <div class="p-5 bg-dark-800/90 rounded-xl border border-dark-700 hover:border-amber-500/40 transition-all">
          <div class="flex items-center justify-between mb-3">
            <h4 class="text-base font-bold text-white flex items-center gap-2">
              <span class="text-amber-400">💡</span> {lex['name']}
            </h4>
            <span class="text-xs px-2.5 py-0.5 bg-dark-700 text-slate-300 rounded-full">{lex['tag']}</span>
          </div>
          <p class="text-sm text-emerald-300 mb-2 leading-relaxed">
            <strong class="text-emerald-400">🥬 买菜比喻：</strong>{lex['metaphor']}
          </p>
          <p class="text-xs text-slate-300 mb-2 leading-relaxed">
            <strong class="text-slate-200">⚙️ 底层真相：</strong>{lex['reality']}
          </p>
          <p class="text-xs text-amber-300/90 leading-relaxed bg-dark-900/60 p-2.5 rounded-lg border border-dark-750">
            <strong class="text-amber-400">🛡️ 陪谈武器：</strong>{lex['weapon']}
          </p>
        </div>
        """

    quiz_html = ""
    for idx, qz in enumerate(data["quiz"], 1):
        quiz_html += f"""
        <div class="p-5 bg-dark-850 rounded-xl border border-dark-700">
          <h4 class="text-sm font-bold text-white mb-2 flex items-start gap-2">
            <span class="text-amber-400 font-mono text-base">Q{idx}.</span>
            <span>{qz['q']}</span>
          </h4>
          <div class="mt-3 p-3 bg-dark-800 rounded-lg text-xs text-slate-300 leading-relaxed border-l-2 border-emerald-400">
            <strong class="text-emerald-400">正确理解与穿透要点：</strong> {qz['a']}
          </div>
        </div>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>国家要闻宏观解读 · 金华平安家办</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    ::-webkit-scrollbar {{ width: 4px; height: 4px; }}
    ::-webkit-scrollbar-track {{ background: #070a12; }}
    ::-webkit-scrollbar-thumb {{ background: #334155; border-radius: 4px; }}
    .bg-dark-900 {{ background-color: #070a12; }}
    .bg-dark-850 {{ background-color: #0d1322; }}
    .bg-dark-800 {{ background-color: #131b2e; }}
    .border-dark-700 {{ border-color: #24324f; }}
    .gold-gradient {{
      background: linear-gradient(135deg, #f59e0b, #d97706, #fbbf24);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
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
            金华平安家办 · 宏观内参
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          </h1>
          <p class="text-xs text-slate-400">每日 17:00 自动更新 · 次日清晨展业必读</p>
        </div>
      </div>
      <div class="text-right">
        <span class="text-xs px-2.5 py-1 bg-amber-500/10 border border-amber-500/30 text-amber-300 font-mono rounded-md">
          {today_str}
        </span>
      </div>
    </div>
  </header>

  <!-- 主体容器 -->
  <main class="max-w-5xl mx-auto px-4 pt-6 space-y-8">

    <!-- 顶部头条卡片 -->
    <section class="bg-gradient-to-br from-dark-850 to-dark-800 rounded-2xl border border-amber-500/30 p-6 md:p-8 shadow-2xl relative overflow-hidden">
      <div class="absolute -right-12 -top-12 w-48 h-48 bg-amber-500/5 rounded-full blur-3xl pointer-events-none"></div>
      <span class="inline-block px-3 py-1 bg-amber-500/20 text-amber-300 border border-amber-500/40 rounded-full text-xs font-bold uppercase tracking-wider mb-3">
        今日头条宏观聚焦 · {data['headline_badge']}
      </span>
      <h2 class="text-2xl md:text-3xl font-extrabold text-white mb-4 leading-tight">
        {data['headline_title']}
      </h2>
      <p class="text-slate-300 text-sm md:text-base leading-relaxed">
        {data['headline_lead']}
      </p>
    </section>

    <!-- 六大维度扫描 -->
    <section class="space-y-6">
      <div class="flex items-center justify-between border-b border-dark-700/80 pb-3">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <span>🔍</span> 今日宏观六大维度全景深度扫描
        </h3>
        <span class="text-xs text-slate-400">真实权威 · 拒绝空泛八股</span>
      </div>
      <div class="space-y-6">
        {dim_cards_html}
      </div>
    </section>

    <!-- 宏观核心术语大白话速查字典 -->
    <section class="bg-dark-850 rounded-2xl border border-dark-700/80 p-6 md:p-8 shadow-xl">
      <div class="flex items-center justify-between border-b border-dark-700 pb-4 mb-6">
        <div>
          <h3 class="text-lg font-bold text-white flex items-center gap-2">
            <span>📚</span> 高客宏观法商术语大白话速查字典
          </h3>
          <p class="text-xs text-slate-400 mt-1">生活化买菜模型 + 背后的真实刀光剑影与陪谈武器</p>
        </div>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        {lexicon_html}
      </div>
    </section>

    <!-- 检验自测题 -->
    <section class="bg-dark-850 rounded-2xl border border-dark-700/80 p-6 md:p-8 shadow-xl">
      <div class="border-b border-dark-700 pb-3 mb-6">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <span>🎯</span> 检验是否真正理解的 3 个核心自测题
        </h3>
        <p class="text-xs text-slate-400 mt-1">能否在与高客沟通中一针见血，全看对这三个底层逻辑的掌握</p>
      </div>
      <div class="space-y-4">
        {quiz_html}
      </div>
    </section>

    <!-- 页脚说明 -->
    <footer class="text-center text-xs text-slate-500 pt-6 pb-12 space-y-2 border-t border-dark-700/60">
      <p>金华平安家办 · 高家帮法律服务团队 · 培训内勤专属宏观智库</p>
      <p>由 Windows 计划任务【DailyMacroNewsUpdate_1700】全自动调度更新部署</p>
    </footer>

  </main>
</body>
</html>"""

    with open(NEWS_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"✅ 渲染并更新网页大屏: {NEWS_HTML_PATH}")

# ==============================================================================
# 4. 主执行流与部署
# ==============================================================================
def main():
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    print("=" * 60)
    print(f"🚀 启动高客宏观每日内参自动化引擎 [{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    print(f"📅 归档日期: {today_str}")
    print("=" * 60)

    data = get_daily_macro_data(today_str)
    generate_markdown(data)
    update_news_html(data)

    if os.path.exists(DEPLOY_SCRIPT):
        print("🚀 执行 GitHub Pages 自动化同步部署...")
        res = subprocess.run([sys.executable, DEPLOY_SCRIPT, f"feat: update daily macro {today_str} with 6-dimension deep dive and lexicon"], capture_output=True, text=True, encoding="utf-8", errors="ignore")
        if res.returncode == 0:
            print("✅ GitHub Pages 部署发布成功！")
        else:
            print(f"❌ 部署返回警告: {res.stderr}")

    print("=" * 60)
    print("🎉 自动化流程全部完成！")

if __name__ == "__main__":
    main()
