# -*- coding: utf-8 -*-
"""
更新 andre4life.github.io portal_links.json 与 index.html:
1. 将 national_news 升级为 economic_daily (金华家办 · 每日经济日报与宏观大政中枢)
2. 设定 isHero: true 并置于首屏核心位置
3. 更新 index.html 中的 isHero 判断逻辑
"""
import json
import os
import re

PORTAL_DIR = r"D:\Antigravity输出\andre4life.github.io"
PORTAL_LINKS_PATH = os.path.join(PORTAL_DIR, "portal_links.json")
INDEX_HTML_PATH = os.path.join(PORTAL_DIR, "index.html")

# 1. 更新 portal_links.json
with open(PORTAL_LINKS_PATH, "r", encoding="utf-8") as f:
    links = json.load(f)

# 寻找或替换
found = False
for item in links:
    if item["id"] in ["national_news", "economic_daily"]:
        item["id"] = "economic_daily"
        item["title"] = "金华家办 · 每日经济日报与宏观大政中枢"
        item["category"] = "business"
        item["categoryName"] = "业务与法商"
        item["icon"] = "📈"
        item["tag"] = "每日经济日报 · 宏观大盘"
        item["badge"] = "每日更新"
        item["url"] = "news/index.html"
        item["desc"] = "十维宏观数据全景矩阵+ECharts交互大屏+三师共诊透析+生活化买菜比喻+高客两分钟展业口袋短语。"
        item["status"] = "active"
        item["isHero"] = True
        found = True
        break

if not found:
    links.insert(1, {
        "id": "economic_daily",
        "title": "金华家办 · 每日经济日报与宏观大政中枢",
        "category": "business",
        "categoryName": "业务与法商",
        "icon": "📈",
        "tag": "每日经济日报 · 宏观大盘",
        "badge": "每日更新",
        "url": "news/index.html",
        "desc": "十维宏观数据全景矩阵+ECharts交互大屏+三师共诊透析+生活化买菜比喻+高客两分钟展业口袋短语。",
        "status": "active",
        "isHero": True
    })

with open(PORTAL_LINKS_PATH, "w", encoding="utf-8") as f:
    json.dump(links, f, ensure_ascii=False, indent=2)
print("✅ portal_links.json 已更新")

# 2. 更新 index.html 中的 isHero 判断
with open(INDEX_HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 替换 const isHero = item.id === 'mindradar'; -> const isHero = item.id === 'mindradar' || item.id === 'economic_daily' || item.isHero === true;
html = re.sub(
    r"const isHero\s*=\s*item\.id\s*===\s*'mindradar'[^;]*;",
    "const isHero = item.id === 'mindradar' || item.id === 'economic_daily' || item.isHero === true;",
    html
)

with open(INDEX_HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)
print("✅ andre4life.github.io/index.html 已更新")
