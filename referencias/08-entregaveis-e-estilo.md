# 08 · Entregáveis e estilo

## Regra de ouro

O mestre da mesa **não gosta de IA**. Tudo que vai pra mesa tem que parecer escrito por um jogador:

- Sem mencionar IA, agente, auditoria, "eu inventei", "esta ficha foi gerada".
- Sem títulos em excesso, sem emoji, sem travessão, pouco negrito.
- Primeira pessoa quando for ficha de personagem ("levanto até 6 paredes", "Como eu jogo").
- Frases curtas, jeito de falar do jogador, vícios de linguagem mantidos quando ele pedir.
- Página do livro entre parênteses do lado da regra, **sem citação longa**.
- Sempre uma seção final **"Perguntar pro mestre"** com as leituras ambíguas e contradições do livro.
- PDF simples: preto e branco, borda fina, sem caixas coloridas, metadados apagados.

## Ficha de personagem (ordem)

1. Nome, subtítulo (nível, especialização, edição).
2. Personagem (2-4 linhas).
3. Atributos (tabela) + nota de onde saiu cada ponto.
4. Status: PV, PE, Defesa, CD, BT, RD, deslocamento, iniciativa + nota de cálculo.
5. TRs e perícias em uma linha cada.
6. Habilidades (tabela Nv / Habilidade / O que faz).
7. Aptidões.
8. Técnica: funcionamento básico em 2 linhas + tabela de feitiços (Nome, Nv, PE, Ação, Efeito).
9. "Como montei os feitiços" (a conta, curta).
10. Invocações / equipamento.
11. "Como eu jogo" (rotina de turno) + fraquezas.
12. Perguntar pro mestre.

## Versão de jogo (MD simples)

Quando o jogador pede "a ficha pra jogar": só números, ações, dano e custo. Nada de explicação.

## Lore

- Curta, em texto corrido, sem subtítulos quando ele pedir "só um texto".
- Deixar 2-3 ganchos soltos para o mestre usar.
- Não inventar fatos que contradigam o que o jogador contou; só arrumar pontuação quando ele pedir isso.

## PDF

`scripts/gerar_pdf.py` monta o PDF a partir de um HTML (PyMuPDF Story, A4, fonte sans, tabelas com borda cinza, número de página no rodapé).

- `th` com cor de fundo sai desalinhado no PyMuPDF: não usar.
- Quebra de página: `<h2 style="page-break-before: always">`.
- Gravar num rascunho e copiar com `shutil.copyfile` (o PDF aberto trava a sobrescrita no Windows).
- Olhar uma página renderizada em PNG antes de mandar.
