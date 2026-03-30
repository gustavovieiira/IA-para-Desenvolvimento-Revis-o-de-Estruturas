# Relatorio - IA para Desenvolvimento + Revisao de Estruturas de Dados I

## 1. Identificacao da equipe

- Disciplina: Estruturas de Dados I
- Data da entrega: 30/03/2026
- Equipe: Gustavo Vieira Wesolowski e Guilherme Renzo
- Integrantes:
  - Gustavo Vieira Wesolowski
  - Guilherme Renzo
- Repositorio GitHub: https://github.com/gustavovieiira/IA-para-Desenvolvimento-Revis-o-de-Estruturas.git

## 2. Ferramenta de IA escolhida

- Nome da ferramenta: ChatGPT / Codex
- Como foi acessada: aplicativo/terminal com suporte a desenvolvimento
- Por que foi escolhida:
  - A ferramenta permite apoiar a equipe em varias etapas do desenvolvimento.
  - Ela ajuda a gerar rascunhos de solucao, revisar logica, explicar estruturas de dados e sugerir testes.
  - O uso em linguagem natural facilita a iteracao rapida durante a resolucao dos desafios.
- Tutorial ou video consultado:
  - Foi utilizado o conhecimento previo da equipe sobre assistentes de IA para programacao.
  - Se a equipe tiver visto video, tutorial ou documentacao, registrar aqui.
- Integracao com IDE:
  - VS Code
- Como a equipe pretende usá-la:
  - Gerar rascunhos iniciais de algoritmos
  - Revisar solucoes propostas pelos integrantes
  - Explicar complexidade de tempo e espaco
  - Sugerir casos de teste
  - Apoiar a identificacao de erros e melhorias

## 3. Estrategia adotada

A equipe selecionou 12 problemas de programacao no estilo code interview, divididos entre arrays, listas encadeadas e pilhas, conforme as regras da atividade. As solucoes foram implementadas em Python, com foco em clareza, corretude e revisao pratica dos conteudos vistos em sala.

Buscamos priorizar problemas classicos de entrevista tecnica, em niveis facil e medio, porque eles exigem o uso direto das estruturas estudadas e permitem discutir abordagens, complexidade e boas praticas de implementacao.

## 4. Distribuicao obrigatoria dos problemas

- Arrays: 5 problemas
- Listas encadeadas: 4 problemas
- Pilhas: 3 problemas
- Total: 12 problemas

## 5. Tabela de problemas resolvidos

| # | Problema | Link | Plataforma | Estrutura principal | Nivel | Justificativa |
|---|----------|------|------------|---------------------|-------|---------------|
| 1 | Two Sum | https://leetcode.com/problems/two-sum/ | LeetCode | Array | Facil | O problema trabalha com acesso por indice e varredura sobre vetor, o que torna arrays a estrutura central da solucao. |
| 2 | Best Time to Buy and Sell Stock | https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ | LeetCode | Array | Facil | Os precos sao fornecidos em sequencia e o algoritmo percorre o array mantendo o menor valor visto ate o momento. |
| 3 | Product of Array Except Self | https://leetcode.com/problems/product-of-array-except-self/ | LeetCode | Array | Medio | A solucao usa o proprio array de resposta com prefixos e sufixos, explorando processamento sequencial sobre vetores. |
| 4 | 3Sum | https://leetcode.com/problems/3sum/ | LeetCode | Array | Medio | Depois da ordenacao do array, a estrategia de dois ponteiros opera diretamente sobre os indices do vetor. |
| 5 | Merge Intervals | https://leetcode.com/problems/merge-intervals/ | LeetCode | Array | Medio | Os intervalos sao armazenados em uma lista de pares e a fusao depende de ordenacao e percorrimento sequencial. |
| 6 | Reverse Linked List | https://leetcode.com/problems/reverse-linked-list/ | LeetCode | Lista encadeada | Facil | O problema exige manipular ponteiros entre nos, caracteristica central de listas encadeadas. |
| 7 | Linked List Cycle | https://leetcode.com/problems/linked-list-cycle/ | LeetCode | Lista encadeada | Facil | A deteccao de ciclo depende da navegacao por referencias entre nos, sem acesso por indice. |
| 8 | Add Two Numbers | https://leetcode.com/problems/add-two-numbers/ | LeetCode | Lista encadeada | Medio | Os numeros sao representados como listas encadeadas, exigindo percorrimento sincronizado e criacao de novos nos. |
| 9 | Remove Nth Node From End of List | https://leetcode.com/problems/remove-nth-node-from-end-of-list/ | LeetCode | Lista encadeada | Medio | A tecnica de dois ponteiros e aplicada sobre a estrutura encadeada para localizar o no a ser removido. |
| 10 | Valid Parentheses | https://leetcode.com/problems/valid-parentheses/ | LeetCode | Pilha | Facil | O controle de abertura e fechamento de simbolos segue naturalmente o comportamento LIFO de uma pilha. |
| 11 | Min Stack | https://leetcode.com/problems/min-stack/ | LeetCode | Pilha | Medio | O problema pede operacoes tipicas de pilha com suporte adicional para recuperar o minimo em tempo constante. |
| 12 | Daily Temperatures | https://leetcode.com/problems/daily-temperatures/ | LeetCode | Pilha | Medio | A pilha monotonicamente decrescente permite resolver o problema com eficiencia ao processar temperaturas. |

## 6. Quantidade de problemas medios

Os problemas de nivel medio escolhidos foram:

- Product of Array Except Self
- 3Sum
- Merge Intervals
- Add Two Numbers
- Remove Nth Node From End of List
- Min Stack
- Daily Temperatures

Total de problemas medios: 7 de 12.

Assim, a atividade atende ao requisito de ter pelo menos metade dos problemas em nivel medio.

## 7. Divisao de responsabilidade entre integrantes

| Integrante | Problemas sob responsabilidade |
|------------|--------------------------------|
| Gustavo Vieira Wesolowski | Two Sum, Product of Array Except Self, Merge Intervals, Reverse Linked List, Add Two Numbers, Valid Parentheses |
| Guilherme Renzo | Best Time to Buy and Sell Stock, 3Sum, Linked List Cycle, Remove Nth Node From End of List, Min Stack, Daily Temperatures |

Observacao: cada integrante deve ficar responsavel por pelo menos 3 problemas.

## 8. Como a IA foi utilizada na pratica

A IA foi utilizada como apoio durante todo o processo de desenvolvimento. Ela ajudou a:

- estruturar o projeto e organizar os arquivos;
- sugerir problemas adequados aos conteudos da disciplina;
- propor rascunhos de algoritmos;
- revisar a corretude das solucoes;
- explicar a complexidade de tempo e espaco;
- sugerir casos de teste;
- melhorar a documentacao e a apresentacao do trabalho.

Apesar disso, a equipe manteve a responsabilidade de revisar criticamente cada resposta fornecida pela IA, verificar a logica das solucoes e confirmar se os algoritmos realmente atendiam ao enunciado dos problemas.

## 9. Conclusao

A atividade permitiu revisar conteudos fundamentais de Estruturas de Dados I de forma pratica, com foco em arrays, listas encadeadas e pilhas. Alem disso, serviu como primeiro contato estruturado com o uso de IA como ferramenta de desenvolvimento de software, mostrando que ela pode acelerar etapas de planejamento, implementacao, revisao e testes quando utilizada com criterio.

Como resultado, a equipe produziu um conjunto organizado de solucoes para problemas classicos de entrevista tecnica, ao mesmo tempo em que desenvolveu maior familiaridade com raciocinio algoritmico, analise de complexidade e uso consciente de IA no processo de programacao.
