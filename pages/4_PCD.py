import pandas as pd
import plotly.express as px
import streamlit as st

# --- Configuração da Página Streamlit ---
st.set_page_config(page_title="Pessoas com Deficiência (PCD)", page_icon=":wheelchair:", layout="wide")

# --- Título Principal da Página ---
st.header("PESSOAS COM DEFICIÊNCIA (PCD)")

# --- 1. Definição Global de Variáveis e DataFrames ---

# População Total PCD
total_pcd_pessoas = 813111
percentual_pcd_pop = 9.5
fonte_populacao_pcd = "IBGE 2022"

# EDUCAÇÃO - TAXA DE ANALFABETISMO
data_analfabetismo_pcd = {
    'Faixa Etária': ['15 anos ou +', '18 anos ou +', '25 anos ou +', '40 anos ou +', '60 anos ou +'],
    'Taxa de Analfabetismo (%)': [22.0, 22.0, 22.0, 24.0, 29.0]
}
df_analfabetismo_pcd = pd.DataFrame(data_analfabetismo_pcd)
fonte_analfabetismo_pcd = "IBGE 2022"

# EDUCAÇÃO - ACESSIBILIDADE NA EDUCAÇÃO BÁSICA
data_acessibilidade_educacao_pcd = {
    'Recurso de Acessibilidade': [
        'Elevador', 'Sinalização sonora', 'Sinalização tátil', 'Sinalização visual',
        'Pisos táteis', 'Corrimão e guarda corpos',
        'Sala de recursos multifuncionais para atendimento educação especializada',
        'Portas de vão livre de no mínimo 80 cm',
        'Banheiro acessível, adequado ao uso de pessoas com deficiência ou mobilidade reduzidas',
        'Rampas'
    ],
    'Com recurso (%)': [1.0, 1.0, 3.0, 5.0, 6.0, 11.0, 19.0, 24.0, 32.0, 38.0],
    'Sem recurso (%)': [99.0, 99.0, 97.0, 95.0, 94.0, 89.0, 81.0, 76.0, 68.0, 62.0]
}
df_acessibilidade_educacao_pcd = pd.DataFrame(data_acessibilidade_educacao_pcd)
# Para gráfico de barras empilhado, melt o DataFrame
df_acessibilidade_educacao_pcd_melted = df_acessibilidade_educacao_pcd.melt(
    id_vars='Recurso de Acessibilidade',
    var_name='Situação',
    value_name='Percentual (%)'
)
fonte_acessibilidade_educacao_pcd = "IBGE 2022"

# EDUCAÇÃO - NÍVEL DE INSTRUÇÃO
data_nivel_instrucao_pcd = {
    'Nível de Instrução': ['Sem instrução e fundamental incompleto', 'Fundamental completo e médio incompleto',
                            'Médio completo e superior incompleto', 'Superior'],
    'Proporção (%)': [69.0, 10.0, 17.0, 4.0]
}
df_nivel_instrucao_pcd = pd.DataFrame(data_nivel_instrucao_pcd)
fonte_nivel_instrucao_pcd = "IBGE 2022"

# SAÚDE - SITUAÇÃO DA SAÚDE (Autoavaliação)
data_situacao_saude_pcd = {
    'Avaliação': ['Muito boa', 'Boa', 'Regular', 'Ruim', 'Muito ruim'],
    'Proporção (%)': [0.6, 17.1, 55.8, 20.6, 5.8]
}
df_situacao_saude_pcd = pd.DataFrame(data_situacao_saude_pcd)
fonte_situacao_saude_pcd = "IBGE 2019 / Ministério da Saúde 2019"

# SAÚDE - PRÁTICA DE EXERCICIO FÍSICO OU ESPORTE
percentual_pratica_exercicio_pcd = 18.7
fonte_pratica_exercicio_pcd = "IBGE 2019 / Ministério da Saúde 2019"

# TRABALHO - PARTICIPAÇÃO NA FORÇA DE TRABALHO POR GRUPO DE IDADE
data_participacao_trabalho_idade_pcd = {
    'Grupo de Idade': ['PCDs 14 a 29 anos', 'PCDs 30 a 49 anos', 'PCDs 50 a 59 anos', 'PCDs 60 anos ou mais'],
    'Participação (%)': [36.0, 63.3, 47.9, 18.2]
}
df_participacao_trabalho_idade_pcd = pd.DataFrame(data_participacao_trabalho_idade_pcd)
fonte_trabalho_pcd = "IBGE 2022" # Fonte comum para seções de trabalho

