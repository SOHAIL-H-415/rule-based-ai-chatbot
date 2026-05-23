@echo off
title Rule-Based AI Chatbot - Git Push Helper
color 0b

echo =====================================================================
echo          RULE-BASED AI CHATBOT - GITHUB PUSH ASSISTANT               
echo =====================================================================
echo.
echo This helper script will configure your remote origin and run 
echo the Git push command. This will trigger the secure Windows 
echo Credential Manager popup on your desktop for authentication.
echo.
echo ---------------------------------------------------------------------
echo STEP 1: Verify Remote URL
echo Setting remote origin to:
echo https://github.com/SOHAIL-H-415/rule-based-ai-chatbot.git
echo ---------------------------------------------------------------------
echo.

:: Remove existing origin if it exists to avoid conflicts
git remote remove origin >nul 2>&1

:: Add the correct remote origin
git remote add origin https://github.com/SOHAIL-H-415/rule-based-ai-chatbot.git

echo Remote origin configured successfully!
echo.
echo ---------------------------------------------------------------------
echo STEP 2: Authenticate and Push
echo ---------------------------------------------------------------------
echo When you press any key, the Git Push will start. 
echo A secure GitHub login window will pop up on your screen.
echo Click "Sign in with your browser" to securely authorize.
echo.
pause
echo.
echo Pushing main branch to remote...
git push -u origin main

if %errorlevel% equ 0 (
    color 0a
    echo.
    echo =====================================================================
    echo SUCCESS: Project pushed successfully to GitHub!
    echo URL: https://github.com/SOHAIL-H-415/rule-based-ai-chatbot
    echo =====================================================================
) else (
    color 0c
    echo.
    echo =====================================================================
    echo ERROR: Push failed. Make sure:
    echo 1. You created the repository on GitHub named "rule-based-ai-chatbot"
    echo 2. You authenticated successfully in the popup window.
    echo =====================================================================
)
echo.
echo Press any key to close this helper...
pause >nul
