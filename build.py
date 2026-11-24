# Junta src.html + web/*.webp num index.html único (abre em qualquer lugar, sem pasta de imagens).
import base64, pathlib, re, sys
root = pathlib.Path(__file__).parent
html = (root / "src.html").read_text()
def uri(name):
    f = root / "web" / f"{name}.webp"
    if not f.exists(): sys.exit(f"faltou imagem: {name}")
    return "data:image/webp;base64," + base64.b64encode(f.read_bytes()).decode()
out = re.sub(r"\{\{(\w+)\}\}", lambda m: uri(m.group(1)), html)
(root / "index.html").write_text(out)
print("ok", len(out) // 1024, "KB")
