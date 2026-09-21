# 06 · Mestrar combate no chat

## Convenções fixas (pedidas pelo jogador)

1. **Ele rola**: o próprio personagem **e as invocações dele** (inclusive o turno autônomo, como o do Igris). Pedir o d20 primeiro e o dano depois, quando o inimigo puder reagir.
2. **Eu rolo**: inimigos, TRs dos inimigos, e personagens que eu controlo num x1. Rolar com Python (`random`) e mostrar o dado cru.
3. **Nunca revelar PV ou PE de inimigo.** Descrever: "arranhado", "bem ferido", "cuspindo sangue", "mais de um terço destruído".
4. Mostrar sempre o dado com modificadores: `d20 [13] + 25 = 38 contra Defesa 28 → acerta`.
5. **Corrigir erro de regra antes de resolver** (ex.: Olhar do Monarca é ação bônus e a bônus já foi gasta; recuar provoca ataque de oportunidade; mover até a aura não alcança).
6. Mapa em texto quando ajudar, cada linha = 3 m, legenda embaixo.
7. **Bloco do inimigo fixado antes da rodada 1**, salvo num arquivo de rascunho, e não muda depois.
8. O inimigo não conhece a ficha do jogador, mas joga para ganhar (mira no ponto fraco, cerca, foca o controlador).
9. Oferecer opções numeradas (A/B/C) quando a decisão não for óbvia, mas aceitar qualquer declaração livre.

## Montar encontro (curvas medidas no Grimório, 140 fichas)

| Patamar | PV | Defesa |
|---|---|---|
| Lacaio | ~46 fixo | ~14 |
| Capanga | 46,6 × ND + 18 | 0,2 × ND + 12,4 |
| Comum | 66,3 × ND + 21 | 1,01 × ND + 15,9 |
| Desafio | 110,5 × ND − 154 | 1,36 × ND + 16,5 |
| Calamidade | ~288,8 × ND − 2138 (sem padrão) | 2,8 × ND − 13,3 |

- Encontro de teste bom: 1 chefe (Desafio), 2 tenentes (Comum), 4 capangas, 8 lacaios.
- Chefe com reação (+5 Def algumas vezes por cena) e habilidade de "fase" abaixo de 50%.
- Solo contra 15 inimigos mata qualquer build de mesa: serve pra achar o ponto fraco, não pra medir força.

## Ordem de um turno

```
Declaração do jogador → checar regra → pedir rolagens → resolver com dados à vista
→ narrar resultado qualitativo → turnos dos inimigos (dados à vista) → estado do jogador (PV/PE)
→ mapa → "O que você faz?"
```

## Regras que sempre aparecem

- Ataque de oportunidade ao sair do alcance de quem está engajado (p.293).
- Uma reação por rodada; ela volta no turno do dono. Invocação tem reação própria.
- Paralisado/Atordoado: sem ações nem reações; ações puramente mentais permitidas.
- Crítico: 20 natural sempre acerta; rola **todos** os dados de dano duas vezes, fixo uma vez (p.307).
- Condição de feitiço: o alvo repete o TR no fim de cada turno dele.
