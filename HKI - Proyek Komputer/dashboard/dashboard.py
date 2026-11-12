import os

import kagglehub
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import base64

ICON_B64 = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAA6lBMVEVHcEz/AAD/AAD/AAD/AAD/AAD+AAD5AAD8AAD/AAD/AAD/AAD/AAD/AADSAAD9AAD0AADvAAD3AAD6AADIAAD/AADPAAD/AADSAAD/AAD/AAD+AADcAAD/AAD/AADjAAD1AAD/AAD/AAD/AAD+AAD/AADjAAD7AAD8AAD/AAD/AAD9AAD/AAD/AAD+AAD/AAD/AACQAAABAAD+AACbKAC0AAD9AAAA2QD////8AACzAACwVwz/wv8A+QAAaQDWAADlAAAA0gAAggD6AAD7AADFAADLAADgAADnAADKAACyAADjAAD7BQWbVwAZlqccAAAAMHRSTlMACQYMV1TvWlau+vzc95LqYV5bkbDmle6Zxe3utInXEmdZssf6UQmPuBKN6VurtFAhHxmFAAABpElEQVQ4y4VTiVbbQAzchAQCBXpQoOWmN5RDs6dNYnOUq9f//04l2SYJTWDe867tGY2ktWxMg1SmVGRZv29gJiClVJZlKoq/UwSiSOnqqkzTBAIUxeXTgtPuZdE/xAzf4n9ZuzsPIvpDtLOPCYIZgERAjoB5pb3nxVq1a3ffVzQDjt8cVLQoNDuHc6D33nmvDw1dC9h/nc39KgnldWnqsKLYFuvoZjXFpvA16yuL9gd2da4qweUbfA86bpvawpjPUh/gFlnjRCidPHRqrYRrf4wFFx3NOvpOdFSdHtiiI2fATGYzR7zQuIe1HXmuasgpShquGCcc7WuF2IOvFzFSfBndEgto5LQ7QkKNnYu6s0APoP6MgVRgoyjYUHuxtpYArRBwjfqdJswJI7wxbwPwg20Zg8EnNojMzg0PM3t9A9ze59LGYMC82IyNREubRi6pNRr4uDs6a4qAEM5/X1xIkYS5sWE0rZXzM4RfoQa+9R5PXOsN7vDzjME+4euEmQXX8Wp57d3Wnu19UddHfDNcvE36MdDM1jSBGRoY658TTOPt+F7hH6SZazOFUAaPAAAAAElFTkSuQmCC"

st.set_page_config(
    page_title="Dashboard Forensik Judi Online 2026",
    page_icon=base64.b64decode(ICON_B64),
    layout="wide",
)

sns.set_theme(style="whitegrid", palette="muted")

KATEGORI_JUDI_ONLINE = [
    "Dormant-Takeover-Syndicate",
    "Direct-Gambling-Collector-Mule",
    "Layering-Mule-Account",
]

DATASET_URL = (
    "https://www.kaggle.com/datasets/luthfimuthathohirin/"
    "indonesia-online-gambling-bank-accounts-forensics"
)

BIBTEX = """@dataset{muthathohirin2026online_gambling_forensics,
  author       = {Luthfi Muthathohirin},
  title        = {Indonesia Online Gambling Transactions and Money Mule Accounts: 2026 Forensic Benchmark},
  year         = {2026},
  publisher    = {Kaggle},
  url          = {https://www.kaggle.com/datasets/luthfimuthathohirin/indonesia-online-gambling-bank-accounts-forensics},
  license      = {Creative Commons Zero v1.0 Universal}
}"""


@st.cache_data(show_spinner="Mengunduh dan memuat dataset...")
def load_data():
    path = kagglehub.dataset_download(
        "luthfimuthathohirin/indonesia-online-gambling-bank-accounts-forensics"
    )
    csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]
    df = pd.read_csv(os.path.join(path, csv_files[0]))
    return df


df = load_data()

st.title("Dashboard Forensik Rekening Money Mule Judi Online 2026")
st.caption(
    "Dataset: Indonesia Online Gambling Bank Accounts Forensics (Kaggle). "
    "Data bersifat sintetis (benchmark riset yang dikalibrasi terhadap tipologi "
    "forensik publik PPATK, BI, OJK) — bukan data transaksi perbankan riil."
)

