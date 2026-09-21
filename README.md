# Códice Amaldiçoado

Skill para o **Claude** sobre o RPG **Feiticeiros & Maldições** (Jujutsu Kaisen), feita no projeto *D&D Pensamentos*.

Ela junta num lugar só tudo o que foi estudado e testado sobre o sistema:

- **Regras essenciais** da Edição Definitiva e o que mudou em relação à v3.0.
- **Criação de feitiços**: tabelas, customização, condições, feitiço focado em condição, Múltiplos Disparos, Golpeador, auxiliares, passivos, inviáveis.
- **Personagens e builds**: origens, talentos, aptidões, ranking do nível 4, as builds "mais roubadas", multiclasse.
- **Controlador e invocações**: Limite de Comando, criação por grau, horda, os furos do limite.
- **Expansão de domínio e votos de restrição**.
- **Como mestrar combate no chat** e montar encontros com as curvas do bestiário.
- **Simulação de duelos** em Python (20.000 lutas por cenário) e os resultados já obtidos.
- **Estilo de entrega**: fichas em PDF com cara de jogador.
- **A campanha**: personagens, lore e trilhas de progressão.
- **Prompts** prontos para agentes de pesquisa e para os pedidos mais comuns.

## Estrutura

```
codice-amaldicoado/
├── SKILL.md                 # entrada da skill e roteador
├── referencias/             # 01 a 10, um assunto por arquivo
├── prompts/                 # prompts reutilizáveis
└── scripts/
    ├── gerar_pdf.py         # HTML → PDF de ficha
    └── simular_duelo.py     # modelo de simulação de duelo
```

## Instalação

Copie a pasta `codice-amaldicoado` para `~/.claude/skills/`. O Claude passa a usar a skill sempre que o assunto for Feiticeiros & Maldições.

Os scripts precisam de Python 3 e `pip install pymupdf`.

## Aviso

Feiticeiros & Maldições pertence aos seus autores. Este repositório **não inclui o livro** nem trechos longos dele: só resumos de regra, números de tabela com a página de referência, e material original do projeto. Para usar a skill você precisa do seu próprio PDF do livro.
