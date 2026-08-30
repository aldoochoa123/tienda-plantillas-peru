# E-commerce Tienda

Experto en e-commerce y gestión de tienda online. Usa esta skill cuando el usuario pida ayuda con la tienda web, mejoras de conversión, experiencia de usuario, gestión de productos, precios, o cualquier aspecto operativo de la tienda online.

## Contexto del proyecto

- Tienda estática en Vercel (HTML/CSS/JS)
- 3,434 plantillas Excel para negocios peruanos
- Autenticación con Supabase (base de datos en la nube)
- Venta directa por WhatsApp
- Sin carrito de compras (flujo: WhatsApp → credenciales → descarga)

## Arquitectura actual

```
Facebook Ad → WhatsApp → Vendedor → Credenciales → index.html → Descarga
```

## Mejoras de conversión recomendadas

### Landing page
- Hero con propuesta de valor clara
- Social proof (testimonios, cantidad de ventas)
- Preview de plantillas (screenshots)
- FAQ section
- Garantía de satisfacción
- CTA claro y visible

### Página de catálogo
- Búsqueda funcional (ya implementada)
- Filtros por categoría y tipo (ya implementado)
- Preview antes de descargar
- Contador de descargas por plantilla

### Post-compra
- Email de bienvenida con guía de uso
- Video tutorial de cómo usar las plantillas
- Programa de referidos

## Métricas clave

| Métrica | Fórmula | Objetivo |
|---------|---------|----------|
| Tasa de conversión | Ventas / Visitantes | > 2% |
| CAC | Gasto ads / Ventas | < S/ 15 |
| LTV | Compra promedio × Recompras | > S/ 50 |
| ROAS | Revenue / Gasto ads | > 3x |

## Directrices

- Priorizar cambios de alto impacto y bajo esfuerzo
- Medir antes y después de cada cambio
- Enfocarse en la experiencia móvil (mayoría de tráfico)
- Mantener la simplicidad (sitio estático = rápido)
