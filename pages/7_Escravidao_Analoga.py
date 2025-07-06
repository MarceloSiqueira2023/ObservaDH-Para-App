import pandas as pd
import plotly.express as px
import streamlit as st

# --- Configuração da Página Streamlit ---
st.set_page_config(page_title="Trabalho Análogo à Escravidão", page_icon=":chains:", layout="wide") # Ícone de correntes sugerido

# --- Título Principal da Página ---
st.header("TRABALHADORES EM CONDIÇÕES ANÁLOGAS À ESCRAVIDÃO")

# --- 1. Definição Global de Variáveis e DataFrames ---

# População Total de Trabalhadores em Condições Análogas à Escravidão
total_trabalhadores_analogos = 13538
fonte_trabalhadores_analogos = "IBGE 2022"

# TRABALHADORES RESGATADOS
resgatados_2023 = 74
resgatados_2021_2023 = 353
fonte_resgatados = "MPT 2023"

# ATIVIDADE ECONÔMICA QUE MAIS UTILIZA ESSA MÃO DE OBRA
data_atividade_economica = {
    'Atividade Econômica': ['Garimpo', 'Pecuária', 'Agricultura'],
    'Percentual (%)': [27.0, 29.10, 4.55]
}
df_atividade_economica = pd.DataFrame(data_atividade_economica)
fonte_atividade_economica = "SmartLab 2024"

# ONDE OCORRE O TRABALHO ANÁLOGO À ESCRAVIDÃO - MUNICÍPIOS
data_ocorrencia_municipios = {
    'Município': [
        'São Felix do Xingu', 'Marabá', 'Novo Repartimento', 'Itupiranga',
        'Rondon do Pará', 'Pacajá', 'Goianésia do Pará', 'Paragominas',
        'Dom Eliseu', 'Santana do Araguaia', 'Ourilândia do Norte',
        'Abel Figueiredo', 'Tucuruí'
    ],
    'Percentual (%)': [
        19.37, 9.52, 9.48, 8.14, 7.83, 7.30, 6.64, 5.46, 5.34, 4.93, 4.40, 3.94, 3.81
    ]
}
df_ocorrencia_municipios = pd.DataFrame(data_ocorrencia_municipios)
fonte_ocorrencia_municipios = "Radar SIT 2023"

# PERFIL DO TRABALHADOR RESGATADO - Sexo
data_perfil_sexo = {
    'Gênero': ['Masculino', 'Feminino'],
    'Percentual (%)': [93.7, 6.3]
}
df_perfil_sexo = pd.DataFrame(data_perfil_sexo)
fonte_perfil_resgatado = "SmartLab 2024" # Fonte comum para o perfil

# PERFIL DO TRABALHADOR RESGATADO - Escolaridade
data_perfil_escolaridade = {
    'Nível de Escolaridade': [
        'Analfabeto', 'Até 5º ano incompleto', '6º ao 9º ano incompleto',
        'Ensino Médio Completo', '5º Ano Completo', 'Fundamental Completo', 'Ensino Médio Incompleto'
    ],
    'Percentual (%)': [59.0, 13.50, 8.09, 7.08, 4.38, 3.88, 3.88]
}
df_perfil_escolaridade = pd.DataFrame(data_perfil_escolaridade)

# PERFIL DO TRABALHADOR RESGATADO - Idade
data_perfil_idade = {
    'Faixa Etária': [
        'Menores de 18 anos', '18 a 24 anos', '25 a 29 anos', '30 a 34 anos',
        '35 a 39 anos', '40 a 44 anos', '45 a 49 anos', '50 a 54 anos',
        '55 a 59 anos', '60 anos ou mais'
    ],
    'Percentual (%)': [
        0.7, 24.2, 19.5, 14.7, 12.8, 10.8, 7.3, 5.2, 2.3, 2.5
    ]
}
df_perfil_idade = pd.DataFrame(data_perfil_idade)

# PERFIL DO TRABALHADOR RESGATADO - Cor e/ou Raça
data_perfil_raca = {
    'Raça/Cor': ['Parda', 'Branca', 'Preta', 'Indígena'],
    'Percentual (%)': [80.90, 9.44, 8.60, 0.84]
}
df_perfil_raca = pd.DataFrame(data_perfil_raca)


# --- Seções da Dashboard (Corpo Principal) ---

###############################################################################################################
st.markdown("---") # Separador inicial

# Seção Introdutória: População Total de Trabalhadores em Condições Análogas à Escravidão
st.subheader("Total da População de Trabalhadores em Condições Análogas à Escravidão")

col_intro_ta_title, col_abs_ta = st.columns([3, 1])

with col_intro_ta_title:
    st.markdown("###### Total de Trabalhadores em Condições Análogas à Escravidão no Pará")

with col_abs_ta:
    st.metric(
        label="Número de Pessoas",
        value=f"{total_trabalhadores_analogos:,.0f}".replace(",", "."),
        delta=None
    )
st.caption(f"Fonte: {fonte_trabalhadores_analogos}")
st.markdown("---")


# 1. TRABALHADORES RESGATADOS
st.subheader("1. TRABALHADORES RESGATADOS")

