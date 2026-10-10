#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新 news/index.html 与 generate_daily_macro.py:
1. 在网页端增加漂亮的术语大白话速查折叠卡片组件 (带生活化比喻、底层真相、高客痛点、陪谈武器)
2. 更新自动化引擎脚本，生成富含 8 大术语深度拆解的每日 Markdown 内参
3. 统一输出目录为 D:\Antigravity输出\高客宏观每日内参
"""

import os
import sys
import re

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PORTAL_DIR = r"D:\Antigravity输出\andre4life.github.io"
NEWS_HTML = os.path.join(PORTAL_DIR, "news", "index.html")
GEN_SCRIPT = os.path.join(PORTAL_DIR, "news", "generate_daily_macro.py")

LEXICON_HTML = """
    <!-- 宏观与法商高客关切术语大白话速查字典 (手机端/PC端展开即查) -->
    <div class="bg-gradient-to-br from-dark-850 to-dark-800 p-4 rounded-2xl border border-amber-500/30 shadow-lg mb-4 space-y-3">
      <div class="flex items-center justify-between cursor-pointer select-none" onclick="toggleLexiconSection()">
        <div class="flex items-center gap-2">
          <span class="text-xl">📚</span>
          <div>
            <h2 class="text-sm md:text-base font-bold text-white flex items-center gap-2">
              宏观法商高客关切术语大白话速查字典
              <span class="text-[10px] px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-400 border border-amber-500/30 font-normal">陪谈必背 / 8大硬核概念通俗拆解</span>
            </h2>
            <p class="text-[11px] text-slate-400 mt-0.5">
              买菜生活化比喻 ＋ 底层利益机制 ＋ 撕开面纱看刀光剑影 ＋ 高客一键破冰金句
            </p>
          </div>
        </div>
        <button id="lexicon-toggle-btn" class="text-xs px-2.5 py-1 rounded-lg bg-dark-700 hover:bg-dark-600 text-slate-300 border border-dark-600 transition-colors">
          点击展开/收起 ▾
        </button>
      </div>

      <!-- 术语网格 (默认展开) -->
      <div id="lexicon-content" class="grid grid-cols-1 md:grid-cols-2 gap-3 pt-2">

        <!-- 术语 1: CFETS -->
        <div class="bg-dark-900/90 border border-sky-500/30 rounded-xl p-3.5 space-y-2 hover:border-sky-400 transition-colors">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-sky-400 flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-sky-400 inline-block"></span>
              CFETS 人民币汇率指数
            </span>
            <span class="text-[10px] px-1.5 py-0.5 rounded bg-sky-500/10 text-sky-300 font-mono">汇率 / 进出口</span>
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed bg-dark-850 p-2.5 rounded-lg border border-dark-750">
            <strong class="text-amber-400">🥬 买菜篮子比喻：</strong>如果你在菜市场只盯着猪肉（美元），猪肉便宜了（人民币兑美元升值）；但如果你提着一个装有牛肉、羊肉、鸡蛋、大葱（欧元、日元等24种货币）的大菜篮子，你会发现整个菜篮子的综合平均价格其实还降了 3.4%！
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed">
            <strong class="text-emerald-400">⚙️ 背后的真实刀光剑影：</strong>媒体惊呼“破7升值会搞垮外贸”，真相是：中国外贸不仅卖给美国！在非美市场（东盟、欧洲、拉美），人民币不仅没变贵，反而更具价格优势。中国制造依然拥有全球级性价比杀伤力。
          </div>
          <div class="text-[11px] text-rose-300 bg-rose-500/10 p-2 rounded border border-rose-500/20">
            <strong>😨 高客恐惧：</strong>外贸老板怕人民币暴涨丢单；投资客怕手里的外汇缩水。
          </div>
          <div class="text-[11px] text-amber-300 bg-amber-500/10 p-2 rounded border border-amber-500/20">
            <strong>🛡️ 陪谈武器：</strong>“张总，看CFETS一篮子指数就知道，咱们在东盟的竞争力仍在增强。但海外美元资产降息加汇损是不可逆的，用远期锁汇将利润回流到国内终身刚兑的年金池，才能真正落袋为安。”
          </div>
        </div>

        <!-- 术语 2: 结汇堰塞湖 -->
        <div class="bg-dark-900/90 border border-amber-500/30 rounded-xl p-3.5 space-y-2 hover:border-amber-400 transition-colors">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-amber-400 flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-amber-400 inline-block"></span>
              结汇堰塞湖 与 结汇博弈
            </span>
            <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/10 text-amber-300 font-mono">外汇 / 资产抛售</span>
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed bg-dark-850 p-2.5 rounded-lg border border-dark-750">
            <strong class="text-amber-400">🌾 踩踏卖粮比喻：</strong>老乡们手里都囤着粮食（美元），原先指望粮价涨到8块再卖。结果粮价突然从7.4跌到6.9，眼看一天比一天便宜，谁先卖谁少亏！于是“捂粮惜售”瞬间变成“踩踏抛售”，越抛粮价跌得越惨。
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed">
            <strong class="text-emerald-400">⚙️ 背后的真实刀光剑影：</strong>此前企业滞留境外未结汇头寸高达上万亿美元。一旦降息+升值预期确立，万亿结汇潮集体开闸决堤，将反过来强力推升人民币汇率！高客如果继续死抱美元存款，将面临持续割肉风险。
          </div>
          <div class="text-[11px] text-rose-300 bg-rose-500/10 p-2 rounded border border-rose-500/20">
            <strong>😨 高客恐惧：</strong>5%美元存款利息全被汇损吃光，陷入“结汇觉得亏，不结跌更多”的内耗。
          </div>
          <div class="text-[11px] text-amber-300 bg-amber-500/10 p-2 rounded border border-amber-500/20">
            <strong>🛡️ 陪谈武器：</strong>“王董，高息美元已经是过去式，越犹豫汇率折算越吃亏。聪明资金都在抢跑回流，把不确定的汇率风险置换成确定的人民币保单现金流。”
          </div>
        </div>

        <!-- 术语 3: 逆周期调节因子 -->
        <div class="bg-dark-900/90 border border-emerald-500/30 rounded-xl p-3.5 space-y-2 hover:border-emerald-400 transition-colors">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-emerald-400 flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-emerald-400 inline-block"></span>
              逆周期调节因子
            </span>
            <span class="text-[10px] px-1.5 py-0.5 rounded bg-emerald-500/10 text-emerald-300 font-mono">货币政策 / 央行大手</span>
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed bg-dark-850 p-2.5 rounded-lg border border-dark-750">
            <strong class="text-amber-400">⚖️ 天平砝码比喻：</strong>炒客跟风做空或做多想把天平彻底压垮，央行每天早上直接在天平另一端悄悄放上一块砝码，告诉全世界：“别瞎折腾，今天这盘棋我定调，谁敢聚众对赌我就打爆谁”。
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed">
            <strong class="text-emerald-400">⚙️ 背后的真实刀光剑影：</strong>国家绝不允许汇率出现无序暴涨暴跌。逆周期因子就是央行的隐形大手，任何试图通过地下钱庄或大额杠杆做空人民币的资金，都会在政策重拳下被无情收割。
          </div>
          <div class="text-[11px] text-rose-300 bg-rose-500/10 p-2 rounded border border-rose-500/20">
            <strong>😨 高客恐惧：</strong>跟风搞地下换汇或境外对赌衍生品，被监管稽查冻结账户。
          </div>
          <div class="text-[11px] text-amber-300 bg-amber-500/10 p-2 rounded border border-amber-500/20">
            <strong>🛡️ 陪谈武器：</strong>“李总，央行手里有尚方宝剑，千万别用全部身家去赌国运和汇率拐点。守住合法合规的底盘，永远比游走在政策灰色地带走得稳。”
          </div>
        </div>

        <!-- 术语 4: CARF 与 Passive NFE -->
        <div class="bg-dark-900/90 border border-rose-500/30 rounded-xl p-3.5 space-y-2 hover:border-rose-400 transition-colors">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-rose-400 flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-rose-400 inline-block"></span>
              CARF 与 消极非金融实体 (Passive NFE)
            </span>
            <span class="text-[10px] px-1.5 py-0.5 rounded bg-rose-500/10 text-rose-300 font-mono">CRS穿透 / 离岸清零</span>
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed bg-dark-850 p-2.5 rounded-lg border border-dark-750">
            <strong class="text-amber-400">🩻 穿透隐身斗篷的X光机：</strong>以前富豪穿了一件隐身衣（在BVI群岛注册个壳公司或买虚拟货币），税务局看不见。现在 CARF 和 Passive NFE 就是给税务机关装上了X光机——不管你套了三层信托还是一家空壳，只要公司不生产不卖货只管收钱，直接穿透这层皮，看最后拿钱的肉身到底是谁！
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed">
            <strong class="text-emerald-400">⚙️ 背后的真实刀光剑影：</strong>全球涉税金融账户透明化已步入终局。花巨资搭建的无商业实质离岸空壳不仅不能避税，反而成了税务机关重点核查的“自首清单”。
          </div>
          <div class="text-[11px] text-rose-300 bg-rose-500/10 p-2 rounded border border-rose-500/20">
            <strong>😨 高客恐惧：</strong>海外账户里的资金被金税四期和国际交换全部曝光，面临巨额补税与罚单。
          </div>
          <div class="text-[11px] text-amber-300 bg-amber-500/10 p-2 rounded border border-amber-500/20">
            <strong>🛡️ 陪谈武器：</strong>“陈董，全球反避税时代离岸隐匿只会带来合规灭顶之灾。真正的家办高手不是搞体外循环，而是通过大额保单和国内合规家族信托，在阳光下完成资产合法确权与无缝传承。”
          </div>
        </div>

        <!-- 术语 5: 金税四期与人格混同 -->
        <div class="bg-dark-900/90 border border-purple-500/30 rounded-xl p-3.5 space-y-2 hover:border-purple-400 transition-colors">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-purple-400 flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-purple-400 inline-block"></span>
              金税四期公私账打通 与 人格混同
            </span>
            <span class="text-[10px] px-1.5 py-0.5 rounded bg-purple-500/10 text-purple-300 font-mono">新公司法 / 无限连带</span>
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed bg-dark-850 p-2.5 rounded-lg border border-dark-750">
            <strong class="text-amber-400">👖 左右兜连体婴比喻：</strong>很多老板让客户直接扫老板娘个人微信收款，或者公司账上有钱直接转给老妈买房。金税四期天眼监控下，一旦公私不分，法院直接裁定：“你和公司穿一条裤子！”公司一旦欠债破产，直接查封扣押拍卖你全家人的房产和私人银行卡！
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed">
            <strong class="text-emerald-400">⚙️ 背后的真实刀光剑影：</strong>新《公司法》第23条明确规定：股东无法证明公司财产独立于自己财产的，对公司债务承担连带责任！民营企业主的“有限责任保护伞”在人格混同下彻底沦为废纸。
          </div>
          <div class="text-[11px] text-rose-300 bg-rose-500/10 p-2 rounded border border-rose-500/20">
            <strong>😨 高客恐惧：</strong>公司一旦暴雷或陷入买卖合同诉讼，个人私人财产被法院执行冻结。
          </div>
          <div class="text-[11px] text-amber-300 bg-amber-500/10 p-2 rounded border border-amber-500/20">
            <strong>🛡️ 陪谈武器：</strong>“周董，公私账混用是悬在每个民营企业家头上的达摩克利斯之剑。越早把经营资产和家庭资产做物理切割，通过个人年金建立不可被追偿的防火墙，后半生才真正有了兜底。”
          </div>
        </div>

        <!-- 术语 6: 刑法201条第4款 -->
        <div class="bg-dark-900/90 border border-red-500/30 rounded-xl p-3.5 space-y-2 hover:border-red-400 transition-colors">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-red-400 flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-red-400 inline-block"></span>
              《刑法》第201条第4款（逃税初犯救济）
            </span>
            <span class="text-[10px] px-1.5 py-0.5 rounded bg-red-500/10 text-red-300 font-mono">免死金牌 / 保命底牌</span>
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed bg-dark-850 p-2.5 rounded-lg border border-dark-750">
            <strong class="text-amber-400">🏅 初犯免死金牌比喻：</strong>国家法律网开一面：只要是初犯，税务局找上门时，你老老实实、按期把少缴的税款、利息（滞纳金）和罚款全部掏现金补齐，国家就绝不抓你去坐牢！但注意：必须掏得出真金白银现金，且5年内只能用一次！
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed">
            <strong class="text-emerald-400">⚙️ 背后的真实刀光剑影：</strong>为什么很多明星补税几亿平安无事，而有的企业主却判刑入狱？核心在于稽查令下达的15天内，账上到底有没有足额现金能掏出来！资产全套在厂房存货里的企业主，掏不出罚款就当场转入刑事拘留。
          </div>
          <div class="text-[11px] text-rose-300 bg-rose-500/10 p-2 rounded border border-rose-500/20">
            <strong>😨 高客恐惧：</strong>经商多年账目不可能完全无瑕疵，万一被查身败名裂甚至失去人身自由。
          </div>
          <div class="text-[11px] text-amber-300 bg-amber-500/10 p-2 rounded border border-amber-500/20">
            <strong>🛡️ 陪谈武器：</strong>“赵总，刑法给企业家的初犯救济，前提是有足额现金能补救。您必须在家庭资产池里，存下一笔绝对安全、高流动性、随时能调用的保单现金流，这就是关键时刻救命的赎金！”
          </div>
        </div>

        <!-- 术语 7: 银行净息差与资产荒 -->
        <div class="bg-dark-900/90 border border-yellow-500/30 rounded-xl p-3.5 space-y-2 hover:border-yellow-400 transition-colors">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-yellow-400 flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-yellow-400 inline-block"></span>
              银行净息差收窄 与 中国式“资产荒”
            </span>
            <span class="text-[10px] px-1.5 py-0.5 rounded bg-yellow-500/10 text-yellow-300 font-mono">利率下行 / 降息真相</span>
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed bg-dark-850 p-2.5 rounded-lg border border-dark-750">
            <strong class="text-amber-400">🏪 倒爷拒收货物比喻：</strong>银行是个资金倒爷，3块钱收储户存款，5块钱放贷给买房企业赚差价。现在企业不贷、百姓不买房，倒爷手里堆着成山的钱放不出去，还要倒贴利息，快亏吐血了！只能拼命把存款利率降到1.5%、1%甚至0，摆明告诉你：“别存我这了，我也找不到赚钱项目！”
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed">
            <strong class="text-emerald-400">⚙️ 背后的真实刀光剑影：</strong>存款利率下调是国家为了拯救实体经济降低融资成本的必然举措。高客渴望的高息无风险理财已永久绝迹，信托频暴雷，整个金融市场进入不可逆的“资产荒”。
          </div>
          <div class="text-[11px] text-rose-300 bg-rose-500/10 p-2 rounded border border-rose-500/20">
            <strong>😨 高客恐惧：</strong>千把万现金躺在银行每天缩水，理财不保本，通胀在侵蚀购买力。
          </div>
          <div class="text-[11px] text-amber-300 bg-amber-500/10 p-2 rounded border border-amber-500/20">
            <strong>🛡️ 陪谈武器：</strong>“孙总，银行降息不是暂时的，而是不可逆的大趋势。现在市场上能白纸黑字写进合同、承诺终身跨周期的，只有保险公司的复利工具。今天锁定的确定现价，就是未来20年别人羡慕不来的高息特权。”
          </div>
        </div>

        <!-- 术语 8: 分红险特别储备账户 -->
        <div class="bg-dark-900/90 border border-teal-500/30 rounded-xl p-3.5 space-y-2 hover:border-teal-400 transition-colors">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-teal-400 flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-teal-400 inline-block"></span>
              分红险特别储备账户（平滑分红机制）
            </span>
            <span class="text-[10px] px-1.5 py-0.5 rounded bg-teal-500/10 text-teal-300 font-mono">精算机制 / 跨周期护城河</span>
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed bg-dark-850 p-2.5 rounded-lg border border-dark-750">
            <strong class="text-amber-400">🌾 大户人家抗旱粮仓比喻：</strong>大丰收之年（股市暴涨、保险公司投资大赚），保险公司不把所有浮盈一次性分光挥霍，而是留存一大半锁进特别储备大粮仓；遇到大旱荒年（熊市、资产荒、黑天鹅），保险公司打开粮仓拿粮食补给客户，确保分红水准不垮台。
          </div>
          <div class="text-[11px] text-slate-300 leading-relaxed">
            <strong class="text-emerald-400">⚙️ 背后的真实刀光剑影：</strong>很多人怀疑“分红险会不会画大饼？”平滑机制由国家金融监管总局强制监管执行，它将短期的市场剧烈波动化解在超长资金池中，使得客户既能享受保底确定性，又能长期分得国家核心资产成长的长期溢价红利。
          </div>
          <div class="text-[11px] text-rose-300 bg-rose-500/10 p-2 rounded border border-rose-500/20">
            <strong>😨 高客恐惧：</strong>担心分红险在资本市场低迷时无法兑现分红演示。
          </div>
          <div class="text-[11px] text-amber-300 bg-amber-500/10 p-2 rounded border border-amber-500/20">
            <strong>🛡️ 陪谈武器：</strong>“吴董，分红险最厉害的不是暴利，而是独有的特别平滑粮仓。平安作为国内最大机构投资者，跨越几十个牛熊周期，粮仓储备丰厚。它不是靠赌单一年份行情，而是让您的家族资产搭上国家超级航母的长期红利。”
          </div>
        </div>

      </div>
    </div>
