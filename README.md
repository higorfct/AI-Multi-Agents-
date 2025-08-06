# Projeto 15: Multiagentes Macroeconômicos com Airflow

# 📊 Macro Pipeline: Análise Macroeconômica Automatizada com Airflow, Docker e LangGraph (LLama)

Este projeto implementa uma **pipeline de dados automatizada** para coletar, analisar e enviar relatórios de **indicadores macroeconômicos** relevantes (PIB, Inflação, Câmbio e Juros) usando:

- **Apache Airflow** (orquestração)
- **Docker** (ambiente isolado e reprodutível)
- **LangGraph com LLama** (agentes de IA para análise automatizada)

O objetivo é **subsidiar decisões estratégicas de uma mineradora** com informações atualizadas e análises geradas por IA.

---

## ⚙️ Funcionalidades

1. **Coleta de Dados via APIs Públicas (Bacen, IBGE)**
   - Coleta automatizada dos indicadores após suas respectivas divulgações.

2. **Análise com Agentes LangGraph + LLama**
   - Cada indicador é analisado por um agente especializado de IA com base em LLM local (LLama).

3. **Geração de Relatórios Automatizados**
   - Relatórios textuais são gerados com insights para tomada de decisão.

4. **Envio por E-mail**
   - Relatórios são enviados automaticamente para os tomadores de decisão.

---

## 🔁 Fluxo da Pipeline (Gráfico)

```mermaid
graph TD
    A[Airflow DAGs Agendados] --> B[Coleta de Dados via APIs Públicas]
    B --> C[Análise por Agentes IA com LangGraph + LLama]
    C --> D[Geração de Relatórios de Conjuntura]
    D --> E[Envio Automático por E-mail]
    E --> F[Tomadores de Decisão da Mineradora]

