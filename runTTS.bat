@echo off
set /p prompt=Enter the text prompt (use quotes to escape special characters "<>"): 
set /p voice=Enter voice to synthesize without quotes("tara", "leah", "jess", "leo", "dan", "mia", "zac", "zoe"): 

powershell -Command "Set-ExecutionPolicy Bypass -Scope Process; .\.venv\Scripts\Activate.ps1; python .\demo.py --prompt \"%prompt%\" --voice  \"%voice%\"; deactivate; [console]::beep(500, 500);" 