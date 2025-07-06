import pandas as pd
import plotly.express as px
import streamlit as st

# --- Configuração da Página Streamlit ---
st.set_page_config(page_title="Quilombolas", page_icon=":house_with_garden:", layout="wide")

# --- Título Principal da Página ---
st.header("QUILOMBOLAS")

# --- 1. Definição Global de Variáveis e DataFrames ---

# População Total Quilombola
total_quilombola_pessoas = 135603
percentual_quilombola_pop = 1.67
fonte_populacao_quilombola = "IBGE 2022"

# DEMOGRAFIA - População Quilombola por Área
data_quilombola_area = {
    'Localidade': ['Área Rural', 'Área Urbana'],
    'Proporção (%)': [67.33, 32.67]
}
df_quilombola_area = pd.DataFrame(data_quilombola_area)

# DEMOGRAFIA - Quilombolas por localização do domicílio
data_quilombola_domicilio = {
    'Localização Domicílio': ['Em territórios Quilombolas', 'Fora de territórios'],
    'Número Absoluto': [44560, 91043],
    'Proporção (%)': [32.86, 67.14]
}
df_quilombola_domicilio = pd.DataFrame(data_quilombola_domicilio)

# DEMOGRAFIA - Registro de Nascimento
data_registro_nascimento_quilombola = {
    'Situação do Registro': ['Com registro em cartório', 'Sem registro'],
    'Proporção (%)': [97.61, 2.22]
}
df_registro_nascimento_quilombola = pd.DataFrame(data_registro_nascimento_quilombola)
fonte_registro_nascimento_quilombola = "IBGE 2022" # CORRIGIDO: Adicionado esta definição

# EDUCAÇÃO - Alfabetização
data_alfabetizacao_quilombola = {
    'Situação': ['Alfabetizados', 'Analfabetismo'],
    'Número Absoluto': [86258, 12503],
    'Proporção (%)': [87.34, 12.66]
}
df_alfabetizacao_quilombola = pd.DataFrame(data_alfabetizacao_quilombola)
fonte_educacao_quilombola = "IBGE 2022"

# INFRAESTRUTURA E SANEAMENTO - Indicadores Gerais
data_infra_saneamento_quilombola = {
    'Indicador': [
        'Abastecimento de água pela rede geral', 'Banheiro de uso exclusivo',
        'Famílias com Acesso à Rede Esgoto', 'Famílias com Acesso a Coleta de Lixo'
    ],
    'Percentual (%)': [49.27, 76.8, 3.65, 45.31]
}
df_infra_saneamento_quilombola = pd.DataFrame(data_infra_saneamento_quilombola)
fonte_infra_saneamento_quilombola = "IBGE 2022"

# INFRAESTRUTURA E SANEAMENTO - Tipos de domicílio
data_tipos_domicilio_quilombola = {
    'Tipo de Domicílio': ['Casa', 'Apartamento', 'Estrutura inacabada', 'Vila ou condomínio', 'Cortiço'],
    'Proporção (%)': [98.04, 0.48, 0.07, 1.26, 0.15],
    'Número Absoluto': [42059, 206, 30, 542, 65]
}
df_tipos_domicilio_quilombola = pd.DataFrame(data_tipos_domicilio_quilombola)

# INFRAESTRUTURA E SANEAMENTO - Características dos domicílios por situação urbana ou rural
data_caracteristicas_domicilio_quilombola = {
    'Característica': [
        'Abastecimento de água pela rede geral',
        'Famílias com Acesso à Rede Esgoto',
        'Famílias com Acesso a Coleta de Lixo'
    ],
    'Urbana (%)': [35.03, 12.59, 35.54],
    'Rural (%)': [37.33, 11.26, 9.77]
}
df_caracteristicas_domicilio_quilombola = pd.DataFrame(data_caracteristicas_domicilio_quilombola)
df_caracteristicas_domicilio_quilombola_melted = df_caracteristicas_domicilio_quilombola.melt(
    id_vars='Característica',
    var_name='Situação',
    value_name='Percentual (%)'
)