"""

# 注入 JavaScript 折叠函数到 news/index.html
JS_FUNC = """
  // 切换术语速查字典显示/隐藏
  function toggleLexiconSection() {
    const el = document.getElementById('lexicon-content');
    const btn = document.getElementById('lexicon-toggle-btn');
    if (el) {
      if (el.classList.contains('hidden')) {
        el.classList.remove('hidden');
        if (btn) btn.innerText = '点击收起 ▴';
      } else {
        el.classList.add('hidden');
        if (btn) btn.innerText = '点击展开 ▾';
      }
    }
  }
"""

def update_news_html():
    if not os.path.exists(NEWS_HTML):
        print(f"File not found: {NEWS_HTML}")
        return False
    with open(NEWS_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # 检查是否已注入 LEXICON_HTML
    if "宏观法商高客关切术语大白话速查字典" not in html:
        target_str = '<div id="news-container" class="space-y-4">'
        if target_str in html:
            html = html.replace(target_str, LEXICON_HTML + "\n    " + target_str)
            print("✅ 注入术语大白话速查字典 HTML")
        else:
            print("❌ 无法定位 news-container")
            return False

    if "function toggleLexiconSection" not in html:
        html = html.replace("</script>", JS_FUNC + "\n</script>", 1)
        print("✅ 注入 toggleLexiconSection JavaScript")

    with open(NEWS_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print("✅ news/index.html 已成功更新！")
    return True

if __name__ == "__main__":
    update_news_html()