# TRABALHO - PARTICIPAÇÃO NA FORÇA DE TRABALHO POR SEXO
data_participacao_trabalho_sexo_pcd = {
    'Sexo': ['Homens', 'Mulheres'],
    'Participação (%)': [42.5, 33.0]
}
df_participacao_trabalho_sexo_pcd = pd.DataFrame(data_participacao_trabalho_sexo_pcd)

# TRABALHO - PARTICIPAÇÃO NA FORÇA DE TRABALHO POR COR OU RAÇA
data_participacao_trabalho_raca_pcd = {
    'Raça/Cor': ['Branca', 'Parda', 'Preta'],
    'Participação (%)': [31.6, 37.8, 39.2]
}
df_participacao_trabalho_raca_pcd = pd.DataFrame(data_participacao_trabalho_raca_pcd)

# TRABALHO - NÍVEL DE OCUPAÇÃO POR GRUPO DE IDADE
data_nivel_ocupacao_idade_pcd = {
    'Grupo de Idade': ['PCDs 14 a 29 anos', 'PCDs 30 a 49 anos', 'PCDs 50 a 59 anos', 'PCDs 60 anos ou mais'],
    'Nível de Ocupação (%)': [30.1, 58.9, 46.0, 17.7]
}
df_nivel_ocupacao_idade_pcd = pd.DataFrame(data_nivel_ocupacao_idade_pcd)

# TRABALHO - NÍVEL DE OCUPAÇÃO POR SEXO
data_nivel_ocupacao_sexo_pcd = {
    'Sexo': ['Homens', 'Mulheres'],
    'Nível de Ocupação (%)': [41.1, 29.9]
}
df_nivel_ocupacao_sexo_pcd = pd.DataFrame(data_nivel_ocupacao_sexo_pcd)

# TRABALHO - NÍVEL DE OCUPAÇÃO POR COR OU RAÇA
data_nivel_ocupacao_raca_pcd = {
    'Raça/Cor': ['Branca', 'Parda', 'Preta'],
    'Nível de Ocupação (%)': [30.2, 35.3, 35.9]
}
df_nivel_ocupacao_raca_pcd = pd.DataFrame(data_nivel_ocupacao_raca_pcd)

# TRABALHO - RENDIMENTO MÉDIO HABITUAL POR SEXO
data_rendimento_medio_sexo_pcd = {
    'Sexo': ['Homens', 'Mulheres'],
    'Rendimento Médio (R$)': [1219, 1237]
}
df_rendimento_medio_sexo_pcd = pd.DataFrame(data_rendimento_medio_sexo_pcd)

# VIOLÊNCIA - NOTIFICAÇÃO POR TIPO DE VIOLÊNCIA
data_notificacao_violencia_pcd = {
    'Tipo de Violência': ['Psicológica/Moral', 'Física', 'Violência sexual', 'Lesão autoprovocada', 'Negligência ou abandono'],
    'Número Absoluto': [73, 111, 50, 33, 22]
}
df_notificacao_violencia_pcd = pd.DataFrame(data_notificacao_violencia_pcd)
fonte_notificacao_violencia_pcd = "Sistema Nacional de Agravo de Notificação (SINAN) / Ministério da Saúde 2022"

# VIOLÊNCIA - PROPORÇÃO DE PESSOAS QUE SOFRERAM VIOLÊNCIA
data_proporcao_sofrimento_violencia_pcd = {
    'Tipo de Violência': [
        'Ameaças e/ou relações sexuais forçadas ou quaisquer outros atos sexuais contra a vontade',
        'Ameaça e/ou ferimento com faca, arma de fogo ou alguma outra arma ou objeto',
        'Ameaça de ferir ou machucar alguém importante',
        'Ameaças, ofensas, xingamentos e exposição de imagens sem consentimento nas redes sociais ou celular',
        'Destruição proposital de pertences',
        'Gritos ou xingamentos',
        'Ofensa, humilhação e/ou ridicularização na frente de outras pessoas',
        'Soco, chute e/ou arrastão pelo cabelo',
        'Tapa ou bofetada',
        'Tentativa ou efetivo estrangulamento, asfixia ou queimadura proposital',
        'Toque, manipulação, beijo e/ou exposição de partes do corpo contra a vontade',
        'Empurrão, segurar com força e/ou jogar algo com a intenção de machucar'
    ],
    'Percentual (%)': [
        0.5, 2.1, 4.7, 1.1, 3.1, 13.9, 10.3, 1.7, 2.4, 1.0, 1.7, 2.3
    ]
}
df_proporcao_sofrimento_violencia_pcd = pd.DataFrame(data_proporcao_sofrimento_violencia_pcd)
fonte_proporcao_sofrimento_violencia_pcd = "Pesquisa Nacional de Saúde, Ouvidoria Nacional de Direitos Humanos 2019 / SINAN 2019"

