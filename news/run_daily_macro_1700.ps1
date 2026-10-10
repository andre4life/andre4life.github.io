# 每日17:00高客宏观与国家大事追踪自动化执行脚本
$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$logDir = "D:\Antigravity输出\高客宏观每日内参"
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

$logFile = "$logDir\daily_macro_run.log"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

"========================================================" | Out-File -FilePath $logFile -Append -Encoding utf8
"[$timestamp] 🚀 每日 17:00 宏观与国家大事追踪自动执行开始..." | Out-File -FilePath $logFile -Append -Encoding utf8
"========================================================" | Out-File -FilePath $logFile -Append -Encoding utf8

$pythonExe = "C:\Users\18201\AppData\Local\Programs\Python\Python311\python.exe"
$scriptPath = "D:\Antigravity输出\andre4life.github.io\news\generate_daily_macro.py"

& $pythonExe $scriptPath *>> $logFile

$endTimestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
"[$endTimestamp] ✅ 任务执行完毕" | Out-File -FilePath $logFile -Append -Encoding utf8
