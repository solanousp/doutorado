import matplotlib.pyplot as plt


def plotar_espectro(df, titulo="Espectro bruto"):
    plt.figure(figsize=(12, 6))
    plt.plot(df["channel"], df["counts"])
    plt.xlabel("Canal")
    plt.ylabel("Contagens")
    plt.title(titulo)
    plt.grid(alpha=0.3)

    nome = titulo.replace(" ", "_").replace("/", "_").lower()
    plt.savefig(f"exports/{nome}.png", dpi=300)

    plt.show()


def comparar_espectros(espectros, titulo="Comparação dos espectros"):

    plt.figure(figsize=(12, 6))

    for df, nome in espectros:

        # normalização em Y
        counts_norm = df["counts"] / df["counts"].max()

        # normalização em X
        x = df["channel"]
        x_norm = (x - x.min()) / (x.max() - x.min())

        plt.plot(x_norm, counts_norm, label=nome)

    plt.xlabel("Canal normalizado")
    plt.ylabel("Contagens normalizadas")
    plt.title(titulo)
    plt.legend()
    plt.grid(alpha=0.3)

    nome = titulo.replace(" ", "_").replace("/", "_").lower()
    plt.savefig(f"exports/{nome}.png", dpi=300)

    plt.show()