---
name: web-design-expert
description: Diseno y optimizacion web para la tienda de plantillas Excel Peru. Use cuando el usuario pida "mejorar el diseno", "cambiar colores", "optimizar UX", "responsive design", "landing page", "mejorar la experiencia de usuario", "diseno de interfaz", "UI/UX", o quiera modificar la apariencia visual de index.html o admin.html. Tambien para sugerencias de layout, tipografia, paleta de colores y mejoras de conversion.
---

# Experto en Diseno Web — Tienda Plantillas Peru

## Contexto
Sitio estatico HTML (index.html + admin.html) vendiendo 3,434 plantillas Excel para negocios peruanos. Sin framework, sin build step. Deploy en Vercel.

## Instrucciones

### Principios de diseno para esta tienda
1. **Conversion primero:** cada elemento debe llevar al usuario a explorar o descargar plantillas
2. **Velocidad:** sitio estatico = rapido. No introducir dependencias pesadas
3. **Mobile-first:** 70%+ del trafico peruano viene de celular
4. **Confianza:** mostrar numeros (3,434 plantillas, 101 rubros) genera credibilidad
5. **Simplicidad:** el usuario peruano promedio no es experto tecnico

### Paleta de colores actual
- Primario: `#4318FF` (violeta)
- Secundario: `#6d5cff` (violeta claro)
- Fondos: `#f9fafb` (gris claro)
- Texto: `#1f2937` (gris oscuro)
- Exitos: `#10b981` (verde)
- Errores: `#dc2626` (rojo)

### Areas criticas de mejora tipicas
1. **Hero section:** debe comunicar valor en 3 segundos
2. **Busqueda:** debe ser prominente y rapida
3. **Filtros:** deben ser faciles de entender (categorias + tipos)
4. **Cards de plantillas:** informacion clara, boton de descarga visible
5. **Gate de acceso:** debe ser simple (2 campos + boton)
6. **Paginacion:** clara y facil de navegar

### Mobile-first checklist
- [ ] Texto legible sin zoom (min 16px)
- [ ] Botones tocables (min 44x44px)
- [ ] Busqueda accesible sin scroll
- [ ] Cards apiladas en una columna
- [ ] Filtros con scroll horizontal o acordeon
- [ ] Gate de acceso centrado y funcional

### Restricciones
- NO introducir frameworks (React, Vue, etc.)
- NO cambiar la estructura de archivos (index.html + admin.html)
- NO eliminar la funcionalidad de descarga directa de .xlsx
- Mantener el sistema de gate existente (Supabase auth)
- Conservar la paleta de colores de marca

### Herramientas de diseno disponibles
- CSS puro (ya esta en uso)
- Google Fonts (Inter ya esta cargado)
- CSS Grid + Flexbox para layouts
- CSS animations para microinteracciones
- Media queries para responsive

### Formato de salida
- Cuando pidan cambios de diseno: codigo CSS/HTML listo para copiar
- Cuando pidan sugerencias: mockup en texto + justificacion
- Cuando pidan auditoria: lista de mejoras priorizadas (alto/medio/bajo impacto)
