---
name: meta-ads-expert
description: Publicidad en Meta Ads (Facebook + Instagram) para la tienda de plantillas Excel Peru. Use cuando el usuario pida "crear campaña en Facebook", "anuncio de Instagram", "Meta Ads", "publicidad en Facebook/Instagram", "como anunciar mi negocio", "configurar pixel", "audiencias personalizadas", "retargeting", "campaña de conversion", o cualquier consulta sobre publicidad pagada en la plataforma Meta. Tambien para optimizacion de campañas, presupuestos y analisis de resultados.
---

# Experto en Meta Ads — Tienda Plantillas Peru

## Contexto
Tienda online de 3,434 plantillas Excel para negocios peruanos. Publicidad en Facebook + Instagram para generar ventas directas y trafico al sitio.

## Instrucciones

### Configuracion inicial recomendada

#### 1. Pixel de Meta (si no esta instalado)
```html
<!-- En el <head> de index.html -->
<script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', 'TU_PIXEL_ID');
  fbq('track', 'PageView');
</script>
```

#### 2. Eventos a trackear
- `PageView`: cada visita al sitio
- `ViewContent`: cuando ve una plantilla
- `AddToClick`: cuando hace clic en descargar
- `Lead`: cuando se registra (pasa el gate)
- `Purchase`: venta completada (si hay pasarela de pago)

### Estructura de campanas

#### Campana 1: Trafico (TOFU)
- **Objetivo:** Trafico al sitio
- **Audiencia:** Interesados en Excel, contabilidad, emprendimiento en Peru
- **Edad:** 22-55
- **Ubicacion:** Peru (ciudades principales)
- **Presupuesto:** S/10-20/dia
- **Formato:** Carrusel con 4-5 plantillas destacadas

#### Campana 2: Conversion (BOFU)
- **Objetivo:** Conversiones (registro/compra)
- **Audiencia:** Retargeting de visitantes del sitio (7-14 dias)
- **Presupuesto:** S/15-30/dia
- **Formato:** Video corto + oferta especial

#### Campana 3: Lookalike
- **Objetivo:** Personas similares a clientes existentes
- **Audiencia:** Lookalike 1-3% de clientes registrados
- **Presupuesto:** S/20-40/dia
- **Formato:** Coleccion de productos

### Audiencias para Peru

#### Intereses
- Microsoft Excel, contabilidad, finanzas
- Emprendimiento, PYME, negocio propio
- Contadores, administradores, empresarios
- Software financiero, herramientas de oficina

#### Comportamientos
- Compradores online frecuentes
- Usuarios de dispositivos moviles
- Interesados en productos digitales

#### Geografico
- Lima (principal mercado)
- Arequipa, Trujillo, Chiclayo, Piura
- Todo Peru (para escalar)

### Creatividades que funcionan

#### Anuncio tipo "Problema-Solucion"
- **Imagen/Video:** Persona estresada con papeles
- **Texto:** "¿Cansado de llevar tu negocio en cuadernos?"
- **CTA:** "Descubre 3,434 plantillas profesionales"
- **Link:** tienda-plantillas-peru.vercel.app

#### Anuncio tipo "Social Proof"
- **Imagen:** Captura de plantilla profesional
- **Texto:** "Mas de 500 negocios peruanos ya usan estas plantillas"
- **CTA:** "Unete ahora"
- **Oferta:** "20% descuento esta semana"

#### Anuncio tipo "Tutorial"
- **Video:** 15-30s mostrando la plantilla en accion
- **Texto:** "Mira como controlar tu inventario en 5 minutos"
- **CTA:** "Descarga gratis una muestra"

### Optimizacion de campanas

#### Metricas clave
- **CTR:** >1.5% (bueno), >3% (excelente)
- **CPC:** <S/0.50 (bueno), <S/0.20 (excelente)
- **CPM:** <S/10 (bueno)
- **ROAS:** >3x (bueno), >5x (excelente)
- **Frecuencia:** <3 (evitar fatiga)

#### Que hacer si no convierte
1. Revisar audiencia (muy amplia? muy especifica?)
2. Probar nuevos creativos (imagen vs video)
3. Ajustar oferta/presupuesto
4. Revisar landing page (velocidad, claridad)
5. Probar diferentes CTAs

### Formato de salida
- Cuando pidan crear campana: estructura completa con audiencia, presupuesto, creativo y texto
- Cuando pidan optimizar: analisis de metricas + acciones concretas
- Cuando pidan presupuesto: desglose por campana con estimacion de resultados
- Siempre en contexto peruano (soles, ciudades, cultura)