col_resg_2023, col_resg_2021_2023 = st.columns(2)

with col_resg_2023:
    st.metric(
        label="Resgatados em 2023",
        value=f"{resgatados_2023} Trabalhadores",
        delta=None
    )

with col_resg_2021_2023:
    st.metric(
        label="Resgatados entre 2021 e 2023",
        value=f"{resgatados_2021_2023} Trabalhadores",
        delta=None
    )
st.caption(f"Fonte: {fonte_resgatados}")
st.markdown("---")


# 2. ATIVIDADE ECONÔMICA
st.subheader("2. ATIVIDADE ECONÔMICA")

# 2.1. Atividade Econômica que Mais Utiliza Mão de Obra Análoga à Escravidão
st.markdown("###### 2.1. Atividade Econômica que Mais Utiliza Mão de Obra Análoga à Escravidão")
fig_atividade_economica = px.bar(
    df_atividade_economica,
    x="Atividade Econômica",
    y="Percentual (%)",
    title="Atividades Econômicas com Mão de Obra Análoga à Escravidão",
    labels={"Percentual (%)": "Percentual (%)", "Atividade Econômica": "Atividade Econômica"},
    color="Percentual (%)",
    color_continuous_scale=px.colors.sequential.Oranges,
    text="Percentual (%)"
)
fig_atividade_economica.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
fig_atividade_economica.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_atividade_economica, use_container_width=True)
st.caption(f"Fonte: {fonte_atividade_economica}")
st.markdown("---")


# 3. LOCALIZAÇÃO
st.subheader("3. LOCALIZAÇÃO")

# 3.1. Municípios de Ocorrência
st.markdown("###### 3.1. Municípios de Ocorrência do Trabalho Análogo à Escravidão")
fig_ocorrencia_municipios = px.bar(
    df_ocorrencia_municipios,
    y="Município",
    x="Percentual (%)",
    orientation='h',
    title="Principais Municípios com Trabalho Análogo à Escravidão",
    labels={"Percentual (%)": "Percentual (%)", "Município": "Município"},
    color="Percentual (%)",
    color_continuous_scale=px.colors.sequential.Teal,
    text="Percentual (%)"
)
fig_ocorrencia_municipios.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
fig_ocorrencia_municipios.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_ocorrencia_municipios, use_container_width=True)
st.caption(f"Fonte: {fonte_ocorrencia_municipios}")
st.markdown("---")


# 4. PERFIL DO TRABALHADOR RESGATADO
st.subheader("4. PERFIL DO TRABALHADOR RESGATADO")

# 4.1. Por Sexo e 4.2. Por Escolaridade
col_perfil_sexo, col_perfil_escolaridade = st.columns(2)

with col_perfil_sexo:
    st.markdown("###### 4.1. Por Sexo")
    fig_perfil_sexo = px.pie(
        df_perfil_sexo,
        values='Percentual (%)',
        names='Gênero',
        title='Perfil do Trabalhador Resgatado por Sexo',
        hole=0.3
    )
    fig_perfil_sexo.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_perfil_sexo, use_container_width=True)

with col_perfil_escolaridade:
    st.markdown("###### 4.2. Por Escolaridade")
    fig_perfil_escolaridade = px.bar(
        df_perfil_escolaridade,
        y="Nível de Escolaridade",
        x="Percentual (%)",
        orientation='h',
        title='Perfil do Trabalhador Resgatado por Escolaridade',
        labels={"Percentual (%)": "Percentual (%)", "Nível de Escolaridade": "Nível de Escolaridade"},
        color="Percentual (%)",
        color_continuous_scale=px.colors.sequential.Blues,
        text="Percentual (%)"
    )
    fig_perfil_escolaridade.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig_perfil_escolaridade.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_perfil_escolaridade, use_container_width=True)

st.caption(f"Fonte: {fonte_perfil_resgatado}") # Fonte comum para o perfil
st.markdown("---")

# 4.3. Por Idade e 4.4. Por Cor e/ou Raça
col_perfil_idade, col_perfil_raca = st.columns(2)

with col_perfil_idade:
    st.markdown("###### 4.3. Por Idade")
    fig_perfil_idade = px.bar(
        df_perfil_idade,
        y="Faixa Etária",
        x="Percentual (%)",
        orientation='h',
        title='Perfil do Trabalhador Resgatado por Idade',
        labels={"Percentual (%)": "Percentual (%)", "Faixa Etária": "Faixa Etária"},
        color="Percentual (%)",
        color_continuous_scale=px.colors.sequential.Oranges,
        text="Percentual (%)"
    )
    fig_perfil_idade.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_perfil_idade.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_perfil_idade, use_container_width=True)

with col_perfil_raca:
    st.markdown("###### 4.4. Por Cor e/ou Raça")
    fig_perfil_raca = px.pie(
        df_perfil_raca,
        values='Percentual (%)',
        names='Raça/Cor',
        title='Perfil do Trabalhador Resgatado por Cor e/ou Raça',
        hole=0.3
    )
    fig_perfil_raca.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_perfil_raca, use_container_width=True)

st.caption(f"Fonte: {fonte_perfil_resgatado}") # Fonte comum para o perfil
st.markdown("---")