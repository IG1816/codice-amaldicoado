"""Gera um PDF de ficha no estilo simples do projeto a partir de um HTML.

Uso:
    python gerar_pdf.py ficha.html Ficha_Final.pdf

Requer: pip install pymupdf
"""
import os
import shutil
import sys
import tempfile

import pymupdf

CSS = """
* { font-family: sans-serif; }
body { font-size: 10pt; color: #111; line-height: 1.3; }
h1 { font-size: 18pt; margin-bottom: 0; }
.sub { color: #444; font-size: 9.5pt; margin-top: 2pt; margin-bottom: 8pt; }
h2 { font-size: 12.5pt; margin-top: 12pt; margin-bottom: 4pt; border-bottom: 1px solid #888; }
h3 { font-size: 11pt; margin-top: 8pt; margin-bottom: 3pt; }
table { border-collapse: collapse; width: 100%; margin-bottom: 5pt; }
th { font-weight: bold; font-size: 9pt; padding: 2pt 3pt; border: 1px solid #999; text-align: left; }
td { font-size: 9pt; padding: 2pt 3pt; border: 1px solid #999; }
.nota { font-size: 8.5pt; color: #333; margin-top: 2pt; }
ul, ol { margin-top: 2pt; margin-bottom: 4pt; }
li { margin-bottom: 1pt; }
"""


def gerar(html_path: str, saida: str, previa: bool = True) -> int:
    html = open(html_path, encoding="utf-8").read()
    tmpdir = tempfile.mkdtemp()
    bruto = os.path.join(tmpdir, "bruto.pdf")
    final = os.path.join(tmpdir, "final.pdf")

    story = pymupdf.Story(html=html, user_css=CSS)
    writer = pymupdf.DocumentWriter(bruto)
    pagina = pymupdf.paper_rect("a4")
    area = pagina + (45, 45, -45, -45)
    mais = 1
    while mais:
        dev = writer.begin_page(pagina)
        mais, _ = story.place(area)
        story.draw(dev)
        writer.end_page()
    writer.close()

    doc = pymupdf.open(bruto)
    total = len(doc)
    for i, pg in enumerate(doc):
        pg.insert_text((pagina.width - 70, pagina.height - 22), f"{i + 1}/{total}",
                       fontsize=8, color=(0.4, 0.4, 0.4))
    doc.set_metadata({})  # sem autor, sem programa
    doc.save(final)
    if previa:  # olhe uma página antes de mandar
        doc[0].get_pixmap(dpi=60).save(os.path.splitext(saida)[0] + "_previa.png")
    doc.close()

    # copiar em vez de salvar direto: no Windows o PDF aberto trava a sobrescrita
    shutil.copyfile(final, saida)
    return total


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("uso: python gerar_pdf.py entrada.html saida.pdf")
    print(gerar(sys.argv[1], sys.argv[2]), "páginas")
