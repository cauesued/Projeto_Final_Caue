import streamlit as st

# Configuração da página (deve ser o primeiro comando Streamlit)
st.set_page_config(page_title="Calculadora Pro", layout="centered")

# CSS customizado
st.markdown("""
<style>
    .stApp { background-color: #0E1117; color: #FFF; }
    div[data-testid="stButton"] button {
        background-color: #262730; color: white; border: 1px solid #4B4B4B;
        height: 60px; font-size: 20px; font-weight: bold; transition: all 0.15s;
    }
    div[data-testid="stButton"] button:hover {
        background-color: #FF4B4B; border-color: #FF4B4B; color: white;
    }
    .stMetric { background-color: #1E1E1E; padding: 20px; border-radius: 10px; border-left: 5px solid #FF4B4B; }
</style>
""", unsafe_allow_html=True)

# Inicialização do estado
state = st.session_state
if 'current_display' not in state:
    state.current_display = '0'
if 'total' not in state:
    state.total = 0.0
if 'last_operation' not in state:
    state.last_operation = None
if 'new_num' not in state:
    state.new_num = True
if 'error' not in state:
    state.error = False

# Utilitários
def format_number(n: float) -> str:
    """Formata número removendo .0 quando inteiro e limitando casas decimais."""
    if n is None:
        return "0"
    if float(n).is_integer():
        return str(int(n))
    return str(round(n, 8)).rstrip('0').rstrip('.')  # evita exibir zeros desnecessários

def safe_float(s: str):
    """Converte string para float com tratamento; retorna None se inválido."""
    try:
        return float(s)
    except Exception:
        return None

# Lógica de cálculo
def calculate_operation():
    """Executa a operação pendente entre state.total e state.current_display.
       Retorna tuple (success: bool, message_or_value)."""
    cur = safe_float(state.current_display)
    if cur is None:
        return False, "Erro: entrada inválida"
    op = state.last_operation

    # Se não há operação pendente, definimos total como o valor atual
    if op is None:
        state.total = cur
        return True, state.total

    try:
        if op == '+':
            state.total = state.total + cur
        elif op == '-':
            state.total = state.total - cur
        elif op == '*':
            state.total = state.total * cur
        elif op == '/':
            if cur == 0:
                return False, "Erro: Div/0"
            state.total = state.total / cur
        else:
            return False, "Erro: operação desconhecida"
    except Exception:
        return False, "Erro"
    return True, state.total

# Manipulador de cliques
def handle_click(char):
    # Limpar
    if char == 'C':
        state.current_display = '0'
        state.total = 0.0
        state.last_operation = None
        state.new_num = True
        state.error = False
        return

    # Se estamos em estado de erro, qualquer tecla (exceto C) reinicia a entrada
    if state.error:
        state.current_display = '0'
        state.total = 0.0
        state.last_operation = None
        state.new_num = True
        state.error = False

    # Operadores
    if char in ['+', '-', '*', '/']:
        # Se o usuário acabou de inserir um número, aplicamos a operação anterior
        if not state.new_num:
            success, result = calculate_operation()
            if not success:
                state.current_display = result
                state.error = True
                state.last_operation = None
                state.new_num = True
                return
            # atualiza visor com resultado parcial
            state.current_display = format_number(result)
        else:
            # usuário pressionou operador duas vezes: apenas atualiza o operador
            # se não houver total definido (ex: começou com 0), definimos total com o visor
            if state.last_operation is None:
                val = safe_float(state.current_display)
                state.total = val if val is not None else 0.0

        state.last_operation = char
        state.new_num = True
        return

    # Igual
    if char == '=':
        if state.last_operation is None:
            # nada a calcular
            state.current_display = format_number(safe_float(state.current_display) or 0.0)
            state.new_num = True
            return
        success, result = calculate_operation()
        if not success:
            state.current_display = result
            state.error = True
            state.last_operation = None
            state.new_num = True
            return
        # mostra resultado final e reseta operação
        state.current_display = format_number(result)
        state.last_operation = None
        state.new_num = True
        return

    # Entrada numérica (0-9 e ponto)
    if state.new_num:
        # iniciar nova entrada
        if char == '.':
            state.current_display = '0.'
        else:
            state.current_display = str(char)
        state.new_num = False
    else:
        # evitar múltiplos pontos
        if char == '.' and '.' in state.current_display:
            return
        # evitar zeros à esquerda desnecessários
        if state.current_display == '0' and char != '.':
            state.current_display = str(char)
        else:
            state.current_display += str(char)

# Interface
st.title("🔢 Calculadora Python")
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-puJcpOvnq50F4JR1O-g_mscVBpo25OmFEA&s', width=300)

# Visor (usar st.metric para estilo, mas garantir string)
display_value = state.current_display
st.metric(label="Resultado", value=display_value)

st.divider()

# Botões
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '.', '='],
    # linha extra para somar e limpar se desejar (opcional)
]

for row in buttons:
    cols = st.columns(4)
    for col, char in zip(cols, row):
        col.button(char, on_click=handle_click, args=[char], use_container_width=True)

st.caption("Desenvolvido com Streamlit — versão otimizada")
