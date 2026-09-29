# Códice Amaldiçoado

Skill de Claude sobre o RPG Feiticeiros & Maldições, do projeto D&D Pensamentos. A entrada é o `SKILL.md`, que aponta para `referencias/`, `prompts/` e `scripts/`.

## Ao editar a skill

- O `SKILL.md` fica curto: postura, fontes, roteador e checklist. Conteúdo novo vai para o arquivo certo em `referencias/`, e o roteador ganha uma linha se abrir um assunto novo.
- Número de regra vem com a página do livro. Sem certeza, diga o que falta confirmar.
- Se uma simulação desmentir algo registrado, corrija a referência e registre em `10-descobertas.md`.

## Verificar

- Mexeu em `scripts/simular_duelo.py`: rode `python scripts/simular_duelo.py` e confira que os resultados batem com `07-simulacao.md`.
- Mexeu em `scripts/gerar_pdf.py`: gere um PDF de teste (precisa do `pymupdf`).

## Como trabalhar

Para o trabalho de manutenção deste repositório, siga a skill `ia-playbook` (em `.claude/skills/`). Ela não faz parte do Códice.
