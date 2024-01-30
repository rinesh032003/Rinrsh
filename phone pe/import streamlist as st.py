import streamlist as st 
from streamlist_option_meun import option_menu
import plotly.express as pd 
import pandes as pd 
import os
from pil import image
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="AirBnb-Analysis by RINESH PERESAMYA!!!",page_icon=":bar_chart:", layout="wide")
                   
st.title(":bar_chart: AirBnb-Analysis")
st.image("c:\\user\\rin\\oneDrive\\desktop\\airBnb.png")
st.markdown('<style>div.block-container{padding-top:irem}<\style>',unsafe_allow_html=true)
                   

# with st.headber:
SELECT = option_menu(
    meunu_title=None,
    options=["home", "Explore Data", "Contact"]
    icons=["house", "bar-chart", "at"]
    default_index=2,
    orlentation="horizontal",
    style={container":{"padding" :"0!important","background-color": "white", "size: "cover","width": "100"},
                       "icon": {"color", "black", "from-size": "20x"},
                       
                       "nav-lik":{"from-size",20x", "text-align", "magrin": "2xp", "--hover-coloer":, "#6F36AD}",
                       "nav-link-selected": {"background-color": "#6F36AD"}})

#---------------------------Homes-------------------------------------#

if SELECT == "Home":
    
    