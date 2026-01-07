import streamlit as st

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-puJcpOvnq50F4JR1O-g_mscVBpo25OmFEA&s', width=600)

st.title("Projeto Final: Calculadora")

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
    
    # para dar clean na tela ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if char == 'C':
        st.session_state['current_display'] = ''
        st.session_state['total'] = 0.0
        st.session_state['last_operation'] = None
        st.session_state['new_num'] = False
        return

    #Local dos buttons de =, +, -, *, / ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if char == '=':
        if st.session_state['last_operation'] and st.session_state['current_display']:
            calculate()
            st.session_state['last_operation'] = None
            st.session_state['new_num'] = True # faz com que limpe o visor -----------------------------------------------------------------------------------------------------------------------------------------
        return

    if char in ['+', '-', '*', '/']:
        if st.session_state['current_display']:
            if st.session_state['last_operation']:
                calculate()
            else:
                st.session_state['total'] = float(st.session_state['current_display'])
            st.session_state['last_operation'] = char
            st.session_state['new_num'] = True # Apos isso se iniciara um novo numero ------------------------------------------------------------------------------------------------------------------------------
        return

    #Local dos números e pontos decimais ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

        #Adiciona o resultado da operação --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        st.session_state['current_display'] = str(st.session_state['total'])
    except ValueError:
        st.session_state['current_display'] = "Erro"
    except ZeroDivisionError:
        st.session_state['current_display'] = "Divisão por zero"

st.metric(label="Resultado/Visor", value=st.session_state['current_display'] if st.session_state['current_display'] else "0")

#aonde esta selecionados os buttons --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Cria as colunas de 4x4 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

