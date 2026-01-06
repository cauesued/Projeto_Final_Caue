import streamlit as st

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-puJcpOvnq50F4JR1O-g_mscVBpo25OmFEA&s', width=600)

st.title("Projeto Final: Calculadora")

# Configuração da página
st.set_page_config(page_title="Calculadora Básica 2026", page_icon="🔢")

st.title("🔢 Calculadora Básica")
st.write("Insira os números e escolha a operação desejada.")

# Entradas de dados
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Primeiro número:", value=0.0)
with col2:
    num2 = st.number_input("Segundo número:", value=0.0)

st.markdown("---")

# Botões de operação
st.write("### Operações")
operacao_col1, operacao_col2, operacao_col3, operacao_col4 = st.columns(4)

resultado = None

with operacao_col1:
    if st.button("➕ Somar", use_container_width=True):
        resultado = num1 + num2

with operacao_col2:
    if st.button("➖ Subtrair", use_container_width=True):
        resultado = num1 - num2

with operacao_col3:
    if st.button("✖️ Multiplicar", use_container_width=True):
        resultado = num1 * num2

with operacao_col4:
    if st.button("➕ Dividir", use_container_width=True):
        if num2 != 0:
            resultado = num1 / num2
        else:
            st.error("Erro: Divisão por zero!")

# Exibição do Resultado
if resultado is not None:
    st.success(f"### Resultado: {resultado}")
