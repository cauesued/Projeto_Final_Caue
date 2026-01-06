import streamlit as st

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-puJcpOvnq50F4JR1O-g_mscVBpo25OmFEA&s', width=600)

st.title("Projeto Final: Calculadora")

for row in range(3):
    cols = st.columns(3) # Cria 3 colunas por linha
    for col_idx in range(3):
        # Calcula o número do botão (1 a 9)
        num = row * 3 + col_idx + 1
        with cols[col_idx]:
            if st.button(f"{num}", key=f"btn_{num}"):
                st.write(f"Você clicou no número: {num}")

import streamlit as st

cols = st.columns(9)
for i in range(9):
    num = i + 1
    if cols[i].button(str(num), key=f"num_{num}"):
        st.success(f"Botão {num} pressionado!")
