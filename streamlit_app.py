import streamlit as st

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-puJcpOvnq50F4JR1O-g_mscVBpo25OmFEA&s', width=600)

st.title("Projeto Final: Calculadora")

if 'display' not in st.session_state:
    st.session_state.display = ""

def press_button(value):
    """Função para atualizar o display quando um botão é pressionado."""
    st.session_state.display += str(value)

st.title("Calculadora Simples com Streamlit")

# 1. Linha acima para exibir o resultado (usando st.text_input para uma aparência de display)
# Desabilitado para edição manual, apenas para visualização
st.text_input("Display", value=st.session_state.display, disabled=True, label_visibility="hidden")

# 2. Layout dos botões em uma grade 3x3
row1_cols = st.columns(3)
with row1_cols[0]:
    st.button("1", on_click=press_button, args=[1])
with row1_cols[1]:
    st.button("2", on_click=press_button, args=[2])
with row1_cols[2]:
    st.button("3", on_click=press_button, args=[3])
    
row2_cols = st.columns(3)
with row2_cols[0]:
    st.button("4", on_click=press_button, args=[4])
with row2_cols[1]:
    st.button("5", on_click=press_button, args=[5])
with row2_cols[2]:
    st.button("6", on_click=press_button, args=[6])
    
row3_cols = st.columns(3)
with row3_cols[0]:
    st.button("7", on_click=press_button, args=[7])
with row3_cols[1]:
    st.button("8", on_click=press_button, args=[8])
with row3_cols[2]:
    st.button("9", on_click=press_button, args=[9])


col1, col2, col3 = st.columns(3)
with col1:
    st.button("0", on_click=press_button, args=[0])
with col3:
    st.button("C", on_click=lambda: st.session_state.update(display=""))

num1 = st.number_input("Digite o primeiro número", value=0.0, format="%.2f")
num2 = st.number_input("Digite o segundo número", value=0.0, format="%.2f")

# Seleção da operação
operacao = st.selectbox("Selecione a operação", ["Somar (+)", "Subtrair (-)", "Multiplicar (*)", "Dividir (/)"])

# Botão para calcular
if st.button("Calcular"):
    resultado = 0
    # Realiza a operação com base na escolha do usuário
    if operacao == "Somar (+)":
        resultado = num1 + num2
        st.success(f"O resultado da soma é: {resultado:.2f}")
    elif operacao == "Subtrair (-)":
        resultado = num1 - num2
        st.success(f"O resultado da subtração é: {resultado:.2f}")
    elif operacao == "Multiplicar (*)":
        resultado = num1 * num2
        st.success(f"O resultado da multiplicação é: {resultado:.2f}")
    elif operacao == "Dividir (/)":
        if num2 != 0:
            resultado = num1 / num2
            st.success(f"O resultado da divisão é: {resultado:.2f}")
        else:
            st.error("Erro: Divisão por zero não é permitida.")
            
# Exemplo de cálculo de porcentagem
st.markdown("---")
st.subheader("Cálculo de Porcentagem")
valor_base = st.number_input("Valor base", value=100.0, format="%.2f", key="base")
porcentagem = st.number_input("Porcentagem a calcular (%)", value=10.0, format="%.2f", key="percent")

if st.button("Calcular Porcentagem"):
    # Para calcular a porcentagem de um número, você usa a fórmula: (porcentagem / 100) * valor_base
    valor_percentual = (porcentagem / 100.0) * valor_base
    st.success(f"{porcentagem:.2f}% de {valor_base:.2f} é: {valor_percentual:.2f}")