# DIREITOS TERRITORIAIS E MEIO AMBIENTE - Regularização Fundiária
data_regularizacao_fundiaria_quilombola = {
    'Indicador': [
        'Processos abertos de Regularização Fundiária junto ao INCRA',
        'Regularização Fundiária junto ao ITERPA'
    ],
    'Valor': [67, 44],
    'Unidade': ['processos', 'Títulos de Terra Coletivos'],
    'Fonte Específica': ['INCRA 2023', 'Agência Pará 2024']
}
df_regularizacao_fundiaria_quilombola = pd.DataFrame(data_regularizacao_fundiaria_quilombola)
fonte_direitos_territoriais_quilombola = "Diversas fontes (ver gráfico)"

# --- Seções da Dashboard (Corpo Principal) ---

###############################################################################################################
st.markdown("---") # Separador inicial

# Seção Introdutória: População Total Quilombola no Pará
st.subheader("Total da População Quilombola no Pará")

col_intro_quilombola_title, col_abs_quilombola, col_perc_quilombola = st.columns([3, 1, 1])

with col_intro_quilombola_title:
    st.markdown("###### Visão Geral da População Quilombola no Pará")

with col_abs_quilombola:
    st.metric(
        label="Número de Pessoas",
        value=f"{total_quilombola_pessoas:,.0f}".replace(",", "."),
        delta=None
    )

with col_perc_quilombola:
    st.metric(
        label="Percentual da População Total",
        value=f"{percentual_quilombola_pop:.2f}%",
        delta=None
    )
st.caption(f"Fonte: {fonte_populacao_quilombola}")
st.markdown("---")


# 1. DEMOGRAFIA
st.subheader("1. DEMOGRAFIA")

# 1.1. População Quilombola por Área e 1.2. Quilombolas por Localização do Domicílio
col_area_quilombola, col_domicilio_quilombola = st.columns(2)

with col_area_quilombola:
    st.markdown("###### 1.1. População Quilombola por Área")
    fig_quilombola_area = px.pie(
        df_quilombola_area,
        values='Proporção (%)',
        names='Localidade',
        title='População Quilombola por Localidade',
        hole=0.3
    )
    fig_quilombola_area.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_quilombola_area, use_container_width=True)

with col_domicilio_quilombola:
    st.markdown("###### 1.2. Quilombolas por Localização do Domicílio")
    # Para incluir o número absoluto no texto do gráfico de pizza
    df_quilombola_domicilio['Texto Completo'] = df_quilombola_domicilio.apply(
        lambda row: f"{row['Localização Domicílio']}<br>({row['Número Absoluto']:,.0f} pessoas)".replace(",", "."), axis=1
    )
    fig_quilombola_domicilio = px.pie(
        df_quilombola_domicilio,
        values='Proporção (%)',
        names='Texto Completo', # Usa o texto completo para labels
        title='Quilombolas por Localização do Domicílio',
        hole=0.3
    )
    fig_quilombola_domicilio.update_traces(textinfo='percent', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_quilombola_domicilio, use_container_width=True)

st.caption(f"Fonte: {fonte_populacao_quilombola}") # Fonte comum para Demografia
st.markdown("---")

# 1.3. Registro de Nascimento
st.subheader("1.3. Registro de Nascimento")
fig_registro_nascimento_quilombola = px.pie(
    df_registro_nascimento_quilombola,
    values='Proporção (%)',
    names='Situação do Registro',
    title='Registro de Nascimento da População Quilombola',
    hole=0.3
)
fig_registro_nascimento_quilombola.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
st.plotly_chart(fig_registro_nascimento_quilombola, use_container_width=True)
st.caption(f"Fonte: {fonte_registro_nascimento_quilombola}") # Fonte específica para registro de nascimento (se diferente)
st.markdown("---")


# 2. EDUCAÇÃO
st.subheader("2. EDUCAÇÃO")

