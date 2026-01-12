import streamlit as st
#Detalhes do site ------------------------------------------------------------------------------------------------------------------------------------------------
st.markdown(
    """
<style>
.stApp {
    background-color: black;
}
</style>
""",
    unsafe_allow_html=True
)

st.markdown("""
<style>
/* Seletor geral para todos os botões, se desejar */
/* .stButton button { background-color: black; color: white; } */

/* Estilo específico para botões com as chaves de 'btn_1' a 'btn_9' */
div[data-testid*="stButton"] > button {
    background-color: darkgray;
    color: white; /* Cor do texto para garantir visibilidade */
    border-radius: 5px;
    margin: 5px;
}

/* Opcional: Efeito hover para os botões */
div[data-testid*="stButton"] > button:hover {
    background-color: #333333; /* Um cinza escuro no hover */
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* Seleciona o primeiro (e geralmente único) botão dentro de um div stButton */
div.stButton > button:first-child {
    color: #000000; /* Define a cor do texto como preto (código hexadecimal #000000) */
    /* Você também pode querer ajustar a cor de fundo para garantir contraste */
    /* background-color: #f0f0f0; */
}

/* Opcional: Estiliza o botão quando o mouse passa por cima (hover) */
div.stButton > button:hover {
    color: #000000; /* Mantém o texto preto no hover */
}
</style>
""", unsafe_allow_html=True)

st.image('https://pt.dreamstime.com/%C3%ADcone-da-calculadora-no-fundo-escuro-image117244544', width=900) # A imagem
#O site ensi -----------------------------------------------------------------------------------------------------------------------------------------------------

st.divider() # Para criar as linhas

st.title("Projeto Final: Calculadora") # O titulo do projeto

st.set_page_config(layout="wide")

if 'current_display' not in st.session_state:
    st.session_state['current_display'] = ''
if 'total' not in st.session_state:
    st.session_state['total'] = 0.0
if 'last_operation' not in st.session_state:
    st.session_state['last_operation'] = None
if 'new_num' not in st.session_state:
    st.session_state['new_num'] = False

def handle_click(char):
    """Gerencia cliques de números e operadores."""
    
    # para dar clean na tela -------------------------------------------------------------------------------------------------------------------------------------
    if char == 'C':
        st.session_state['current_display'] = ''
        st.session_state['total'] = 0.0
        st.session_state['last_operation'] = None
        st.session_state['new_num'] = False
        return

    #Local dos buttons de =, +, -, *, / --------------------------------------------------------------------------------------------------------------------------
    if char == '=':
        if st.session_state['last_operation'] and st.session_state['current_display']:
            calculate()
            st.session_state['last_operation'] = None
            st.session_state['new_num'] = True # faz com que limpe o visor ---------------------------------------------------------------------------------------
        return

    if char in ['+', '-', '*', '/']:
        if st.session_state['current_display']:
            if st.session_state['last_operation']:
                calculate()
            else:
                st.session_state['total'] = float(st.session_state['current_display'])
            st.session_state['last_operation'] = char
            st.session_state['new_num'] = True # Apos isso se iniciara um novo numero ----------------------------------------------------------------------------
        return

    #Local dos números e pontos decimais -------------------------------------------------------------------------------------------------------------------------
    if st.session_state['new_num']:
        st.session_state['current_display'] = str(char)
        st.session_state['new_num'] = False
    else:
        
        if char == '.' and '.' in st.session_state['current_display']:
            return
        st.session_state['current_display'] += str(char)

def calculate():
    """Executa a operação pendente."""
    try:
        current_val = float(st.session_state['current_display'])
        if st.session_state['last_operation'] == '+':
            st.session_state['total'] += current_val
        elif st.session_state['last_operation'] == '-':
            st.session_state['total'] -= current_val
        elif st.session_state['last_operation'] == '*':
            st.session_state['total'] *= current_val
        elif st.session_state['last_operation'] == '/':
            if current_val != 0:
                st.session_state['total'] /= current_val
            else:
                st.session_state['current_display'] = "Erro"
                st.session_state['total'] = 0.0
                return

        
        #Adiciona o resultado da operação ------------------------------------------------------------------------------------------------------------------------
        st.session_state['current_display'] = str(st.session_state['total'])
    except ValueError:
        st.session_state['current_display'] = "Erro"
    except ZeroDivisionError:
        st.session_state['current_display'] = "Divisão por zero"

st.metric(label="Fassa sua conta aqui", value=st.session_state['current_display'] if st.session_state['current_display'] else "0")

#aonde esta selecionados os buttons ------------------------------------------------------------------------------------------------------------------------------
st.divider()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Cria as colunas de 4x4 -----------------------------------------------------------------------------------------------------------------------------------------
for row in buttons:
    cols = st.columns(4) 
    for col, button_char in zip(cols, row):
        with col:
            st.button(
                button_char, 
                on_click=handle_click, 
                args=[button_char], 
                use_container_width=True 
            )

