# Arte de divulgação · Aula "Como vender mais com os leads que você já tem"

Formato 1080x1350 (feed/Instagram retrato). Identidade BrandsDecoded: preto quente `#1A1410`,
off-white `#FAF8F4`, laranja `#FF4500`, Instrument Sans (display) e Inter (texto).

| Arquivo | O que é |
|---|---|
| `arte-aula-leads-lucas-brito-1080x1350.png` | Consultoria, versão escura (principal) |
| `arte-aula-leads-lucas-brito-1080x1350-clara.png` | Consultoria, fundo off-white |
| `arte-aula-leads-lucas-brito-blueprint-1080x1350.png` | Mentoria Blueprint, versão escura |
| `arte-aula-leads-lucas-brito-blueprint-1080x1350-clara.png` | Mentoria Blueprint, fundo off-white |
| `arte.html` | Fonte editável da arte (HTML/CSS) |
| `assets/lucas-brito-enhanced.png` | Foto original ampliada 2x e nitidez recuperada |
| `assets/lucas-brito-cutout.png` | Foto tratada com fundo removido (usada na arte) |
| `fonts/` | Instrument Sans e Inter (Google Fonts, licença OFL) |
| `render.py` | Renderiza o HTML em PNG via Playwright/Chromium |

## Como re-renderizar

```bash
pip install playwright
python3 render.py "$PWD/arte.html" saida.png dark Consultoria   # tema: dark|light · rótulo: Consultoria|Blueprint
```

O script usa o Chromium em `/opt/pw-browsers`; ajuste `executable_path` se o caminho for outro.
