import streamlit as st
import math

st.set_page_config(page_title="Calculadora Streamlit", page_icon="🧮", layout="centered")

st.title("Calculadora em Streamlit")
st.write("Uma calculadora simples com histórico usando `st.session_state`.")

# Inicializa histórico
if "history" not in st.session_state:
    st.session_state.history = []

# Entrada de valores
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Valor A", value=0.0, format="%.8f")
with col2:
    b = st.number_input("Valor B", value=0.0, format="%.8f")

# Operações disponíveis
ops = {
    "Adicionar (+)": "+",
    "Subtrair (-)": "-",
    "Multiplicar (×)": "*",
    "Dividir (÷)": "/",
    "Potência (A^B)": "**",
    "Raiz quadrada de A": "sqrt_a",
    "Percentual (A% de B)": "percent",
    "Limpar histórico": "clear"
}
op = st.selectbox("Operação", list(ops.keys()))

# Executa operação
result = None
error = None

if st.button("Calcular"):
    key = ops[op]
    try:
        if key == "+":
            result = a + b
        elif key == "-":
            result = a - b
        elif key == "*":
            result = a * b
        elif key == "/":
            if b == 0:
                raise ZeroDivisionError("Divisão por zero")
            result = a / b
        elif key == "**":
            result = a ** b
        elif key == "sqrt_a":
            if a < 0:
                raise ValueError("Raiz de número negativo")
            result = math.sqrt(a)
        elif key == "percent":
            # calcula A% de B -> (A/100) * B
            result = (a / 100.0) * b
        elif key == "clear":
            st.session_state.history = []
            st.success("Histórico limpo.")
        # registra no histórico se houver resultado numérico
        if result is not None:
            entry = f"{a} {key} {b} = {result}" if key not in ("sqrt_a", "clear", "percent") else (
                f"sqrt({a}) = {result}" if key == "sqrt_a" else f"{a}% de {b} = {result}"
            )
            st.session_state.history.insert(0, entry)
    except Exception as e:
        error = str(e)

# Mostra resultado ou erro
if error:
    st.error(f"Erro: {error}")
elif result is not None:
    st.success(f"Resultado: **{result}**")

# Mostra histórico
st.subheader("Histórico")
if st.session_state.history:
    for i, h in enumerate(st.session_state.history[:20], start=1):
        st.write(f"{i}. {h}")
else:
    st.write("Nenhum cálculo registrado ainda.")

# Pequenas dicas
st.markdown("---")
st.write("Dicas: use a operação Potência para exponenciação; escolha Raiz quadrada para extrair raiz de A; use Percentual para calcular A% de B.")
