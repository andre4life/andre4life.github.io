@echo off
chcp 65001 >nul
cd /d "D:\Antigravity输出\andre4life.github.io\news"
set "LOG_DIR=D:\Antigravity输出\高客宏观每日内参"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"
set "LOG_FILE=%LOG_DIR%\daily_macro_run.log"

echo ======================================================== >> "%LOG_FILE%"
echo [%date% %time%] 🚀 每日 17:00 宏观与国家大事追踪自动执行开始... >> "%LOG_FILE%"
echo ======================================================== >> "%LOG_FILE%"

"C:\Users\18201\AppData\Local\Programs\Python\Python311\python.exe" generate_daily_macro.py >> "%LOG_FILE%" 2>&1

echo [%date% %time%] ✅ 任务执行完毕 >> "%LOG_FILE%"
