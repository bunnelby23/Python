import streamlit as st
import pandas as pd

st.set_page_config(page_title="SUPERMERCADO LANTERNA", page_icon="🛒", layout="centered")

st.title("SUPERMERCADO LANTERNA")
st.subheader("Onde você compra e agente te passa a perna")


precos_itens = {
    "Arroz (5kg)": 25.90,
    "Feijão Carioca (1kg)": 8.50,
    "Açúcar Refinado (1kg)": 4.20,
    "Sal Refinado (1kg)": 2.50,
    "Óleo de Soja (900ml)": 6.80,
    "Café Torrado e Moído (500g)": 18.90,
    "Macarrão Espaguete (500g)": 3.75,
    "Molho de Tomate (340g)": 2.40,
    "Leite Integral (1L)": 5.49,
    "Manteiga com Sal (200g)": 11.20,
    "Queijo Muçarela Fatiado (1kg)": 42.90,
    "Iogurte Natural (170g)": 2.80,
    "Pão de Forma (500g)": 7.50,
    "Ovos Brancos (Dúzia)": 9.80,
    "Peito de Frango (1kg)": 16.90,
    "Banana Prata (1kg)": 5.50,
    "Tomate Italiano (1kg)": 7.90,
    "Cebola (1kg)": 4.50,
    "Sabão em Pó (1kg)": 14.90,
    "Detergente Líquido (500ml)": 2.20
    }

def calcular_preco_total(itens_selecionados):
    total = sum(precos_itens[item] for item in itens_selecionados)
    return total

itens_selecionados = st.multiselect(
   label =  "Selecione os itens do supermercado:",
    options=list(precos_itens.keys())
)

if itens_selecionados:
    st.subheader("Itens Selecionados:")
    for item in itens_selecionados:
        st.write(f"- {item}: R$ {precos_itens[item]:.2f}")

        total_compra = calcular_preco_total(itens_selecionados)
        

        st.divider()
    st.metric(label="Total da Compra", value=f"R$ {total_compra:.2f}")
else:
    st.info("Nenhum item selecionado. Marque os produtos acima para ver o valor total.")