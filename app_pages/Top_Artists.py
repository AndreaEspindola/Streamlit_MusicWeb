import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.image("images/logo_encabezado.png", width=80) 
    st.title("🎨 Top Artists")
    st.write("Explore the most popular artists from the dataset.")
    
    # Load data
    df = pd.read_csv("new_spotify-2023-corrected-dos.csv", encoding="ISO-8859-1")

    # Count the number of songs per artist
    artist_counts = df['artist(s)_name'].value_counts().head(10)

    # Display the top artists
    st.subheader("Top 10 Artists with the Most Songs in the Dataset")
    st.dataframe(artist_counts.reset_index().rename(columns={'index': 'Artist', 'artist(s)_name': 'Number of Songs'}))

    # Create a bar chart for top artists
    st.subheader("Artists with the Most Songs Chart")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(artist_counts.index, artist_counts.values, color='coral')
    ax.set_xlabel("Number of Songs")
    ax.set_ylabel("Artist")
    ax.set_title("Top 10 Artists with the Most Songs")
    ax.invert_yaxis()  # Invert the order to show the artist with the most songs at the top
    st.pyplot(fig)
    
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


