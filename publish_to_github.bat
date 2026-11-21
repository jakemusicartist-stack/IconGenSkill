@echo off
setlocal EnableDelayedExpansion

title Publish macOS Icon Designer Skill to GitHub

echo =======================================================================
echo        PUBLISH macOS ICON DESIGNER SKILL TO GITHUB
echo =======================================================================
echo.

where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Git is not installed or not found in PATH!
    echo Please install Git from https://git-scm.com/
    pause
    exit /b 1
)

echo [1/4] Checking Git repository status...
if not exist ".git" (
    echo       Initializing new Git repository (branch: main)...
    git init -b main >nul 2>&1
    if %ERRORLEVEL% NEQ 0 git init >nul 2>&1
) else (
    echo       Existing Git repository detected.
)

echo.
echo [2/4] Staging files and creating commit...
git add .
git status --porcelain | findstr "^[MADRCU]" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    git commit -m "feat: initial release of macos-icon-designer multi-agent skill"
    echo       [OK] Committed changes.
) else (
    echo       No new changes to commit.
)

echo.
echo [3/4] GitHub Remote Configuration:
git remote get-url origin >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    for /f "tokens=*" %%u in ('git remote get-url origin') do set "EXISTING_REMOTE=%%u"
    echo       Current remote origin: !EXISTING_REMOTE!
    set /p "CHANGE_REMOTE=Do you want to use this remote? [Y/N, default Y]: "
    if /i "!CHANGE_REMOTE!"=="N" (
        set /p "REPO_URL=Enter your new GitHub repository URL: "
        if not "!REPO_URL!"=="" (
            git remote set-url origin !REPO_URL!
        )
    )
) else (
    echo       No GitHub remote URL is configured yet.
    echo       Create a new repository on GitHub (e.g. https://github.com/new)
    echo.
    set /p "REPO_URL=Enter your GitHub repository URL [default: https://github.com/jakemusicartist-stack/IconGenSkill.git]: "
    if "!REPO_URL!"=="" set "REPO_URL=https://github.com/jakemusicartist-stack/IconGenSkill.git"
    git remote add origin !REPO_URL!
)

echo.
echo [4/4] Pushing to GitHub (main branch)...
git branch -M main >nul 2>&1
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo =======================================================================
    echo   [SUCCESS] Your skill has been published to GitHub!
    echo =======================================================================
    echo Anyone can now clone and install your skill with:
    echo   git clone ^<your-repo-url^>
    echo   cd macos-icon-designer
    echo   install.bat
    echo =======================================================================
) else (
    echo.
    echo [NOTE] Git push encountered an error or needs authentication.
    echo If this is a private repo or SSH/PAT is required, verify:
    echo   1. gh auth login (GitHub CLI) OR
    echo   2. Your Personal Access Token (PAT)
    echo Then run: git push -u origin main
)

echo.
pause
exit /b 0
