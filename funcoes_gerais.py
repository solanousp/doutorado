import pandas as pd


def ler_dat_espectro(caminho_arquivo: str) -> pd.DataFrame:
    """
    Lê um arquivo .dat com duas colunas:
    channel counts
    """
    df = pd.read_csv(
        caminho_arquivo,
        sep=r"\s+",
        comment="#",
        header=None,
        names=["channel", "counts"],
        usecols=[0, 1],
        engine="python"
    )

    df["channel"] = pd.to_numeric(df["channel"], errors="coerce")
    df["counts"] = pd.to_numeric(df["counts"], errors="coerce")

    df = df.dropna(subset=["channel", "counts"]).reset_index(drop=True)

    df["channel"] = df["channel"].astype(int)
    df["counts"] = df["counts"].astype(float)

    return df


def resumir_espectro(df: pd.DataFrame) -> dict:
    """
    Retorna um resumo simples do espectro.
    """
    return {
        "n_canais": int(len(df)),
        "canal_min": int(df["channel"].min()),
        "canal_max": int(df["channel"].max()),
        "counts_total": float(df["counts"].sum()),
        "counts_max": float(df["counts"].max()),
        "canal_pico_global": int(df.loc[df["counts"].idxmax(), "channel"]),
    }
        
def aplicar_roi(df, canal_min=0, canal_max=500):
    """
    Aplica uma região de interesse (ROI) ao espectro.
    """
    return df[
        (df["channel"] >= canal_min) &
        (df["channel"] <= canal_max)
    ].reset_index(drop=True)


def remover_ultimos_percentual_canais(
    df: pd.DataFrame,
    percentual: float = 0.10
) -> pd.DataFrame:
    """
    Remove os últimos 'percentual' dos canais do espectro.

    Exemplo:
    percentual=0.10 remove os últimos 10% dos canais.
    """
    if not 0 <= percentual < 1:
        raise ValueError("percentual deve estar entre 0 e 1.")

    canal_max = int(df["channel"].max())
    canal_corte = int(canal_max * (1 - percentual))

    return df[df["channel"] <= canal_corte].reset_index(drop=True)