# 2.1. Alfabetização
st.markdown("###### 2.1. Alfabetização")
fig_alfabetizacao_quilombola = px.pie(
    df_alfabetizacao_quilombola,
    values='Proporção (%)',
    names='Situação',
    title='Taxa de Alfabetização da População Quilombola',
    hole=0.3
)
fig_alfabetizacao_quilombola.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
st.plotly_chart(fig_alfabetizacao_quilombola, use_container_width=True)
st.caption(f"Fonte: {fonte_educacao_quilombola}")
st.markdown("---")


# 3. INFRAESTRUTURA E SANEAMENTO
st.subheader("3. INFRAESTRUTURA E SANEAMENTO")

# 3.1. Indicadores Gerais
st.markdown("###### 3.1. Indicadores Gerais de Infraestrutura e Saneamento")
fig_infra_saneamento_quilombola = px.bar(
    df_infra_saneamento_quilombola,
    y="Indicador",
    x="Percentual (%)",
    orientation='h',
    title="Infraestrutura e Saneamento em Domicílios Quilombolas",
    labels={"Percentual (%)": "Percentual (%)", "Indicador": "Indicador"},
    color="Percentual (%)",
    color_continuous_scale=px.colors.sequential.Plotly3,
    text="Percentual (%)"
)
fig_infra_saneamento_quilombola.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
fig_infra_saneamento_quilombola.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_infra_saneamento_quilombola, use_container_width=True)
st.caption(f"Fonte: {fonte_infra_saneamento_quilombola}")
st.markdown("---")

# 3.2. Tipos de Domicílio
st.markdown("###### 3.2. Tipos de Domicílio")
fig_tipos_domicilio_quilombola = px.pie(
    df_tipos_domicilio_quilombola,
    values='Proporção (%)',
    names='Tipo de Domicílio',
    title='Tipos de Domicílio com Moradores Quilombolas',
    hole=0.3
)
fig_tipos_domicilio_quilombola.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
st.plotly_chart(fig_tipos_domicilio_quilombola, use_container_width=True)
st.caption(f"Fonte: {fonte_infra_saneamento_quilombola}")
st.markdown("---")

# 3.3. Características dos Domicílios por Situação Urbana ou Rural
st.markdown("###### 3.3. Características dos Domicílios por Situação Urbana ou Rural")
fig_caracteristicas_domicilio_quilombola = px.bar(
    df_caracteristicas_domicilio_quilombola_melted,
    y="Característica",
    x="Percentual (%)",
    color="Situação",
    barmode="group",
    orientation='h',
    title="Características de Domicílios Quilombolas por Situação Urbana ou Rural",
    labels={"Percentual (%)": "Percentual (%)", "Característica": "Característica", "Situação": "Situação"},
    text="Percentual (%)"
)
fig_caracteristicas_domicilio_quilombola.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
fig_caracteristicas_domicilio_quilombola.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_caracteristicas_domicilio_quilombola, use_container_width=True)
st.caption(f"Fonte: {fonte_infra_saneamento_quilombola}")
st.markdown("---")


# 4. DIREITOS TERRITORIAIS E MEIO AMBIENTE
st.subheader("4. DIREITOS TERRITORIAIS E MEIO AMBIENTE")

# 4.1. Regularização Fundiária
st.markdown("###### 4.1. Regularização Fundiária")
col_incra_quilombola, col_iterpa_quilombola = st.columns(2)

with col_incra_quilombola:
    st.metric(
        label=df_regularizacao_fundiaria_quilombola['Indicador'].iloc[0],
        value=f"{df_regularizacao_fundiaria_quilombola['Valor'].iloc[0]:.0f} {df_regularizacao_fundiaria_quilombola['Unidade'].iloc[0]}",
        delta=None
    )
with col_iterpa_quilombola:
    st.metric(
        label=df_regularizacao_fundiaria_quilombola['Indicador'].iloc[1],
        value=f"{df_regularizacao_fundiaria_quilombola['Valor'].iloc[1]:.0f} {df_regularizacao_fundiaria_quilombola['Unidade'].iloc[1]}",
        delta=None
    )
st.caption(f"Fonte: {df_regularizacao_fundiaria_quilombola['Fonte Específica'].iloc[0]} / {df_regularizacao_fundiaria_quilombola['Fonte Específica'].iloc[1]} (consolidado)")
st.markdown("---")