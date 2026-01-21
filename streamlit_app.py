import streamlit as st

st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

# --- Helpers ---
def format_number_str(s, max_chars=12):
    """Formata string numérica para exibição curta."""
    try:
        val = float(s)
        if val.is_integer():
            out = str(int(val))
        else:
            out = f"{val:.8f}".rstrip("0").rstrip(".")
    except Exception:
        out = str(s)
    if len(out) > max_chars:
        try:
            out = f"{float(s):.6e}"
        except Exception:
            out = out[:max_chars]
    return out

# --- Estado inicial ---
if "display" not in st.session_state:
    st.session_state.display = "0"
if "operand" not in st.session_state:
    st.session_state.operand = None
if "operator" not in st.session_state:
    st.session_state.operator = None
if "reset_next" not in st.session_state:
    st.session_state.reset_next = False

# --- Ações ---
def press_digit(d):
    disp = st.session_state.display
    if st.session_state.reset_next or disp == "0":
        st.session_state.display = d
        st.session_state.reset_next = False
    else:
        if len(disp) < 16:
            st.session_state.display = disp + d

def press_dot():
    if st.session_state.reset_next:
        st.session_state.display = "0."
        st.session_state.reset_next = False
    elif "." not in st.session_state.display:
        st.session_state
