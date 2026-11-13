"""Rebuild the standalone HTML without any runtime network dependencies."""
import base64
from pathlib import Path

root = Path(__file__).resolve().parent
html = (root / 'page.html').read_text()
library = (root / 'three.min.js').read_text().replace('</script', '<\\/script')
atlas = base64.b64encode((root / 'expressions.png').read_bytes()).decode()
original = base64.b64encode((root / 'portrait.jpg').read_bytes()).decode()
html = html.replace('/*__THREE__*/', library)
html = html.replace('__ATLAS__', 'data:image/png;base64,' + atlas)
html = html.replace('__ORIGINAL__', 'data:image/jpeg;base64,' + original)
(root / 'index.html').write_text(html)
print(f'Built {root / "index.html"} ({len(html):,} characters)')
