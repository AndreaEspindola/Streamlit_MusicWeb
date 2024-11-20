import streamlit as st
from streamlit_option_menu import option_menu
from app_pages import Home, Top_Artists, Trends_by_Release_Year, Top_Songs

st.set_page_config(
    page_title="Music App",
    layout="wide",
    page_icon="💫"
)


# Configuración del menú en el sidebar
with st.sidebar:
    
    # Imagen de perfil centrada con columnas
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("images/logo.png", width=140)

    # Información del usuario
    st.markdown("""
    <div class="user-info" style="text-align: center; padding: 2px 0;">
        <strong style="font-size: 17px;">Ale Espindola</strong><br>
        <span style="font-size: 14px; color: gray;">A91639288@gmail.com</span><br>
    </div>
    """, unsafe_allow_html=True)

    # Menú de navegación con título e ícono centrados
    selected = option_menu(
        
        menu_title="Popular Music",
        options=["Home", "Top Artists", "Trends by Release Year", "Top Songs"],
        icons=["house", "bar-chart", "calendar"], 
        menu_icon="headphones",
        default_index=0,
        styles={
            "container": {"padding": "2px", "background-color": "#f0f2f6"},
            "icon": {"color": "#80233F", "font-size": "25px"},
            "nav-link": {
                "font-size": "15px", 
                "text-align": "left", 
                "padding": "2px 10px",
                "margin": "2px 0px", 
                "--hover-color": "#eee"
            },
            "nav-link-selected": {
                "background-color": "#DE5D83", 
                "color": "white",             
                "font-weight": "bold"  
                },
            "menu-title": {
                "font-size": "17px",
                "font-weight": "bold",
                "text-align": "center",
                "margin": "0px",
                "color": "#333",
            }
        }
    )
          
# Enrutamiento de páginas
if selected == "Home":
    Home.main()
elif selected == "Top Artists":
    Top_Artists.main()   
elif selected == "Playlist Analysis":
    Playlist_Analysis.main()  
elif selected == "Top Songs":
    Top_Songs.main()
elif selected == "Trends by Release Year":
    Trends_by_Release_Year.main()


