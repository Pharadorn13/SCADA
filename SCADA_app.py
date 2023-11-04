import streamlit as s
import pandas as p
table=p.DataFrame({"Machine Name":["NISSEI1","NISSEI2","NISSEI3","NISSEI4","NISSEI5","NISSEI6","NISSEI7","NISSEI8","NISSEI9","NISSEI10","NISSEI11","NISSEI12","NISSEI13"],"MACHINE NUMBER":["G-7018","G-7019","G-7026","G-7027","G-7028","G-7033","G-7049","G-7035","G-7036","G-7040","G-7041","G-7048","G-7054"]})
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
s.metric(label="Wind Speed",value="120ms\^-1",delta="1.4ms\^-1")
s.table(table)
s.dataframe(table)
<img src=Pic1.png>

