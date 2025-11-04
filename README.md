# Jogo da Velha com Inteligência Artificial

## Descrição do projeto
Projeto desenvolvido como parte do Bloco Formativo 3 da disciplina de Inteligência Artificial.  
O jogo da velha foi implementado com três níveis de dificuldade, utilizando algoritmos de busca competitiva.

## Níveis de dificuldade
| Nível | Estratégia | Descrição |
|-------|-------------|------------|
| 1 | Aleatório | Escolhe jogadas aleatoriamente. |
| 2 | Monte Carlo | Usa simulações estocásticas para avaliar jogadas. |
| 3 | Min-Max com poda Alfa-Beta | Joga de forma perfeita, analisando todos os estados possíveis. |

## Estrutura do Projeto
├── game.py # Regras do jogo e controle do tabuleiro
├── agents.py # Implementação dos três agentes (fácil, médio, difícil)
├── runner.py # Interface principal e gerenciamento das partidas