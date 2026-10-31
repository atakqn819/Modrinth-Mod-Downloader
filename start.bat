@echo off
chcp 65001 >nul
title Modrinth Mod Manager v1.1.1
cls
echo =======================================================
echo    Modrinth Mod Manager v1.1.1 (Official Release)
echo    Fabric MC 26.3 · Mods · Textures · Shaders · Packs
echo =======================================================
echo.
echo [1/2] Checking Python environment...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo Please install Python 3.10+ from https://www.python.org/
    echo Or run ModrinthModManager.exe directly!
    echo.
    pause
    exit /b 1
)

echo [2/2] Launching Modrinth Mod Manager...
echo.
python "%~dp0modrinth_downloader.py"
if errorlevel 1 (
    echo.
    echo [ERROR] Application terminated with an error!
    echo.
    pause
)
