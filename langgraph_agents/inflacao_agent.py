from langgraph.graph import StateGraph
from llama_cpp import Llama
import pandas as pd
import requests
import os

model_path = os.getenv("LLAMA_MODEL_PATH")
llm = Llama(model_path=model_path)

def fetch_data():
    response = requests.get("https://api.bcb.gov.br/dados/inflacao")
    return pd.DataFrame(response.json())

def analyze_data(data):
    latest = data.iloc[-1]
    prompt = f\"Dados recentes de inflacao: {{latest.to_dict()}}. Gere uma análise macroeconômica para uma mineradora.\"
    output = llm(prompt, max_tokens=512)
    return output["choices"][0]["text"]

def build_agent():
    def run(_):
        data = fetch_data()
        analysis = analyze_data(data)
        return {{"analysis": analysis}}

    graph = StateGraph()
    graph.add_node("analyze", run)
    graph.set_entry_point("analyze")
    return graph.compile()

agent = build_agent()
