# -*- coding: utf-8 -*-
import subprocess
import os
import sys
import re

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

PORTAL_DIR = r"D:\Antigravity输出\andre4life.github.io"
HOME = os.path.expanduser("~")
CRED_PATH = os.path.join(HOME, ".git-credentials")

if not os.path.exists(CRED_PATH):
    print("未检测到 ~/.git-credentials 凭据文件")
    sys.exit(1)

with open(CRED_PATH, encoding="utf-8") as f:
    cred = f.read()

m = re.search(r"https://([^:]+):([^@]+)@github\.com", cred)
if not m:
    print("无法从 .git-credentials 解析 GitHub 凭据")
    sys.exit(1)

USER, TOKEN = m.group(1), m.group(2)
AUTH_URL = f"https://{USER}:{TOKEN}@github.com/andre4life/andre4life.github.io.git"

def run(cmd, check=True):
    env = dict(os.environ)
    env["GIT_TERMINAL_PROMPT"] = "0"
    r = subprocess.run(cmd, cwd=PORTAL_DIR, capture_output=True, text=True, env=env, shell=True)
    if check and r.returncode != 0:
        print(f"命令执行警告 [{cmd}]:\n{r.stderr.strip()}")
    return r

print("==================================================")
print("正在部署个人数字中枢至 https://andre4life.github.io/ ...")
print("==================================================")

run("git add -A")
status_res = run("git status --porcelain", check=False)

if status_res.stdout.strip():
    run('git commit -m "feat: deploy Master Portal and MindRadar Workbench"')
    print("本地变更已完成提交")
else:
    print("无新变更需要提交")

# Push to GitHub
print("正在推送至 GitHub Pages 远端仓库...")
push_cmd = f'git -c credential.helper= push "{AUTH_URL}" main'
push_res = run(push_cmd, check=False)

if push_res.returncode == 0:
    print("==================================================")
    print("部署成功！")
    print("个人数字中枢总链接: https://andre4life.github.io/")
    print("心智雷达工作台直达: https://andre4life.github.io/mindradar/")
    print("==================================================")
else:
    print("尝试 fetch & merge 后重新推送...")
    run("git fetch origin main")
    run("git merge origin/main --ff-only")
    retry_push = run(push_cmd, check=False)
    if retry_push.returncode == 0:
        print("重试推送成功！")
    else:
        print("推送失败:", retry_push.stderr.strip())
