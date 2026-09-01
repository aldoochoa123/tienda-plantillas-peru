"""
Script de migración: Reemplaza plantillas actuales por las nuevas v2
"""

import os
import json
import shutil
import re
from pathlib import Path

BASE = Path(r"C:\Users\golde\Documents\tienda-plantillas-peru")
PLANTILLAS_OLD = BASE / "plantillas"
PLANTILLAS_NEW = BASE / "plantillas-3200"
BACKUP_DIR = BASE / "plantillas-viejas"
INDEX_HTML = BASE / "index.html"

# Mapeo de carpetas a categorías
FOLDER_TO_CAT = {
    "Alimentos_y_Bebidas": "Alimentos y Bebidas",
    "Comercio_y_Retail": "Comercio y Retail",
    "Servicios": "Servicios",
    "Salud_y_Bienestar": "Salud y Bienestar",
    "Educacion": "Educación",
    "Transporte_y_Logistica": "Transporte y Logística",
    "Construccion_e_Industria": "Construcción e Industria",
    "Entretenimiento": "Entretenimiento",
    "Profesionales": "Profesionales",
}

# Iconos por categoría
CAT_ICONS = {
    "Alimentos y Bebidas": ("🍽️", "#ef4444"),
    "Comercio y Retail": ("🏪", "#f59e0b"),
    "Servicios": ("⚡", "#3b82f6"),
    "Salud y Bienestar": ("🏥", "#10b981"),
    "Educación": ("📚", "#8b5cf6"),
    "Transporte y Logística": ("🚚", "#f97316"),
    "Construcción e Industria": ("🏗️", "#6b7280"),
    "Entretenimiento": ("🎉", "#ec4899"),
    "Profesionales": ("💼", "#06b6d4"),
}

# Iconos por tipo de plantilla
TYPE_ICONS = {
    "Dashboard": "📊", "Control de Ventas": "💰", "Control de Inventario": "📦",
    "Presupuesto": "📅", "Flujo de Caja": "💵", "Gestion de Proyectos": "📋",
    "Control de Gastos": "🧾", "Planilla de Personal": "👥", "Cuentas por Cobrar": "📑",
    "Caja Diaria": "🏧", "Compras": "🛒", "Balance": "⚖️",
    "Estado de Resultados": "📈", "Flujo de Efectivo": "💹",
    "Conciliacion": "🏦", "Libro Diario": "📒", "Ratios": "📐",
    "Control Tributario": "🏛️", "Presupuesto Centros": "🏭",
    "Activos Fijos": "🔧", "Punto de Equilibrio": "⚖️",
    "Estados Comparativos": "📊", "Costeo": "🔨",
    "Calculadora CTS": "🧮", "Calculadora Gratificaciones": "🎁",
    "Cuadro de Amortizacion": "💳", "Calculadora Vacaciones": "🏖️",
    "Calculadora AFP": "👴", "Calculadora Nomina": "📄",
    "Calculadora ROI": "📈", "Calculadora IPC": "📊",
    "Capacidad Endeudamiento": "💳", "Proyeccion": "💹",
    "Analisis de KPIs": "🎯",
}

