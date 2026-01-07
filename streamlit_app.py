import streamlit as st

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-puJcpOvnq50F4JR1O-g_mscVBpo25OmFEA&s', width=600)

st.title("Projeto Final: Calculadora")

st.set_page_config(page_title="Calculadora Streamlit", layout="centered")

# Inicializa o estado da sessão para armazenar a expressão (se ainda não existir)
if 'expression' not in st.session_state:
    st.session_state.expression = ""

def add_to_expression(value):
    """Adiciona um valor (número ou operador) à expressão."""
    st.session_state.expression += str(value)

def clear_expression():
    """Limpa a expressão."""
    st.session_state.expression = ""

def calculate_result():
    """Avalia a expressão e exibe o resultado."""
    try:
        # Usa eval para avaliar a expressão matemática
        # Substitui '%' por '/100*' para cálculo percentual simples
        expression = st.session_state.expression.replace('%', '/100*')
        result = str(eval(expression))
        st.session_state.expression = result
    except Exception as e:
        st.session_state.expression = "Erro"

# --- Layout da Interface ---

st.title("Calculadora")

# Display (linha acima)
# Usa um container para garantir que o input fique acima dos botões
with st.container():
    st.text_input("Expressão", value=st.session_state.expression, key="display", disabled=True, label_visibility="hidden")

# Definição dos botões em uma grade 4x4
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['%', '0', '=', '+']
]

# Cria a grade de botões usando st.columns
for row in buttons:
    cols = st.columns(len(row))
    for col, button_label in zip(cols, row):
        with col:
            if button_label == '=':
                st.button(button_label, on_click=calculate_result, use_container_width=True)
            elif button_label == 'C': # Adiciona um botão 'C' para limpar
                 st.button(button_label, on_click=clear_expression, use_container_width=True)
            else:
                st.button(button_label, on_click=add_to_expression, args=(button_label,), use_container_width=True)

# Botão extra para limpar a expressão (opcional, pode ser adicionado na grade)
st.button("Limpar (C)", on_click=clear_expression)
