import streamlit as st

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-puJcpOvnq50F4JR1O-g_mscVBpo25OmFEA&s', width=600)

st.title("Projeto Final: Calculadora")

# 1. Inicialize st.session_state para armazenar o valor
if 'numero_atual' not in st.session_state:
    st.session_state['numero_atual'] = 0

# 2. Defina funções de callback para os botões
def incrementar_numero():
    st.session_state['numero_atual'] += 1

def decrementar_numero():
    st.session_state['numero_atual'] -= 1

# 3. Crie um local específico para exibir o número
# st.empty() cria um container descartável que pode ser reescrito
placeholder = st.empty()

# 4. Exiba o número atual no local específico
# Isso será atualizado sempre que o script rodar e o estado mudar
with placeholder:
    st.write(f"O número atual é: **:blue[{st.session_state['numero_atual']}]**")

# 5. Coloque os botões em um local diferente, por exemplo, em colunas
col1, col2 = st.columns(2)

with col1:
    # Use on_click para chamar a função de callback
    st.button('Incrementar (+1)', on_click=incrementar_numero)

with col2:
    st.button('Decrementar (-1)', on_click=decrementar_numero)

# Opcional: Adicionar um input numérico que também controla o valor
# Se você quiser que o usuário digite um valor diretamente
st.number_input('Ou digite um valor diretamente:'),
    value=st.session_state['numero_atual'],
    key='input_manual',

streamlit run calculadora.py
    on_change=lambda: st.session_state.update({'numero_atual': st.session_state['input_manual']})
