import streamlit as st

st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")
st.title("Calculadora com botões")

# Helpers
def format_number(n, max_chars=12):
    """Formata número para exibição: remove zeros finais e limita tamanho."""
    try:
        # se for inteiro, mostra sem ponto
        if float(n).is_integer():
            s = str(int(float(n)))
        else:
            # mostra até 8 casas decimais, remove zeros finais
            s = f"{float(n):.8f}".rstrip("0").rstrip(".")
    except Exception:
        s = str(n)
    # corta se muito longo, mantendo notação simples
    if len(s) > max_chars:
        # tenta notação científica curta
        s = f"{float(n):.6e}"
    return s

# Inicializa estado
if "display" not in st.session_state:
    st.session_state.display = "0"
if "operand" not in st.session_state:
    st.session_state.operand = None
if "operator" not in st.session_state:
    st.session_state.operator = None
if "reset_next" not in st.session_state:
    st.session_state.reset_next = False

# Funções de ação
def press_digit(d):
    if st.session_state.reset_next or st.session_state.display == "0":
        st.session_state.display = d
        st.session_state.reset_next = False
    else:
        # evita overflow de caracteres
        if len(st.session_state.display) < 16:
            st.session_state.display += d

def press_dot():
    if st.session_state.reset_next:
        st.session_state.display = "0."
        st.session_state.reset_next = False
    elif "." not in st.session_state.display:
        st.session_state.display += "."

def clear_all():
    st.session_state.display = "0"
    st.session_state.operand = None
    st.session_state.operator = None
    st.session_state.reset_next = False

def backspace():
    if st.session_state.reset_next:
        st.session_state.display = "0"
        st.session_state.reset_next = False
    else:
        s = st.session_state.display
        if len(s) <= 1:
            st.session_state.display = "0"
        else:
            st.session_state.display = s[:-1]

def set_operator(op):
    try:
        st.session_state.operand = float(st.session_state.display)
    except:
        st.session_state.operand = 0.0
    st.session_state.operator = op
    st.session_state.reset_next = True

def calculate():
    if st.session_state.operator is None or st.session_state.operand is None:
        return
    try:
        a = st.session_state.operand
        b = float(st.session_state.display)
        op = st.session_state.operator
        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            res = a / b
        elif op == "**":
            res = a ** b
        else:
            res = b
        st.session_state.display = format_number(res)
    except ZeroDivisionError:
        st.session_state.display = "Erro: divisão por 0"
    except Exception:
        st.session_state.display = "Erro"
    finally:
        st.session_state.operator = None
        st.session_state.operand = None
        st.session_state.reset_next = True

# Visor
st.markdown("**Visor**")
st.write(f"<div style='font-size:32px; padding:10px; background:#f5f5f5; border-radius:6px; text-align:right'>{format_number(st
