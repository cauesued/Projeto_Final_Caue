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

st.set_page_config(layout="wide")

if 'current_display' not in st.session_state:
    st.session_state['current_display'] = ''
if 'total' not in st.session_state:
    st.session_state['total'] = 0.0
if 'last_operation' not in st.session_state:
    st.session_state['last_operation'] = None
if 'new_num' not in st.session_state:
    st.session_state['new_num'] = False

# --- 2. Lógica da Calculadora ---

def handle_click(char):
    """Gerencia cliques de números e operadores."""
    
    # Lógica para limpar o visor
    if char == 'C':
        st.session_state['current_display'] = ''
        st.session_state['total'] = 0.0
        st.session_state['last_operation'] = None
        st.session_state['new_num'] = False
        return

    # Lógica para o botão de igual
    if char == '=':
        if st.session_state['last_operation'] and st.session_state['current_display']:
            calculate()
            st.session_state['last_operation'] = None
            st.session_state['new_num'] = True # Próximo clique numérico limpa o visor
        return

    # Lógica para operadores (+, -, *, /)
    if char in ['+', '-', '*', '/']:
        if st.session_state['current_display']:
            if st.session_state['last_operation']:
                calculate()
            else:
                st.session_state['total'] = float(st.session_state['current_display'])
            st.session_state['last_operation'] = char
            st.session_state['new_num'] = True # Indica que o próximo dígito inicia um novo número
        return

    # Lógica para números e ponto decimal
    if st.session_state['new_num']:
        st.session_state['current_display'] = str(char)
        st.session_state['new_num'] = False
    else:
        # Previne múltiplos pontos decimais
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

        # Atualiza o visor com o resultado da operação
        st.session_state['current_display'] = str(st.session_state['total'])
    except ValueError:
        st.session_state['current_display'] = "Erro"
    except ZeroDivisionError:
        st.session_state['current_display'] = "Divisão por zero"

# --- 3. Interface do Usuário (UI) ---

st.title("Calculadora Streamlit 4x4")

# Visor: uma linha acima dos botões
# st.metric é usado para um visual de "visor" simples
st.metric(label="Resultado/Visor", value=st.session_state['current_display'] if st.session_state['current_display'] else "0")

# Layout da grade de botões 4x4
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Cria as colunas para o layout da grade
for row in buttons:
    cols = st.columns(4) # Cria 4 colunas de largura igual para cada linha
    for col, button_char in zip(cols, row):
        # Cada botão chama a função handle_click com seu caractere correspondente
        with col:
            st.button(
                button_char, 
                on_click=handle_click, 
                args=[button_char], 
                use_container_width=True # Faz o botão preencher a coluna inteira
            )

# --- 4. Executando o Aplicativo ---
# Para rodar o aplicativo, salve o arquivo como `app.py` e execute no terminal:
# streamlit run app.py
