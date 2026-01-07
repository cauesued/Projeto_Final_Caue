import streamlit as st

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-puJcpOvnq50F4JR1O-g_mscVBpo25OmFEA&s', width=600)

st.title("Projeto Final: Calculadora")

if 'current_value' not in st.session_state:
    st.session_state.current_value = ""
if 'result' not in st.session_state:
    st.session_state.result = None

# Função para lidar com o clique dos botões numéricos e de operação
def button_click(value):
    if value == "=":
        try:
            # Avalia a expressão matemática no current_value
            st.session_state.result = eval(st.session_state.current_value)
            st.session_state.current_value = str(st.session_state.result)
        except Exception:
            st.session_state.result = "Erro"
    elif value == "C":
        # Limpa o display
        st.session_state.current_value = ""
        st.session_state.result = None
    elif value == "%":
        # Adiciona o sinal de porcentagem (requer tratamento mais complexo para lógica real de %)
        # Para uma calculadora básica, trataremos como concatenação para simplificar
        st.session_state.current_value += value
    else:
        # Adiciona o valor/operação ao display
        st.session_state.current_value += str(value)

# Exibe o campo de texto principal para o resultado/entrada
display_text = st.session_state.current_value
if st.session_state.result is not None and st.session_state.result != "Erro":
    display_text = str(st.session_state.result)
st.text_input("Resultado", value=display_text, key="display", disabled=True)

# Define o layout dos botões em colunas
# Criaremos 4 colunas por linha
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=button_click, args=["7"])
    st.button("4", on_click=button_click, args=["4"])
    st.button("1", on_click=button_click, args=["1"])
    st.button("C", on_click=button_click, args=["C"])

with col2:
    st.button("8", on_click=button_click, args=["8"])
    st.button("5", on_click=button_click, args=["5"])
    st.button("2", on_click=button_click, args=["2"])
    st.button("0", on_click=button_click, args=["0"])

with col3:
    st.button("9", on_click=button_click, args=["9"])
    st.button("6", on_click=button_click, args=["6"])
    st.button("3", on_click=button_click, args=["3"])
    st.button(".", on_click=button_click, args=["."])

with col4:
    st.button("÷", on_click=button_click, args=["/"])
    st.button("×", on_click=button_click, args=["*"])
    st.button("-", on_click=button_click, args=["-"])
    st.button("+", on_click=button_click, args=["+"])
    st.button("%", on_click=button_click, args=["%"]) # O uso real de % exigiria lógica mais avançada
    st.button("=", on_click=button_click, args=["="])

numeros = range(1, 10)

# Cria colunas para dispor os botões horizontalmente
cols = st.columns(9) # Cria 9 colunas de largura igual

# Itera sobre os números e cria um botão em cada coluna
for i, num in enumerate(numeros):
    with cols[i]:
        # Cada botão tem um texto (ex: '1') e uma chave única (ex: 'btn_1')
        if st.button(str(num), key=f"btn_{num}"):
            st.session_state['numero_selecionado'] = num
