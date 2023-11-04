import streamlit as s
s.title("SUNSTAR")
s.subheader("SUNSTAR ENGINEERING THAILAND")
s.header("GRINDING")
s.text("DISPLAY REALTIME STATUS FROM NISSEI MACHINE")
s.markdown("**NISSEI** *MACHINE* DETAILS")
s.markdown("# MACHINE")
s.markdown("## MACHINE")
s.markdown("---")
s.markdown("[GOOGLE](https://www.google.com/)")
s.caption("THIS IS CAPTION")
s.latex(r"\begin{pmatrix}a&b \\c&d\end{pmatrix}")
json={"a":"1,2,3","b":"4,5,6"}
s.json(json)
code="""
print("Hello")
def funct()
    return 0;"""
s.code(code,language="python")
s.write("## H2")
s.metric(Label="Wind Speed",value="120ms\^-1",delta="1.4ms\^-1")
