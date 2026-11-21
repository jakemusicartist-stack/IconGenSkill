@echo off
setlocal EnableDelayedExpansion

title macOS App Icon Designer - Multi-Agent Skill Installer

echo =======================================================================
echo    APPLE macOS APP ICON DESIGNER - MULTI-AGENT SKILL INSTALLER
echo =======================================================================
echo.

set "SCRIPT_DIR=%~dp0"
set "SOURCE_SKILL=%SCRIPT_DIR%skills\macos-icon-designer"
set "IS_SILENT=0"

if not exist "%SOURCE_SKILL%\SKILL.md" (
    if exist "%SCRIPT_DIR%SKILL.md" (
        set "SOURCE_SKILL=%SCRIPT_DIR%"
    ) else (
        echo [ERROR] Could not find macos-icon-designer skill files!
        echo Expected at: %SOURCE_SKILL%
        if "%~1"=="" pause
        exit /b 1
    )
)

:: Check Python installation
where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    for /f "tokens=*" %%v in ('python --version 2^>^&1') do set "PY_VER=%%v"
    echo [OK] Detected Python: !PY_VER!
) else (
    where py >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        for /f "tokens=*" %%v in ('py -3 --version 2^>^&1') do set "PY_VER=%%v"
        echo [OK] Detected Python: !PY_VER!
    ) else (
        echo [WARNING] Python was not found in PATH.
        echo Python is recommended to run the icon preview and .icns export tools.
    )
)

:: Optional Python Pillow check
python -c "import PIL" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [INFO] Pillow library is not installed yet [needed for .icns export].
    echo        You can install it later with: pip install Pillow
)

:: Check command-line arguments for silent/flag-based install
if /i "%~1"=="--all" (
    set "IS_SILENT=1"
    goto :install_all
)
if /i "%~1"=="--gemini" (
    set "IS_SILENT=1"
    goto :install_gemini
)
if /i "%~1"=="--claude" (
    set "IS_SILENT=1"
    goto :install_claude
)
if /i "%~1"=="--universal" (
    set "IS_SILENT=1"
    goto :install_universal
)
if /i "%~1"=="--custom" (
    set "IS_SILENT=1"
    set "CUSTOM_PATH=%~2"
    goto :install_custom_flag
)

echo.
echo -----------------------------------------------------------------------
echo  Select AI Agent environment for installation:
echo -----------------------------------------------------------------------
echo   [1] Universal [Install to ALL supported AI agents detected] (Recommended)
echo   [2] Google Antigravity ^& Gemini CLI (%USERPROFILE%\.gemini\config\skills)
echo   [3] Claude Code (%USERPROFILE%\.claude\skills)
echo   [4] Universal Agents Standard (%USERPROFILE%\.agents\skills)
echo   [5] Custom workspace / project folder
echo   [6] Cancel and Exit
echo.

set /p "CHOICE=Enter your choice [1-6, default 1]: "
if "%CHOICE%"=="" set "CHOICE=1"

if "%CHOICE%"=="1" goto :install_all
if "%CHOICE%"=="2" goto :install_gemini
if "%CHOICE%"=="3" goto :install_claude
if "%CHOICE%"=="4" goto :install_universal
if "%CHOICE%"=="5" goto :install_custom_prompt
if "%CHOICE%"=="6" goto :exit_clean

echo Invalid choice. Defaulting to Universal install...
goto :install_all

:install_all
echo.
echo [1/3] Installing to Google Antigravity / Gemini CLI...
call :copy_skill "%USERPROFILE%\.gemini\config\skills\macos-icon-designer"

echo.
echo [2/3] Installing to Claude Code...
call :copy_skill "%USERPROFILE%\.claude\skills\macos-icon-designer"

echo.
echo [3/3] Installing to Universal Agents Standard (.agents)...
call :copy_skill "%USERPROFILE%\.agents\skills\macos-icon-designer"

goto :success

:install_gemini
echo.
echo Installing to Google Antigravity / Gemini CLI...
call :copy_skill "%USERPROFILE%\.gemini\config\skills\macos-icon-designer"
goto :success

:install_claude
echo.
echo Installing to Claude Code...
call :copy_skill "%USERPROFILE%\.claude\skills\macos-icon-designer"
goto :success

:install_universal
echo.
echo Installing to Universal Agents Standard (.agents)...
call :copy_skill "%USERPROFILE%\.agents\skills\macos-icon-designer"
goto :success

:install_custom_prompt
echo.
set /p "CUSTOM_PATH=Enter destination directory path: "
:install_custom_flag
if "%CUSTOM_PATH%"=="" (
    echo [ERROR] No destination path provided.
    if "%IS_SILENT%"=="0" pause
    exit /b 1
)
call :copy_skill "%CUSTOM_PATH%\macos-icon-designer"
goto :success

:copy_skill
set "DEST_DIR=%~1"
echo   Destination: "%DEST_DIR%"
if not exist "%DEST_DIR%" mkdir "%DEST_DIR%" >nul 2>&1
robocopy "%SOURCE_SKILL%" "%DEST_DIR%" /E /NJH /NJS /NDL /NC /NS >nul
if %ERRORLEVEL% LEQ 7 (
    echo   [SUCCESS] Installed cleanly.
) else (
    echo   [ERROR] Failed to copy files. Error code: %ERRORLEVEL%
)
exit /b 0

:success
echo.
echo =======================================================================
echo   INSTALLATION COMPLETED SUCCESSFULLY!
echo =======================================================================
echo.
echo How to use in your AI Agent:
echo   Simply ask your AI agent (Gemini, Claude, Antigravity, Cursor, etc.):
echo   - "Design a macOS app icon for my new project [AppName]"
echo   - "Create a vector squircle icon in Apple HIG style for [Metaphor]"
echo   - "Generate a liquid glass macOS dock icon for [AppName]"
echo.
echo The agent will automatically activate the 'macos-icon-designer' skill,
echo conduct the 6-question discovery interview, and build your 100%% vector SVG!
echo =======================================================================
echo.
if "%IS_SILENT%"=="0" pause
exit /b 0

:exit_clean
echo Installation cancelled.
exit /b 0
