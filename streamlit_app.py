import streamlit as st

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-puJcpOvnq50F4JR1O-g_mscVBpo25OmFEA&s', width=600)

st.title("Projeto Final: Calculadora")

# Container para exibir a entrada/saída (simulação de um display)
st.container(border=True).markdown("<h3 style='text-align: right;'>0</h3>", unsafe_allow_html=True)

# Organiza os botões em uma grade 3x3
st.markdown("#### Teclado Numérico")

# Linha 1 (7, 8, 9)
col1, col2, col3 = st.columns(3)
with col1:
    st.button("7", use_container_width=True)
with col2:
    st.button("8", use_container_width=True)
with col3:
    st.button("9", use_container_width=True)

# Linha 2 (4, 5, 6)
col4, col5, col6 = st.columns(3)
with col4:
    st.button("4", use_container_width=True)
with col5:
    st.button("5", use_container_width=True)
with col6:
    st.button("6", use_container_width=True)

# Linha 3 (1, 2, 3)
col7, col8, col9 = st.columns(3)
with col7:
    st.button("1", use_container_width=True)
with col8:
    st.button("2", use_container_width=True)
with col9:
    st.button("3", use_container_width=True)

# Você pode adicionar mais funcionalidades e botões (0, +, -, etc.) seguindo o mesmo padrão.
