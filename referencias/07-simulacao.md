# 07 · Simulação de luta

Quando o pedido é "quem ganha", "testa essa ficha", "x1", "roda o nível X": **simular, não opinar.**

## Método

1. **Fechar as duas fichas no nível pedido** com as regras da Definitiva (PV, PE, Defesa, RD, TRs, iniciativa, ataques e dano por fórmula).
2. **Definir a estratégia de cada lado** como faria um jogador bom (e testar a estratégia alternativa quando houver uma óbvia; ex.: dano duplo em vez de trava).
3. **Modelar o que decide**: iniciativa (e rerrolagem), reações (Cobrir-se, Reforço Reativo, Anular Técnica, Aura Anuladora), condições (Paralisado tira turno e reação), PE por rodada, limite de ações.
4. Rodar **20.000 lutas** por cenário (`scripts/simular_duelo.py` é o modelo).
5. Reportar: % de vitória, **PV que sobra no vencedor**, rodadas médias e **uma luta narrada** quando ajudar.
6. **Listar as simplificações** (campo aberto, crítico aproximado, estratégia fixa, sem aliados).
7. Se o resultado contrariar algo dito antes, **corrigir explicitamente**.

## Resultados já obtidos (guardar para não refazer)

| Duelo | Nível | Resultado |
|---|---|---|
| Apagador (Técnico) × Vale | 4 | Apagador 86% |
| Apagador × Vale | 10 | Apagador 99% (com Feitiço Rápido) |
| Apagador × Vale | 20 | Apagador 69% (sem Feitiço Rápido: Vale 100%) |
| Pistoleiro Técnico × Pistoleiro Combatente × Restringido | 4 | Técnico 80% no total, Combatente 49%, Restringido 21% |
| Pistoleiro Técnico × Vale | 4 | Pistoleiro 94-99% |
| Pistoleiro Técnico × Vale | 10 | Pistoleiro 99%; com Aura Anuladora no Vale, 78-83% |
| Pistoleiro Técnico × Vale | 20 | Pistoleiro 68%; **com Aura Anuladora, Vale 100%** |
| Técnico × Combatente (pistoleiros) | 5 / 10 / 20 | Combate 62% / Técnica 62% / Técnica 76-78% |
| Técnico nv20 com dano duplo (~370 por turno) × Vale nv20 com Aura Anuladora + Anular Técnica | 20 | Técnico 69% |
| Monarca nv10 solo × 15 inimigos (Catedral dos Ossos) | 10 | derrota na rodada 6 (PE acabou na 4, ataques de oportunidade custaram ~41 PV) |
| Hélio nv10 × Monarca nv10 (jogado no chat) | 10 | Monarca venceu na rodada 2 (Hélio chegou a 6 m e foi cercado) |

## Lições que se repetem

- **Quem age primeiro e trava ganha.** Especialista em Técnica com Feitiço Rápido (trava na bônus, dano na comum) domina x1 do nível 8 em diante.
- **O Controlador é o ponto fraco do próprio exército.** Aura Anuladora protege da trava, mas não do dano duplo (dois feitiços de nível 5 no turno via Feitiço Rápido).
- **Um turno de exército no nível 20 (~550-575) mata qualquer peça de vidro.**
- Nível 5 é a janela do Esp. em Combate; nível 7 é o salto do Técnico (Paralisado).
