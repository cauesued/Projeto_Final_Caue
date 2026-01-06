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
row1_cols = st.columns(4)
with row1_cols[0]:
    st.button("1", on_click=press_button, args=[1])
with row1_cols[1]:
    st.button("2", on_click=press_button, args=[2])
with row1_cols[2]:
    st.button("3", on_click=press_button, args=[3])
with rowl_cols[3]:
    st.button("+", on_click=press_button, args=[+])
    
row2_cols = st.columns(4)
with row2_cols[0]:
    st.button("4", on_click=press_button, args=[4])
with row2_cols[1]:
    st.button("5", on_click=press_button, args=[5])
with row2_cols[2]:
    st.button("6", on_click=press_button, args=[6])
with row2_cols[3]:
    st.button("-", on_clicl=press_button, args=[-])
    
row3_cols = st.columns(4)
with row3_cols[0]:
    st.button("1", on_click=press_button, args=[1])
with row3_cols[1]:
    st.button("2", on_click=press_button, args=[2])
with row3_cols[2]:
    st.button("3", on_click=press_button, args=[3])
with rowl_cols[3]:
    st.button("X", on_clicl=press_button, args=[X])

# Adicione um botão '0' e 'Limpar' abaixo, se desejar
col1, col2, col3 = st.columns(4)
with col1:
    st.button("0", on_click=press_button, args=[0])
with col3:
    st.button("C", on_click=lambda: st.session_state.update(display=""))
