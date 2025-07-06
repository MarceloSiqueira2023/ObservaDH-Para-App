import pandas as pd
import plotly.express as px
import streamlit as st

# --- Configuração da Página Streamlit ---
# Ajuste o page_title e page_icon conforme a página atual
st.set_page_config(page_title="População Negra", page_icon=":raising_hand:", layout="wide")

# --- Título Principal da Página ---
st.header("POPULAÇÃO NEGRA")

# --- 1. Definição Global de Variáveis e DataFrames ---

# Variáveis de Fonte (centralizadas no topo para evitar NameError)
fonte_populacao_negra = "IBGE 2022"
fonte_genero_sexualidade = "Pesquisa Nacional de Saúde (PNS) IBGE 2019" # CORRIGIDO: Movido para o topo
fonte_renda_escolaridade_negra = "IBGE 2023 / IPEA 2023 / INEP 2023"
fonte_educacao_genero_negra = "PNAD IBGE 2023 / INEP 2023"
fonte_educacao_tradicionais_negra = "PNAD IBGE 2023 / INEP 2023 / Censo Quilombola 2023"
fonte_saude_geral_negra = "Diversas fontes (ver gráfico)" # Fonte consolidada para o caption
fonte_denuncias_sus_negra = "Ouvidoria SUS PA 2023"
fonte_concentracao_negra = "IBGE 2022"
fonte_mulheres_negras_mercado_perc = "Diversas fontes (ver gráfico)"
fonte_mulheres_negras_mercado_outros_geral = "Diversas fontes (ver gráfico)"
fonte_violencia_negra_geral = "Diversas fontes (ver gráfico)"
fonte_violencia_negra_ambientes = "Iniciativa Negra 2024"
fonte_racismo_religioso_geral = "Diversas fontes (ver gráfico)"
fonte_seguridade_social_lgbt = "Censo Sistema Único de Assistência Social (SUAS) 2022" # Fonte comum para SEGURIDADE SOCIAL
fonte_violencia_lgbt = "Ouvidoria Nacional de Direitos Humanos 2022 / Sistema de Informação de Agravos de Notificação (SINAN) 2015-2022"


# População Total e Negra no Pará (Introdução)
total_pop_para = 8120131
total_pop_negra_para = 6467067

# DEMOGRAFIA - Distribuição Percentual
percentual_pop_negra_para = 79.6
data_idade_negra = {
    'Faixa Etária': ['0 a 14 anos', '15 a 29 anos', '30 a 59 anos', '60+'],
    'Proporção (%)': [25.3, 26.1, 38.4, 10.2]
}
df_idade_negra = pd.DataFrame(data_idade_negra)

data_sexo_negra = {
    'Gênero': ['Homens', 'Mulheres'],
    'Proporção (%)': [50.3, 49.7]
}
df_sexo_negra = pd.DataFrame(data_sexo_negra)

data_localidade_negra = {
    'Localidade': ['Urbana', 'Rural'],
    'Proporção (%)': [70.2, 29.8]
}
df_localidade_negra = pd.DataFrame(data_localidade_negra)

# RENDA E ESCOLARIDADE - Renda Média e Indicadores Sociais
renda_media_negra = 1435.00
populacao_extrema_pobreza_negra = 18.7
taxa_analfabetismo_negra = 11.66
conclusao_ensino_medio_negra = 52.3

# EDUCAÇÃO - Analfabetismo e Conclusão EM por Gênero
data_educacao_mulheres_negra = {
    'Localidade': ['Urbano', 'Rural', 'Total'],
    'Analfabetismo (%)': [5.2, 13.8, 7.4],
    'Conclusão do Ensino Médio (%)': [59.4, 42.8, 55.9]
}
df_educacao_mulheres_negra = pd.DataFrame(data_educacao_mulheres_negra)

