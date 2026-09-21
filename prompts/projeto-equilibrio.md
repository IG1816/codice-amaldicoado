# PROJETO EQUILÍBRIO — Errata de Balanceamento para Feiticeiros & Maldições v3.0

## Carta de missão (o prompt)

> Você é um designer de sistemas de RPG de mesa. Sua tarefa é auditar matematicamente o
> sistema **Feiticeiros & Maldições v3.0** e produzir uma **errata de balanceamento** que:
>
> 1. **Preserve 100% da identidade e fidelidade** do sistema original — nada de reescrever
>    o jogo. Toda correção deve ser reconhecível como "o mesmo jogo, ajustado".
> 2. **Achate o escalonamento** para que a diferença de poder entre um personagem nível 5,
>    10, 15 e 20 seja significativa mas não absurda — hoje ela é exponencial.
> 3. **Elimine armadilhas de build (traps)**: nenhuma origem ou especialização pode ser
>    objetivamente a escolha errada. Se uma opção é 30%+ mais fraca que a mediana em
>    poder efetivo, ela está quebrada e precisa de compensação.
> 4. **Abra variedade de build**: hoje o sistema empurra todo mundo pra um punhado de rotas
>    ótimas. O objetivo é que existam **múltiplos caminhos viáveis para ser forte**,
>    não um só.
> 5. **Torne multiclasse uma escolha real** — hoje é uma punição mecânica disfarçada de
>    liberdade.
>
> Você tem acesso ao livro inteiro e ao bestiário. Leia tudo antes de propor qualquer número.
> Nenhuma correção pode ser baseada em intuição: toda mudança precisa de justificativa
> matemática (DPR, TTK, curva de recurso, economia de ação).

---

## Fontes obrigatórias

| Fonte | Caminho | O que contém |
|---|---|---|
| Livro de Regras v3.0 | `F&M- Livro de Regras v3.0.pdf` (369 págs, texto extraído em `scratchpad/fm_regras_v3.txt`) | Núcleo: criação, origens, especializações, aptidões, talentos, criação de técnica, combate |
| Grimório das Maldições | `livros/F&M 2.5 - Grimório das Maldições (Versão 1).pdf` (texto em `scratchpad/grimorio.txt`) | Guia de criação de inimigos, ND, patamares, dotes |
| Grimório Tracker (web) | https://grimorio-fm.vercel.app/ | 165 fichas prontas — a "verdade de campo" do que o sistema produz em ND 5-30 |
| Enciclopédia Amaldiçoada v0.6 | `livros/Feiticeiros e Maldições - Enciclopédia Amaldiçoada v0.6.pdf` | Técnicas canônicas adaptadas |

---

## Princípios de design que guiam as correções

1. **Precisão limitada (bounded accuracy) parcial.** Ataque e Defesa não podem divergir
   ao ponto de "sempre acerta" ou "nunca acerta". Alvo: taxa de acerto entre 50-75% contra
   um alvo de nível equivalente, em qualquer nível.
2. **TTK (time to kill) estável.** O número de rodadas para derrotar um inimigo de ND
   equivalente deve ficar aproximadamente constante (3-5 rodadas) do nível 1 ao 20.
   Se no nível 20 uma luta dura 25 rodadas ou 1 rodada, está quebrado.
3. **Economia de ação é o eixo mais perigoso.** Qualquer habilidade que conceda ação extra,
   reação ilimitada ou negação incondicional precisa de custo real e limite por rodada.
4. **Recurso finito não pode ser a única defesa.** Provado em simulação: defesas que
   dependem de PE perdem sempre no jogo longo contra defesas gratuitas. Nenhuma build
   pode ser "invencível por 6 rodadas e inútil depois".
5. **Custo de oportunidade simétrico.** Se a Especialização A recebe mais PE, ela recebe
   menos PV ou menos habilidades. Hoje isso não é verdade em vários casos.
6. **Fidelidade temática acima de simetria numérica.** Sukuna deve continuar sendo mais
   forte que um estudante de 1º ano. O que não pode acontecer é *dois personagens do mesmo
   nível* terem diferença de poder de 3x por causa de escolha de origem.

---

## Eixos de auditoria (o que precisa ser medido)

### A. Assimetria de Origem
Cada uma das 7 origens (Inato, Herdado, Derivado, Restringido, Feto Amaldiçoado Híbrido,
Sem Técnica, Corpo Amaldiçoado Mutante) vale quantos "pontos de poder" no nível 1, 5, 10, 20?
Quais são traps?

### B. Assimetria de Especialização
As 6 especializações (Lutador, Esp. em Combate, Esp. em Técnica, Controlador, Suporte,
Restringido): PV/PE por nível, número de habilidades, qualidade das habilidades base,
capstone nível 20. Curva comparativa.

**Suspeita inicial a verificar:** Especialista em Técnica parece dominante — 6 PE/nível
+ modificador de atributo no máximo, **Adiantar a Evolução** (acesso a feitiços de nível
superior 1-2 níveis antes de todo mundo), **Conjuração Aprimorada** (bônus de dano que
escala com nível de personagem), e **Foco Amaldiçoado** com 3 opções todas fortes
(Economia zera custo de feitiços nível 1).

### C. Escalonamento matemático de Feitiços/Técnicas
Tabelas conhecidas (dano alvo único, teste de resistência):
- Nível 0: 1d10 (méd 5) · Nível 1: 3d8 (14) · Nível 2: 7d8 (31) · Nível 3: 12d8 (54)
- Nível 4: 14d10 (77) · Nível 5: 18d12 (116) · Técnica Máxima: 26d12 (169)

Isso é crescimento de ~8x do nível 1 ao 5. **PV cresce na mesma proporção?** Medir e
corrigir a curva se não crescer.

Comparar com **Técnicas Marciais do Restringido** (níveis 1-4 apenas, custos 2/5/8/12 Estamina)
— o Restringido está competindo em pé de igualdade ou está condenado?

### D. Aptidões, Talentos e Votos
Votos de Restrição são multiplicadores — são exploráveis? Quais talentos são obrigatórios
(sinal de design quebrado) e quais nunca são escolhidos (sinal de lixo)?

### E. Economia de ação e combate
Ações por turno, reações, sequência de ataques, condições. Onde estão os exploits?
(Referência de campo: a reação **Infinito** do Gojo declara "pode utilizar quantas vezes
for capaz" — exceção explícita à regra de 1 reação/rodada. Isso é design intencional de
boss ou vazamento de balanceamento?)

### F. Multiclasse
Requisitos, o que se ganha, o que se perde. Por que ninguém faz? Como tornar viável sem
virar a rota ótima?

---

## Entregáveis

1. **Relatório de auditoria** — todos os problemas encontrados, com números.
2. **Errata de balanceamento** — correções concretas, em formato de regra pronta pra mesa.
3. **Tabela de conversão** — como adaptar personagens existentes pras novas regras.
4. **Guia de variedade de build** — demonstração de que existem 5+ rotas viáveis distintas
   pra ser forte, não uma só.

---

## Método de execução

Equipe de auditoria em paralelo (5 agentes), cada um com um eixo, seguido de consolidação
matemática e redação da errata.
