import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.image("images/logo_encabezado.png", width=80) 
    st.title("🎵 Top Songs")
    st.write("Explore the most popular songs from the dataset.")
    
    # Load data
    df = pd.read_csv("new_spotify-2023-corrected-dos.csv", encoding="ISO-8859-1")

    # Clean the 'streams' column
    if 'streams' in df.columns:
        df['streams'] = df['streams'].astype(str)
        df['streams'] = df['streams'].str.replace(r'[^\d]', '', regex=True)
        df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
        df = df.dropna(subset=['streams'])
        df['streams'] = df['streams'].astype(int)

    # Select the number of songs to display
    top_n = st.slider("Select the number of songs to display:", min_value=5, max_value=50, value=10)

    # Display the most popular songs
    top_songs = df.nlargest(top_n, 'streams')[['track_name', 'artist(s)_name', 'streams']]
    st.subheader(f"Top {top_n} Songs by Streams")
    st.dataframe(top_songs)

    # Create a horizontal bar chart for top songs
    st.subheader("Most Popular Songs Chart")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_songs['track_name'], top_songs['streams'], color='skyblue')
    ax.set_xlabel("Number of Streams")
    ax.set_ylabel("Song")
    ax.set_title(f"Top {top_n} Most Popular Songs")
    ax.invert_yaxis()  # Invert the order to show the most popular song at the top
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
