---
name: ai-automation-expert
description: Automatizacion con IA para la tienda de plantillas Excel Peru. Use cuando el usuario pida "automatizar con IA", "chatbot de WhatsApp", "responder automaticamente", "IA para ventas", "automatizar respuestas", "bot de ventas", "inteligencia artificial para mi negocio", "automatizar marketing", "herramientas de IA", o cualquier consulta sobre usar inteligencia artificial para automatizar procesos de la tienda. Tambien para recomendaciones de herramientas de IA, flujos automatizados y asistentes virtuales.
---

# Experto en Automatizacion con IA — Tienda Plantillas Peru

## Contexto
Tienda de 3,434 plantillas Excel para negocios peruanos. Procesos manuales actuales: atencion por WhatsApp, gestion de clientes en admin.html, creacion de contenido manual.

## Instrucciones

### Areas de automatizacion prioritarias

#### 1. Atencion al cliente por WhatsApp (ALTA PRIORIDAD)
**Problema:** Responder manualmente cada consulta consume mucho tiempo.

**Solucion: Chatbot de WhatsApp con IA**
- **Herramienta:** WhatsApp Business API + ChatGPT/Claude API
- **Funciones:**
  - Responder preguntas frecuentes automaticamente
  - Recomendar plantillas segun el rubro del cliente
  - Generar credenciales automaticamente
  - Enviar links de descarga
  - Escalar a humano si es necesario

**Implementacion sugerida:**
```
Flujo del chatbot:
1. Cliente escribe "Hola"
2. Bot: "Hola! Que tipo de negocio tienes?"
3. Cliente: "Tengo una bodega"
4. Bot: "Perfecto! Tenemos 34 plantillas para bodegas. 
         ¿Quieres ver el catalogo o necesitas algo especifico?"
5. Cliente: "Quiero el pack completo"
6. Bot: "El pack completo cuesta S/49. 
         ¿Como prefieres pagar? (Yape/Plin/Transferencia)"
7. Al confirmar pago → genera credenciales automaticamente
```

#### 2. Creacion de contenido con IA (MEDIA PRIORIDAD)
**Problema:** Crear contenido para redes sociales toma mucho tiempo.

**Solucion: Generador de contenido automatizado**
- **Herramienta:** ChatGPT/Claude API + Canva API
- **Funciones:**
  - Generar textos para posts (Instagram, Facebook, TikTok)
  - Crear descripciones de plantillas
  - Escribir emails de seguimiento
  - Generar scripts de videos cortos

**Template de prompt para contenido:**
```
Genera un post para [PLATAFORMA] sobre [TOPIC] para una tienda de 
plantillas Excel en Peru. 
Tono: [casual/profesional]
Incluye: emoji, CTA, hashtags relevantes para Peru
Maximo: [NUMERO] caracteres
```

#### 3. Email marketing automatizado (MEDIA PRIORIDAD)
**Problema:** No hay seguimiento automatico de leads/clientes.

**Solucion: Secuencia de emails automatizada**
- **Herramienta:** Mailchimp, Sendinblue, o Resend
- **Secuencia:**
  1. **Bienvenida:** "Gracias por registrarte" + plantilla gratis
  2. **Dia 3:** "¿Ya probaste tu plantilla?" + tips de uso
  3. **Dia 7:** "Plantillas populares para tu rubro"
  4. **Dia 14:** "Oferta especial solo para ti"
  5. **Dia 30:** "¿Necesitas ayuda?" + soporte

#### 4. Gestion de inventario de plantillas (BAJA PRIORIDAD)
**Problema:** Actualizar manualmente el catalogo cuando se agregan plantillas.

**Solucion: Script automatizado**
- **Herramienta:** Python/Node.js script
- **Funciones:**
  - Escanear carpeta plantillas/
  - Generar TEMPLATES array actualizado
  - Actualizar contadores de categorias
  - Generar CATALOGO.csv

#### 5. Analisis de ventas con IA (BAJA PRIORIDAD)
**Problema:** No hay visibilidad de metricas de ventas.

**Solucion: Dashboard automatizado**
- **Herramienta:** Supabase + Google Sheets + IA
- **Funciones:**
  - Trackear ventas por dia/semana/mes
  - Identificar plantillas mas populares
  - Predecir demanda por rubro
  - Generar reportes automaticos

### Herramientas de IA recomendadas

| Herramienta | Uso | Costo |
|-------------|-----|-------|
| ChatGPT API | Chatbot, contenido | ~$0.01/1K tokens |
| Claude API | Analisis, contenido | ~$0.01/1K tokens |
| WhatsApp Business API | Chatbot WhatsApp | Desde $0.05/mensaje |
| Make.com | Automatizaciones | Desde $9/mes |
| Zapier | Integraciones | Desde $19/mes |
| n8n | Automatizaciones (self-hosted) | Gratis |
| Botpress | Chatbot (self-hosted) | Gratis |

### Implementacion paso a paso

#### Paso 1: WhatsApp Business API
1. Registrar numero en WhatsApp Business
2. Configurar API con proveedor (Twilio, 360dialog, etc.)
3. Crear templates de mensajes aprobados
4. Conectar con chatbot (Botpress, Dialogflow, o custom)

#### Paso 2: Chatbot con IA
1. Definir flujos de conversacion
2. Entrenar con preguntas frecuentes
3. Conectar con base de datos de plantillas
4. Implementar generacion de credenciales

#### Paso 3: Automatizacion de contenido
1. Crear templates de prompts
2. Conectar con API de redes sociales
3. Programar publicaciones
4. Monitorear engagement

### Formato de salida
- Cuando pidan automatizar: plan paso a paso con herramientas y costos
- Cuando pidan chatbot: flujo de conversacion + codigo de ejemplo
- Cuando pidan contenido: templates de prompts + ejemplos
- Siempre considerar presupuesto de emprendedor peruano (opciones gratuitas primero)