# CIDADANIA - Políticas de Acessibilidade
fonte_cidadania_pcd_secult = "Secult PA 2024"
guia_acessibilidade = "Guia de Acessibilidade, Inclusão e Protagonismo da Pessoa com Deficiência e do Migrante"

# CIDADANIA - Direito à Gratuidade no Transporte Público
fonte_cidadania_pcd_artran = "Lei Estadual nº 10.308/ 2023. Agência de Regulação e Controle dos Serviços Públicos de Transporte ARTRAN 2025"
direito_gratuidade_transporte = "Direito à Gratuidade no Transporte Público"

# CIDADANIA - Políticas Públicas agregadas de apoio
fonte_cidadania_pcd_seaster = "Secretaria de Estado de Assistência Social, Trabalho, Emprego e Renda SEASTER 2025"
politicas_publicas_apoio = """
Acolhimento psicossocial, inserção ao mercado de trabalho,
a programas de habitação ‘Sua Casa’, qualificação de órgãos
para melhor atendimento à pessoa com deficiência e
à promoção de serviços de saúde
"""

# SEGURIDADE SOCIAL - Beneficiários de Prestação Continuada
beneficiarios_bpc_numero = 131812
beneficiarios_bpc_percentual = 16.2
fonte_beneficiarios_bpc = "IBGE / Benefício de Prestação Continuada (BPC) 2022"


# --- Seções da Dashboard (Corpo Principal) ---

###############################################################################################################
st.markdown("---") # Separador inicial

# Seção Introdutória: População Total PCD
st.subheader("Total da População PCD no Pará")

col_intro_pcd_title, col_abs_pcd, col_perc_pcd = st.columns([3, 1, 1])

with col_intro_pcd_title:
    st.markdown("###### Total da População PCD no Pará")

with col_abs_pcd:
    st.metric(
        label="Número de Pessoas",
        value=f"{total_pcd_pessoas:,.0f}".replace(",", "."),
        delta=None
    )

with col_perc_pcd:
    st.metric(
        label="Percentual na População Total",
        value=f"{percentual_pcd_pop:.1f}%",
        delta=None
    )
st.caption(f"Fonte: {fonte_populacao_pcd}")
st.markdown("---")


# 1. EDUCAÇÃO
st.header("1. EDUCAÇÃO")

# 1.1. Taxa de Analfabetismo
st.subheader("1.1. Taxa de Analfabetismo")

fig_analfabetismo_pcd = px.bar(
    df_analfabetismo_pcd,
    x="Faixa Etária",
    y="Taxa de Analfabetismo (%)",
    title="Taxa de Analfabetismo de PCDs por Faixa Etária",
    labels={"Taxa de Analfabetismo (%)": "Taxa (%)"},
    color="Taxa de Analfabetismo (%)",
    color_continuous_scale=px.colors.sequential.Plotly3,
    text="Taxa de Analfabetismo (%)"
)
fig_analfabetismo_pcd.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_analfabetismo_pcd.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_analfabetismo_pcd, use_container_width=True)
st.caption(f"Fonte: {fonte_analfabetismo_pcd}")
st.markdown("---")

# 1.2. Acessibilidade na Educação Básica
st.subheader("1.2. Acessibilidade na Educação Básica")

