import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Título e introducción
    st.image("images/logo_encabezado.png", width=80)
    st.title("🎵 Music Analytics Dashboard")
    st.write("Welcome! Explore the most popular songs and artists, discover trends, and analyze the dataset's key insights.")
    
    # Cargar datos
    df = pd.read_csv("new_spotify-2023-corrected-dos.csv", encoding="ISO-8859-1")

    # Estadísticas clave
    total_songs = len(df)
    total_streams = df['streams'].sum()
    top_artist = df['artist(s)_name'].value_counts().idxmax()

    # Mostrar estadísticas clave
    st.subheader("Key Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Songs", total_songs)
    col2.metric("Total Streams", f"{total_streams:,}")
    col3.metric("Top Artist", top_artist)

    # Gráfica de distribución por año de lanzamiento
    st.subheader("Distribution of Songs by Release Year")
    if 'released_year' in df.columns:
        release_year_counts = df['released_year'].value_counts().sort_index()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(release_year_counts.index, release_year_counts.values, color='mediumpurple')
        ax.set_xlabel("Year")
        ax.set_ylabel("Number of Songs")
        ax.set_title("Songs Released per Year")
        st.pyplot(fig)
    else:
        st.write("The dataset does not contain a 'released_year' column.")
        
    st.markdown(
    """
    <style>
    /* Footer fijo en la parte inferior */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #FFC0CB; /* Color rosa */
        color: white;
        text-align: right;
        padding: 10px;
        font-size: 14px;
    }
    /* Ajuste del padding inferior para que no se superponga el contenido con el footer */
    .main > div {
        padding-bottom: 50px;
    }
    </style>
    <div class="footer">
        Ale Espindola &copy; 2024
    </div>
    """,
    unsafe_allow_html=True
    )

