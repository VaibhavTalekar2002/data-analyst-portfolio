import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Vaibhav Talekar | Data Analyst", layout="wide")

# ---------- ADVANCED UI CSS ----------

st.markdown("""
<style>

<style>

header {visibility: hidden;}
[data-testid="stToolbar"] {display:none;}
[data-testid="stDecoration"] {display:none;}
[data-testid="stStatusWidget"] {visibility:hidden;}

.block-container{
padding-top:1rem;
padding-left:3rem;
padding-right:3rem;
}

.stApp{
background: linear-gradient(-45deg,#141e30,#243b55,#1c1c1c,#0f2027);
background-size:400% 400%;
animation: gradient 12s ease infinite;
color:white;
font-family:'Segoe UI';
margin-top:-60px;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.title{
font-size:72px;
font-weight:800;
text-align:left;
letter-spacing:1px;
background: linear-gradient(90deg,#00F5A0,#00D9F5,#FC00FF);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
margin-bottom:5px;
}

.subtitle{
font-size:26px;
text-align:left;
color:#cfcfcf;
font-weight:500;
}

.exp-text{
font-size:18px;
text-align:left;
color:#8fd3ff;
margin-top:6px;
}
            
.card{
background: linear-gradient(145deg,rgba(255,255,255,0.08),rgba(255,255,255,0.02));
padding:18px;
border-radius:16px;
backdrop-filter: blur(14px);
box-shadow:0 10px 35px rgba(0,0,0,0.4);
text-align:center;
transition: all 0.35s ease;
border:1px solid rgba(255,255,255,0.08);
position:relative;
overflow:hidden;
}

.card:before{
content:"";
position:absolute;
top:-2px;
left:-2px;
right:-2px;
bottom:-2px;
background: linear-gradient(90deg,#00F5A0,#00D9F5,#FC00FF);
z-index:-1;
filter: blur(20px);
opacity:0;
transition:0.3s;
}

.card:hover:before{
opacity:0.6;
}

.card:hover{
transform: translateY(-8px) scale(1.03);
}
.metric{
font-size:34px;
font-weight:800;
background: linear-gradient(90deg,#00F5A0,#00D9F5,#FC00FF);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.card-text{
font-size:14px;
color:#cfcfcf;
margin-top:4px;
}

            
/* ---------- FLIP CARD ---------- */

.flip-card {
width:100%;
max-width:700px;
height:260px;
margin:auto;
perspective:1000px;
}

.flip-card-inner {
position:relative;
width:100%;
height:100%;
text-align:center;
transition:transform 0.8s;
transform-style:preserve-3d;
}

.flip-card:hover .flip-card-inner {
transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
position:absolute;
width:100%;
height:100%;
border-radius:18px;
backface-visibility:hidden;
padding:30px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
}

.flip-card-front{
background: linear-gradient(145deg,rgba(255,255,255,0.08),rgba(255,255,255,0.03));
box-shadow:0 8px 32px rgba(0,0,0,0.37);
}

.flip-card-back{
background: linear-gradient(135deg,#00dbde,#fc00ff);
color:white;
transform: rotateY(180deg);
}

.skill-title{
font-size:26px;
font-weight:600;
margin-bottom:20px;
}

.skill-list{
font-size:18px;
line-height:1.8;
}

.project{
background: linear-gradient(145deg,rgba(255,255,255,0.08),rgba(255,255,255,0.03));
padding:30px;
border-radius:18px;
backdrop-filter: blur(12px);
box-shadow:0 15px 35px rgba(0,0,0,0.4);
transition: all 0.35s ease;
border:1px solid rgba(255,255,255,0.12);
}

.project:hover{
transform: translateY(-10px);
box-shadow:0 0 30px rgba(0,255,200,0.5);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.skill-container{
display:grid;
grid-template-columns: repeat(3,1fr);
gap:25px;
margin-top:20px;
}

.skill-card{
background: linear-gradient(145deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02));
border-radius:18px;
padding:25px;
text-align:center;
transition: all 0.35s ease;
border:1px solid rgba(255,255,255,0.1);
box-shadow:0 10px 30px rgba(0,0,0,0.3);
}

.skill-card:hover{
transform: translateY(-8px) scale(1.05);
box-shadow:0 0 25px rgba(0,255,200,0.6);
border:1px solid rgba(0,255,200,0.7);
}

.skill-icon{
font-size:40px;
margin-bottom:10px;
}

.skill-name{
font-size:20px;
font-weight:600;
margin-bottom:5px;
}

.skill-level{
font-size:16px;
opacity:0.8;
}

</style>
            
<style>

.skill-progress-container{
margin-top:20px;
}

.skill-row{
margin-bottom:22px;
}

.skill-label{
font-size:18px;
font-weight:600;
margin-bottom:6px;
}

.skill-bar{
width:100%;
height:12px;
background:rgba(255,255,255,0.06);
border-radius:30px;
overflow:hidden;
box-shadow: inset 0 0 6px rgba(0,0,0,0.5);
}
            
.skill-fill{
height:100%;
border-radius:20px;
background: linear-gradient(90deg,#00F5A0,#00D9F5,#FC00FF);
animation: load 2s ease-in-out;
box-shadow:0 0 10px rgba(0,255,200,0.6);
}

@keyframes load{
0%{width:0;}
}

</style>
            
""", unsafe_allow_html=True)



