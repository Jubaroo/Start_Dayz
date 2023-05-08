@echo off
REM This script deletes unnecessary log files, RPT files, and mdmp files from the DayZ folder.
REM Usage: Start_Dayz.bat

set "DayZFolder=%LOCALAPPDATA%\DayZ"
if not exist "%DayZFolder%" (
  echo Error: DayZ folder not found.
  pause
  exit /b 1
)

set "total_size=0"
set "files_deleted=false"
pushd "%DayZFolder%" || (
  echo Error: Could not switch to the DayZ folder.
  pause
  exit /b 1
)
if exist (*.log *.RPT *.mdmp) (
  for /r %%f in (*.log *.RPT *.mdmp) do (
    set "files_deleted=true"
    set /a "total_size+=%%~zf"
    del "%%~ff"
  )
)

if "%files_deleted%"=="true" (
  for /f "delims=" %%a in ('echo %total_size%') do echo Total size of deleted files: %%~za MB
) else (
  echo No files were deleted.
)

popd

echo.
set /a "countdown=5"
for /l %%i in (%countdown%,-1,1) do (
  echo Launching DayZ in %%i seconds...
  timeout /t 1 /nobreak >nul
)
  
  start steam://rungameid/221100
)
