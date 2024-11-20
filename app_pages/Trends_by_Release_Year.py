import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.image("images/logo_encabezado.png", width=80)
    st.title("📅 Trends by Release Year")
    st.write("Analyze how song releases and their popularity have evolved over the years.")

    # Cargar datos
    df = pd.read_csv("new_spotify-2023-corrected-dos.csv", encoding="ISO-8859-1")

    # Verificar si la columna 'released_year' existe
    if 'released_year' in df.columns:
        # Agregar slider para seleccionar el rango de años
        min_year = int(df['released_year'].min())
        max_year = int(df['released_year'].max())
        year_range = st.slider(
            "Select the year range:",
            min_value=min_year,
            max_value=max_year,
            value=(min_year, max_year),
        )

        # Filtrar el dataset por rango de años
        filtered_df = df[(df['released_year'] >= year_range[0]) & (df['released_year'] <= year_range[1])]

        # Gráfico: Evolución de canciones por año
        st.subheader("Number of Songs Released by Year")
        songs_per_year = filtered_df['released_year'].value_counts().sort_index()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(songs_per_year.index, songs_per_year.values, marker='o', color='dodgerblue')
        ax.set_xlabel("Year")
        ax.set_ylabel("Number of Songs")
        ax.set_title("Song Releases Over the Years")
        st.pyplot(fig)

        # Gráfico: Streams acumulados por año
        st.subheader("Total Streams by Year")
        streams_per_year = filtered_df.groupby('released_year')['streams'].sum()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(streams_per_year.index, streams_per_year.values, color='darkorange')
        ax.set_xlabel("Year")
        ax.set_ylabel("Total Streams")
        ax.set_title("Total Streams Over the Years")
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