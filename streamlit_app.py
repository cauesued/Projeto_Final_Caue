import streamlit as st

# 1. Configuração da página (DEVE ser o primeiro comando Streamlit)
st.set_page_config(page_title="Calculadora Pro", layout="centered")

# 2. Estilização CSS Customizada
st.markdown("""
<style>
    /* Fundo do App */
    .stApp { background-color: #0E1117; }
    
    /* Estilo dos Botões */
    div[data-testid="stButton"] button {
        background-color: #262730;
        color: white;
        border: 1px solid #4B4B4B;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    /* Efeito Hover */
    div[data-testid="stButton"] button:hover {
        background-color: #FF4B4B;
        border-color: #FF4B4B;
        color: white;
    }

    /* Estilo específico para o visor */
    .stMetric {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF4B4B;
    }
</style>
""", unsafe_allow_html=True)

# 3. Inicialização do State
if 'current_display' not in st.session_state:
    st.session_state['current_display'] = '0'
if 'total' not in st.session_state:
    st.session_state['total'] = 0.0
if 'last_operation' not in st.session_state:
    st.session_state['last_operation'] = None
if 'new_num' not in st.session_state:
    st.session_state['new_num'] = True

# 4. Funções de Lógica
def calculate():
    try:
        current_val = float(st.session_state['current_display'])
        op = st.session_state['last_operation']
        
        if op == '+': st.session_state['total'] += current_val
        elif op == '-': st.session_state['total'] -= current_val
        elif op == '*': st.session_state['total'] *= current_val
        elif op == '/': 
            if current_val != 0:
                st.session_state['total'] /= current_val
            else:
                return "Erro: Div/0"
        
        # Formata para remover .0 se for inteiro
        res = st.session_state['total']
        return str(int(res)) if res.is_integer() else str(round(res, 4))
    except Exception:
        return "Erro"

def handle_click(char):
    if char == 'C':
        st.session_state['current_display'] = '0'
        st.session_state['total'] = 0.0
        st.session_state['last_operation'] = None
        st.session_state['new_num'] = True
        return

    if char in ['+', '-', '*', '/']:
        if st.session_state['last_operation'] and not st.session_state['new_num']:
            res = calculate()
            st.session_state['current_display'] = res
        else:
            st.session_state['total'] = float(st.session_state['current_display'])
        
        st.session_state['last_operation'] = char
        st.session_state['new_num'] = True
        return

    if char == '=':
        if st.session_state['last_operation']:
            res = calculate()
            st.session_state['current_display'] = res
            st.session_state['last_operation'] = None
            st.session_state['new_num'] = True
        return

    # Entrada de Números
    if st.session_state['new_num']:
        st.session_state['current_display'] = str(char)
        st.session_state['new_num'] = False
    else:
        if char == '.' and '.' in st.session_state['current_display']:
            return
        st.session_state['current_display'] += str(char)

# 5. Interface Visual
st.title("🔢 Calculadora Python")
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-puJcpOvnq50F4JR1O-g_mscVBpo25OmFEA&s', width=300)

# Visor
st.metric(label="Resultado", value=st.session_state['current_display'])

st.divider()

# Grid de Botões
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    cols = st.columns(4)
    for col, char in zip(cols, row):
        col.button(char, on_click=handle_click, args=[char], use_container_width=True)

st.caption("Desenvolvido com Streamlit")
