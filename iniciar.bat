@echo off
title Tienda Plantillas Excel - Servidor Local
echo.
echo  ============================================
echo   Servidor Local - Tienda Plantillas Peru
echo  ============================================
echo.
echo  Puerto: 3000
echo  URL: http://localhost:3000
echo.
echo  Para apagar, cierra esta ventana o ejecuta
echo  detener.bat
echo.
echo  Abriendo navegador...
echo.

start "" "http://localhost:3000"
python -m http.server 3000
