@echo off
chcp 65001 >nul
echo ======================================================== >> "D:\Antigravity输出\高客宏观早参\daily_macro_run.log"
echo [每日17:00宏观与国家大事追踪] 启动于 %date% %time% >> "D:\Antigravity输出\高客宏观早参\daily_macro_run.log"
echo ======================================================== >> "D:\Antigravity输出\高客宏观早参\daily_macro_run.log"

cd /d "D:\Antigravity输出\andre4life.github.io"
"C:\Users\18201\AppData\Local\Programs\Python\Python311\python.exe" "D:\Antigravity输出\andre4life.github.io\news\generate_daily_macro.py" >> "D:\Antigravity输出\高客宏观早参\daily_macro_run.log" 2>&1

echo 任务执行完毕于 %date% %time% >> "D:\Antigravity输出\高客宏观早参\daily_macro_run.log"