# ---------- HEADER ----------

st.markdown(
"""
<div style="margin-top:40px;margin-bottom:30px">

<p class="title">Vaibhav Talekar</p>

<p class="subtitle">
Data Analyst • SQL • Python • Power BI
</p>

<p class="exp-text">
2.5 Years Experience in Data Analytics
</p>

</div>
""",
unsafe_allow_html=True
)

# ---------- KPI CARDS ----------

# Row 1
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('''
    <div class="card">
    <div class="metric">2.5</div>
    <div class="card-text">Years Experience</div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="card">
    <div class="metric">9/10</div>
    <div class="card-text">SQL</div>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown('''
    <div class="card">
    <div class="metric">7/10</div>
    <div class="card-text">Python</div>
    </div>
    ''', unsafe_allow_html=True)

st.write("")  # spacing between rows


# Row 2
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown('''
    <div class="card">
    <div class="metric">2.5</div>
    <div class="card-text">Dashboard Experience</div>
    </div>
    ''', unsafe_allow_html=True)


with col5:
    st.markdown('''
    <div class="card">
    <div class="metric">7.25</div>
    <div class="card-text">LPA Current</div>
    </div>
    ''', unsafe_allow_html=True)

with col6:
    st.markdown('''
    <div class="card">
    <div class="metric">9.5</div>
    <div class="card-text">LPA Expected</div>
    </div>
    ''', unsafe_allow_html=True)

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

# ---------- TECHNICAL SKILLS ----------

st.markdown('<p class="section-title">Technical Skill Analysis</p>', unsafe_allow_html=True)

st.markdown("""

<div class="skill-progress-container">

<div class="skill-row">
<div class="skill-label">SQL — 90%</div>
<div class="skill-bar">
<div class="skill-fill" style="width:90%"></div>
</div>
</div>

<div class="skill-row">
<div class="skill-label">Python — 70%</div>
<div class="skill-bar">
<div class="skill-fill" style="width:70%"></div>
</div>
</div>

<div class="skill-row">
<div class="skill-label">Power BI — 80%</div>
<div class="skill-bar">
<div class="skill-fill" style="width:80%"></div>
</div>
</div>

<div class="skill-row">
<div class="skill-label">Automation — 80%</div>
<div class="skill-bar">
<div class="skill-fill" style="width:80%"></div>
</div>
</div>

<div class="skill-row">
<div class="skill-label">Predictive Analytics — 70%</div>
<div class="skill-bar">
<div class="skill-fill" style="width:70%"></div>
</div>
</div>

</div>

""", unsafe_allow_html=True)

# ---------- PROJECT ----------

st.markdown('<p class="section-title">Key Project</p>', unsafe_allow_html=True)

st.markdown("""
<div class="project">

<h3>Finlytizs Automation Project</h3>

<b>Problem</b><br>
Manual reporting workflows required repetitive effort and time.

<br>

<b>Solution</b><br>
Developed SQL automation scripts and optimized SQL queries  
to streamline reporting processes using Jasper Reports.

<br>

<b>Impact</b>

<ul>
<li>Reduced manual workload</li>
<li>Faster report generation</li>
<li>Improved data accuracy</li>
</ul>

</div>
""", unsafe_allow_html=True)

# ---------- WORK STYLE ----------

st.markdown('<p class="section-title">Work Style</p>', unsafe_allow_html=True)

st.markdown("""
<div class="project">

✔ Comfortable working independently once requirements are defined  

✔ Experienced in building Power BI dashboards and business reports  

✔ Developed automation scripts using Python & SQL  

✔ Exposure to predictive analytics and data modeling  

</div>
""", unsafe_allow_html=True)

# ---------- CONTACT ----------

st.markdown('<p class="section-title">Contact</p>', unsafe_allow_html=True)

st.markdown("""
<div class="project">

📧 Email: vtalekar0734@gmail.com  

🔗 LinkedIn: https://www.linkedin.com/in/vaibhav-talekar-37056224b/ 
 
</div>
""", unsafe_allow_html=True)