fig_acessibilidade_educacao_pcd = px.bar(
    df_acessibilidade_educacao_pcd_melted,
    y="Recurso de Acessibilidade",
    x="Percentual (%)",
    color="Situação",
    barmode="group", # Barras agrupadas para comparar Com/Sem recurso
    orientation='h',
    title="Percentual de Escolas com Recurso de Acessibilidade",
    labels={"Percentual (%)": "Percentual (%)", "Recurso de Acessibilidade": "Recurso", "Situação": "Situação"},
    text="Percentual (%)"
)
fig_acessibilidade_educacao_pcd.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_acessibilidade_educacao_pcd.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_acessibilidade_educacao_pcd, use_container_width=True)
st.caption(f"Fonte: {fonte_acessibilidade_educacao_pcd}")
st.markdown("---")

# 1.3. Nível de Instrução
st.subheader("1.3. Nível de Instrução")
fig_nivel_instrucao_pcd = px.pie(
    df_nivel_instrucao_pcd,
    values='Proporção (%)',
    names='Nível de Instrução',
    title='Nível de Instrução de Pessoas PCDs (25 anos ou mais)',
    hole=0.3
)
fig_nivel_instrucao_pcd.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
st.plotly_chart(fig_nivel_instrucao_pcd, use_container_width=True)
st.caption(f"Fonte: {fonte_nivel_instrucao_pcd}")
st.markdown("---")


# 2. SAÚDE
st.header("2. SAÚDE")

# 2.1. Situação da Saúde (Autoavaliação)
st.subheader("2.1. Situação da Saúde (Autoavaliação)")

fig_situacao_saude_pcd = px.pie(
    df_situacao_saude_pcd,
    values='Proporção (%)',
    names='Avaliação',
    title='Autoavaliação da Situação de Saúde de PCDs',
    hole=0.3
)
fig_situacao_saude_pcd.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
st.plotly_chart(fig_situacao_saude_pcd, use_container_width=True)
st.caption(f"Fonte: {fonte_situacao_saude_pcd}")
st.markdown("---")

# 2.2. Prática de Exercício Físico ou Esporte
st.subheader("2.2. Prática de Exercício Físico ou Esporte")

st.metric(
    label="Porcentagem de PCDs que Praticam Exercício Físico ou Esporte",
    value=f"{percentual_pratica_exercicio_pcd:.1f}%",
    delta=None
)
st.caption(f"Fonte: {fonte_pratica_exercicio_pcd}")
st.markdown("---")


# 3. TRABALHO
st.header("3. TRABALHO")

# 3.1. Participação na Força de Trabalho por Grupo de Idade
st.subheader("3.1. Participação na Força de Trabalho por Grupo de Idade")

fig_participacao_trabalho_idade_pcd = px.bar(
    df_participacao_trabalho_idade_pcd,
    x="Grupo de Idade",
    y="Participação (%)",
    title="Participação de PCDs na Força de Trabalho por Grupo de Idade",
    labels={"Participação (%)": "Percentual de Participação (%)", "Grupo de Idade": "Grupo de Idade"},
    color="Participação (%)",
    color_continuous_scale=px.colors.sequential.Oranges,
    text="Participação (%)"
)
fig_participacao_trabalho_idade_pcd.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_participacao_trabalho_idade_pcd.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_participacao_trabalho_idade_pcd, use_container_width=True)
st.caption(f"Fonte: {fonte_trabalho_pcd}")
st.markdown("---")

# 3.2. Participação na Força de Trabalho por Sexo e 3.3. Participação na Força de Trabalho por Cor ou Raça
col_part_sexo_pcd, col_part_raca_pcd = st.columns(2)

with col_part_sexo_pcd:
    st.subheader("3.2. Participação na Força de Trabalho por Sexo")
    fig_participacao_trabalho_sexo_pcd = px.bar(
        df_participacao_trabalho_sexo_pcd,
        x="Sexo",
        y="Participação (%)",
        title="Participação de PCDs na Força de Trabalho por Sexo",
        labels={"Participação (%)": "Percentual de Participação (%)", "Sexo": "Sexo"},
        color="Participação (%)",
        color_continuous_scale=px.colors.sequential.Greens,
        text="Participação (%)"
    )
    fig_participacao_trabalho_sexo_pcd.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_participacao_trabalho_sexo_pcd.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_participacao_trabalho_sexo_pcd, use_container_width=True)
    st.caption(f"Fonte: {fonte_trabalho_pcd}")

