@echo off
echo.
echo  Deteniendo servidor...
echo.

taskkill /F /FI "WINDOWTITLE eq Tienda Plantillas Excel - Servidor Local" 2>nul

if %errorlevel%==0 (
    echo  Servidor detenido correctamente.
) else (
    echo  No se encontro el servidor ejecutandose.
)

echo.
pause