data_educacao_homens_negra = {
    'Localidade': ['Urbano', 'Rural', 'Total'],
    'Analfabetismo (%)': [5.8, 14.6, 8.2],
    'Conclusão do Ensino Médio (%)': [52.3, 38.6, 48.7]
}
df_educacao_homens_negra = pd.DataFrame(data_educacao_homens_negra)

# EDUCAÇÃO - Analfabetismo e Conclusão EM por Populações Tradicionais
data_educacao_tradicionais_negra = {
    'População': ['População Ribeirinha', 'População Quilombola'],
    'Analfabetismo (%)': [15.4, 12.66],
    'Conclusão do Ensino Médio (%)': [34.5, 35.7]
}
df_educacao_tradicionais_negra = pd.DataFrame(data_educacao_tradicionais_negra)

# SAÚDE - Prevalência de Doenças e Acesso a Serviços
data_saude_negra = {
    'Indicador de Saúde': [
        'Prevalência de Anemia Falciforme', 'Deficiência de G6PD', 'Diabetes Mellitus',
        'Miomas Uterinos', 'Cobertura Pré-Natal (7+ consultas)', 'Acesso a Medicamentos Básicos',
        'Acompanhamento Hipertensos', 'Acompanhamento Diabéticos'
    ],
    'Valor (%)': [76.5, 12.8, 2.8, 32.4, 25.6, 58.3, 45.6, 62.4],
    'Fonte Específica': [
        'ABPN 2012', 'DATASUS 2023', 'IBGE 2019', 'SUS-PA 2023',
        'SINAC 2023', 'RENAME 2023', 'HIPERDIA 2023', 'HEMOCENTRO PA 2023'
    ]
}
df_saude_negra = pd.DataFrame(data_saude_negra)

# SAÚDE - Denúncias de Discriminação no SUS
denuncias_discriminacao_sus = 245

# CONCENTRAÇÃO POPULACIONAL - Bairros
data_concentracao_bairros_negra = {
    'Bairro (Cidade)': [
        'Jurunas (BELÉM)', 'Guamá (BELÉM)', 'Terra Firme (BELÉM)', 'Sacramenta (BELÉM)',
        'Nova União (MARITUBA)', 'Jaderlândia (ANANINDEUA)', 'Nova Conquista (MARABÁ)',
        'Promissão (PARAGOMINAS)', 'Infraero (SANTANA DO ARAGUAIA)',
        'São Félix (CASTANHAL)', 'Jaderlândia (CASTANHAL)', 'Novo Horizonte (SANTARÉM)',
        'Betânia (ALTAMIRA)', 'Liberdade (PARAUAPEBAS)'
    ],
    'Concentração (%)': [82.3, 81.7, 80.5, 79.8, 83.4, 82.8, 78.6, 76.8, 75.4, 77.2, 76.8, 77.9, 74.8, 75.6]
}
df_concentracao_bairros_negra = pd.DataFrame(data_concentracao_bairros_negra)

# EMPREGABILIDADE - Mulheres Negras no Mercado de Trabalho (Percentuais)
data_mulheres_negras_mercado_perc = {
    'Indicador': [
        'Trabalho Doméstico', 'Empreendedoras', 'Ensino Superior Completo',
        'Cursos Profissionalizantes', 'Serviços', 'Taxa de Desemprego', 'Taxa de Informalidade'
    ],
    'Valor (%)': [28.7, 22.4, 15.6, 28.7, 45.3, 21.4, 64.5]
}
df_mulheres_negras_mercado_perc = pd.DataFrame(data_mulheres_negras_mercado_perc)

# EMPREGABILIDADE - Mulheres Negras no Mercado de Trabalho (Outros Indicadores)
data_mulheres_negras_mercado_outros = {
    'Indicador': ['Horas Semanais Trabalho Doméstico', 'Denúncias de Racismo no Trabalho', 'Assédio Moral/Sexual'],
    'Valor': [21.5, 156, 189],
    'Unidade': ['Horas', 'Casos', 'Casos'],
    'Fonte': ['IBGE 2023', 'MPT PA 2023', 'MPT PA 2023 (Assumido)']
}
df_mulheres_negras_mercado_outros = pd.DataFrame(data_mulheres_negras_mercado_outros)

