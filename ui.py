import streamlit as st
import pandas as pd
from equacao import Equação
class InicioUI:
    def main():
        st.header("Calculos com Bhaskara")
        a = st.text_input("A")
        b = st.text_input("B")
        c = st.text_input("C")
        if st.button("Calcular"):
            e = Equação(float(a), float(b), float(c))
            st.write(e.calc_delta())
            st.write(e.calc_x1())
            st.write(e.calc_x2())
            e.calc_p()
            grafico = pd.DataFrame(
             {
              "col1": e.get_px(),
              "col2": e.get_py(),
             }
            )
            

            st.line_chart(grafico, x="col1", y="col2")