with col_part_raca_pcd:
    st.subheader("3.3. Participação na Força de Trabalho por Cor ou Raça")
    fig_participacao_trabalho_raca_pcd = px.bar(
        df_participacao_trabalho_raca_pcd,
        x="Raça/Cor",
        y="Participação (%)",
        title="Participação de PCDs na Força de Trabalho por Cor ou Raça",
        labels={"Participação (%)": "Percentual de Participação (%)", "Raça/Cor": "Raça/Cor"},
        color="Participação (%)",
        color_continuous_scale=px.colors.sequential.Blues,
        text="Participação (%)"
    )
    fig_participacao_trabalho_raca_pcd.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_participacao_trabalho_raca_pcd.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_participacao_trabalho_raca_pcd, use_container_width=True)
    st.caption(f"Fonte: {fonte_trabalho_pcd}")
st.markdown("---")

# 3.4. Nível de Ocupação por Grupo de Idade e 3.5. Nível de Ocupação por Sexo
col_ocup_idade_pcd, col_ocup_sexo_pcd = st.columns(2)

with col_ocup_idade_pcd:
    st.subheader("3.4. Nível de Ocupação por Grupo de Idade")
    fig_nivel_ocupacao_idade_pcd = px.bar(
        df_nivel_ocupacao_idade_pcd,
        x="Grupo de Idade",
        y="Nível de Ocupação (%)",
        title="Nível de Ocupação de PCDs por Grupo de Idade",
        labels={"Nível de Ocupação (%)": "Percentual de Ocupação (%)", "Grupo de Idade": "Grupo de Idade"},
        color="Nível de Ocupação (%)",
        color_continuous_scale=px.colors.sequential.Oranges,
        text="Nível de Ocupação (%)"
    )
    fig_nivel_ocupacao_idade_pcd.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_nivel_ocupacao_idade_pcd.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_nivel_ocupacao_idade_pcd, use_container_width=True)
    st.caption(f"Fonte: {fonte_trabalho_pcd}")

with col_ocup_sexo_pcd:
    st.subheader("3.5. Nível de Ocupação por Sexo")
    fig_nivel_ocupacao_sexo_pcd = px.bar(
        df_nivel_ocupacao_sexo_pcd,
        x="Sexo",
        y="Nível de Ocupação (%)",
        title="Nível de Ocupação de PCDs por Sexo",
        labels={"Nível de Ocupação (%)": "Percentual de Ocupação (%)", "Sexo": "Sexo"},
        color="Nível de Ocupação (%)",
        color_continuous_scale=px.colors.sequential.Greens,
        text="Nível de Ocupação (%)"
    )
    fig_nivel_ocupacao_sexo_pcd.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_nivel_ocupacao_sexo_pcd.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_nivel_ocupacao_sexo_pcd, use_container_width=True)
    st.caption(f"Fonte: {fonte_trabalho_pcd}")
st.markdown("---")

# 3.6. Nível de Ocupação por Cor ou Raça e 3.7. Rendimento Médio Habitual por Sexo
col_ocup_raca_pcd, col_rend_sexo_pcd = st.columns(2)

with col_ocup_raca_pcd:
    st.subheader("3.6. Nível de Ocupação por Cor ou Raça")
    fig_nivel_ocupacao_raca_pcd = px.bar(
        df_nivel_ocupacao_raca_pcd,
        x="Raça/Cor",
        y="Nível de Ocupação (%)",
        title="Nível de Ocupação de PCDs por Cor ou Raça",
        labels={"Nível de Ocupação (%)": "Percentual de Ocupação (%)", "Raça/Cor": "Raça/Cor"},
        color="Nível de Ocupação (%)",
        color_continuous_scale=px.colors.sequential.Blues,
        text="Nível de Ocupação (%)"
    )
    fig_nivel_ocupacao_raca_pcd.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_nivel_ocupacao_raca_pcd.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_nivel_ocupacao_raca_pcd, use_container_width=True)
    st.caption(f"Fonte: {fonte_trabalho_pcd}")

with col_rend_sexo_pcd:
    st.subheader("3.7. Rendimento Médio Habitual por Sexo")
    fig_rendimento_medio_sexo_pcd = px.bar(
        df_rendimento_medio_sexo_pcd,
        x="Sexo",
        y="Rendimento Médio (R$)",
        title="Rendimento Médio Habitual de PCDs por Sexo",
        labels={"Rendimento Médio (R$)": "Rendimento Médio (R$)", "Sexo": "Sexo"},
        color="Rendimento Médio (R$)",
        color_continuous_scale=px.colors.sequential.Plasma,
        text="Rendimento Médio (R$)"
    )
    fig_rendimento_medio_sexo_pcd.update_traces(texttemplate='R$ %{text:,.0f}', textposition='outside')
    fig_rendimento_medio_sexo_pcd.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_rendimento_medio_sexo_pcd, use_container_width=True)
    st.caption(f"Fonte: {fonte_trabalho_pcd}")