# VIOLÊNCIA CONTRA A POPULAÇÃO NEGRA - Indicadores Gerais
data_violencia_negra_geral = {
    'Tipo de Violência': ['Homicídios', 'Feminicídio', 'Violência sexual'],
    'Valor (%)': [93.0, 17.62, 56.7],
    'Fonte Específica': ['SEGUP 2022', 'Alma Preta Jornalismo 2024', 'FAPESPA 2023']
}
df_violencia_negra_geral = pd.DataFrame(data_violencia_negra_geral)

# VIOLÊNCIA CONTRA A POPULAÇÃO NEGRA - Ambientes
data_violencia_negra_ambientes = {
    'Ambiente': ['Violência Doméstica', 'Via Pública'],
    'Proporção (%)': [57.0, 56.7]
}
df_violencia_negra_ambientes = pd.DataFrame(data_violencia_negra_ambientes)

# VIOLÊNCIA CONTRA A POPULAÇÃO NEGRA - Racismo Religioso
data_racismo_religioso = {
    'Tipo de Registro': ['Ataques a Terreiros', 'Denúncias', 'Processos Judiciais: ações em andamento'],
    'Número Absoluto': [89, 178, 156],
    'Unidade': ['Casos', 'Ocorrências', 'Processos'],
    'Fonte Específica': ['SEGUP PA 2023', 'SEJUDH PA 2023', 'TJ PA 2023']
}
df_racismo_religioso = pd.DataFrame(data_racismo_religioso)

# --- Seções da Dashboard (Corpo Principal) ---

###############################################################################################################
st.markdown("---") # Separador inicial

# Seção Introdutória: População Total Negra no Pará
st.subheader("Total da População Negra no Pará")

col_intro_pn_total, col_abs_pn_total, col_abs_pn_negra = st.columns([3, 1, 1])

with col_intro_pn_total:
    st.markdown("###### Total da População Negra no Pará")

with col_abs_pn_total:
    st.metric(
        label="População Total do Pará",
        value=f"{total_pop_para:,.0f}".replace(",", "."),
        delta=None
    )

with col_abs_pn_negra:
    st.metric(
        label="População Negra do Pará",
        value=f"{total_pop_negra_para:,.0f}".replace(",", "."),
        delta=None
    )
st.caption(f"Fonte: {fonte_populacao_negra}")
st.markdown("---")


# 1. DEMOGRAFIA
st.subheader("1. DEMOGRAFIA")

# 1.1. Distribuição Percentual da População Negra
st.markdown("###### 1.1. Distribuição Percentual da População Negra")

col_demog_total, col_demog_idade, col_demog_sexo, col_demog_local = st.columns([1, 1, 1, 1])

with col_demog_total:
    st.metric(
        label="Total da População Negra no Pará",
        value=f"{percentual_pop_negra_para:.1f}%",
        delta=None
    )

with col_demog_idade:
    fig_idade_negra = px.pie(
        df_idade_negra,
        values='Proporção (%)',
        names='Faixa Etária',
        title='Por Faixa Etária',
        hole=0.3
    )
    fig_idade_negra.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_idade_negra, use_container_width=True)

with col_demog_sexo:
    fig_sexo_negra = px.pie(
        df_sexo_negra,
        values='Proporção (%)',
        names='Gênero',
        title='Por Sexo',
        hole=0.3
    )
    fig_sexo_negra.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_sexo_negra, use_container_width=True)

with col_demog_local:
    fig_localidade_negra = px.pie(
        df_localidade_negra,
        values='Proporção (%)',
        names='Localidade',
        title='Por Localidade',
        hole=0.3
    )
    fig_localidade_negra.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_localidade_negra, use_container_width=True)

