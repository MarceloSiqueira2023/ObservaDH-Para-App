import pandas as pd
import plotly.express as px
import streamlit as st

# --- Seção  IDOSOS ---
st.header(" IDOSOS")

# --- 0. População Total de Idosos ---
st.subheader("População Total de Idosos no Pará")

# Dados da População Idosa
total_idosos_pessoas = 876422
percentual_idosos_pop = 10.8
fonte_populacao_idosos = "IBGE 2022"

col_title_idosos, col_abs_idosos, col_perc_idosos = st.columns([3, 1, 1])

with col_title_idosos:
    st.markdown("###### Total da População Idosa no Pará")

with col_abs_idosos:
    st.metric(
        label="Número de Pessoas Idosas",
        value=f"{total_idosos_pessoas:,.0f}".replace(",", "."),
        delta=None
    )

with col_perc_idosos:
    st.metric(
        label="Percentual na População Total",
        value=f"{percentual_idosos_pop:.1f}%",
        delta=None
    )
st.caption(f"Fonte: {fonte_populacao_idosos}")
st.markdown("---")

# --- 1. EDUCAÇÃO ---
st.subheader("1. EDUCAÇÃO - Analfabetismo")

# Dados de Analfabetismo
data_analfabetismo_idosos = {
    'População': ['Branca', 'Negra', 'TOTAL'],
    'Analfabetismo (%)': [16.4, 27.9, 44.3]
}
df_analfabetismo_idosos = pd.DataFrame(data_analfabetismo_idosos)
fonte_analfabetismo_idosos = "IBGE 2022"

# Gráfico de Barras para Analfabetismo
fig_analfabetismo_idosos = px.bar(
    df_analfabetismo_idosos,
    x="População",
    y="Analfabetismo (%)",
    title="Taxa de Analfabetismo entre Idosos",
    labels={"Analfabetismo (%)": "Taxa (%)"},
    color="Analfabetismo (%)",
    color_continuous_scale=px.colors.sequential.Plotly3,
    text="Analfabetismo (%)"
)
fig_analfabetismo_idosos.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_analfabetismo_idosos.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_analfabetismo_idosos, use_container_width=True)
st.caption(f"Fonte: {fonte_analfabetismo_idosos}")
st.markdown("---")

# --- 2. EMPREGO ---
st.subheader("2. EMPREGO")

# Dados de Emprego
taxa_informalidade_idosos = 70.9
taxa_desocupacao_idosos = 9.0
fonte_emprego_idosos = "IBGE 2022"

col_informalidade_idosos, col_desocupacao_idosos = st.columns(2)

with col_informalidade_idosos:
    st.metric(
        label="Taxa de Informalidade",
        value=f"{taxa_informalidade_idosos:.1f}%",
        delta=None
    )

with col_desocupacao_idosos:
    st.metric(
        label="Taxa de Desocupação",
        value=f"{taxa_desocupacao_idosos:.1f}%",
        delta=None
    )
st.caption(f"Fonte: {fonte_emprego_idosos}")
st.markdown("---")

# --- 3. RENDIMENTO ---
st.subheader("3. RENDIMENTO")

# Dados de Rendimento
renda_idosos = 2157.00
fonte_rendimento_idosos = "IBGE 2022"

st.metric(
    label="Renda Média",
    value=f"R$ {renda_idosos:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), # Formatação para BRL
    delta=None
)
st.caption(f"Fonte: {fonte_rendimento_idosos}")
st.markdown("---")

# --- 4. ASSISTÊNCIA SOCIAL ---
st.subheader("4. ASSISTÊNCIA SOCIAL")

# Dados de Assistência Social - Números Absolutos e Percentuais
data_assistencia_social_idosos = {
    'Indicador': [
        'Total de Pessoas Idosas',
        'Total Beneficiárias do BPC',
        'Centro de Referência Especializado de Assistência Social'
    ],
    'Número Absoluto': [589093, 114023, 87],
    'Percentual (%)': [100.0, 19.0, 100.0]
}
df_assistencia_social_idosos = pd.DataFrame(data_assistencia_social_idosos)
fonte_assistencia_social_idosos = "Benefício de Prestação Continuada (BPC) e Sistema Único de Assistência Social (SUAS) 2022"

# Layout em colunas para os metrics
st.markdown("###### Visão Geral dos Benefícios e Estruturas")
col_as_1, col_as_2, col_as_3 = st.columns(3)

with col_as_1:
    st.metric(
        label=df_assistencia_social_idosos['Indicador'].iloc[0],
        value=f"{df_assistencia_social_idosos['Número Absoluto'].iloc[0]:,.0f}".replace(",", "."),
        delta=None
    )
    st.metric(
        label=f"{df_assistencia_social_idosos['Indicador'].iloc[0]} (%)",
        value=f"{df_assistencia_social_idosos['Percentual (%)'].iloc[0]:.0f}%",
        delta=None
    )