with st.sidebar:
    st.header("Filter Analisis")
    selected_risk = st.multiselect(
        "Klasifikasi risiko (subset terindikasi judi online)",
        options=KATEGORI_JUDI_ONLINE,
        default=KATEGORI_JUDI_ONLINE,
    )
    selected_institution = st.multiselect(
        "Jenis institusi",
        options=sorted(df["institution_type"].unique()),
        default=sorted(df["institution_type"].unique()),
    )
    st.markdown("---")
    st.markdown(
        "**Pertanyaan bisnis:**\n"
        "1. Kombinasi kanal x KYC paling berisiko\n"
        "2. Institusi dengan eksposur risiko tertinggi\n"
        "3. Indikator anomali paling dominan"
    )
    st.markdown("---")
    with st.expander("Sumber Data & Sitasi"):
        st.markdown(
            "**Dataset:** Indonesia Online Gambling Transactions and Money Mule "
            "Accounts: 2026 Forensic Benchmark  \n"
            "**Author:** Luthfi Muthathohirin (2026)  \n"
            "**Publisher:** Kaggle  \n"
            "**Lisensi:** Creative Commons Zero v1.0 Universal  \n"
            f"**URL:** [Kaggle — Indonesia Online Gambling Bank Accounts Forensics]({DATASET_URL})"
        )
        st.code(BIBTEX, language="bibtex")

if not selected_risk:
    st.warning("Pilih minimal satu klasifikasi risiko untuk memulai analisis.")
    st.stop()

high_risk_df = df[
    df["account_risk_classification"].isin(selected_risk)
    & df["institution_type"].isin(selected_institution)
].copy()
df_filtered = df[df["institution_type"].isin(selected_institution)].copy()

if high_risk_df.empty:
    st.warning("Tidak ada rekening yang cocok dengan kombinasi filter saat ini.")
    st.stop()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Rekening", f"{len(df_filtered):,}")
col2.metric("Rekening Terindikasi Judi Online", f"{len(high_risk_df):,}")
col3.metric(
    "Proporsi Berisiko",
    f"{len(high_risk_df) / len(df_filtered) * 100:.1f}%",
)
col4.metric(
    "Rata-rata Passthrough Velocity",
    f"{high_risk_df['passthrough_velocity_pct'].mean():.2f}%",
)

tab1, tab2, tab3 = st.tabs(
    [
        "Pertanyaan 1 — Kanal x KYC",
        "Pertanyaan 2 — Institusi",
        "Pertanyaan 3 — Indikator Anomali",
    ]
)

with tab1:
    st.subheader("Kombinasi kanal transaksi x status KYC paling berisiko")

    channel_kyc_agg = (
        high_risk_df.groupby(
            ["primary_transaction_channel", "kyc_verification_status"], observed=True
        )
        .agg(
            n_accounts=("account_id", "count"),
            avg_late_night_pct=("late_night_transaction_ratio", "mean"),
            avg_passthrough_pct=("passthrough_velocity_pct", "mean"),
        )
        .reset_index()
    )

    metric_choice = st.radio(
        "Metrik heatmap",
        options=[
            "avg_passthrough_pct",
            "avg_late_night_pct",
            "n_accounts",
        ],
        format_func=lambda x: {
            "avg_passthrough_pct": "Rata-rata Passthrough Velocity (%)",
            "avg_late_night_pct": "Rata-rata Late-Night Transaction Ratio (%)",
            "n_accounts": "Jumlah Rekening",
        }[x],
        horizontal=True,
    )

    pivot = channel_kyc_agg.pivot(
        index="kyc_verification_status",
        columns="primary_transaction_channel",
        values=metric_choice,
    )
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.heatmap(
        pivot,
        annot=True,
        fmt="d" if metric_choice == "n_accounts" else ".2f",
        cmap="Reds" if metric_choice != "n_accounts" else "Blues",
        linewidths=0.5,
        ax=ax,
    )
    ax.set_title("Kanal Transaksi x Status KYC — Rekening Terindikasi Judi Online")
    ax.set_xlabel("Kanal Transaksi Utama")
    ax.set_ylabel("Status Verifikasi KYC")
    st.pyplot(fig)
    plt.close(fig)

    st.dataframe(
        channel_kyc_agg.sort_values(metric_choice, ascending=False)
        .round(3)
        .reset_index(drop=True),
        use_container_width=True,
        hide_index=True,
    )
    st.info(
        "Passthrough velocity seragam tinggi (~97%) di semua kombinasi; "
        "pembeda prioritas adalah late-night ratio (tertinggi pada BI-FAST dengan "
        "KYC lemah) dan jumlah rekening (terbesar pada QRIS x rekening jual-beli)."
    )

