import streamlit as st
import pandas as pd 
import time
table = pd.DataFrame({"Column 1": [1,2,3,4,5,6,7], "Column 2": [11,12,13,14,15,16,17]})
st.markdown("""
<style>
    .css-1a1tcp.e1ewe7hr3
    
    {
        visibility: hidden;
    }
    .css-h5rgaw.e1g8pov61
    {
        visibility: hidden;
    }    
</style>
""",unsafe_allow_html=True)
st.title("Hi I am StreamList WebApp")
st.subheader("Hi I am the SubHeader")
st.header("I am the Header")
st.text("I am the Text here")
st.markdown("**Hello World** i am Markdown")
st.markdown("[Google](https://www.google.com)")
st.markdown("---")
# st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
json={"a":"1,2,3","b":"4,5,6"}
st.json(json)
code ="""
print(Hello world!)
def funct():
    return 0;"""

st.code(code,language="python")
st.write("## H2 TAG") #SWISS Amry Knife
#-1 is a superscript done by hitting tab when mouse pointer is after 1
st.metric(label="Wind Speed",value="120ms⁻¹", delta="1.4ms⁻¹")
st.metric(label="Heat Wave",value="120ms⁻¹", delta="-1.4ms⁻¹")

#Create Data Frame
st.table(table)
st.dataframe(table)

st.image("sample.png", caption="This is my image", width=680)
st.video("GetAdminSigninOptions.js.mp4")
st.audio("kick-bass.mp3")

# How to remove hamburger and other things
st.markdown("---")
images=st.file_uploader("Please Upload an Image")
if images in images:
    for image in images:
        st.image(image)
val = st.time_input("Set Timer")
print(val)
bar = st.progress(0)
for i in range(10):
    bar.progress((i+1)*10)
    time.sleep(1)