with col_as_2:
    st.metric(
        label=df_assistencia_social_idosos['Indicador'].iloc[1],
        value=f"{df_assistencia_social_idosos['Número Absoluto'].iloc[1]:,.0f}".replace(",", "."),
        delta=None
    )
    st.metric(
        label=f"{df_assistencia_social_idosos['Indicador'].iloc[1]} (%)",
        value=f"{df_assistencia_social_idosos['Percentual (%)'].iloc[1]:.0f}%",
        delta=None
    )

with col_as_3:
    st.metric(
        label=df_assistencia_social_idosos['Indicador'].iloc[2],
        value=f"{df_assistencia_social_idosos['Número Absoluto'].iloc[2]:.0f}",
        delta=None
    )
    st.metric(
        label=f"{df_assistencia_social_idosos['Indicador'].iloc[2]} (%)",
        value=f"{df_assistencia_social_idosos['Percentual (%)'].iloc[2]:.0f}%",
        delta=None
    )
st.caption(f"Fonte: {fonte_assistencia_social_idosos}")
st.markdown("---")

# --- 4.1. Percentual de CREAS que ofertaram serviços... ---
st.subheader("4.1. Percentual de CREAS que ofertaram serviços de proteção por tipo de violação/violência")

# Dados de Percentual de CREAS que ofertaram serviços
data_creas_servicos_idosos = {
    'Tipo de Violação/Violência': [
        'Por Negligência ou Abandono',
        'Violência Psicológica',
        'Violência Patrimonial',
        'Violência/Violação de Direitos de Pessoas com Deficiência',
        'Violência Física',
        'Situação de Rua',
        'Discriminação por Raça/Etnia',
        'Exploração Sexual',
        'Discriminação por Orientação Sexual e/ou Identidade de Gênero',
        'Abuso Sexual/Violência Sexual',
        'Pessoas em Situação de Imigração Internacional e/ou Refúgio',
        'Trabalho em Condição Análoga à Escravidão',
        'Tráfico de Pessoas'
    ],
    'Percentual de CREAS (%)': [
        82.5, 74.1, 69.9, 62.2, 58.0, 38.5, 20.3, 18.9, 18.2, 17.5, 16.1, 10.5, 10.5
    ]
}
df_creas_servicos_idosos = pd.DataFrame(data_creas_servicos_idosos)

# Gráfico de Barras Horizontal
fig_creas_servicos_idosos = px.bar(
    df_creas_servicos_idosos,
    y="Tipo de Violação/Violência",
    x="Percentual de CREAS (%)",
    orientation='h',
    title="Percentual de CREAS que ofertaram serviços por tipo de violação/violência",
    labels={"Percentual de CREAS (%)": "Percentual de CREAS (%)",
            "Tipo de Violação/Violência": "Tipo de Violação/Violência"},
    color="Percentual de CREAS (%)",
    color_continuous_scale=px.colors.sequential.Viridis,
    text="Percentual de CREAS (%)"
)
fig_creas_servicos_idosos.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_creas_servicos_idosos.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_creas_servicos_idosos, use_container_width=True)
st.caption(f"Fonte: {fonte_assistencia_social_idosos}") # Mesma fonte do bloco principal de assistência social
st.markdown("---")

# --- 5. NOTIFICAÇÕES DE VIOLÊNCIA ---
st.subheader("5. NOTIFICAÇÕES DE VIOLÊNCIA")

# Dados de Notificações de Violência (Tipo Geral)
data_notificacoes_violencia_geral_idosos = {
    'Tipo de Violência': [
        'Psicológica/Moral', 'Física', 'Negligência ou Abandono',
        'Lesão Autoprovocada', 'Financeira/Econômica', 'Tortura',
        'Sexual', 'Outro Tipo de Violência'
    ],
    'Número de Notificações': [250, 234, 47, 44, 30, 25, 15, 28]
}
df_notificacoes_violencia_geral_idosos = pd.DataFrame(data_notificacoes_violencia_geral_idosos)
fonte_notificacoes_violencia_geral_idosos = "Sistema de Informação de Agravos de Notificações (SINAN) 2022"

# Gráfico de Barras Vertical
fig_notificacoes_violencia_geral_idosos = px.bar(
    df_notificacoes_violencia_geral_idosos,
    x="Tipo de Violência",
    y="Número de Notificações",
    title="Notificações de Violência contra Idosos por Tipo",
    labels={"Número de Notificações": "Número de Notificações",
            "Tipo de Violência": "Tipo de Violência"},
    color="Número de Notificações",
    color_continuous_scale=px.colors.sequential.Purples,
    text="Número de Notificações"
)
fig_notificacoes_violencia_geral_idosos.update_traces(texttemplate='%{text}', textposition='outside')
fig_notificacoes_violencia_geral_idosos.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_notificacoes_violencia_geral_idosos, use_container_width=True)
st.caption(f"Fonte: {fonte_notificacoes_violencia_geral_idosos}")
st.markdown("---")

