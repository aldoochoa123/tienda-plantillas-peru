# AGENTS.md

## What this is

Static HTML site selling 3,434 Excel templates for Peruvian businesses. No framework, no build step, no backend. Two HTML files are the entire app.

## Architecture

- `index.html` — public catalog with search, filters, pagination, and download. Contains a password gate overlay.
- `admin.html` — client management panel (add/delete clients, generate credentials, send WhatsApp messages).
- `plantillas/` — 3,434 `.xlsx` files across 9 category folders. Files are downloaded directly via `fetch()` (no SheetJS — this is intentional to preserve Excel formatting, charts, and colors).
- `CATALOGO.csv` — flat catalog of all templates (source of truth for the data).
- `iniciar.bat` / `detener.bat` — Windows scripts to start/stop a local Python HTTP server on port 3000.

## Critical data flow

The `TEMPLATES` array in `index.html` (line ~346) is a **hardcoded JSON blob** with all 3,434 template metadata entries. This is NOT loaded from `CATALOGO.csv` at runtime — it's embedded inline. If you add/remove/rename template files, you must update BOTH:
1. The actual `.xlsx` files in `plantillas/`
2. The `TEMPLATES` array in `index.html`
3. `CATALOGO.csv` (for the downloadable catalog)
4. The filter chip counts in `index.html` (category and type counts are hardcoded in HTML)

## Auth system (client-side only)

- **No backend.** Auth is entirely in the browser via `localStorage`.
- Admin (`admin.html`) stores clients as `localStorage.clients` (JSON array).
- Catalog (`index.html`) reads the same `localStorage.clients` to validate login.
- Username = WhatsApp number (normalized: digits only, strip leading `51`).
- Password = auto-generated: `PE` + last 6 digits of phone. Compared uppercase.
- Session gate uses `sessionStorage.gate_ok` — survives page reload within tab, not across tabs.
- **Implication**: clients added in one browser/device are invisible in another. This is a known limitation, not a bug to fix casually.

## File naming convention

```
plantillas/{Categoria}/{NN}-{slug}-{Rubro}.xlsx
```
- `NN` = zero-padded sequence number (01-34)
- `slug` = kebab-case template type (e.g., `dashboard-financiero`, `control-ventas`)
- `Rubro` = PascalCase business type (e.g., `Bodega`, `Polleria`)
- Category folder names use spaces: `Alimentos y Bebidas`, `Comercio y Retail`

## Dev server

```bash
# Option 1: Python (what iniciar.bat uses)
python -m http.server 3000

# Option 2: Node (what package.json dev script uses)
npx serve . -l 3000
```

No hot reload, no transpilation. Edit HTML, refresh browser.

## Custom Skills (`.mimocode/skills/`)

15 business skills created for growth and marketing:
- `social-media-expert` — Estrategia de redes sociales
- `web-design-expert` — Diseno y UX del sitio
- `social-sales-design` — Graficos para vender en redes
- `digital-marketing-expert` — Marketing digital completo
- `meta-ads-expert` — Publicidad Facebook + Instagram
- `facebook-ads-expert` — Solo Facebook (grupos, pagina, ads)
- `online-sales-expert` — Tecnicas de venta online
- `ai-automation-expert` — Automatizacion con IA
- `hotmart-expert` — Vender productos digitales en Hotmart
- `curso-ventas-expert` — Estrategias para vender cursos online
- `cursos-online-expert` — Crear y producir cursos online
- `ia-expert` — Inteligencia artificial aplicada a negocios
- `whatsapp-business-expert` — WhatsApp Business para ventas
- `diseno-interiores-expert` — Diseno de interiores y melamina
- `diseno-web-apple-expert` — Diseno web estilo Apple premium

Invoke with `/skill-name`. All are Peru-market focused.

## What NOT to do

- Don't introduce a build system or bundler — the site is intentionally static for simple deployment (GitHub Pages, Netlify, etc.).
- Don't replace the direct `.xlsx` download with SheetJS — the whole point is preserving native Excel formatting.
- Don't move the `TEMPLATES` data out of `index.html` without updating the rendering logic that depends on it being a synchronous inline array.
- Don't hardcode real phone numbers or credentials — the WhatsApp link in the gate uses a placeholder (`51999999999`).
