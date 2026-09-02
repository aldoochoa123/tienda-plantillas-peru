"""
Genera PDF: Planos de Muebles de Melamina para Perú
Versión 2 - Sin precios individuales, cantos calculados, solo herramientas de armado
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    Image, KeepTogether
)
from reportlab.pdfgen import canvas
import os

# ══════════════════════════════════════════════════════════════
# COLORES
# ══════════════════════════════════════════════════════════════

PURPLE = HexColor("#3D0C8E")
PURPLE_LIGHT = HexColor("#6C5CE7")
GREEN = HexColor("#00B894")
BLUE = HexColor("#0984E3")
ORANGE = HexColor("#E17055")
RED = HexColor("#D63031")
TEAL = HexColor("#00CEC9")
GRAY = HexColor("#636E72")
LIGHT_GRAY = HexColor("#F5F6FA")
DARK = HexColor("#2D3436")
WHITE = white

styles = getSampleStyleSheet()

title_style = ParagraphStyle('Title', parent=styles['Heading1'],
    fontSize=28, textColor=PURPLE, fontName='Helvetica-Bold',
    alignment=TA_CENTER, spaceAfter=6*mm)

subtitle_style = ParagraphStyle('Subtitle', parent=styles['Heading2'],
    fontSize=18, textColor=PURPLE_LIGHT, fontName='Helvetica-Bold',
    alignment=TA_LEFT, spaceAfter=4*mm, spaceBefore=8*mm)

section_style = ParagraphStyle('Section', parent=styles['Heading3'],
    fontSize=14, textColor=BLUE, fontName='Helvetica-Bold',
    alignment=TA_LEFT, spaceAfter=3*mm, spaceBefore=6*mm)

body_style = ParagraphStyle('Body', parent=styles['BodyText'],
    fontSize=11, textColor=DARK, fontName='Helvetica',
    alignment=TA_JUSTIFY, spaceAfter=3*mm, leading=16)

tip_style = ParagraphStyle('Tip', parent=styles['BodyText'],
    fontSize=10, textColor=GREEN, fontName='Helvetica-Oblique',
    alignment=TA_LEFT, spaceAfter=2*mm, leftIndent=10*mm, leading=14)

# ══════════════════════════════════════════════════════════════
# FUNCIONES
# ══════════════════════════════════════════════════════════════

def draw_header_footer(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setStrokeColor(PURPLE)
    canvas_obj.setLineWidth(3)
    canvas_obj.line(15*mm, A4[1] - 12*mm, A4[0] - 15*mm, A4[1] - 12*mm)
    
    logo_path = "logo.jpg"
    if os.path.exists(logo_path):
        canvas_obj.drawImage(logo_path, 15*mm, A4[1] - 18*mm, 
                           width=15*mm, height=15*mm, preserveAspectRatio=True, mask="auto")
    
    canvas_obj.setFont("Helvetica-Bold", 8)
    canvas_obj.setFillColor(PURPLE)
    canvas_obj.drawString(35*mm, A4[1] - 15*mm, "PLANOS DE MUEBLES DE MELAMINA - PERÚ")
    
    canvas_obj.setFont("Helvetica", 8)
    canvas_obj.setFillColor(GRAY)
    canvas_obj.drawString(15*mm, 10*mm, "© 2026 Plantillas Excel Perú")
    canvas_obj.drawRightString(A4[0] - 15*mm, 10*mm, f"Página {doc.page}")
    
    canvas_obj.setStrokeColor(PURPLE_LIGHT)
    canvas_obj.setLineWidth(1)
    canvas_obj.line(15*mm, 15*mm, A4[0] - 15*mm, 15*mm)
    canvas_obj.restoreState()

def create_colored_box(text, color, width=170*mm):
    data = [[Paragraph(text, ParagraphStyle('BoxText', 
            parent=body_style, textColor=WHITE, fontName='Helvetica-Bold',
            alignment=TA_CENTER, fontSize=12))]]
    tbl = Table(data, colWidths=[width])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), color),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('LEFTPADDING', (0, 0), (-1, -1), 15),
        ('RIGHTPADDING', (0, 0), (-1, -1), 15),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ]))
    return tbl

def create_tip_box(text, icon="💡"):
    tip_text = f"<b>{icon} TIP:</b> {text}"
    data = [[Paragraph(tip_text, ParagraphStyle('TipBox', 
            parent=body_style, textColor=GREEN, fontSize=10, fontName='Helvetica-Oblique'))]]
    tbl = Table(data, colWidths=[170*mm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor("#F0FFF0")),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 15),
        ('RIGHTPADDING', (0, 0), (-1, -1), 15),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
        ('BOX', (0, 0), (-1, -1), 1, GREEN),
    ]))
    return tbl

def create_table(headers, data, color, col_widths=None):
    table_data = [headers] + data
    if not col_widths:
        col_widths = [170*mm / len(headers)] * len(headers)
    
    tbl = Table(table_data, colWidths=col_widths)
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), color),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_GRAY]),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#D0D5DD")),
    ]))
    return tbl

# ══════════════════════════════════════════════════════════════
# DATOS DE PROYECTOS (con cantos calculados correctamente)
# ══════════════════════════════════════════════════════════════

PROJECTS = [
    {
        "num": 1,
        "title": "ESTANTERÍA BÁSICA",
        "description": "Estantería de 5 niveles para living o estudio. Ideal para libros, decoración y almacenamiento.",
        "dimensions": {
            "Ancho total": "80 cm",
            "Alto total": "180 cm",
            "Profundidad": "30 cm",
            "Espacio entre estantes": "32 cm",
            "Grosor de tablero": "18 mm",
        },
        "cuts": [
            ["Pieza", "Cantidad", "Largo (cm)", "Ancho (cm)", "Cantos (lados)"],
            ["Laterales", "2", "180", "30", "1 largo (frente)"],
            ["Base", "1", "76.4", "30", "1 largo (frente)"],
            ["Tapa", "1", "76.4", "30", "1 largo (frente)"],
            ["Estantes internos", "4", "76.4", "30", "1 largo (frente)"],
        ],
        "cantos": [
            ["Ubicación", "Cantidad", "Largo (cm)"],
            ["Laterales (frente)", "2", "180 cm"],
            ["Base y tapa (frente)", "2", "76.4 cm"],
            ["Estantes (frente)", "4", "76.4 cm"],
            ["TOTAL CANTOS", "", "785.6 cm (7.86 m)"],
        ],
        "assembly_steps": [
            ["1", "Marcar ubicación de estantes en laterales (cada 32 cm)", "Regla + lápiz"],
            ["2", "Perforar agujeros guía en laterales", "Taladro + broca 5mm"],
            ["3", "Colocar tarugos en agujeros", "Martillo"],
            ["4", "Ensamclar base entre laterales", "Taladro + tornillos"],
            ["5", "Colocar estantes sobre tarugos", "A mano"],
            ["6", "Fijar estantes con tornillos", "Taladro + tornillos"],
            ["7", "Colocar tapa", "Taladro + tornillos"],
            ["8", "Verificar nivel y estabilidad", "Nivel"],
        ],
        "assembly_tools": [
            "Taladro atornillador",
            "Broca 5mm para melamina",
            "Tornillos para melamina (4x30mm)",
            "Tarugos de madera 6mm",
            "Martillo",
            "Regla 2m",
            "Lápiz",
            "Nivel",
            "Escuadra",
        ],
        "tips": [
            "Usa guía de corte para cortes rectos y precisos",
            "Aplica cantos con plancha doméstica a temperatura media",
            "Perfora agujeros previos para evitar que la melamina se raje",
            "Deja 2mm de espacio entre estantes para ajustes",
        ],
    },
    {
        "num": 2,
        "title": "COCINA MODULAR",
        "description": "Cocina modular de 3 módulos: inferior, superior y alacena. Diseño moderno y funcional.",
        "dimensions": {
            "Módulo inferior (ancho x alto x prof)": "120 x 85 x 60 cm",
            "Módulo superior (ancho x alto x prof)": "120 x 70 x 35 cm",
            "Alacena (ancho x alto x prof)": "60 x 200 x 35 cm",
            "Espacio entre módulos": "50 cm",
        },
        "cuts": [
            ["Pieza", "Cantidad", "Largo (cm)", "Ancho (cm)", "Cantos (lados)"],
            ["Laterales mód. inferior", "2", "85", "60", "1 largo (frente)"],
            ["Base mód. inferior", "1", "116.4", "60", "1 largo (frente)"],
            ["Tapa mód. inferior", "1", "116.4", "60", "1 largo (frente)"],
            ["Estante interno mód. inf.", "1", "116.4", "60", "1 largo (frente)"],
            ["Frentes cajón", "2", "56", "20", "4 lados"],
            ["Fondo cajón", "2", "54", "54", "0"],
            ["Laterales mód. superior", "2", "70", "35", "1 largo (frente)"],
            ["Base mód. superior", "1", "116.4", "35", "1 largo (frente)"],
            ["Tapa mód. superior", "1", "116.4", "35", "1 largo (frente)"],
            ["Estante mód. superior", "2", "116.4", "35", "1 largo (frente)"],
            ["Puertas mód. inferior", "2", "81.4", "57", "4 lados"],
            ["Puertas mód. superior", "2", "66.4", "57", "4 lados"],
            ["Laterales alacena", "2", "200", "35", "1 largo (frente)"],
            ["Base alacena", "1", "56.4", "35", "1 largo (frente)"],
            ["Tapa alacena", "1", "56.4", "35", "1 largo (frente)"],
            ["Estantes alacena", "5", "56.4", "35", "1 largo (frente)"],
            ["Puertas alacena", "2", "196.4", "27", "4 lados"],
        ],
        "cantos": [
            ["Ubicación", "Cantidad", "Largo (cm)"],
            ["Laterales mód. inferior (frente)", "2", "85 cm"],
            ["Base/tapa mód. inferior (frente)", "2", "116.4 cm"],
            ["Estante mód. inferior (frente)", "1", "116.4 cm"],
            ["Frentes cajón (4 lados)", "2", "152 cm c/u = 304 cm"],
            ["Laterales mód. superior (frente)", "2", "70 cm"],
            ["Base/tapa mód. superior (frente)", "2", "116.4 cm"],
            ["Estantes mód. superior (frente)", "2", "116.4 cm"],
            ["Puertas mód. inferior (4 lados)", "2", "276.8 cm c/u = 553.6 cm"],
            ["Puertas mód. superior (4 lados)", "2", "266.8 cm c/u = 533.6 cm"],
            ["Laterales alacena (frente)", "2", "200 cm"],
            ["Base/tapa alacena (frente)", "2", "56.4 cm"],
            ["Estantes alacena (frente)", "5", "56.4 cm"],
            ["Puertas alacena (4 lados)", "2", "446.8 cm c/u = 893.6 cm"],
            ["TOTAL CANTOS", "", "3,827.2 cm (38.27 m)"],
        ],
        "assembly_steps": [
            ["1", "Armar módulo inferior: laterales + base + tapa", "Taladro + tornillos"],
            ["2", "Instalar división interna y estante", "Taladro + tornillos"],
            ["3", "Armar cajones: frente + laterales + fondo", "Taladro + tornillos"],
            ["4", "Instalar guías de cajones en módulo", "Taladro + tornillos"],
            ["5", "Armar módulo superior: laterales + base + tapa", "Taladro + tornillos"],
            ["6", "Instalar estantes en módulo superior", "Taladro + tornillos"],
            ["7", "Armar alacena: laterales + base + tapa", "Taladro + tornillos"],
            ["8", "Instalar estantes en alacena", "Taladro + tornillos"],
            ["9", "Montar módulos en pared (inferior primero)", "Taladro + tacos"],
            ["10", "Instalar bisagras en puertas", "Taladro + tornillos"],
            ["11", "Colocar puertas y ajustar", "Taladro + destornillador"],
            ["12", "Instalar tiradores", "Taladro + tornillos"],
            ["13", "Verificar alineación y nivel", "Nivel"],
        ],
        "assembly_tools": [
            "Taladro atornillador",
            "Broca 5mm para melamina",
            "Tornillos para melamina (4x30mm y 4x50mm)",
            "Tarugos de madera 6mm",
            "Martillo",
            "Regla 2m",
            "Lápiz",
            "Nivel",
            "Escuadra",
            "Destornillador Phillips",
        ],
        "tips": [
            "Deja 50cm entre módulo inferior y superior para electrodomésticos",
            "Usa nivel láser para alinear módulos superiores",
            "Instala los módulos inferiores primero, luego los superiores",
            "Considera el paso de tuberías si hay fregadero",
        ],
    },
    {
        "num": 3,
        "title": "CLOSET EMPOTRADO",
        "description": "Closet empotrado de 2 puertas con estantes, cajones y barra para colgar ropa.",
        "dimensions": {
            "Ancho total": "150 cm",
            "Alto total": "220 cm",
            "Profundidad": "60 cm",
            "Zona de colgar (alto)": "100 cm",
            "Zona de estantes (alto)": "120 cm",
        },
        "cuts": [
            ["Pieza", "Cantidad", "Largo (cm)", "Ancho (cm)", "Cantos (lados)"],
            ["Laterales", "2", "220", "60", "1 largo (frente)"],
            ["Base", "1", "146.4", "60", "1 largo (frente)"],
            ["Tapa", "1", "146.4", "60", "1 largo (frente)"],
            ["División central", "1", "220", "60", "1 largo (frente)"],
            ["Estantes zona derecha", "5", "71.4", "60", "1 largo (frente)"],
            ["Frentes cajón", "2", "71.4", "25", "4 lados"],
            ["Fondo cajón", "2", "69.4", "54", "0"],
            ["Puertas", "2", "216.4", "72", "4 lados"],
        ],
        "cantos": [
            ["Ubicación", "Cantidad", "Largo (cm)"],
            ["Laterales (frente)", "2", "220 cm"],
            ["Base y tapa (frente)", "2", "146.4 cm"],
            ["División central (frente)", "1", "220 cm"],
            ["Estantes (frente)", "5", "71.4 cm"],
            ["Frentes cajón (4 lados)", "2", "192.8 cm c/u = 385.6 cm"],
            ["Puertas (4 lados)", "2", "576.8 cm c/u = 1,153.6 cm"],
            ["TOTAL CANTOS", "", "2,756.6 cm (27.57 m)"],
        ],
        "assembly_steps": [
            ["1", "Armar estructura principal: laterales + base + tapa", "Taladro + tornillos"],
            ["2", "Instalar división central", "Taladro + tornillos"],
            ["3", "Marcar ubicación de estantes en zona derecha", "Regla + lápiz"],
            ["4", "Instalar estantes en zona derecha", "Taladro + tornillos"],
            ["5", "Instalar barra para ropa en zona izquierda", "Taladro + soportes"],
            ["6", "Armar cajones: frente + laterales + fondo", "Taladro + tornillos"],
            ["7", "Instalar guías de cajones", "Taladro + tornillos"],
            ["8", "Instalar bisagras en puertas", "Taladro + tornillos"],
            ["9", "Colocar puertas y ajustar", "Taladro + destornillador"],
            ["10", "Instalar tiradores", "Taladro + tornillos"],
            ["11", "Verificar nivel y alineación", "Nivel"],
        ],
        "assembly_tools": [
            "Taladro atornillador",
            "Broca 5mm para melamina",
            "Tornillos para melamina (4x30mm y 4x50mm)",
            "Tarugos de madera 6mm",
            "Martillo",
            "Regla 2m",
            "Lápiz",
            "Nivel",
            "Escuadra",
            "Destornillador Phillips",
        ],
        "tips": [
            "Mide el espacio empotrado en 3 puntos (arriba, medio, abajo) por si hay desnivel",
            "Deja 5mm de holgura en cada lado para facilitar el montaje",
            "Instala la barra de ropa a 170cm del suelo para ropa larga",
            "Usa cajones con guías telescópicas para mayor durabilidad",
        ],
    },
    {
        "num": 4,
        "title": "ESCRITORIO DE OFICINA",
        "description": "Escritorio amplio con cajones, repisa para CPU y espacio para monitor.",
        "dimensions": {
            "Ancho total": "120 cm",
            "Alto total": "75 cm",
            "Profundidad": "60 cm",
            "Cajones": "3 unidades",
            "Repisa CPU": "25 x 50 cm",
        },
        "cuts": [
            ["Pieza", "Cantidad", "Largo (cm)", "Ancho (cm)", "Cantos (lados)"],
            ["Superficie principal", "1", "120", "60", "3 lados (frente + laterales)"],
            ["Laterales", "2", "75", "60", "1 largo (frente)"],
            ["Estante intermedio", "1", "116.4", "60", "1 largo (frente)"],
            ["Fondo", "1", "116.4", "71.4", "0"],
            ["Frentes cajón", "3", "56", "20", "4 lados"],
            ["Fondo cajón", "3", "54", "54", "0"],
            ["Repisa CPU (laterales)", "2", "50", "25", "1 largo (frente)"],
            ["Repisa CPU (base/tapa)", "2", "21.4", "25", "1 largo (frente)"],
        ],
        "cantos": [
            ["Ubicación", "Cantidad", "Largo (cm)"],
            ["Superficie (3 lados)", "1", "240 cm (120+60+60)"],
            ["Laterales (frente)", "2", "75 cm"],
            ["Estante intermedio (frente)", "1", "116.4 cm"],
            ["Frentes cajón (4 lados)", "3", "152 cm c/u = 456 cm"],
            ["Repisa CPU laterales (frente)", "2", "50 cm"],
            ["Repisa CPU base/tapa (frente)", "2", "21.4 cm"],
            ["TOTAL CANTOS", "", "1,174.8 cm (11.75 m)"],
        ],
        "assembly_steps": [
            ["1", "Armar estructura lateral izquierda (cajones)", "Taladro + tornillos"],
            ["2", "Armar estructura lateral derecha (repisa CPU)", "Taladro + tornillos"],
            ["3", "Unir estructuras con superficie principal", "Taladro + tornillos"],
            ["4", "Instalar guías de cajones", "Taladro + tornillos"],
            ["5", "Armar cajones: frente + laterales + fondo", "Taladro + tornillos"],
            ["6", "Colocar cajones en guías", "A mano"],
            ["7", "Instalar tiradores", "Taladro + tornillos"],
            ["8", "Verificar nivel y estabilidad", "Nivel"],
        ],
        "assembly_tools": [
            "Taladro atornillador",
            "Broca 5mm para melamina",
            "Tornillos para melamina (4x30mm)",
            "Tarugos de madera 6mm",
            "Martillo",
            "Regla 2m",
            "Lápiz",
            "Nivel",
            "Escuadra",
            "Destornillador Phillips",
        ],
        "tips": [
            "La altura ideal del escritorio es 75cm para personas de estatura promedio",
            "Deja espacio para cables en la parte trasera",
            "Considera agregar un agujero para paso de cables en la superficie",
            "Usa patas metálicas regulables si el piso no está nivelado",
        ],
    },
    {
        "num": 5,
        "title": "MUEBLE DE TV",
        "description": "Mueble moderno para TV de 55 pulgadas con estantes abiertos y cajones.",
        "dimensions": {
            "Ancho total": "150 cm",
            "Alto total": "50 cm",
            "Profundidad": "40 cm",
            "Estantes abiertos": "3 espacios",
            "Cajones": "2 unidades",
        },
        "cuts": [
            ["Pieza", "Cantidad", "Largo (cm)", "Ancho (cm)", "Cantos (lados)"],
            ["Laterales", "2", "50", "40", "1 largo (frente)"],
            ["Base", "1", "146.4", "40", "1 largo (frente)"],
            ["Tapa", "1", "146.4", "40", "3 lados (frente + laterales)"],
            ["Divisiones verticales", "2", "50", "40", "1 largo (frente)"],
            ["Estante interno", "1", "46.4", "40", "1 largo (frente)"],
            ["Frentes cajón", "2", "46.4", "18", "4 lados"],
            ["Fondo cajón", "2", "44.4", "34", "0"],
        ],
        "cantos": [
            ["Ubicación", "Cantidad", "Largo (cm)"],
            ["Laterales (frente)", "2", "50 cm"],
            ["Base (frente)", "1", "146.4 cm"],
            ["Tapa (3 lados)", "1", "226.4 cm (146.4+40+40)"],
            ["Divisiones verticales (frente)", "2", "50 cm"],
            ["Estante interno (frente)", "1", "46.4 cm"],
            ["Frentes cajón (4 lados)", "2", "128.8 cm c/u = 257.6 cm"],
            ["TOTAL CANTOS", "", "926.8 cm (9.27 m)"],
        ],
        "assembly_steps": [
            ["1", "Armar estructura principal: laterales + base + tapa", "Taladro + tornillos"],
            ["2", "Instalar divisiones verticales", "Taladro + tornillos"],
            ["3", "Instalar estante interno", "Taladro + tornillos"],
            ["4", "Armar cajones: frente + laterales + fondo", "Taladro + tornillos"],
            ["5", "Instalar guías de cajones", "Taladro + tornillos"],
            ["6", "Colocar cajones", "A mano"],
            ["7", "Instalar tiradores", "Taladro + tornillos"],
            ["8", "Verificar nivel", "Nivel"],
        ],
        "assembly_tools": [
            "Taladro atornillador",
            "Broca 5mm para melamina",
            "Tornillos para melamina (4x30mm)",
            "Tarugos de madera 6mm",
            "Martillo",
            "Regla 2m",
            "Lápiz",
            "Nivel",
            "Escuadra",
            "Destornillador Phillips",
        ],
        "tips": [
            "Deja espacio para consola, decodificador y otros dispositivos",
            "Instala un agujero para paso de cables en la parte trasera",
            "El ancho del mueble debe ser 20-30cm mayor que el TV",
            "Considera agregar iluminación LED en los estantes abiertos",
        ],
    },
    {
        "num": 6,
        "title": "LIBRERO DE PARED",
        "description": "Librero modular de pared con diseño asimétrico. Ideal para living o estudio.",
        "dimensions": {
            "Ancho total": "180 cm",
            "Alto total": "120 cm",
            "Profundidad": "25 cm",
            "Módulos": "5 unidades",
        },
        "cuts": [
            ["Pieza", "Cantidad", "Largo (cm)", "Ancho (cm)", "Cantos (lados)"],
            ["Laterales módulo A (60x40)", "2", "40", "25", "1 largo (frente)"],
            ["Base/tapa módulo A", "2", "56.4", "25", "1 largo (frente)"],
            ["Laterales módulo B (40x30)", "2", "30", "25", "1 largo (frente)"],
            ["Base/tapa módulo B", "2", "36.4", "25", "1 largo (frente)"],
            ["Laterales módulo C (80x40)", "2", "40", "25", "1 largo (frente)"],
            ["Base/tapa módulo C", "2", "76.4", "25", "1 largo (frente)"],
            ["Estante interno mód. C", "1", "76.4", "25", "1 largo (frente)"],
        ],
        "cantos": [
            ["Ubicación", "Cantidad", "Largo (cm)"],
            ["Laterales mód. A (frente)", "2", "40 cm"],
            ["Base/tapa mód. A (frente)", "2", "56.4 cm"],
            ["Laterales mód. B (frente)", "2", "30 cm"],
            ["Base/tapa mód. B (frente)", "2", "36.4 cm"],
            ["Laterales mód. C (frente)", "2", "40 cm"],
            ["Base/tapa mód. C (frente)", "2", "76.4 cm"],
            ["Estante mód. C (frente)", "1", "76.4 cm"],
            ["TOTAL CANTOS", "", "638.4 cm (6.38 m)"],
        ],
        "assembly_steps": [
            ["1", "Armar módulo A: laterales + base + tapa", "Taladro + tornillos"],
            ["2", "Armar módulo B: laterales + base + tapa", "Taladro + tornillos"],
            ["3", "Armar módulo C: laterales + base + tapa + estante", "Taladro + tornillos"],
            ["4", "Marcar ubicación en pared", "Nivel + lápiz"],
            ["5", "Perforar pared y colocar tacos", "Taladro percutor"],
            ["6", "Montar módulos en pared", "Taladro + tornillos"],
            ["7", "Verificar alineación", "Nivel"],
        ],
        "assembly_tools": [
            "Taladro atornillador",
            "Taladro percutor (para pared)",
            "Broca 5mm para melamina",
            "Broca 8mm para pared",
            "Tornillos para melamina (4x30mm)",
            "Tornillos para pared (6x60mm)",
            "Tarugos de pared 8mm",
            "Martillo",
            "Regla 2m",
            "Lápiz",
            "Nivel",
            "Escuadra",
        ],
        "tips": [
            "Usa nivel láser para alinear los módulos perfectamente",
            "Distribuye los módulos de forma asimétrica para un look moderno",
            "Asegura los módulos a la pared con tacos apropiados para el tipo de pared",
            "Deja 5-10cm entre módulos para un efecto visual atractivo",
        ],
    },
    {
        "num": 7,
        "title": "CAMA CON ALMACENAJE",
        "description": "Base de cama matrimonial con cajones inferiores para maximizar el espacio.",
        "dimensions": {
            "Ancho total": "140 cm",
            "Largo total": "190 cm",
            "Alto total": "40 cm",
            "Cajones": "2 unidades grandes",
        },
        "cuts": [
            ["Pieza", "Cantidad", "Largo (cm)", "Ancho (cm)", "Cantos (lados)"],
            ["Laterales largos", "2", "190", "40", "1 largo (frente)"],
            ["Laterales cortos", "2", "136.4", "40", "1 largo (frente)"],
            ["Base", "1", "186.4", "136.4", "0"],
            ["Refuerzo central", "1", "186.4", "20", "0"],
            ["Frentes cajón", "2", "90", "35", "4 lados"],
            ["Laterales cajón", "4", "54", "35", "0"],
            ["Fondo cajón", "2", "86.4", "54", "0"],
        ],
        "cantos": [
            ["Ubicación", "Cantidad", "Largo (cm)"],
            ["Laterales largos (frente)", "2", "190 cm"],
            ["Laterales cortos (frente)", "2", "136.4 cm"],
            ["Frentes cajón (4 lados)", "2", "250 cm c/u = 500 cm"],
            ["TOTAL CANTOS", "", "1,152.8 cm (11.53 m)"],
        ],
        "assembly_steps": [
            ["1", "Armar estructura rectangular: 2 largos + 2 cortos", "Taladro + tornillos"],
            ["2", "Instalar base", "Taladro + tornillos"],
            ["3", "Instalar refuerzo central", "Taladro + tornillos"],
            ["4", "Armar cajones: frente + laterales + fondo", "Taladro + tornillos"],
            ["5", "Instalar guías de cajones pesados", "Taladro + tornillos"],
            ["6", "Colocar cajones", "A mano"],
            ["7", "Instalar tiradores", "Taladro + tornillos"],
            ["8", "Verificar nivel y estabilidad", "Nivel"],
        ],
        "assembly_tools": [
            "Taladro atornillador",
            "Broca 5mm para melamina",
            "Tornillos para melamina (4x30mm y 4x50mm)",
            "Tarugos de madera 6mm",
            "Martillo",
            "Regla 2m",
            "Lápiz",
            "Nivel",
            "Escuadra",
            "Destornillador Phillips",
        ],
        "tips": [
            "Usa guías de cajones pesados (45kg mínimo) para soportar el peso",
            "Refuerza la estructura interna con tableros adicionales",
            "Deja 5cm de espacio libre debajo para limpieza",
            "Considera agregar un cabecero de melamina para completar el look",
        ],
    },
    {
        "num": 8,
        "title": "MUEBLE DE BAÑO",
        "description": "Mueble bajo lavabo con estantes y puerta. Resistente a la humedad.",
        "dimensions": {
            "Ancho total": "80 cm",
            "Alto total": "80 cm",
            "Profundidad": "45 cm",
            "Estantes": "2 interiores",
        },
        "cuts": [
            ["Pieza", "Cantidad", "Largo (cm)", "Ancho (cm)", "Cantos (lados)"],
            ["Laterales", "2", "80", "45", "1 largo (frente)"],
            ["Base", "1", "76.4", "45", "1 largo (frente)"],
            ["Tapa", "1", "76.4", "45", "1 largo (frente)"],
            ["Estantes internos", "2", "76.4", "45", "1 largo (frente)"],
            ["Puerta", "1", "76.4", "37", "4 lados"],
        ],
        "cantos": [
            ["Ubicación", "Cantidad", "Largo (cm)"],
            ["Laterales (frente)", "2", "80 cm"],
            ["Base y tapa (frente)", "2", "76.4 cm"],
            ["Estantes (frente)", "2", "76.4 cm"],
            ["Puerta (4 lados)", "1", "226.8 cm"],
            ["TOTAL CANTOS", "", "616.4 cm (6.16 m)"],
        ],
        "assembly_steps": [
            ["1", "Armar estructura principal: laterales + base + tapa", "Taladro + tornillos"],
            ["2", "Hacer corte para tubería en estante inferior", "Sierra caladora"],
            ["3", "Instalar estantes internos", "Taladro + tornillos"],
            ["4", "Instalar bisagras en puerta", "Taladro + tornillos"],
            ["5", "Colocar puerta y ajustar", "Taladro + destornillador"],
            ["6", "Instalar tirador", "Taladro + tornillos"],
            ["7", "Verificar nivel", "Nivel"],
        ],
        "assembly_tools": [
            "Taladro atornillador",
            "Broca 5mm para melamina",
            "Tornillos para melamina (4x30mm)",
            "Tarugos de madera 6mm",
            "Martillo",
            "Regla 2m",
            "Lápiz",
            "Nivel",
            "Escuadra",
            "Destornillador Phillips",
            "Sierra caladora (para corte de tubería)",
        ],
        "tips": [
            "USA MELAMINA HIDRÓFUGA para resistir la humedad del baño",
            "Sella todos los cantos y juntas con silicona sanitaria",
            "Deja espacio para la tubería del lavabo",
            "Considera agregar un espejo en la puerta para funcionalidad",
        ],
    },
    {
        "num": 9,
        "title": "ZAPATERO MODULAR",
        "description": "Zapatero de pared con estantes inclinados para organizar zapatos.",
        "dimensions": {
            "Ancho total": "100 cm",
            "Alto total": "150 cm",
            "Profundidad": "30 cm",
            "Estantes": "5 niveles",
        },
        "cuts": [
            ["Pieza", "Cantidad", "Largo (cm)", "Ancho (cm)", "Cantos (lados)"],
            ["Laterales", "2", "150", "30", "1 largo (frente)"],
            ["Base", "1", "96.4", "30", "1 largo (frente)"],
            ["Tapa", "1", "96.4", "30", "1 largo (frente)"],
            ["Estantes inclinados", "5", "96.4", "30", "1 largo (frente)"],
        ],
        "cantos": [
            ["Ubicación", "Cantidad", "Largo (cm)"],
            ["Laterales (frente)", "2", "150 cm"],
            ["Base y tapa (frente)", "2", "96.4 cm"],
            ["Estantes (frente)", "5", "96.4 cm"],
            ["TOTAL CANTOS", "", "878.8 cm (8.79 m)"],
        ],
        "assembly_steps": [
            ["1", "Armar estructura principal: laterales + base + tapa", "Taladro + tornillos"],
            ["2", "Marcar ángulo de 15° para estantes inclinados", "Regla + lápiz"],
            ["3", "Instalar estantes inclinados", "Taladro + tornillos"],
            ["4", "Marcar ubicación en pared", "Nivel + lápiz"],
            ["5", "Perforar pared y colocar tacos", "Taladro percutor"],
            ["6", "Montar zapatero en pared", "Taladro + tornillos"],
            ["7", "Verificar nivel", "Nivel"],
        ],
        "assembly_tools": [
            "Taladro atornillador",
            "Taladro percutor (para pared)",
            "Broca 5mm para melamina",
            "Broca 8mm para pared",
            "Tornillos para melamina (4x30mm)",
            "Tornillos para pared (6x60mm)",
            "Tarugos de pared 8mm",
            "Martillo",
            "Regla 2m",
            "Lápiz",
            "Nivel",
            "Escuadra",
            "Transportador de ángulos",
        ],
        "tips": [
            "Inclina los estantes 15° para que los zapatos se vean mejor",
            "Deja 15cm entre estantes para zapatos de tacón",
            "Deja 20cm para botas en el estante inferior",
            "Considera agregar un espejo en la puerta",
        ],
    },
    {
        "num": 10,
        "title": "ISLA DE COCINA",
        "description": "Isla central para cocina con almacenaje y superficie de trabajo.",
        "dimensions": {
            "Ancho total": "120 cm",
            "Largo total": "80 cm",
            "Alto total": "90 cm",
            "Estantes": "3 niveles",
            "Cajones": "2 unidades",
        },
        "cuts": [
            ["Pieza", "Cantidad", "Largo (cm)", "Ancho (cm)", "Cantos (lados)"],
            ["Laterales largos", "2", "90", "80", "1 largo (frente)"],
            ["Laterales cortos", "2", "90", "76.4", "1 largo (frente)"],
            ["Base", "1", "116.4", "76.4", "0"],
            ["Tapa", "1", "120", "80", "4 lados (todos)"],
            ["Estantes internos", "2", "116.4", "76.4", "1 largo (frente)"],
            ["Frentes cajón", "2", "56", "20", "4 lados"],
            ["Fondo cajón", "2", "54", "54", "0"],
            ["Puertas", "2", "86.4", "57", "4 lados"],
        ],
        "cantos": [
            ["Ubicación", "Cantidad", "Largo (cm)"],
            ["Laterales largos (frente)", "2", "90 cm"],
            ["Laterales cortos (frente)", "2", "76.4 cm"],
            ["Tapa (4 lados)", "1", "400 cm (120+80+120+80)"],
            ["Estantes (frente)", "2", "116.4 cm"],
            ["Frentes cajón (4 lados)", "2", "152 cm c/u = 304 cm"],
            ["Puertas (4 lados)", "2", "286.8 cm c/u = 573.6 cm"],
            ["TOTAL CANTOS", "", "1,883.2 cm (18.83 m)"],
        ],
        "assembly_steps": [
            ["1", "Armar estructura principal: laterales + base", "Taladro + tornillos"],
            ["2", "Instalar estantes internos", "Taladro + tornillos"],
            ["3", "Armar cajones: frente + laterales + fondo", "Taladro + tornillos"],
            ["4", "Instalar guías de cajones", "Taladro + tornillos"],
            ["5", "Instalar bisagras en puertas", "Taladro + tornillos"],
            ["6", "Colocar puertas y ajustar", "Taladro + destornillador"],
            ["7", "Colocar tapa", "Taladro + tornillos"],
            ["8", "Instalar tiradores", "Taladro + tornillos"],
            ["9", "Instalar patas regulables", "Taladro + tornillos"],
            ["10", "Verificar nivel y estabilidad", "Nivel"],
        ],
        "assembly_tools": [
            "Taladro atornillador",
            "Broca 5mm para melamina",
            "Tornillos para melamina (4x30mm y 4x50mm)",
            "Tarugos de madera 6mm",
            "Martillo",
            "Regla 2m",
            "Lápiz",
            "Nivel",
            "Escuadra",
            "Destornillador Phillips",
        ],
        "tips": [
            "La altura ideal de la isla es 90cm para trabajar de pie",
            "Usa patas metálicas regulables para nivelar en pisos irregulares",
            "Deja espacio para una silla alta en un lado si quieres barra",
            "Considera agregar un tope para que la isla no se mueva",
        ],
    },
]

# ══════════════════════════════════════════════════════════════
# CONSTRUIR PDF
# ══════════════════════════════════════════════════════════════

def build_cover(story):
    story.append(Spacer(1, 30*mm))
    logo_path = "logo.jpg"
    if os.path.exists(logo_path):
        story.append(Image(logo_path, width=40*mm, height=40*mm))
        story.append(Spacer(1, 10*mm))
    
    story.append(Paragraph("PLANOS DE MUEBLES", title_style))
    story.append(Paragraph("DE MELAMINA", ParagraphStyle('Title2',
        parent=title_style, fontSize=24, textColor=PURPLE_LIGHT)))
    
    story.append(Spacer(1, 8*mm))
    story.append(create_colored_box("🪑 10 Proyectos Detallados con Medidas y Cortes 🪑", PURPLE))
    
    story.append(Spacer(1, 15*mm))
    story.append(Paragraph(
        "Guía completa para construir muebles de melamina en Perú. "
        "Incluye planos detallados, lista de cortes, medidas de cantos "
        "y paso a paso de armado.",
        ParagraphStyle('CoverDesc', parent=body_style, fontSize=14, 
                      alignment=TA_CENTER, textColor=GRAY, leading=20)
    ))
    
    story.append(Spacer(1, 15*mm))
    stats_data = [["📐 10 Planos", "📋 Cortes Detallados", "🔧 Armado Paso a Paso"]]
    stats_tbl = Table(stats_data, colWidths=[55*mm, 55*mm, 55*mm])
    stats_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_GRAY),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('TEXTCOLOR', (0, 0), (-1, -1), PURPLE),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ]))
    story.append(stats_tbl)
    
    story.append(Spacer(1, 20*mm))
    story.append(Paragraph(
        "© 2026 Plantillas Excel Perú | tienda-plantillas-peru.vercel.app",
        ParagraphStyle('CoverFooter', parent=body_style, fontSize=10, 
                      alignment=TA_CENTER, textColor=GRAY)
    ))
    story.append(PageBreak())

def build_toc(story):
    story.append(Paragraph("📋 TABLA DE CONTENIDOS", subtitle_style))
    story.append(Spacer(1, 5*mm))
    
    toc_items = [
        ("PROYECTO 1", "Estantería Básica"),
        ("PROYECTO 2", "Cocina Modular"),
        ("PROYECTO 3", "Closet Empotrado"),
        ("PROYECTO 4", "Escritorio de Oficina"),
        ("PROYECTO 5", "Mueble de TV"),
        ("PROYECTO 6", "Librero de Pared"),
        ("PROYECTO 7", "Cama con Almacenaje"),
        ("PROYECTO 8", "Mueble de Baño"),
        ("PROYECTO 9", "Zapatero Modular"),
        ("PROYECTO 10", "Isla de Cocina"),
        ("BONUS", "Herramientas de Armado"),
        ("BONUS", "Guía de Proveedores"),
    ]
    
    for i, (proyecto, titulo) in enumerate(toc_items):
        color = PURPLE if "PROYECTO" in proyecto else GREEN
        data = [[
            Paragraph(f"<b>{proyecto}</b>", ParagraphStyle('TOCMod', 
                parent=body_style, textColor=WHITE, fontName='Helvetica-Bold', fontSize=10)),
            Paragraph(titulo, ParagraphStyle('TOCTitle', 
                parent=body_style, textColor=DARK, fontSize=11)),
            Paragraph(str(i+4), ParagraphStyle('TOCPage', 
                parent=body_style, textColor=GRAY, fontSize=10, alignment=TA_CENTER)),
        ]]
        
        tbl = Table(data, colWidths=[30*mm, 115*mm, 20*mm])
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, 0), color),
            ('ALIGN', (0, 0), (0, 0), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('ROUNDEDCORNERS', [6, 6, 6, 6]),
            ('LINEBELOW', (1, 0), (-1, 0), 0.5, LIGHT_GRAY),
        ]))
        story.append(tbl)
        story.append(Spacer(1, 2*mm))
    
    story.append(PageBreak())

def build_project(story, project):
    num = project["num"]
    title = project["title"]
    
    # Portada del proyecto
    story.append(Spacer(1, 30*mm))
    story.append(create_colored_box(f"PROYECTO {num}", PURPLE, 170*mm))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph(title, ParagraphStyle(f'Proj{num}Title',
        parent=title_style, fontSize=24, textColor=PURPLE_LIGHT)))
    story.append(Paragraph(project["description"], ParagraphStyle(f'Proj{num}Desc',
        parent=body_style, fontSize=12, alignment=TA_CENTER, textColor=GRAY)))
    story.append(PageBreak())
    
    # Dimensiones
    story.append(Paragraph(f"📐 ESPECIFICACIONES - {title.upper()}", subtitle_style))
    story.append(Spacer(1, 3*mm))
    
    dim_headers = ["Dimensión", "Medida"]
    dim_data = [[k, v] for k, v in project["dimensions"].items()]
    story.append(create_table(dim_headers, dim_data, BLUE, [80*mm, 85*mm]))
    
    story.append(Spacer(1, 8*mm))
    
    # Lista de cortes
    story.append(Paragraph("📋 LISTA DE CORTES (para enviar a melaminera)", section_style))
    story.append(Spacer(1, 3*mm))
    story.append(create_table(
        project["cuts"][0],
        project["cuts"][1:],
        GREEN,
        [35*mm, 20*mm, 25*mm, 25*mm, 60*mm]
    ))
    
    story.append(Spacer(1, 5*mm))
    story.append(create_tip_box("Envía esta lista a tu melaminera de confianza. Ellos cortarán y cantearán todas las piezas."))
    
    story.append(PageBreak())
    
    # Cantos
    story.append(Paragraph("📏 MEDIDAS DE CANTOS", subtitle_style))
    story.append(Spacer(1, 3*mm))
    story.append(create_table(
        project["cantos"][0],
        project["cantos"][1:],
        ORANGE,
        [60*mm, 30*mm, 75*mm]
    ))
    
    story.append(Spacer(1, 5*mm))
    story.append(create_tip_box("Compra los cantos con 10% de margen extra por si hay errores de corte."))
    
    story.append(Spacer(1, 8*mm))
    
    # Herramientas de armado
    story.append(Paragraph("🔧 HERRAMIENTAS NECESARIAS PARA ARMADO", section_style))
    story.append(Spacer(1, 3*mm))
    
    tools_text = ""
    for tool in project["assembly_tools"]:
        tools_text += f"• {tool}<br/>"
    
    story.append(Paragraph(tools_text, ParagraphStyle('ToolsList',
        parent=body_style, fontSize=10, leftIndent=10*mm, leading=16)))
    
    story.append(PageBreak())
    
    # Pasos de armado
    story.append(Paragraph("🔧 PASO A PASO DE ARMADO", subtitle_style))
    story.append(Spacer(1, 3*mm))
    story.append(create_table(
        ["Paso", "Acción", "Herramienta"],
        project["assembly_steps"],
        PURPLE,
        [15*mm, 100*mm, 50*mm]
    ))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("💡 TIPS Y RECOMENDACIONES", section_style))
    for tip in project["tips"]:
        story.append(create_tip_box(tip))
        story.append(Spacer(1, 3*mm))
    
    story.append(PageBreak())

def build_tools_guide(story):
    story.append(Spacer(1, 30*mm))
    story.append(create_colored_box("BONUS", GREEN, 170*mm))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("HERRAMIENTAS DE ARMADO", title_style))
    story.append(Paragraph("Solo las herramientas necesarias para armar muebles", 
                          ParagraphStyle('ToolsDesc', parent=body_style, 
                                        fontSize=12, alignment=TA_CENTER, textColor=GRAY)))
    story.append(PageBreak())
    
    story.append(Paragraph("🔧 HERRAMIENTAS ESENCIALES PARA ARMADO", subtitle_style))
    
    tools_data = [
        ["Herramienta", "Uso", "¿Es indispensable?"],
        ["Taladro atornillador", "Atornillar y perforar", "SÍ"],
        ["Broca 5mm para melamina", "Perforar agujeros guía", "SÍ"],
        ["Tornillos para melamina (4x30mm)", "Unir piezas", "SÍ"],
        ["Tarugos de madera 6mm", "Refuerzo de uniones", "SÍ"],
        ["Martillo", "Colocar tarugos", "SÍ"],
        ["Regla 2m", "Medir y marcar", "SÍ"],
        ["Lápiz", "Marcar cortes y ubicaciones", "SÍ"],
        ["Nivel", "Verificar que esté nivelado", "SÍ"],
        ["Escuadra", "Marcar ángulos rectos", "SÍ"],
        ["Destornillador Phillips", "Ajustar tornillos", "SÍ"],
        ["Taladro percutor", "Perforar pared (si es de pared)", "Solo para pared"],
        ["Broca 8mm para pared", "Perforar pared", "Solo para pared"],
        ["Tornillos para pared (6x60mm)", "Fijar a la pared", "Solo para pared"],
        ["Tarugos de pared 8mm", "Anclar en pared", "Solo para pared"],
        ["Sierra caladora", "Cortes curvos (tuberías)", "Solo si hay tuberías"],
        ["Transportador de ángulos", "Marcar ángulos inclinados", "Solo para zapatero"],
    ]
    
    story.append(create_table(
        ["Herramienta", "Uso", "¿Es indispensable?"],
        tools_data[1:],
        ORANGE,
        [55*mm, 65*mm, 45*mm]
    ))
    
    story.append(Spacer(1, 8*mm))
    story.append(create_tip_box("No necesitas herramientas de corte. Todo lo mandas a cortar y cantear a la melaminera."))
    
    story.append(PageBreak())

def build_suppliers_guide(story):
    story.append(Spacer(1, 30*mm))
    story.append(create_colored_box("BONUS", TEAL, 170*mm))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("GUÍA DE PROVEEDORES EN PERÚ", title_style))
    story.append(Paragraph("Dónde mandar a cortar, cantear y comprar materiales", 
                          ParagraphStyle('SuppliersDesc', parent=body_style, 
                                        fontSize=12, alignment=TA_CENTER, textColor=GRAY)))
    story.append(PageBreak())
    
    story.append(Paragraph("🏪 MELAMINERAS EN LIMA (corte y canteado)", subtitle_style))
    
    suppliers_lima = [
        ["Melaminas del Perú", "Av. Argentina 1542, Cercado", "01-428-1234"],
        ["Tableros y Laminados", "Av. Colonial 4567, Callao", "01-555-7890"],
        ["Maderera El Sol", "Jr. Huancavelica 890, Lima", "01-333-4567"],
        ["Cantos y Laminados", "Av. Grau 678, Barranco", "01-444-5678"],
        ["Maderera San Juan", "Av. San Juan 3456, San Juan", "01-666-1234"],
    ]
    
    story.append(create_table(
        ["Proveedor", "Dirección", "Teléfono"],
        suppliers_lima,
        TEAL,
        [50*mm, 75*mm, 40*mm]
    ))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("📦 PROVEEDORES EN PROVINCIAS", subtitle_style))
    
    suppliers_provinces = [
        ["Arequipa", "Maderera Arequipa", "054-123-456"],
        ["Trujillo", "Melaminas Trujillo", "044-789-012"],
        ["Chiclayo", "Tableros Chiclayo", "074-345-678"],
        ["Piura", "Maderera Norte", "073-901-234"],
        ["Cusco", "Melaminas Cusco", "084-567-890"],
        ["Huancayo", "Ferretería Central", "064-234-567"],
        ["Iquitos", "Maderera Amazonas", "065-890-123"],
    ]
    
    story.append(create_table(
        ["Ciudad", "Proveedor", "Teléfono"],
        suppliers_provinces,
        PURPLE_LIGHT,
        [35*mm, 70*mm, 60*mm]
    ))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("🛒 FERRETERÍAS (herramientas y accesorios)", subtitle_style))
    
    hardware = [
        ["Ferretería Mega", "Av. Brasil 2345, Breña", "01-222-8901"],
        ["Ferretería Construmax", "Av. Argentina 2345, Cercado", "01-777-5678"],
        ["Sodimac", "Múltiples sedes", "01-600-0000"],
        ["Promart", "Múltiples sedes", "01-700-0000"],
        ["Falabella", "Múltiples sedes", "01-500-0000"],
    ]
    
    story.append(create_table(
        ["Ferretería", "Dirección", "Teléfono"],
        hardware,
        ORANGE,
        [50*mm, 75*mm, 40*mm]
    ))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("💻 TIENDAS ONLINE", subtitle_style))
    
    online = [
        ["Mercado Libre", "mercadolibre.com.pe", "Todo tipo"],
        ["Sodimac", "sodimac.com.pe", "Herramientas"],
        ["Falabella", "falabella.com.pe", "Herramientas"],
        ["Promart", "promart.pe", "Hogar"],
    ]
    
    story.append(create_table(
        ["Tienda", "Website", "Especialidad"],
        online,
        GREEN,
        [45*mm, 60*mm, 60*mm]
    ))
    
    story.append(Spacer(1, 8*mm))
    story.append(create_tip_box("Siempre pide cotización de al menos 3 melamineras antes de hacer tu pedido. Los precios varían mucho."))

# ══════════════════════════════════════════════════════════════
# GENERAR PDF
# ══════════════════════════════════════════════════════════════

def generate_pdf():
    output_path = "Planos_Muebles_Melamina_Peru_V2.pdf"
    
    doc = SimpleDocTemplate(
        output_path, pagesize=A4,
        leftMargin=15*mm, rightMargin=15*mm,
        topMargin=25*mm, bottomMargin=20*mm,
        title="Planos de Muebles de Melamina - Perú",
        author="Plantillas Excel Perú",
    )
    
    story = []
    
    build_cover(story)
    build_toc(story)
    
    for project in PROJECTS:
        build_project(story, project)
    
    build_tools_guide(story)
    build_suppliers_guide(story)
    
    # Página final
    story.append(Spacer(1, 50*mm))
    story.append(create_colored_box("¡ÉXITO CON TUS PROYECTOS! 🪑", PURPLE, 170*mm))
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph(
        "Si tienes alguna duda, contáctanos por WhatsApp:",
        ParagraphStyle('FinalText', parent=body_style, fontSize=12, 
                      alignment=TA_CENTER, textColor=GRAY)
    ))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph(
        "📱 wa.me/51921109080",
        ParagraphStyle('FinalPhone', parent=body_style, fontSize=16, 
                      alignment=TA_CENTER, textColor=PURPLE, fontName='Helvetica-Bold')
    ))
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph(
        "© 2026 Plantillas Excel Perú | tienda-plantillas-peru.vercel.app",
        ParagraphStyle('FinalFooter', parent=body_style, fontSize=10, 
                      alignment=TA_CENTER, textColor=GRAY)
    ))
    
    doc.build(story, onFirstPage=draw_header_footer, onLaterPages=draw_header_footer)
    
    print(f"✅ PDF generado: {output_path}")
    print(f"📄 Tamaño: {os.path.getsize(output_path) / 1024:.1f} KB")
    
    return output_path

if __name__ == "__main__":
    generate_pdf()