# --- 5.1. NOTIFICAÇÕES DE VIOLÊNCIA - Integridade ---
st.subheader("5.1. NOTIFICAÇÕES DE VIOLÊNCIA - Integridade")

# Dados de Notificações de Violência (Integridade)
data_notificacoes_violencia_integridade_idosos = {
    'Tipo de Violação de Integridade': [
        'Integridade Física - Exposição de Risco à Saúde',
        'Integridade Física - Maus Tratos',
        'Integridade Psíquica - Tortura Psíquica',
        'Integridade Psíquica - Insubsistência Afetiva',
        'Integridade Psíquica - Constrangimento',
        'Integridade Psíquica - Ameaça ou Coação',
        'Integridade Psíquica - Exposição',
        'Integridade Patrimonial - Individual',
        'Integridade - Negligência',
        'Integridade Física - Insubsistência Material'
    ],
    'Número de Notificações': [
        60619, 55028, 50557, 43777, 41075, 28645, 28165, 27214, 27106, 24683
    ]
}
df_notificacoes_violencia_integridade_idosos = pd.DataFrame(data_notificacoes_violencia_integridade_idosos)
fonte_notificacoes_violencia_integridade_idosos = "Ouvidoria Nacional de Direitos Humanos 2022"

# Gráfico de Barras Horizontal
fig_notificacoes_violencia_integridade_idosos = px.bar(
    df_notificacoes_violencia_integridade_idosos,
    y="Tipo de Violação de Integridade",
    x="Número de Notificações",
    orientation='h',
    title="Notificações de Violação de Integridade contra Idosos",
    labels={"Número de Notificações": "Número de Notificações",
            "Tipo de Violação de Integridade": "Tipo de Violação"},
    color="Número de Notificações",
    color_continuous_scale=px.colors.sequential.Sunset,
    text="Número de Notificações"
)
fig_notificacoes_violencia_integridade_idosos.update_traces(texttemplate='%{text}', textposition='outside')
fig_notificacoes_violencia_integridade_idosos.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_notificacoes_violencia_integridade_idosos, use_container_width=True)
st.caption(f"Fonte: {fonte_notificacoes_violencia_integridade_idosos}")
st.markdown("---")

# --- 6. PROPORÇÃO DE PESSOAS IDOSAS QUE SOFRERAM VIOLÊNCIA ---
st.subheader("6. PROPORÇÃO DE PESSOAS IDOSAS QUE SOFRERAM VIOLÊNCIA")

# Dados de Proporção de Pessoas Idosas que Sofreram Violência
data_proporcao_violencia_idosos = {
    'Tipo de Violência': [
        'Gritos ou Xingamentos',
        'Ofensa, humilhação e ou ridicularização na frente de outras pessoas',
        'Ameaça de ferir ou machucar alguém importante',
        'Toque, manipulação, beijo e ou exposição de parte do corpo contra a vontade',
        'Ameaça ou ferimento com faca, arma de fogo ou alguma outra arma ou objeto',
        'Ameaças, ofensas, xingamentos e exposição de imagens sem consentimento nas redes sociais ou celular',
        'Tapa ou bofetada',
        'Destruição proposital de pertences',
        'Soco, chute e ou arrastão pelo cabelo',
        'Ameaças e ou relações sexuais forçadas ou quaisquer outros atos sexuais contra a vontade',
        'Tentativa ou efetivo estrangulamento, asfixia ou queimadura proposital'
    ],
    'Percentual (%)': [
        7.3, 6.8, 2.8, 0.5, 0.5, 0.5, 0.4, 0.4, 0.4, 0.0, 0.0
    ]
}
df_proporcao_violencia_idosos = pd.DataFrame(data_proporcao_violencia_idosos)
fonte_proporcao_violencia_idosos = "IBGE 2019"

# Gráfico de Barras Horizontal
fig_proporcao_violencia_idosos = px.bar(
    df_proporcao_violencia_idosos,
    y="Tipo de Violência",
    x="Percentual (%)",
    orientation='h',
    title="Proporção de Pessoas Idosas que Sofreram Violência por Tipo",
    labels={"Percentual (%)": "Percentual (%)", "Tipo de Violência": "Tipo de Violência"},
    color="Percentual (%)",
    color_continuous_scale=px.colors.sequential.Plasma,
    text="Percentual (%)"
)
fig_proporcao_violencia_idosos.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_proporcao_violencia_idosos.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_proporcao_violencia_idosos, use_container_width=True)
st.caption(f"Fonte: {fonte_proporcao_violencia_idosos}")
st.markdown("---") # Fim da seção IDOSOS