# Mapeo de patrones de filename a tipos de plantilla
FILENAME_TO_TYPE = {
    "Dashboard-Financiero": "Dashboard Financiero",
    "Control-Ventas": "Control de Ventas",
    "Control-Inventario": "Control de Inventario",
    "Presupuesto-Anual": "Presupuesto Anual",
    "Flujo-Caja": "Flujo de Caja",
    "Gestion-Proyectos": "Gestión de Proyectos",
    "Control-Gastos": "Control de Gastos",
    "Planilla-Personal": "Planilla de Personal",
    "Cuentas-Cobrar": "Cuentas por Cobrar",
    "Caja-Diaria": "Caja Diaria",
    "Compras-y-Proveedores": "Compras y Proveedores",
    "Balance-General": "Balance General",
    "Estado-de-Resultados": "Estado de Resultados",
    "Flujo-de-Efectivo-Indirecto": "Flujo de Efectivo Indirecto",
    "Conciliacion-Bancaria": "Conciliación Bancaria",
    "Libro-Diario-y-Mayor": "Libro Diario y Mayor",
    "Ratios-Financieros": "Ratios Financieros",
    "Control-Tributario": "Control Tributario",
    "Presupuesto-Centros-de-Costo": "Presupuesto Centros de Costo",
    "Activos-Fijos-y-Depreciacion": "Activos Fijos y Depreciación",
    "Punto-de-Equilibrio": "Punto de Equilibrio",
    "Estados-Comparativos-3-Anos": "Estados Comparativos 3 Años",
    "Costeo-por-Ordenes-de-Trabajo": "Costeo porÓrdenes de Trabajo",
    "Calculadora-CTS": "Calculadora CTS",
    "Calculadora-Gratificaciones": "Calculadora Gratificaciones",
    "Cuadro-de-Amortizacion": "Cuadro de Amortización",
    "Calculadora-Vacaciones": "Calculadora Vacaciones",
    "Calculadora-AFP-ONP": "Calculadora AFP/ONP",
    "Calculadora-Nomina": "Calculadora Nómina",
    "Calculadora-ROI": "Calculadora ROI",
    "Calculadora-IPC": "Calculadora IPC",
    "Capacidad-Endeudamiento": "Capacidad Endeudamiento",
    "Proyeccion-Flujo-de-Caja": "Proyección Flujo de Caja",
    "Analisis-de-KPIs": "Análisis de KPIs",
}

def get_type_from_filename(filename):
    """Extrae el tipo de plantilla del nombre del archivo"""
    name = filename.replace(".xlsx", "")
    # Remover el número inicial
    parts = name.split("-", 1)
    if len(parts) > 1 and parts[0].isdigit():
        name = parts[1]
    
    # Buscar coincidencia en el mapeo
    for pattern, template_type in FILENAME_TO_TYPE.items():
        if name.startswith(pattern):
            return template_type
    
    # Si no encuentra coincidencia, intentar extraer el tipo
    # El tipo es todo excepto la última parte (que es el rubro)
    parts = name.split("-")
    if len(parts) >= 2:
        # Remover la última parte (rubro) y unir el resto
        type_parts = parts[:-1]
        name = "-".join(type_parts)
    # Reemplazar guiones por espacios para mejor legibilidad
    name = name.replace("-", " ")
    return name

def get_rubro_from_filename(filename):
    """Extrae el rubro del nombre del archivo"""
    name = filename.replace(".xlsx", "")
    parts = name.split("-", 1)
    if len(parts) > 1 and parts[0].isdigit():
        name = parts[1]
    # El rubro es la última parte después del último guión
    parts = name.split("-")
    if len(parts) >= 2:
        return parts[-1]
    return ""

def get_icon_and_color(template_type, categoria):
    """Obtiene icono y color para un tipo de plantilla"""
    # Buscar icono por tipo
    icon = "📊"
    for key, val in TYPE_ICONS.items():
        if key.lower() in template_type.lower():
            icon = val
            break
    
    # Color por categoría
    _, color = CAT_ICONS.get(categoria, ("📊", "#6b7280"))
    return icon, color

def scan_new_templates():
    """Escanea las nuevas plantillas y genera el array TEMPLATES"""
    templates = []
    
    for folder_name, categoria in FOLDER_TO_CAT.items():
        folder = PLANTILLAS_NEW / folder_name
        if not folder.exists():
            continue
        
        for filename in sorted(os.listdir(folder)):
            if not filename.endswith(".xlsx"):
                continue
            
            filepath = f"{folder_name}/{filename}"
            template_type = get_type_from_filename(filename)
            rubro = get_rubro_from_filename(filename)
            icon, color = get_icon_and_color(template_type, categoria)
            
            # Productos genéricos por rubro
            productos = f"Producto 1 | Producto 2 | Producto 3 | Producto 4"
            
            templates.append({
                "archivo": filepath,
                "plantilla": template_type,
                "rubro": rubro,
                "categoria": categoria,
                "productos": productos,
                "icono": icon,
                "color": color,
            })
    
    return templates

def count_by_category(templates):
    """Cuenta plantillas por categoría"""
    counts = {}
    for t in templates:
        cat = t["categoria"]
        counts[cat] = counts.get(cat, 0) + 1
    return counts

