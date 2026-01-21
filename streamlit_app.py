import streamlit as st

st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")
st.title("Calculadora com botões")

# Helpers
def format_number(n, max_chars=12):
    """Formata número para exibição: remove zeros finais e limita tamanho."""
    try:
        val = float(n)
        if val.is_integer():
            s = str(int(val))
        else:
            s = f"{val:.8f}".rstrip("0").rstrip(".")
    except Exception:
        s = str(n)
    if len(s) > max_chars:
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
        if len(st.session_state.display) < 16:
            st.session_state.display += d

def press_dot():
    if st.session_state.reset_next:
        st.session_state.display = "0."
        st.session_state.reset_next = False
    elif "." not in st.session_state.display:
        st.session