with tab2:
    st.subheader("Jenis institusi dengan eksposur risiko tertinggi")

    institution_analysis = (
        df_filtered.groupby("institution_type", observed=True)
        .agg(total_accounts=("account_id", "count"))
        .join(
            high_risk_df.groupby("institution_type", observed=True).agg(
                high_risk_accounts=("account_id", "count"),
                avg_aml_risk_score=("aml_composite_risk_score", "mean"),
            )
        )
        .fillna(0)
    )
    institution_analysis["high_risk_pct"] = (
        institution_analysis["high_risk_accounts"]
        / institution_analysis["total_accounts"]
        * 100
    )
    institution_analysis = institution_analysis.sort_values(
        "high_risk_pct", ascending=False
    )

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    sns.barplot(
        data=institution_analysis.reset_index(),
        x="high_risk_pct",
        y="institution_type",
        hue="institution_type",
        palette="Reds_r",
        legend=False,
        ax=axes[0],
    )
    axes[0].set_title("Proporsi Rekening Berisiko per Institusi (%)")
    axes[0].set_xlabel("Proporsi (%)")
    axes[0].set_ylabel("")
    sns.barplot(
        data=institution_analysis.reset_index(),
        x="avg_aml_risk_score",
        y="institution_type",
        hue="institution_type",
        palette="Oranges_r",
        legend=False,
        ax=axes[1],
    )
    axes[1].set_title("Rata-rata AML Composite Risk Score (Rekening Berisiko)")
    axes[1].set_xlabel("Skor rata-rata")
    axes[1].set_ylabel("")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.dataframe(
        institution_analysis.round(2).reset_index(),
        use_container_width=True,
        hide_index=True,
    )
    st.info(
        "Digital Neo-Bank dan penyedia e-wallet memiliki proporsi rekening "
        "berisiko tertinggi (~33%); pembeda utama adalah jumlah/proporsi, "
        "bukan skor AML rata-rata yang relatif setara antar institusi."
    )

with tab3:
    st.subheader("Indikator anomali utama paling dominan")

    anomaly_analysis = (
        high_risk_df.groupby("primary_anomaly_indicator", observed=True)
        .agg(
            n_accounts=("account_id", "count"),
            avg_late_night_pct=("late_night_transaction_ratio", "mean"),
            avg_passthrough_pct=("passthrough_velocity_pct", "mean"),
            avg_aml_risk_score=("aml_composite_risk_score", "mean"),
        )
        .sort_values("n_accounts", ascending=False)
    )
    anomaly_analysis["share_pct"] = (
        anomaly_analysis["n_accounts"] / len(high_risk_df) * 100
    )

    fig, ax = plt.subplots(figsize=(12, 5))
    sns.barplot(
        data=anomaly_analysis.reset_index(),
        x="n_accounts",
        y="primary_anomaly_indicator",
        hue="primary_anomaly_indicator",
        palette="viridis",
        legend=False,
        ax=ax,
    )
    ax.set_title("Indikator Anomali Utama pada Rekening Terindikasi Judi Online")
    ax.set_xlabel("Jumlah rekening")
    ax.set_ylabel("")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.dataframe(
        anomaly_analysis.round(2).reset_index(),
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("**Komposisi klasifikasi risiko per indikator anomali**")
    crosstab = pd.crosstab(
        high_risk_df["primary_anomaly_indicator"],
        high_risk_df["account_risk_classification"],
    )
    fig, ax = plt.subplots(figsize=(12, 5))
    crosstab.plot(kind="barh", stacked=True, colormap="Set2", edgecolor="white", ax=ax)
    ax.set_title("Komposisi Klasifikasi Risiko per Indikator Anomali")
    ax.set_xlabel("Jumlah rekening")
    ax.set_ylabel("")
    ax.legend(title="Klasifikasi Risiko", bbox_to_anchor=(1.02, 1), loc="upper left")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.info(
        "Dormant-Sudden-High-Volume dan VPN-Proxy-Multi-Device-Churn mendominasi "
        "(~95% rekening berisiko); kasus VPN-Proxy eksklusif pada klasifikasi "
        "Dormant-Takeover-Syndicate."
    )

st.markdown("---")
st.caption(
    "Proyek Analisis Data — Alif Setyo Wisnuaji | Matematika S1, "
    "Fakultas Sains dan Matematika, Universitas Diponegoro"
)
