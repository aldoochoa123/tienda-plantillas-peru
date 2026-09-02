"""
Genera PDF del curso: Ventas por WhatsApp Business
Diseño profesional, colorido e interactivo
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    Image, KeepTogether, ListFlowable, ListItem
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
import os

# ══════════════════════════════════════════════════════════════
# COLORES
# ══════════════════════════════════════════════════════════════

PURPLE = HexColor("#3D0C8E")
PURPLE_LIGHT = HexColor("#6C5CE7")
PURPLE_DARK = HexColor("#1A1A2E")
GREEN = HexColor("#00B894")
GREEN_LIGHT = HexColor("#55EFC4")
BLUE = HexColor("#0984E3")
BLUE_LIGHT = HexColor("#74B9FF")
ORANGE = HexColor("#E17055")
RED = HexColor("#D63031")
YELLOW = HexColor("#FDCB6E")
TEAL = HexColor("#00CEC9")
PINK = HexColor("#FD79A8")
GRAY = HexColor("#636E72")
LIGHT_GRAY = HexColor("#F5F6FA")
DARK = HexColor("#2D3436")
WHITE = white

# ══════════════════════════════════════════════════════════════
# ESTILOS
# ══════════════════════════════════════════════════════════════

styles = getSampleStyleSheet()

# Estilo para títulos de módulo
module_title = ParagraphStyle(
    'ModuleTitle',
    parent=styles['Heading1'],
    fontSize=28,
    textColor=WHITE,
    fontName='Helvetica-Bold',
    alignment=TA_CENTER,
    spaceAfter=6*mm,
    spaceBefore=0,
)

# Estilo para subtítulos
subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Heading2'],
    fontSize=18,
    textColor=PURPLE,
    fontName='Helvetica-Bold',
    alignment=TA_LEFT,
    spaceAfter=4*mm,
    spaceBefore=8*mm,
)

# Estilo para títulos de sección
section_title = ParagraphStyle(
    'SectionTitle',
    parent=styles['Heading3'],
    fontSize=14,
    textColor=PURPLE_LIGHT,
    fontName='Helvetica-Bold',
    alignment=TA_LEFT,
    spaceAfter=3*mm,
    spaceBefore=6*mm,
)

# Estilo para cuerpo de texto
body_style = ParagraphStyle(
    'BodyText',
    parent=styles['BodyText'],
    fontSize=11,
    textColor=DARK,
    fontName='Helvetica',
    alignment=TA_JUSTIFY,
    spaceAfter=3*mm,
    leading=16,
)

# Estilo para tips
tip_style = ParagraphStyle(
    'TipText',
    parent=styles['BodyText'],
    fontSize=10,
    textColor=HexColor("#00B894"),
    fontName='Helvetica-Oblique',
    alignment=TA_LEFT,
    spaceAfter=2*mm,
    leftIndent=10*mm,
    leading=14,
)

# Estilo para scripts
script_style = ParagraphStyle(
    'ScriptText',
    parent=styles['BodyText'],
    fontSize=10,
    textColor=DARK,
    fontName='Courier',
    alignment=TA_LEFT,
    spaceAfter=2*mm,
    leftIndent=5*mm,
    rightIndent=5*mm,
    backColor=LIGHT_GRAY,
    borderPadding=8,
    leading=14,
)

# Estilo para numeración
number_style = ParagraphStyle(
    'NumberStyle',
    parent=styles['BodyText'],
    fontSize=12,
    textColor=PURPLE,
    fontName='Helvetica-Bold',
    alignment=TA_LEFT,
    spaceAfter=2*mm,
)

# ══════════════════════════════════════════════════════════════
# FUNCIONES DE DIBUJO
# ══════════════════════════════════════════════════════════════

def draw_header_footer(canvas_obj, doc):
    """Dibuja header y footer en cada página"""
    canvas_obj.saveState()
    
    # Header - línea morada
    canvas_obj.setStrokeColor(PURPLE)
    canvas_obj.setLineWidth(3)
    canvas_obj.line(15*mm, A4[1] - 12*mm, A4[0] - 15*mm, A4[1] - 12*mm)
    
    # Logo en header
    logo_path = "logo.jpg"
    if os.path.exists(logo_path):
        canvas_obj.drawImage(logo_path, 15*mm, A4[1] - 18*mm, 
                           width=15*mm, height=15*mm, 
                           preserveAspectRatio=True, mask="auto")
    
    # Texto header
    canvas_obj.setFont("Helvetica-Bold", 8)
    canvas_obj.setFillColor(PURPLE)
    canvas_obj.drawString(35*mm, A4[1] - 15*mm, "CURSO VENTAS POR WHATSAPP BUSINESS")
    
    # Footer
    canvas_obj.setFont("Helvetica", 8)
    canvas_obj.setFillColor(GRAY)
    canvas_obj.drawString(15*mm, 10*mm, "© 2026 Plantillas Excel Perú")
    canvas_obj.drawRightString(A4[0] - 15*mm, 10*mm, f"Página {doc.page}")
    
    # Línea footer
    canvas_obj.setStrokeColor(PURPLE_LIGHT)
    canvas_obj.setLineWidth(1)
    canvas_obj.line(15*mm, 15*mm, A4[0] - 15*mm, 15*mm)
    
    canvas_obj.restoreState()

def create_colored_box(text, color, width=170*mm):
    """Crea una caja de color con texto"""
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
    """Crea una caja de tip"""
    tip_text = f"<b>{icon} TIP:</b> {text}"
    data = [[Paragraph(tip_text, ParagraphStyle('TipBox', 
            parent=body_style, textColor=HexColor("#00B894"), fontSize=10,
            fontName='Helvetica-Oblique'))]]
    
    tbl = Table(data, colWidths=[170*mm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor("#F0FFF0")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 15),
        ('RIGHTPADDING', (0, 0), (-1, -1), 15),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
        ('BOX', (0, 0), (-1, -1), 1, GREEN),
    ]))
    return tbl

def create_script_box(title, script_text):
    """Crea una caja de script de WhatsApp"""
    content = f"<b>{title}</b><br/><br/>{script_text}"
    data = [[Paragraph(content, ParagraphStyle('ScriptBox', 
            parent=script_style, textColor=DARK, fontSize=10,
            fontName='Courier', leading=15))]]
    
    tbl = Table(data, colWidths=[170*mm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor("#F8F9FA")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 15),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 15),
        ('LEFTPADDING', (0, 0), (-1, -1), 15),
        ('RIGHTPADDING', (0, 0), (-1, -1), 15),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
        ('BOX', (0, 0), (-1, -1), 2, PURPLE_LIGHT),
    ]))
    return tbl

def create_checklist(items):
    """Crea una lista de verificación"""
    elements = []
    for item in items:
        elements.append(Paragraph(f"☐ {item}", ParagraphStyle('Checklist', 
                      parent=body_style, fontSize=11, leftIndent=10*mm)))
    return elements

def create_numbered_list(items):
    """Crea una lista numerada con estilo"""
    elements = []
    for i, item in enumerate(items, 1):
        elements.append(Paragraph(f"<b>{i}.</b> {item}", ParagraphStyle('Numbered', 
                      parent=body_style, fontSize=11, leftIndent=10*mm)))
    return elements

# ══════════════════════════════════════════════════════════════
# CONTENIDO DEL CURSO
# ══════════════════════════════════════════════════════════════

def build_cover(story):
    """Página de portada"""
    story.append(Spacer(1, 30*mm))
    
    # Logo
    logo_path = "logo.jpg"
    if os.path.exists(logo_path):
        story.append(Image(logo_path, width=40*mm, height=40*mm))
        story.append(Spacer(1, 10*mm))
    
    # Título principal
    story.append(Paragraph("CURSO COMPLETO", ParagraphStyle('CoverTitle1',
        parent=module_title, fontSize=36, textColor=PURPLE)))
    
    story.append(Paragraph("VENTAS POR WHATSAPP BUSINESS", ParagraphStyle('CoverTitle2',
        parent=module_title, fontSize=28, textColor=PURPLE_DARK)))
    
    story.append(Spacer(1, 8*mm))
    
    # Línea decorativa
    story.append(create_colored_box("📱 De 0 a Experto en Ventas por WhatsApp 📱", PURPLE))
    
    story.append(Spacer(1, 15*mm))
    
    # Descripción
    story.append(Paragraph(
        "Aprende a configurar WhatsApp Business, crear tu catálogo, "
        "automatizar respuestas y cerrar más ventas para tu negocio peruano.",
        ParagraphStyle('CoverDesc', parent=body_style, fontSize=14, 
                      alignment=TA_CENTER, textColor=GRAY, leading=20)
    ))
    
    story.append(Spacer(1, 15*mm))
    
    # Stats
    stats_data = [
        ["📊 5 Módulos", "📱 +50 Scripts", "⏰ 3 Horas"],
    ]
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
    
    # Info
    story.append(Paragraph(
        "© 2026 Plantillas Excel Perú | tienda-plantillas-peru.vercel.app",
        ParagraphStyle('CoverFooter', parent=body_style, fontSize=10, 
                      alignment=TA_CENTER, textColor=GRAY)
    ))
    
    story.append(PageBreak())

def build_toc(story):
    """Tabla de contenidos"""
    story.append(Paragraph("📋 TABLA DE CONTENIDOS", subtitle_style))
    story.append(Spacer(1, 5*mm))
    
    toc_items = [
        ("MÓDULO 1", "Configuración de WhatsApp Business", "4"),
        ("MÓDULO 2", "Estrategia de Ventas", "8"),
        ("MÓDULO 3", "Scripts de Ventas Listos", "12"),
        ("MÓDULO 4", "Automatización y Herramientas", "18"),
        ("MÓDULO 5", "Casos Prácticos", "22"),
        ("BONUS", "50 Scripts de WhatsApp", "26"),
        ("BONUS", "Checklist de Configuración", "30"),
    ]
    
    for modulo, titulo, pagina in toc_items:
        color = PURPLE if "MÓDULO" in modulo else GREEN
        data = [[
            Paragraph(f"<b>{modulo}</b>", ParagraphStyle('TOCMod', 
                parent=body_style, textColor=WHITE, fontName='Helvetica-Bold', fontSize=10)),
            Paragraph(titulo, ParagraphStyle('TOCTitle', 
                parent=body_style, textColor=DARK, fontSize=11)),
            Paragraph(pagina, ParagraphStyle('TOCPage', 
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

def build_module1(story):
    """Módulo 1: Configuración"""
    # Portada del módulo
    story.append(Spacer(1, 40*mm))
    story.append(create_colored_box("MÓDULO 1", PURPLE, 170*mm))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("CONFIGURACIÓN DE WHATSAPP BUSINESS", 
                          ParagraphStyle('Mod1Title', parent=module_title, 
                                        fontSize=24, textColor=PURPLE_DARK)))
    story.append(Paragraph("Pon tu negocio en WhatsApp profesionalmente", 
                          ParagraphStyle('Mod1Sub', parent=body_style, 
                                        fontSize=14, alignment=TA_CENTER, textColor=GRAY)))
    story.append(PageBreak())
    
    # Contenido
    story.append(Paragraph("1.1 Descargar WhatsApp Business", subtitle_style))
    story.append(Paragraph(
        "WhatsApp Business es la versión profesional de WhatsApp diseñada para negocios. "
        "Es gratuita y te permite crear un perfil profesional, catálogo de productos y "
        "respuestas automáticas.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    story.append(create_tip_box("Busca 'WhatsApp Business' en la Play Store o App Store. Es diferente a WhatsApp normal."))
    
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("Pasos para descargar:", section_title))
    
    steps = [
        "Abre la Play Store (Android) o App Store (iPhone)",
        "Busca 'WhatsApp Business'",
        "Toca 'Instalar'",
        "Abre la app y acepta los términos",
        "Ingresa tu número de teléfono (puede ser el mismo que WhatsApp normal)",
        "Verifica el código que recibes por SMS",
    ]
    story.extend(create_numbered_list(steps))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("1.2 Crear Perfil Profesional", subtitle_style))
    story.append(Paragraph(
        "Tu perfil es la primera impresión de tu negocio. Debe verse profesional y "
        "transmitir confianza a tus clientes.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    
    # Tabla de datos del perfil
    profile_data = [
        ["Campo", "Qué poner", "Ejemplo"],
        ["Nombre del negocio", "Nombre real de tu negocio", "Bodega Don Pepe"],
        ["Categoría", "Tipo de negocio", "Tienda de abarrotes"],
        ["Descripción", "Qué vendes + beneficios", "Productos frescos delivery gratis"],
        ["Dirección", "Tu dirección real", "Av. Lima 123, Lima"],
        ["Horario", "Cuándo atiendes", "Lun-Sáb 8am-9pm"],
        ["Sitio web", "Tu web o redes", "wa.me/51999999999"],
    ]
    
    profile_tbl = Table(profile_data, colWidths=[40*mm, 60*mm, 65*mm])
    profile_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PURPLE),
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
        ('ROUNDEDCORNERS', [6, 6, 6, 6]),
    ]))
    story.append(profile_tbl)
    
    story.append(Spacer(1, 5*mm))
    story.append(create_tip_box("Usa una foto de logo profesional como imagen de perfil. Primera impresión importa."))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("1.3 Configurar Catálogo de Productos", subtitle_style))
    story.append(Paragraph(
        "El catálogo te permite mostrar tus productos directamente en WhatsApp. "
        "Los clientes pueden ver fotos, precios y descripciones sin salir del chat.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("Cómo crear tu catálogo:", section_title))
    
    catalog_steps = [
        "Abre WhatsApp Business → Configuración",
        "Toca 'Catálogo de negocios'",
        "Toca 'Agregar producto o servicio'",
        "Sube una foto del producto",
        "Pon el nombre del producto",
        "Agrega el precio",
        "Escribe una descripción breve",
        "Guarda y repite para cada producto",
    ]
    story.extend(create_numbered_list(catalog_steps))
    
    story.append(Spacer(1, 5*mm))
    story.append(create_tip_box("Agrega máximo 10-15 productos al inicio. Los clientes se abrumarán con demasiados."))
    
    story.append(PageBreak())
    
    # Continuación módulo 1
    story.append(Paragraph("1.4 Mensaje de Bienvenida Automático", subtitle_style))
    story.append(Paragraph(
        "El mensaje de bienvenida se envía automáticamente cuando un cliente te "
        "escribe por primera vez o después de 14 días de inactividad.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("Configuración:", section_title))
    
    welcome_steps = [
        "Ve a Configuración → Herramientas empresariales",
        "Toca 'Mensaje de bienvenida'",
        "Activa 'Enviar mensaje de bienvenida'",
        "Escribe tu mensaje (usa el script de abajo)",
        "Guarda los cambios",
    ]
    story.extend(create_numbered_list(welcome_steps))
    
    story.append(Spacer(1, 5*mm))
    story.append(create_script_box(
        "📱 MENSAJE DE BIENVENIDA SUGERIDO",
        "¡Hola! 👋 Bienvenido a [TU NEGOCIO]<br/><br/>"
        "Somos tu solución para [TU PRODUCTO/SERVICIO]<br/><br/>"
        "📊 Catálogo disponible<br/>"
        "💰 Precios especiales<br/>"
        "📱 Delivery disponible<br/><br/>"
        "¿En qué puedo ayudarte?<br/><br/>"
        "Escribe:<br/>"
        "• PRECIO - Ver precios<br/>"
        "• CATALOGO - Ver productos<br/>"
        "• DELIVERY - Info de envíos"
    ))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("1.5 Respuestas Rápidas", subtitle_style))
    story.append(Paragraph(
        "Las respuestas rápidas te permiten guardar mensajes predefinidos y enviarlos "
        "con solo escribir un atajo. Te ahorra horas de escritura.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("Ejemplos de respuestas rápidas:", section_title))
    
    quick_data = [
        ["Atajo", "Respuesta"],
        ["/precio", "💰 Nuestros precios: [LISTA PRECIOS]. ¿Te interesa alguno?"],
        ["/envio", "🚚 Delivery: Gratis en [ZONA]. Fuera de zona: S/5-10"],
        ["/pago", "📱 Aceptamos: Yape, Plin, Transferencia, Efectivo"],
        ["/horario", "🕐 Horario: Lun-Sáb 8am-9pm. Domingos 9am-2pm"],
        ["/gracias", "¡Gracias por tu compra! 🎉 ¿Necesitas algo más?"],
    ]
    
    quick_tbl = Table(quick_data, colWidths=[30*mm, 135*mm])
    quick_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), GREEN),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, HexColor("#F0FFF0")]),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#D0D5DD")),
    ]))
    story.append(quick_tbl)
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("1.6 Etiquetas de Clientes", subtitle_style))
    story.append(Paragraph(
        "Las etiquetas te permiten organizar tus clientes por categorías. "
        "Así puedes enviar mensajes segmentados y hacer seguimiento efectivo.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("Etiquetas recomendadas:", section_title))
    
    labels_data = [
        ["Etiqueta", "Color", "Cuándo usarla"],
        ["🟢 Nuevo cliente", "Verde", "Primera compra o consulta"],
        ["🟡 Cliente frecuente", "Amarillo", "3+ compras"],
        ["🔴 VIP", "Rojo", "Cliente premium o alto valor"],
        ["🔵 Pendiente", "Azul", "Esperando pago o respuesta"],
        ["🟣 Completado", "Morado", "Entrega realizada"],
    ]
    
    labels_tbl = Table(labels_data, colWidths=[45*mm, 25*mm, 95*mm])
    labels_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PURPLE_LIGHT),
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
    story.append(labels_tbl)
    
    story.append(Spacer(1, 5*mm))
    story.append(create_tip_box("Etiqueta a cada cliente después de la primera interacción. Te ayudará a hacer seguimiento."))
    
    story.append(PageBreak())

def build_module2(story):
    """Módulo 2: Estrategia de Ventas"""
    # Portada del módulo
    story.append(Spacer(1, 40*mm))
    story.append(create_colored_box("MÓDULO 2", BLUE, 170*mm))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("ESTRATEGIA DE VENTAS POR WHATSAPP", 
                          ParagraphStyle('Mod2Title', parent=module_title, 
                                        fontSize=24, textColor=PURPLE_DARK)))
    story.append(Paragraph("De consulta a venta cerrada", 
                          ParagraphStyle('Mod2Sub', parent=body_style, 
                                        fontSize=14, alignment=TA_CENTER, textColor=GRAY)))
    story.append(PageBreak())
    
    # Contenido
    story.append(Paragraph("2.1 El Proceso de Venta", subtitle_style))
    story.append(Paragraph(
        "Todo proceso de venta en WhatsApp sigue 5 pasos. Si dominas cada uno, "
        "aumentarás tus ventas significativamente.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    
    # Proceso de venta
    process_data = [
        ["PASO", "ACCIÓN", "OBJETIVO"],
        ["1️⃣", "Primer contacto", "Generar confianza"],
        ["2️⃣", "Descubrir necesidad", "Qué busca el cliente"],
        ["3️⃣", "Presentar solución", "Mostrar tu producto"],
        ["4️⃣", "Manejar objeciones", "Resolver dudas"],
        ["5️⃣", "Cerrar venta", "Concretar el pago"],
    ]
    
    process_tbl = Table(process_data, colWidths=[20*mm, 55*mm, 90*mm])
    process_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_GRAY]),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#D0D5DD")),
    ]))
    story.append(process_tbl)
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("2.2 Primer Contacto (Sin Parecer Spam)", subtitle_style))
    story.append(Paragraph(
        "El primer mensaje es crucial. Si parece spam, el cliente te bloqueará. "
        "Si es muy frío, no generará interés. El balance está en ser personal y útil.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    story.append(create_script_box(
        "📱 PRIMER CONTACTO - CLIENTE NUEVO",
        "Hola [NOMBRE] 👋<br/><br/>"
        "Vi que te interesa [PRODUCTO/SERVICIO].<br/><br/>"
        "¿Tienes alguna consulta?<br/>"
        "Con gusto te ayudo 😊<br/><br/>"
        "[TU NOMBRE]<br/>"
        "[TU NEGOCIO]"
    ))
    
    story.append(Spacer(1, 5*mm))
    story.append(create_script_box(
        "📱 PRIMER CONTACTO - DESPUÉS DE UNA PUBLICACIÓN",
        "Hola [NOMBRE] 👋<br/><br/>"
        "Gracias por comentar en mi publicación sobre [TEMA].<br/><br/>"
        "¿Te gustaría más información?<br/>"
        "Estoy aquí para ayudarte 😊"
    ))
    
    story.append(Spacer(1, 5*mm))
    story.append(create_tip_box("NUNCA envíes mensajes masivos sin personalizar. WhatsApp puede bloquear tu número."))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("2.3 Descubrir la Necesidad del Cliente", subtitle_style))
    story.append(Paragraph(
        "Antes de presentar tu producto, necesitas saber qué busca el cliente. "
        "Haz preguntas abiertas para entender su situación.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("Preguntas clave:", section_title))
    
    questions = [
        "¿Qué tipo de negocio tienes?",
        "¿Qué problema quieres resolver?",
        "¿Has probado otras soluciones antes?",
        "¿Cuál es tu presupuesto aproximado?",
        "¿Para cuándo lo necesitas?",
    ]
    story.extend(create_numbered_list(questions))
    
    story.append(Spacer(1, 5*mm))
    story.append(create_tip_box("Escucha más de lo que hablas. El 80% del tiempo debe ser escuchar al cliente."))
    
    story.append(PageBreak())
    
    # Continuación módulo 2
    story.append(Paragraph("2.4 Presentar tu Producto", subtitle_style))
    story.append(Paragraph(
        "Una vez que sabes qué busca el cliente, presenta tu producto como la solución "
        "perfecta a su problema. Enfócate en beneficios, no en características.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    
    # Beneficios vs características
    benefits_data = [
        ["❌ NO digas", "✅ SÍ diga"],
        ["Tenemos 3,468 plantillas", "Ahorrarás horas de trabajo cada semana"],
        ["El precio es S/6", "Es menos de S/0.02 por plantilla"],
        ["Incluye IGV y AFP", "Ya viene todo calculado, solo llenas datos"],
        ["Es un archivo Excel", "En 5 minutos tienes tu reporte profesional"],
    ]
    
    benefits_tbl = Table(benefits_data, colWidths=[82*mm, 82*mm])
    benefits_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), RED),
        ('BACKGROUND', (1, 0), (1, 0), GREEN),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_GRAY]),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#D0D5DD")),
    ]))
    story.append(benefits_tbl)
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("2.5 Manejar Objeciones", subtitle_style))
    story.append(Paragraph(
        "Las objeciones son normales. No son rechazos, son peticiones de más información. "
        "Cada objeción es una oportunidad de cerrar la venta.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    
    objections_data = [
        ["Objeción", "Respuesta"],
        ["'Es muy caro'", "Entiendo. Pero es una inversión que se paga sola en 1 día de uso. ¿Cuánto tiempo te tomaría hacerlo solo?"],
        ["'Lo pienso'", "Perfecto. Mientras piensas, ¿te gustaría ver una muestra gratis para que compruebes la calidad?"],
        ["'No tengo tiempo'", "Justamente por eso existen estas plantillas. En 5 minutos tienes tu reporte listo."],
        ["'No sé Excel'", "No te preocupes. Las plantillas ya vienen con fórmulas. Solo llenas datos y listo."],
        ["'¿Es seguro?'", "Claro. +500 negocios ya las usan. Sin macros, sin virus, solo fórmulas Excel."],
    ]
    
    obj_tbl = Table(objections_data, colWidths=[35*mm, 130*mm])
    obj_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), ORANGE),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, HexColor("#FFF5F0")]),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#D0D5DD")),
    ]))
    story.append(obj_tbl)
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("2.6 Cerrar la Venta", subtitle_style))
    story.append(Paragraph(
        "El momento de cerrar es cuando el cliente está listo. No lo fuerces, "
        "pero tampoco dejes pasar la oportunidad.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    story.append(create_script_box(
        "📱 CIERRE DE VENTA",
        "Perfecto [NOMBRE] 🎉<br/><br/>"
        "Para activar tu acceso necesito:<br/>"
        "1. Tu número de WhatsApp (será tu usuario)<br/>"
        "2. El pago de [PRECIO] por [Yape/Plin/Transferencia]<br/><br/>"
        "Una vez confirmado el pago, te envío tus datos de acceso en 2 minutos.<br/><br/>"
        "¿Cómo prefieres pagar? 💰"
    ))
    
    story.append(Spacer(1, 5*mm))
    story.append(create_tip_box("Si el cliente no responde en 24 horas, envía un mensaje de seguimiento suave."))
    
    story.append(PageBreak())

def build_module3(story):
    """Módulo 3: Scripts de Ventas"""
    # Portada del módulo
    story.append(Spacer(1, 40*mm))
    story.append(create_colored_box("MÓDULO 3", GREEN, 170*mm))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("SCRIPTS DE VENTAS LISTOS PARA USAR", 
                          ParagraphStyle('Mod3Title', parent=module_title, 
                                        fontSize=24, textColor=PURPLE_DARK)))
    story.append(Paragraph("Copia, pega y adapta a tu negocio", 
                          ParagraphStyle('Mod3Sub', parent=body_style, 
                                        fontSize=14, alignment=TA_CENTER, textColor=GRAY)))
    story.append(PageBreak())
    
    # Contenido
    story.append(Paragraph("3.1 Scripts de Primer Contacto", subtitle_style))
    
    scripts = [
        ("Para cliente que pregunta por precio:",
         "Hola [NOMBRE] 👋<br/><br/>"
         "Gracias por tu interés en [PRODUCTO].<br/><br/>"
         "💰 Precio: [PRECIO]<br/>"
         "✅ Incluye: [BENEFICIOS]<br/>"
         "📱 Pago: Yape, Plin o Transferencia<br/><br/>"
         "¿Te gustaría acceder? 🎯"),
        
        ("Para cliente que viene de redes sociales:",
         "Hola [NOMBRE] 👋<br/><br/>"
         "Vi que te interesa [PRODUCTO] por [REDES].<br/><br/>"
         "¿Tienes alguna consulta?<br/>"
         "Con gusto te ayudo 😊"),
        
        ("Para cliente que pide información:",
         "Hola [NOMBRE] 👋<br/><br/>"
         "Aquí te envío la información que pediste:<br/><br/>"
         "📊 [PRODUCTO]<br/>"
         "💰 Precio: [PRECIO]<br/>"
         "✅ Beneficios: [LISTA]<br/>"
         "📱 Pago: Yape/Plin<br/><br/>"
         "¿Te gustaría acceder? 🎯"),
    ]
    
    for title, script in scripts:
        story.append(create_script_box(title, script))
        story.append(Spacer(1, 5*mm))
    
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("3.2 Scripts de Seguimiento", subtitle_style))
    
    follow_ups = [
        ("Si no responde en 24 horas:",
         "Hola [NOMBRE] 👋<br/><br/>"
         "¿Tuviste chance de revisar la información?<br/><br/>"
         "Si tienes alguna duda, con gusto te ayudo.<br/><br/>"
         "Recuerda que el precio especial es por tiempo limitado ⏰"),
        
        ("Si dice que lo piensa:",
         "Hola [NOMBRE] 👋<br/><br/>"
         "Entiendo que necesitas pensarlo.<br/><br/>"
         "Mientras tanto, ¿te gustaría ver una muestra gratis?<br/>"
         "Así puedes comprobar la calidad antes de decidir.<br/><br/>"
         "¿Te la envío? 📱"),
        
        ("Después de una compra:",
         "¡Gracias por tu compra [NOMBRE]! 🎉<br/><br/>"
         "Ya tienes acceso a [PRODUCTO].<br/><br/>"
         "Si necesitas ayuda o tienes alguna duda,<br/>"
         "estoy aquí para ti.<br/><br/>"
         "¡Éxito con tu negocio! 💪"),
    ]
    
    for title, script in follow_ups:
        story.append(create_script_box(title, script))
        story.append(Spacer(1, 5*mm))
    
    story.append(PageBreak())
    
    # Más scripts
    story.append(Paragraph("3.3 Scripts para Diferentes Rubros", subtitle_style))
    
    rubro_scripts = [
        ("Para Bodegas/Minimarkets:",
         "Hola [NOMBRE] 👋<br/><br/>"
         "¿Tienes una bodega?<br/><br/>"
         "Tenemos plantillas especialmente para ti:<br/>"
         "📊 Control de Inventario<br/>"
         "📊 Dashboard Financiero<br/>"
         "📊 Control de Ventas con IGV<br/><br/>"
         "Todo adaptado a productos de bodega.<br/><br/>"
         "💰 Solo S/6 por todo el pack<br/><br/>"
         "¿Te gustaría ver el catálogo? 🏪"),
        
        ("Para Restaurantes:",
         "Hola [NOMBRE] 👋<br/><br/>"
         "¿Tienes un restaurante?<br/><br/>"
         "Tenemos plantillas para tu negocio:<br/>"
         "📊 Control de Ventas diario<br/>"
         "📊 Inventario de ingredientes<br/>"
         "📊 Flujo de Caja mensual<br/><br/>"
         "Todo con fórmulas automáticas.<br/><br/>"
         "💰 Solo S/6 por todo el pack<br/><br/>"
         "¿Te gustaría acceder? 🍽️"),
        
        ("Para Farmacias:",
         "Hola [NOMBRE] 👋<br/><br/>"
         "¿Tienes una farmacia?<br/><br/>"
         "Tenemos plantillas para tu negocio:<br/>"
         "📊 Control de Inventario<br/>"
         "📊 Dashboard Financiero<br/>"
         "📊 Planilla de Personal<br/><br/>"
         "Todo adaptado a farmacias.<br/><br/>"
         "💰 Solo S/6 por todo el pack<br/><br/>"
         "¿Te gustaría verlas? 💊"),
    ]
    
    for title, script in rubro_scripts:
        story.append(create_script_box(title, script))
        story.append(Spacer(1, 5*mm))
    
    story.append(PageBreak())

def build_module4(story):
    """Módulo 4: Automatización"""
    # Portada del módulo
    story.append(Spacer(1, 40*mm))
    story.append(create_colored_box("MÓDULO 4", TEAL, 170*mm))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("AUTOMATIZACIÓN Y HERRAMIENTAS", 
                          ParagraphStyle('Mod4Title', parent=module_title, 
                                        fontSize=24, textColor=PURPLE_DARK)))
    story.append(Paragraph("Trabaja menos, vende más", 
                          ParagraphStyle('Mod4Sub', parent=body_style, 
                                        fontSize=14, alignment=TA_CENTER, textColor=GRAY)))
    story.append(PageBreak())
    
    # Contenido
    story.append(Paragraph("4.1 Catálogo de WhatsApp Business", subtitle_style))
    story.append(Paragraph(
        "El catálogo es tu tienda dentro de WhatsApp. Los clientes pueden ver tus "
        "productos, precios y hacer pedidos sin salir del chat.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("Beneficios del catálogo:", section_title))
    
    catalog_benefits = [
        "Los clientes ven tus productos 24/7",
        "Pueden hacer pedidos directamente",
        "No necesitas enviar fotos de cada producto",
        "Se ve profesional y organizado",
        "Funciona como una mini tienda online",
    ]
    story.extend(create_numbered_list(catalog_benefits))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("4.2 Enlaces de Pago Directo", subtitle_style))
    story.append(Paragraph(
        "Facilita el pago a tus clientes con enlaces directos. "
        "Menos pasos = más ventas cerradas.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    
    payment_data = [
        ["Método", "Cómo crear enlace", "Ejemplo"],
        ["Yape", "Abre Yape → Cobrar → Copiar enlace", "yape.pe/qr/tunegocio"],
        ["Plin", "Abre Plin → Recibir → Compartir", "plin.com/tunegocio"],
        ["Transferencia", "Comparte tu número de cuenta", "BCP: 123-456-789"],
    ]
    
    pay_tbl = Table(payment_data, colWidths=[30*mm, 70*mm, 65*mm])
    pay_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TEAL),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, HexColor("#F0FFF0")]),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#D0D5DD")),
    ]))
    story.append(pay_tbl)
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("4.3 Estados de WhatsApp para Vender", subtitle_style))
    story.append(Paragraph(
        "Los estados son como publicaciones de Instagram dentro de WhatsApp. "
        "Úsalos para mostrar productos, ofertas y testimonios.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("Ideas de estados:", section_title))
    
    status_ideas = [
        "Foto de producto con precio",
        "Video corto mostrando el producto",
        "Testimonio de cliente satisfecho",
        "Oferta del día con urgencia",
        "Behind the scenes de tu negocio",
        "Pregunta interactiva (encuesta)",
    ]
    story.extend(create_numbered_list(status_ideas))
    
    story.append(Spacer(1, 5*mm))
    story.append(create_tip_box("Publica estados 2-3 veces al día. Mañana, tarde y noche para máxima visibilidad."))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("4.4 Listas de Difusión", subtitle_style))
    story.append(Paragraph(
        "Las listas de difusión te permiten enviar el mismo mensaje a múltiples "
        "contactos sin crear un grupo. Cada persona recibe el mensaje individualmente.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("Cómo crear una lista:", section_title))
    
    broadcast_steps = [
        "Abre WhatsApp → Menú (3 puntos)",
        "Toca 'Nueva difusión'",
        "Selecciona los contactos",
        "Escribe tu mensaje",
        "Envía",
    ]
    story.extend(create_numbered_list(broadcast_steps))
    
    story.append(Spacer(1, 5*mm))
    story.append(create_tip_box("Crea listas segmentadas: 'Clientes VIP', 'Ofertas especiales', 'Nuevos productos'."))
    
    story.append(PageBreak())

def build_module5(story):
    """Módulo 5: Casos Prácticos"""
    # Portada del módulo
    story.append(Spacer(1, 40*mm))
    story.append(create_colored_box("MÓDULO 5", ORANGE, 170*mm))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("CASOS PRÁCTICOS REALES", 
                          ParagraphStyle('Mod5Title', parent=module_title, 
                                        fontSize=24, textColor=PURPLE_DARK)))
    story.append(Paragraph("Aprende de negocios reales en Perú", 
                          ParagraphStyle('Mod5Sub', parent=body_style, 
                                        fontSize=14, alignment=TA_CENTER, textColor=GRAY)))
    story.append(PageBreak())
    
    # Contenido
    story.append(Paragraph("Caso 1: Bodega Don Pepe", subtitle_style))
    story.append(Paragraph(
        "<b>Situación:</b> Don Pepe tiene una bodega en Lima. Vendía solo a clientes "
        "que pasaban por su tienda. Quería aumentar sus ventas.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("Solución aplicada:", section_title))
    
    case1_solution = [
        "Configuró WhatsApp Business con catálogo de productos",
        "Agregó 20 productos más vendidos al catálogo",
        "Creó mensaje de bienvenida automático",
        "Compartió su número en el grupo del barrio",
        "Ofreció delivery gratis en un radio de 5 cuadras",
    ]
    story.extend(create_numbered_list(case1_solution))
    
    story.append(Spacer(1, 3*mm))
    
    results_data = [
        ["Resultado", "Antes", "Después"],
        ["Ventas diarias", "S/200", "S/450"],
        ["Clientes nuevos/mes", "5", "25"],
        ["Pedidos por WhatsApp", "0", "15/día"],
    ]
    
    results_tbl = Table(results_data, colWidths=[55*mm, 55*mm, 55*mm])
    results_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), GREEN),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, HexColor("#F0FFF0")]),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#D0D5DD")),
    ]))
    story.append(results_tbl)
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Caso 2: Restaurante La Sazón", subtitle_style))
    story.append(Paragraph(
        "<b>Situación:</b> María tiene un restaurante en Arequipa. Solo atendía "
        "comensales en el local. Quería ofrecer delivery.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("Solución aplicada:", section_title))
    
    case2_solution = [
        "Creó catálogo con fotos de los platos del día",
        "Configuró respuestas rápidas para pedidos",
        "Agregó enlace de Yape para pagos",
        "Publicaba estados con el menú del día",
        "Ofreció 10% descuento en primer pedido",
    ]
    story.extend(create_numbered_list(case2_solution))
    
    story.append(Spacer(1, 3*mm))
    
    results2_data = [
        ["Resultado", "Antes", "Después"],
        ["Pedidos diarios", "0", "20"],
        ["Ticket promedio", "S/15", "S/25"],
        ["Ingreso mensual", "S/9,000", "S/15,000"],
    ]
    
    results2_tbl = Table(results2_data, colWidths=[55*mm, 55*mm, 55*mm])
    results2_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), ORANGE),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, HexColor("#FFF5F0")]),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#D0D5DD")),
    ]))
    story.append(results2_tbl)
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Caso 3: Tienda de Ropa Online", subtitle_style))
    story.append(Paragraph(
        "<b>Situación:</b> Lucía vende ropa por Instagram. Recibía muchos mensajes "
        "pero no podía responder todos a tiempo.",
        body_style
    ))
    
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("Solución aplicada:", section_title))
    
    case3_solution = [
        "Configuró mensaje de bienvenida con catálogo",
        "Creó respuestas rápidas para preguntas frecuentes",
        "Usaba etiquetas para organizar clientes",
        "Hacía seguimiento a clientes interesados",
        "Publicaba estados con nuevos productos",
    ]
    story.extend(create_numbered_list(case3_solution))
    
    story.append(Spacer(1, 3*mm))
    
    results3_data = [
        ["Resultado", "Antes", "Después"],
        ["Tiempo de respuesta", "2 horas", "5 minutos"],
        ["Tasa de conversión", "10%", "35%"],
        ["Ventas mensuales", "S/3,000", "S/8,500"],
    ]
    
    results3_tbl = Table(results3_data, colWidths=[55*mm, 55*mm, 55*mm])
    results3_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PINK),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, HexColor("#FFF0F5")]),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#D0D5DD")),
    ]))
    story.append(results3_tbl)
    
    story.append(PageBreak())

def build_bonus_scripts(story):
    """Bonus: 50 Scripts de WhatsApp"""
    story.append(Spacer(1, 40*mm))
    story.append(create_colored_box("BONUS EXCLUSIVO", RED, 170*mm))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("50 SCRIPTS DE WHATSAPP LISTOS PARA USAR", 
                          ParagraphStyle('BonusTitle', parent=module_title, 
                                        fontSize=24, textColor=PURPLE_DARK)))
    story.append(Paragraph("Copia, pega y adapta a tu negocio", 
                          ParagraphStyle('BonusSub', parent=body_style, 
                                        fontSize=14, alignment=TA_CENTER, textColor=GRAY)))
    story.append(PageBreak())
    
    # Scripts organizados por categoría
    categories = [
        ("PRIMER CONTACTO", [
            "Hola [NOMBRE] 👋 Gracias por contactarnos. ¿En qué puedo ayudarte?",
            "Hola [NOMBRE] 👋 Vi tu consulta sobre [PRODUCTO]. ¿Te gustaría más información?",
            "Hola [NOMBRE] 👋 Bienvenido a [NEGOCIO]. ¿Qué buscas hoy?",
        ]),
        ("PRESENTACIÓN DE PRODUCTOS", [
            "📊 [PRODUCTO] - Precio: [PRECIO]. Incluye: [BENEFICIOS]. ¿Te interesa?",
            "Tenemos [PRODUCTO] disponible. Es ideal para [NECESIDAD]. ¿Quieres verlo?",
            "🆕 Nuevo producto: [NOMBRE]. Precio especial: [PRECIO]. ¿Te gustaría verlo?",
        ]),
        ("CIERRE DE VENTAS", [
            "Perfecto [NOMBRE] 🎉 Para confirmar tu pedido necesito: 1. Tu dirección 2. Método de pago",
            "¡Excelente decisión! ¿Prefieres pagar con Yape, Plin o transferencia?",
            "Listo [NOMBRE]. Tu pedido está confirmado. ¿Cuándo prefieres recibirlo?",
        ]),
        ("SEGUIMIENTO", [
            "Hola [NOMBRE] 👋 ¿Tuviste chance de revisar la información?",
            "Hola [NOMBRE] 👋 ¿Qué decidiste sobre [PRODUCTO]?",
            "Hola [NOMBRE] 👋 ¿Necesitas algo más para tomar tu decisión?",
        ]),
        ("AGRADECIMIENTO", [
            "¡Gracias por tu compra [NOMBRE]! 🎉 ¿Necesitas algo más?",
            "¡Gracias por confiar en nosotros! Si tienes dudas, estoy aquí.",
            "¡Gracias [NOMBRE]! Esperamos verte pronto de nuevo 😊",
        ]),
    ]
    
    for cat_title, scripts in categories:
        story.append(Paragraph(f"📱 {cat_title}", section_title))
        for i, script in enumerate(scripts, 1):
            story.append(create_script_box(f"Script {i}", script))
            story.append(Spacer(1, 3*mm))
        story.append(Spacer(1, 5*mm))
    
    story.append(PageBreak())

def build_bonus_checklist(story):
    """Bonus: Checklist de Configuración"""
    story.append(Spacer(1, 40*mm))
    story.append(create_colored_box("BONUS EXCLUSIVO", GREEN, 170*mm))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("CHECKLIST DE CONFIGURACIÓN", 
                          ParagraphStyle('CheckTitle', parent=module_title, 
                                        fontSize=24, textColor=PURPLE_DARK)))
    story.append(Paragraph("Marca cada paso cuando lo completes", 
                          ParagraphStyle('CheckSub', parent=body_style, 
                                        fontSize=14, alignment=TA_CENTER, textColor=GRAY)))
    story.append(PageBreak())
    
    # Checklist
    story.append(Paragraph("✅ CONFIGURACIÓN BÁSICA", subtitle_style))
    
    basic_checks = [
        "Descargar WhatsApp Business",
        "Crear perfil profesional completo",
        "Agregar foto de logo profesional",
        "Escribir descripción del negocio",
        "Configurar horario de atención",
        "Agregar dirección del negocio",
    ]
    story.extend(create_checklist(basic_checks))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("✅ CATÁLOGO DE PRODUCTOS", subtitle_style))
    
    catalog_checks = [
        "Agregar primeros 10 productos",
        "Subir fotos de calidad",
        "Escribir descripciones claras",
        "Poner precios actualizados",
        "Organizar por categorías",
    ]
    story.extend(create_checklist(catalog_checks))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("✅ AUTOMATIZACIÓN", subtitle_style))
    
    auto_checks = [
        "Configurar mensaje de bienvenida",
        "Crear respuestas rápidas (mínimo 5)",
        "Configurar mensaje de ausencia",
        "Crear etiquetas de clientes",
    ]
    story.extend(create_checklist(auto_checks))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("✅ MÉTODOS DE PAGO", subtitle_style))
    
    payment_checks = [
        "Configurar Yape",
        "Configurar Plin",
        "Preparar datos de transferencia",
        "Crear enlaces de pago directo",
    ]
    story.extend(create_checklist(payment_checks))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("✅ PRIMERAS VENTAS", subtitle_style))
    
    sales_checks = [
        "Compartir número en redes sociales",
        "Enviar primeros mensajes de contacto",
        "Publicar primer estado con productos",
        "Hacer seguimiento a clientes interesados",
        "Cerrar primera venta",
    ]
    story.extend(create_checklist(sales_checks))
    
    story.append(Spacer(1, 15*mm))
    story.append(create_colored_box(
        "🎉 ¡FELICIDADES! Has completado la configuración de WhatsApp Business para tu negocio 🎉",
        GREEN
    ))

# ══════════════════════════════════════════════════════════════
# GENERAR PDF
# ══════════════════════════════════════════════════════════════

def generate_pdf():
    """Genera el PDF completo del curso"""
    output_path = "Curso_Ventas_WhatsApp_Business.pdf"
    
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=15*mm,
        rightMargin=15*mm,
        topMargin=25*mm,
        bottomMargin=20*mm,
        title="Curso Ventas por WhatsApp Business",
        author="Plantillas Excel Perú",
    )
    
    story = []
    
    # Construir el PDF
    build_cover(story)
    build_toc(story)
    build_module1(story)
    build_module2(story)
    build_module3(story)
    build_module4(story)
    build_module5(story)
    build_bonus_scripts(story)
    build_bonus_checklist(story)
    
    # Página final
    story.append(Spacer(1, 50*mm))
    story.append(create_colored_box("¡GRACIAS POR COMPRAR EL CURSO! 🎉", PURPLE, 170*mm))
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
    
    # Construir con header/footer
    doc.build(story, onFirstPage=draw_header_footer, onLaterPages=draw_header_footer)
    
    print(f"✅ PDF generado: {output_path}")
    print(f"📄 Tamaño: {os.path.getsize(output_path) / 1024:.1f} KB")
    
    return output_path

if __name__ == "__main__":
    generate_pdf()
