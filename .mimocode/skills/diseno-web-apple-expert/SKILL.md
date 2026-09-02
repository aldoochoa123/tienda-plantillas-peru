---
name: diseno-web-apple-expert
description: Experto en diseno web estilo Apple para sitios en Peru. Use cuando el usuario pregunte "diseno web Apple", "estilo Apple", "pagina web minimalista", "UI moderna", "diseno premium", "sitio web profesional", "landing page elegante", "diseno de interfaz", "UX premium", "estilo Cupertino", o cualquier consulta sobre crear o mejorar sitios web con el nivel de calidad, elegancia y experiencia de usuario de Apple. Tambien para rediseñar la tienda actual con este estilo.
---

# Experto en Diseno Web Apple — Tienda Plantillas Peru

## Contexto
El usuario tiene una tienda de plantillas Excel en Peru (tienda-plantillas-peru.vercel.app). Quiere que su sitio web tenga el nivel de diseno y experiencia de usuario de Apple: limpio, premium, elegante, facil de usar.

## Instrucciones

### 1. Principios del diseno Apple

**Los 5 pilares:**
1. **Simplicidad**: menos es mas. Eliminar todo lo que no sea esencial
2. **Espacio en blanco**: dejar respirar el contenido. Padding generoso
3. **Tipografia limpia**: San Francisco (system-ui), jerarquia clara
4. **Animaciones suaves**: transiciones de 0.3s, easing natural
5. **Foco en el producto**: el contenido es el heroe, no la interfaz

### 2. Paleta de colores estilo Apple (adaptada a la tienda)

**Base:**
```css
--bg-primary: #FFFFFF;
--bg-secondary: #F5F5F7;
--bg-tertiary: #FBFBFD;
--text-primary: #1D1D1F;
--text-secondary: #86868B;
--text-tertiary: #AEAEB2;
```

**Acentos (manteniendo el morado de la marca):**
```css
--accent: #3D0C8E;          /* Morado de la tienda */
--accent-light: #6B3FA0;    /* Morado claro */
--accent-hover: #2D0A6E;    /* Morado oscuro hover */
--accent-bg: #F3EEFF;       /* Fondo morado suave */
```

**Estados:**
```css
--success: #30D158;
--warning: #FFD60A;
--error: #FF453A;
--info: #0A84FF;
```

### 3. Tipografia Apple

**Escala tipografica:**
```css
/* Titulos */
.hero-title { font-size: 56px; font-weight: 700; letter-spacing: -0.025em; }
.section-title { font-size: 40px; font-weight: 600; letter-spacing: -0.02em; }
.card-title { font-size: 24px; font-weight: 600; }

/* Cuerpo */
.body-large { font-size: 21px; font-weight: 400; line-height: 1.5; }
.body-regular { font-size: 17px; font-weight: 400; line-height: 1.5; }
.body-small { font-size: 14px; font-weight: 400; line-height: 1.4; }

/* Caption */
.caption { font-size: 12px; font-weight: 400; color: var(--text-secondary); }
```

**Font stack:**
```css
font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 
             'SF Pro Text', 'Helvetica Neue', Arial, sans-serif;
```

### 4. Componentes estilo Apple

#### Botones
```css
.btn-primary {
  background: var(--accent);
  color: white;
  border: none;
  border-radius: 980px; /* Apple usa border-radius pill */
  padding: 12px 24px;
  font-size: 17px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}
.btn-primary:hover {
  background: var(--accent-hover);
  transform: scale(1.02);
}
```

#### Cards
```css
.card {
  background: white;
  border-radius: 20px;
  padding: 32px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 30px rgba(0,0,0,0.12);
}
```

#### Inputs
```css
.input {
  background: var(--bg-secondary);
  border: 1px solid transparent;
  border-radius: 12px;
  padding: 14px 16px;
  font-size: 17px;
  transition: all 0.2s ease;
}
.input:focus {
  border-color: var(--accent);
  background: white;
  box-shadow: 0 0 0 4px rgba(61, 12, 142, 0.1);
  outline: none;
}
```

### 5. Layout y espaciado Apple

**Grid system:**
```css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

/* Secciones con mucho espacio */
section {
  padding: 120px 0; /* Apple usa mucho espacio vertical */
}

/* Grid de productos */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
}
```

**Espaciado consistente:**
- Entre secciones: 100-120px
- Entre elementos: 24-32px
- Dentro de cards: 24-32px
- Padding de botones: 12-16px vertical, 24-32px horizontal

### 6. Animaciones Apple

**Transiciones base:**
```css
/* Easing Apple */
--ease-apple: cubic-bezier(0.25, 0.1, 0.25, 1);

/* Fade in */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Scroll reveal */
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.8s var(--ease-apple);
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

**Micro-interacciones:**
- Hover en cards: translateY(-4px) + shadow mas pronunciada
- Click en boton: scale(0.98) rapido, luego scale(1)
- Scroll: parallax suave en hero, fade-in en secciones
- Loading: spinner minimalista o skeleton screens

### 7. Secciones de la tienda (rediseño Apple)

#### Hero section
```
+------------------------------------------+
|                                          |
|    +3000 Plantillas Excel               |
|    para tu negocio en Peru              |
|                                          |
|    [Explorar Plantillas]  [Ver Precios] |
|                                          |
|    Mockup de plantillas flotando         |
|                                          |
+------------------------------------------+
```

#### Seccion de categorias
```
+------------------------------------------+
|  Categorias                              |
|                                          |
|  [Card 1] [Card 2] [Card 3]            |
|  [Card 4] [Card 5] [Card 6]            |
|                                          |
|  Cada card: icono + nombre + count       |
+------------------------------------------+
```

#### Seccion de producto destacado
```
+------------------------------------------+
|  [Imagen grande del producto]            |
|                                          |
|  Pack Completo                           |
|  +3000 plantillas profesionales          |
|  Solo S/6 c/u                            |
|                                          |
|  [Comprar Ahora]                         |
+------------------------------------------+
```

### 8. Responsive Apple

**Breakpoints:**
```css
/* Mobile first */
@media (min-width: 768px) { /* iPad */ }
@media (min-width: 1024px) { /* Desktop */ }
@media (min-width: 1440px) { /* Large desktop */ }
```

**Mobile:**
- Stack vertical, full-width cards
- Font sizes reducidos 20%
- Padding reducido a 16px
- Bottom navigation bar (estilo app)

### 9. Implementacion para la tienda actual

**Cambios prioritarios en index.html:**
1. Aplicar paleta de colores Apple + morado de marca
2. Rediseñar hero con tipografia grande y limpia
3. Cards de productos con border-radius 20px y hover suave
4. Espaciado generoso entre secciones
5. Animaciones de scroll reveal
6. Input de busqueda estilo Apple
7. Filtros con pills redondeados
8. Footer minimalista

**NO cambiar:**
- Estructura de datos (TEMPLATES array)
- Logica de descarga (.xlsx directo)
- Sistema de auth (Supabase)
- Funcionalidad existente

### Formato de salida
- Cuando pidan rediseño: CSS completo listo para aplicar
- Cuando pidan componentes: HTML + CSS con el estilo Apple
- Cuando pidan mejorar UX: recomendaciones especificas con codigo
- Siempre mantener la identidad de marca (#3D0C8E) con estetica Apple
