from src.collector import collect_macro_data
from src.llm import generate_section
import os

def run_agents_pipeline():
    data = collect_macro_data()

    pib_analysis = generate_section("PIB", data['pib'])
    inflation_analysis = generate_section("Inflação", data['inflacao'])
    exchange_analysis = generate_section("Câmbio", data['cambio'])
    interest_analysis = generate_section("Juros", data['juros'])

    full_context = f"""
    Situação macroeconômica atual:
    {pib_analysis}
    {inflation_analysis}
    {exchange_analysis}
    {interest_analysis}

    Contextualize o cenário acima para a indústria de mineração e elabore um relatório estratégico.
    """

    final_report = generate_section("Relatório Final", full_context)

    os.makedirs("output", exist_ok=True)
    with open("output/relatorio_mineracao.txt", "w", encoding="utf-8") as f:
        f.write(final_report)
