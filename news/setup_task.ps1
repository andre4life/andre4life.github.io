# 注册每日17:00任务计划 (使用当前用户实际SID避免中文域名映射问题)
$ErrorActionPreference = "Stop"

$taskName = "DailyMacroNewsUpdate_1700"
$sid = [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value
$principal = New-ScheduledTaskPrincipal -UserId $sid -LogonType Interactive

$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Bypass -WindowStyle Hidden -File `"`"D:\Antigravity输出\andre4life.github.io\news\run_daily_macro_1700.ps1`"`""
$trigger = New-ScheduledTaskTrigger -Daily -At "17:00"
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Description "每日下午17:00自动抓取截至当日的宏观动态与国家大事并部署至个人工作台" -Force

Write-Host "✅ 任务计划 [$taskName] 注册成功！"
$task = Get-ScheduledTask -TaskName $taskName
$info = Get-ScheduledTaskInfo -TaskName $taskName
[PSCustomObject]@{
    TaskName = $task.TaskName
    State = $task.State
    NextRunTime = $info.NextRunTime
    LastRunTime = $info.LastRunTime
} | Format-List
