# Prompts de agente de pesquisa

Prompts usados para mandar um agente varrer o livro extraído em texto (`fm_def.txt`, marcadores `--- PAGE N ---`). Trocar o caminho do arquivo antes de usar.

---

## 1. Varredura para um Controlador de nível 4

> Você é um analista de regras do RPG "Feiticeiros & Maldições" (F&M). O texto completo da edição definitiva está em `<caminho>/fm_def.txt`, com marcadores "--- PAGE N ---". A página impressa não é sempre N − 1: confira o fólio impresso e reporte sempre a página impressa.
>
> Extraia informação factual (sem inventar, citando página e trecho curto) para montar um CONTROLADOR de NÍVEL 4 o mais forte possível:
> 1. Lista completa de origens (verifique se existe alguma nova além das sete conhecidas).
> 2. Todos os talentos que um personagem de nível 4 pode pegar, com pré-requisito.
> 3. Aptidões acessíveis com Aura e Controle e Leitura 1 ou 2, e quais servem para quem luta por invocações.
> 4. Criação de invocações: todas as ações simples, complexas, com custo e características, com valores por grau (especialmente 4º) e custo em PE.
> 5. Regras de horda, invocação voadora, montaria e tamanho grande.
>
> Não proponha builds. Só dados organizados, com página e citação curta. Seja completo nos itens 3 e 4.

---

## 2. Expansão de domínio

> Você é analista de regras de F&M, edição definitiva (`<caminho>/fm_def.txt`). Reporte sempre a página impressa.
>
> Levante tudo sobre Expansão de Domínio:
> 1. Todas as aptidões de Domínio e Barreira com pré-requisito exato (nível e nível de aptidão), custo, ação e efeito.
> 2. Quantos pontos de nível de aptidão existem em cada nível, as fontes extras, e em que nível exato um Controlador consegue Incompleta, Completa e Acerto Garantido, e quanto sobra para Aura e Controle e Leitura.
> 3. Guia de criação: efeitos por nível de Domínio, regra de fortalecer, todas as tabelas de efeito e os benefícios automáticos ao abrir.
> 4. Acerto Garantido: regras completas, limites, condições permitidas e proibidas, Abertura de 0.2 segundos.
> 5. Exaustão de Técnica, duração, confronto, contestação e resistência do domo.
> 6. Se existe regra sobre invocações dentro de uma expansão e se os efeitos valem para os ataques delas. Diga claramente se o livro é omisso.
>
> Não proponha builds.

---

## 3. Auditoria de um plano de progressão

> Você é auditor de regras de F&M, edição definitiva (`<caminho>/fm_def.txt`). Reporte sempre a página impressa.
>
> Para cada afirmação abaixo, responda CONFIRMADO / ERRADO / OMISSO NO LIVRO, com citação curta e página:
> [colar as afirmações numeradas do plano, por exemplo: Limite de Comando, exceção do Mestre do Controle, regras de Horda, Fantoche Supremo, Melhoria de Controlador, Potencial Superior, Flanco Avançado, limite de sustentados, Autonomia, número de invocações, comandos por ação, graus por nível]
>
> Além disso entregue: a lista completa de habilidades da especialização por nível de acesso, e as tabelas de criação de invocação para todos os graus.
>
> Não proponha builds. Só auditoria e dados.

---

## 4. Comparar duas edições

> Extraia o texto dos dois PDFs com PyMuPDF, página por página. Compare palavra por palavra por página (difflib), ignorando diferenças só de espaço e de quebra de tabela. Liste as páginas com mudança real, e para cada trecho mostre "antes" e "depois" com contexto. Depois agrupe em: regras gerais, origens, cada especialização, feitiços e equipamento, votos. Diga o impacto em cada ficha do jogador.