st.caption(f"Fonte: {fonte_genero_sexualidade}") # Fonte comum para a Demografia
st.markdown("---")


# 2. RENDA E ESCOLARIDADE
st.subheader("2. RENDA E ESCOLARIDADE")

# 2.1. Renda Média
st.markdown("###### 2.1. Renda Média")
st.metric(
    label="Renda Média",
    value=f"R$ {renda_media_negra:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), # Formatação para BRL
    delta=None
)
st.caption(f"Fonte: {fonte_renda_escolaridade_negra}")
st.markdown("---")

# 2.2. Indicadores Sociais (Pobreza, Analfabetismo, Conclusão EM)
st.markdown("###### 2.2. Indicadores Sociais")
col_sociais_1, col_sociais_2, col_sociais_3 = st.columns(3)

with col_sociais_1:
    st.metric(
        label="População em Extrema Pobreza",
        value=f"{populacao_extrema_pobreza_negra:.1f}%",
        delta=None
    )
with col_sociais_2:
    st.metric(
        label="Taxa de Analfabetismo",
        value=f"{taxa_analfabetismo_negra:.2f}%",
        delta=None
    )
with col_sociais_3:
    st.metric(
        label="Conclusão do Ensino Médio",
        value=f"{conclusao_ensino_medio_negra:.1f}%",
        delta=None
    )
st.caption(f"Fonte: {fonte_renda_escolaridade_negra}")
st.markdown("---")


# 3. EDUCAÇÃO (Seção principal para indicadores de educação)
st.subheader("3. EDUCAÇÃO")

# 3.1. Indicadores por Gênero: Mulheres
st.markdown("###### 3.1. Indicadores por Gênero: Mulheres")
data_melted_mulheres = df_educacao_mulheres_negra.melt(
    id_vars='Localidade',
    var_name='Tipo de Indicador',
    value_name='Percentual (%)'
)
fig_mulheres_educacao = px.bar(
    data_melted_mulheres,
    x="Localidade",
    y="Percentual (%)",
    color="Tipo de Indicador",
    barmode="group",
    title="Analfabetismo e Conclusão do Ensino Médio (Mulheres)",
    labels={"Percentual (%)": "Percentual (%)", "Localidade": "Localidade", "Tipo de Indicador": "Indicador"},
    text="Percentual (%)"
)
fig_mulheres_educacao.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_mulheres_educacao.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_mulheres_educacao, use_container_width=True)
st.caption(f"Fonte: {fonte_educacao_genero_negra}")
st.markdown("---")

# 3.2. Indicadores por Gênero: Homens
st.markdown("###### 3.2. Indicadores por Gênero: Homens")
data_melted_homens = df_educacao_homens_negra.melt(
    id_vars='Localidade',
    var_name='Tipo de Indicador',
    value_name='Percentual (%)'
)
fig_homens_educacao = px.bar(
    data_melted_homens,
    x="Localidade",
    y="Percentual (%)",
    color="Tipo de Indicador",
    barmode="group",
    title="Analfabetismo e Conclusão do Ensino Médio (Homens)",
    labels={"Percentual (%)": "Percentual (%)", "Localidade": "Localidade", "Tipo de Indicador": "Indicador"},
    text="Percentual (%)"
)
fig_homens_educacao.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_homens_educacao.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_homens_educacao, use_container_width=True)
st.caption(f"Fonte: {fonte_educacao_genero_negra}")
st.markdown("---")

# 3.3. Indicadores por Populações Tradicionais
st.markdown("###### 3.3. Indicadores por Populações Tradicionais")
data_melted_tradicionais = df_educacao_tradicionais_negra.melt(
    id_vars='População',
    var_name='Tipo de Indicador',
    value_name='Percentual (%)'
)
fig_tradicionais_educacao = px.bar(
    data_melted_tradicionais,
    x="População",
    y="Percentual (%)",
    color="Tipo de Indicador",
    barmode="group",
    title="Analfabetismo e Conclusão do Ensino Médio (Populações Tradicionais)",
    labels={"Percentual (%)": "Percentual (%)", "População": "População", "Tipo de Indicador": "Indicador"},
    text="Percentual (%)"
)
fig_tradicionais_educacao.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
fig_tradicionais_educacao.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_tradicionais_educacao, use_container_width=True)
st.caption(f"Fonte: {fonte_educacao_tradicionais_negra}")
st.markdown("---")