st.markdown("---")


# 3.8. SEGURIDADE SOCIAL (Antiga seção 6, agora subtópico de TRABALHO)
st.subheader("3.8. SEGURIDADE SOCIAL") # Título da nova subseção

# 3.8.1. Beneficiários de Prestação Continuada
st.markdown("###### 3.8.1. Beneficiários de Prestação Continuada") # Mantendo a numeração interna da seção

col_bpc_num, col_bpc_perc = st.columns(2)

with col_bpc_num:
    st.metric(
        label="Número de Beneficiários de BPC",
        value=f"{beneficiarios_bpc_numero:,.0f}".replace(",", "."),
        delta=None
    )
with col_bpc_perc:
    st.metric(
        label="Percentual de Beneficiários de BPC na População PCD",
        value=f"{beneficiarios_bpc_percentual:.1f}%",
        delta=None
    )
st.caption(f"Fonte: {fonte_beneficiarios_bpc}")
st.markdown("---")


# 4. VIOLÊNCIA (Antigo tópico 4, agora mantém sua posição)
st.header("4. VIOLÊNCIA")

# 4.1. Notificação por Tipo de Violência
st.subheader("4.1. Notificação por Tipo de Violência")

fig_notificacao_violencia_pcd = px.bar(
    df_notificacao_violencia_pcd,
    x="Tipo de Violência",
    y="Número Absoluto",
    title="Notificação de Violência contra PCDs por Tipo",
    labels={"Número Absoluto": "Número de Notificações", "Tipo de Violência": "Tipo de Violência"},
    color="Número Absoluto",
    color_continuous_scale=px.colors.sequential.Purples,
    text="Número Absoluto"
)
fig_notificacao_violencia_pcd.update_traces(texttemplate='%{text}', textposition='outside')
fig_notificacao_violencia_pcd.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_notificacao_violencia_pcd, use_container_width=True)
st.caption(f"Fonte: {fonte_notificacao_violencia_pcd}")
st.markdown("---")

# 4.2. Proporção de Pessoas que Sofreram Violência
st.subheader("4.2. Proporção de Pessoas que Sofreram Violência")

fig_proporcao_sofrimento_violencia_pcd = px.bar(
    df_proporcao_sofrimento_violencia_pcd,
    y="Tipo de Violência",
    x="Percentual (%)",
    orientation='h',
    title="Proporção de Pessoas PCDs que Sofreram Violência por Tipo",
    labels={"Percentual (%)": "Percentual (%)", "Tipo de Violência": "Tipo de Violência"},
    color="Percentual (%)",
    color_continuous_scale=px.colors.sequential.Plasma,
    text="Percentual (%)"
)
fig_proporcao_sofrimento_violencia_pcd.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_proporcao_sofrimento_violencia_pcd.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_proporcao_sofrimento_violencia_pcd, use_container_width=True)
st.caption(f"Fonte: {fonte_proporcao_sofrimento_violencia_pcd}")
st.markdown("---")


# 5. CIDADANIA (Antigo tópico 5, agora mantém sua posição)
st.header("5. CIDADANIA")

# 5.1. Políticas de Acessibilidade e Apoio (seção descritiva)
st.subheader("5.1. Políticas de Acessibilidade e Apoio")

st.markdown("###### Políticas de Acessibilidade")
st.write(f"- **Guia de Acessibilidade, Inclusão e Protagonismo da Pessoa com Deficiência e do Migrante**")
st.caption(f"Fonte: {fonte_cidadania_pcd_secult}")

st.markdown("###### Direito à Gratuidade no Transporte Público")
st.write(f"- {direito_gratuidade_transporte}")
st.caption(f"Fonte: {fonte_cidadania_pcd_artran}")

st.markdown("###### Políticas Públicas Agregadas de Apoio")
st.write(f"- {politicas_publicas_apoio}")
st.caption(f"Fonte: {fonte_cidadania_pcd_seaster}")
st.markdown("---")