from funcoes_gerais import (
    ler_dat_espectro,
    resumir_espectro,
    aplicar_roi
)

from visualizacao import (
    plotar_espectro,
    comparar_espectros
)


def main():

    arquivos = {
        "Ba-133": "dados/Ba133_teste_001_eh_0.dat",
        "Cs-137": "dados/Cs137_teste_001_eh_0.dat",
        "Na-22": "dados/Na22_teste_001_eh_0.dat",
        "Na-22/CS-137": "dados/Na22_Cs137_001_eh_0.dat",
        "BG": "dados/SemFonte_001_eh_0.dat"
    }

    rois = {
        "Ba-133": (0, 49),          # ajuste aqui
        "Cs-137": (0, 350),
        "Na-22": (0, 300),
        "Na-22/CS-137": (0, 350),
        "BG": (0, 500)
    }

    espectros = []

    for nome, caminho in arquivos.items():

        df = ler_dat_espectro(caminho)

        canal_min, canal_max = rois[nome]
        df_roi = aplicar_roi(df, canal_min=canal_min, canal_max=canal_max)

        print(f"\n=== {nome} ===")
        print(f"ROI: {canal_min} a {canal_max}")
        print(resumir_espectro(df_roi))

        plotar_espectro(
            df_roi,
            titulo=f"{nome} - espectro ROI"
        )

        espectros.append((df_roi, nome))

    comparar_espectros(
        espectros,
        titulo="Comparação dos espectros (ROI)"
    )


if __name__ == "__main__":
    main()