# 4. SAÚDE
st.subheader("4. SAÚDE")

# 4.1. Prevalência de Doenças e Acesso a Serviços
st.markdown("###### 4.1. Prevalência de Doenças e Acesso a Serviços")
fig_saude_negra = px.bar(
    df_saude_negra,
    y="Indicador de Saúde",
    x="Valor (%)",
    orientation='h',
    title="Prevalência de Doenças e Acesso a Serviços de Saúde",
    labels={"Valor (%)": "Percentual (%)", "Indicador de Saúde": "Indicador"},
    color="Valor (%)",
    color_continuous_scale=px.colors.sequential.Plasma,
    text="Valor (%)"
)
fig_saude_negra.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_saude_negra.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_saude_negra, use_container_width=True)
st.caption(f"Fonte: {', '.join(df_saude_negra['Fonte Específica'].unique())}") # Exibe todas as fontes
st.markdown("---")

# 4.2. Denúncias de Discriminação no SUS
st.markdown("###### 4.2. Denúncias de Discriminação no SUS")
st.metric(
    label="Denúncias de Discriminação no SUS",
    value=f"{denuncias_discriminacao_sus} casos",
    delta=None
)
st.caption(f"Fonte: {fonte_denuncias_sus_negra}")
st.markdown("---")


# 5. CONCENTRAÇÃO POPULACIONAL
st.subheader("5. CONCENTRAÇÃO POPULACIONAL")

# 5.1. Bairros com Maior Concentração Populacional
st.markdown("###### 5.1. Bairros com Maior Concentração Populacional")
fig_concentracao_bairros_negra = px.bar(
    df_concentracao_bairros_negra,
    y="Bairro (Cidade)",
    x="Concentração (%)",
    orientation='h',
    title="Bairros do Pará com Maior Concentração de População Negra",
    labels={"Concentração (%)": "Percentual (%)", "Bairro (Cidade)": "Bairro (Cidade)"},
    color="Concentração (%)",
    color_continuous_scale=px.colors.sequential.Teal,
    text="Concentração (%)"
)
fig_concentracao_bairros_negra.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_concentracao_bairros_negra.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_concentracao_bairros_negra, use_container_width=True)
st.caption(f"Fonte: {fonte_concentracao_negra}")
st.markdown("---")


# 6. EMPREGABILIDADE - MULHERES NEGRAS
st.subheader("6. EMPREGABILIDADE - MULHERES NEGRAS")

# 6.1. Indicadores Percentuais
st.markdown("###### 6.1. Indicadores Percentuais no Mercado de Trabalho")
fig_mulheres_negras_mercado_perc = px.bar(
    df_mulheres_negras_mercado_perc,
    y="Indicador",
    x="Valor (%)",
    orientation='h',
    title="Mulheres Negras no Mercado de Trabalho: Indicadores Percentuais",
    labels={"Valor (%)": "Percentual (%)", "Indicador": "Indicador"},
    color="Valor (%)",
    color_continuous_scale=px.colors.sequential.Oranges,
    text="Valor (%)"
)
fig_mulheres_negras_mercado_perc.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_mulheres_negras_mercado_perc.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_mulheres_negras_mercado_perc, use_container_width=True)
st.caption(f"Fonte: IBGE 2023, SEBRAE PA 2023, SENAC PA 2023 (consolidado)") # Consolidar fontes
st.markdown("---")

# 6.2. Outros Indicadores
st.markdown("###### 6.2. Outros Indicadores no Mercado de Trabalho")
col_mulheres_neg_met_1, col_mulheres_neg_met_2, col_mulheres_neg_met_3 = st.columns(3)