def count_by_type(templates):
    """Cuenta plantillas por tipo"""
    counts = {}
    for t in templates:
        tt = t["plantilla"]
        counts[tt] = counts.get(tt, 0) + 1
    return counts

def update_index_html(templates):
    """Actualiza el archivo index.html con los nuevos datos"""
    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Generar nuevo array TEMPLATES
    templates_json = json.dumps(templates, ensure_ascii=False, indent=0)
    
    # Reemplazar el array existente
    pattern = r'const TEMPLATES = \[.*?\];'
    new_content = re.sub(pattern, f'const TEMPLATES = {templates_json};', content, flags=re.DOTALL)
    
    # Actualizar contadores de categorías
    cat_counts = count_by_category(templates)
    for cat, count in cat_counts.items():
        # Buscar el chip de categoría y actualizar el count
        pattern = rf'(data-cat="{cat}">[^<]*<span class="count">)\d+(</span>)'
        new_content = re.sub(pattern, rf'\g<1>{count}\2', new_content)
    
    # Actualizar contador total
    total = len(templates)
    new_content = re.sub(r'<span class="result-count"[^>]*>\d+[,.]?\d* plantillas</span>', 
                        f'<span class="result-count" id="resultCount">{total:,} plantillas</span>', 
                        new_content)
    
    # Actualizar "Mostrando X de Y"
    new_content = re.sub(r'Mostrando <strong>\d+</strong> de <strong>\d+[,.]?\d*</strong>',
                        f'Mostrando <strong>60</strong> de <strong>{total:,}</strong>',
                        new_content)
    
    # Actualizar stats del hero
    new_content = re.sub(r'<span class="hero-stat-num">\d+[,.]?\d*</span><span class="hero-stat-label">Plantillas</span>',
                        f'<span class="hero-stat-num">{total:,}</span><span class="hero-stat-label">Plantillas</span>',
                        new_content)
    
    with open(INDEX_HTML, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    return total

def main():
    print("=" * 60)
    print("MIGRACIÓN DE PLANTILLAS")
    print("=" * 60)
    
    # 1. Backup
    print("\n[1/4] Creando backup de plantillas actuales...")
    if PLANTILLAS_OLD.exists():
        if BACKUP_DIR.exists():
            shutil.rmtree(BACKUP_DIR)
        shutil.copytree(PLANTILLAS_OLD, BACKUP_DIR)
        print(f"  ✅ Backup en: {BACKUP_DIR}")
    else:
        print("  ⚠️ No existe carpeta plantillas/ actual")
    
    # 2. Reemplazar
    print("\n[2/4] Reemplazando plantillas...")
    if PLANTILLAS_OLD.exists():
        shutil.rmtree(PLANTILLAS_OLD)
    shutil.copytree(PLANTILLAS_NEW, PLANTILLAS_OLD)
    
    # Contar archivos
    total_files = sum(1 for _, _, files in os.walk(PLANTILLAS_OLD) for f in files if f.endswith('.xlsx'))
    print(f"  ✅ {total_files} plantillas copiadas a plantillas/")
    
    # 3. Actualizar index.html
    print("\n[3/4] Actualizando index.html...")
    templates = scan_new_templates()
    total = update_index_html(templates)
    print(f"  ✅ Array TEMPLATES actualizado: {total} registros")
    
    # Mostrar resumen por categoría
    cat_counts = count_by_category(templates)
    print("\n  Categorías:")
    for cat, count in sorted(cat_counts.items()):
        print(f"    • {cat}: {count}")
    
    # 4. Resumen
    print("\n[4/4] Resumen")
    print(f"  • Plantillas anteriores: respaldadas en plantillas-viejas/")
    print(f"  • Plantillas nuevas: {total} en plantillas/")
    print(f"  • index.html: actualizado")
    
    print("\n" + "=" * 60)
    print("✅ MIGRACIÓN COMPLETADA")
    print("=" * 60)
    print("\nPróximos pasos:")
    print("  1. Abre index.html en el navegador para verificar")
    print("  2. Prueba la búsqueda y los filtros")
    print("  3. Prueba descargar una plantilla")
    print("  4. Si todo está bien, puedes eliminar plantillas-viejas/")

if __name__ == "__main__":
    main()