with col_mulheres_neg_met_1:
    st.metric(
        label=f"{df_mulheres_negras_mercado_outros['Indicador'].iloc[0]} ({df_mulheres_negras_mercado_outros['Unidade'].iloc[0]})",
        value=f"{df_mulheres_negras_mercado_outros['Valor'].iloc[0]:.1f}"
    )
with col_mulheres_neg_met_2:
    st.metric(
        label=f"{df_mulheres_negras_mercado_outros['Indicador'].iloc[1]} ({df_mulheres_negras_mercado_outros['Unidade'].iloc[1]})",
        value=f"{df_mulheres_negras_mercado_outros['Valor'].iloc[1]:.0f}"
    )
with col_mulheres_neg_met_3:
    st.metric(
        label=f"{df_mulheres_negras_mercado_outros['Indicador'].iloc[2]} ({df_mulheres_negras_mercado_outros['Unidade'].iloc[2]})",
        value=f"{df_mulheres_negras_mercado_outros['Valor'].iloc[2]:.0f}"
    )
st.caption("Fonte: IBGE 2023, MPT PA 2023 (consolidado)") # Consolidar fontes
st.markdown("---")


# 7. VIOLÊNCIA CONTRA A POPULAÇÃO NEGRA
st.subheader("7. VIOLÊNCIA CONTRA A POPULAÇÃO NEGRA")

# 7.1. Indicadores Gerais
st.markdown("###### 7.1. Indicadores Gerais de Violência")
fig_violencia_negra_geral = px.bar(
    df_violencia_negra_geral,
    x="Tipo de Violência",
    y="Valor (%)",
    title="Homicídios, Feminicídio e Violência Sexual",
    labels={"Valor (%)": "Percentual (%)", "Tipo de Violência": "Tipo de Violência"},
    color="Valor (%)",
    color_continuous_scale=px.colors.sequential.Reds,
    text="Valor (%)"
)
fig_violencia_negra_geral.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
fig_violencia_negra_geral.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_violencia_negra_geral, use_container_width=True)
st.caption(f"Fonte: SEGUP 2022, Alma Preta Jornalismo 2024, FAPESPA 2023 (consolidado)") # Consolidar fontes
st.markdown("---")

# 7.2. Ambientes de Ocorrência
st.markdown("###### 7.2. Ambientes onde ocorre a Violência")
fig_violencia_negra_ambientes = px.bar(
    df_violencia_negra_ambientes,
    x="Ambiente",
    y="Proporção (%)",
    title="Ambientes de Ocorrência da Violência",
    labels={"Proporção (%)": "Percentual (%)", "Ambiente": "Ambiente"},
    color="Proporção (%)",
    color_continuous_scale=px.colors.sequential.Greys,
    text="Proporção (%)"
)
fig_violencia_negra_ambientes.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_violencia_negra_ambientes.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_violencia_negra_ambientes, use_container_width=True)
st.caption(f"Fonte: Iniciativa Negra 2024")
st.markdown("---")

# 7.3. Racismo Religioso
st.markdown("###### 7.3. Racismo Religioso")
fig_racismo_religioso = px.bar(
    df_racismo_religioso,
    x="Tipo de Registro",
    y="Número Absoluto",
    color="Número Absoluto",
    color_continuous_scale=px.colors.sequential.Purples,
    text="Número Absoluto",
    title="Violações Relacionadas ao Racismo Religioso",
    labels={"Número Absoluto": "Número de Registros", "Tipo de Registro": "Tipo de Registro"}
)
fig_racismo_religioso.update_traces(texttemplate='%{text}', textposition='outside')
fig_racismo_religioso.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_racismo_religioso, use_container_width=True)
st.caption(f"Fonte: SEGUP PA 2023, SEJUDH PA 2023, TJ PA 2023 (consolidado)") # Consolidar fontes
st.markdown("---")