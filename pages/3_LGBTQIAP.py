import pandas as pd
import plotly.express as px
import streamlit as st

# --- Configuração da Página Streamlit ---
st.set_page_config(page_title="LGBTQIAP+", page_icon=":rainbow:", layout="wide")

# --- Título Principal da Página ---
st.header("LGBTQIAP+")

# --- 1. Definição Global de Variáveis e DataFrames ---

# População Total LGBTQIAP+
total_pop_lgbt = 115398
fonte_pop_lgbt = "IBGE 2019"

# GÊNERO E SEXUALIDADE - Orientação Sexual
data_orientacao_sexual = {
    'Orientação Sexual': ['Heterossexual', 'Recusou responder', 'Homossexual', 'Não Sabe', 'Bissexual', 'Outra orientação'],
    'Proporção (%)': [92.4, 2.3, 1.2, 1.1, 0.7, 0.1]
}
df_orientacao_sexual = pd.DataFrame(data_orientacao_sexual)
fonte_genero_sexualidade = "Pesquisa Nacional de Saúde (PNS) IBGE 2019"

# CONTEXTO SOCIOECONÔMICO - Perfil Étnico/Racial
data_perfil_etnico_racial = {
    'Orientação Sexual': ['Heterossexual', 'Recusou responder', 'Homossexual', 'Não Sabe', 'Bissexual', 'Outra orientação'],
    'Branco (%)': [43.05, 40.01, 42.03, 32.4, 41.2, 41.6],
    'Parda (%)': [43.6, 47.2, 45.5, 54.6, 43.2, 51.5],
    'Preta (%)': [11.5, 11.5, 10.7, 12.1, 13.2, 6.9],
    'Amarela (%)': [0.9, 0.8, 0.8, 0.5, 1.1, 0.0],
    'Indígena (%)': [0.5, 0.3, 0.7, 0.5, 1.2, 0.0]
}
df_perfil_etnico_racial = pd.DataFrame(data_perfil_etnico_racial)
df_perfil_etnico_racial_melted = df_perfil_etnico_racial.melt(
    id_vars='Orientação Sexual',
    var_name='Raça/Cor',
    value_name='Proporção (%)'
)

# CONTEXTO SOCIOECONÔMICO - Localidade
data_localidade_sexualidade = {
    'Orientação Sexual': ['Heterossexual', 'Recusou responder', 'Homossexual', 'Não Sabe', 'Bissexual'],
    'Urbano (%)': [86.2, 86.7, 94.2, 80.5, 93.1],
    'Rural (%)': [13.8, 16.7, 5.8, 19.5, 5.8]
}
df_localidade_sexualidade = pd.DataFrame(data_localidade_sexualidade)
df_localidade_sexualidade_melted = df_localidade_sexualidade.melt(
    id_vars='Orientação Sexual',
    var_name='Localidade',
    value_name='Proporção (%)'
)

# CONTEXTO SOCIOECONÔMICO - Faixa Etária
data_faixa_etaria_sexualidade = {
    'Faixa Etária': ['18 a 29', '30 a 39', '40 a 49', '50 a 59', '60 a 69', '70 a 79', '80 ou mais'],
    'Heterossexual (%)': [20.9, 21.1, 18.4, 17.3, 12.5, 6.7, 3.0],
    'Recusou responder (%)': [31.0, 16.2, 15.5, 18.8, 10.4, 6.5, 1.5],
    'Homossexual (%)': [51.08, 24.6, 13.3, 7.8, 1.8, 0.3, 0.4],
    'Não sabe (%)': [34.2, 18.8, 14.3, 12.0, 5.0, 4.1, 2.6],
    'Bissexual (%)': [67.9, 16.1, 6.9, 6.7, 1.7, 0.5, 0.1],
    'Outra orientação (%)': [45.4, 16.0, 11.7, 9.4, 6.6, 9.9, 0.9]
}
df_faixa_etaria_sexualidade = pd.DataFrame(data_faixa_etaria_sexualidade)
df_faixa_etaria_sexualidade_melted = df_faixa_etaria_sexualidade.melt(
    id_vars='Faixa Etária',
    var_name='Orientação Sexual',
    value_name='Proporção (%)'
)

# CONDIÇÕES DE SAÚDE - Autoavaliação
data_autoavaliacao_saude = {
    'Orientação Sexual': ['Heterossexual', 'Recusou responder', 'Homossexual', 'Não Sabe', 'Bissexual', 'Outra orientação'],
    'Muito Boa (%)': [15, 12, 23, 10, 19, 7],
    'Boa (%)': [51, 51, 54, 55, 49, 47],
    'Regular (%)': [28, 32, 21, 29, 28, 39],
    'Ruim (%)': [2, 4, 2, 5, 2, 6],
    'Muito Ruim (%)': [1, 1, 0, 1, 2, 1]
}
df_autoavaliacao_saude = pd.DataFrame(data_autoavaliacao_saude)
df_autoavaliacao_saude_melted = df_autoavaliacao_saude.melt(
    id_vars='Orientação Sexual',
    var_name='Autoavaliação de Saúde',
    value_name='Proporção (%)'
)
fonte_condicoes_saude = "PNS 2019 / Cadastro Nacional de Estabelecimentos de Saúde 2023 / IBGE"

# CONDIÇÕES DE SAÚDE - Unidades (Centros POP)
data_centros_pop = {
    'Indicador': ['Número Total de Centro POP', 'Atenderam Pessoas LGBTQIAP+', 'Tiveram profissionais capacitados'],
    'Contagem': [6, 5, 2]
}
df_centros_pop = pd.DataFrame(data_centros_pop)

# CONDIÇÕES DE SAÚDE - Saúde Mental
data_saude_mental_lgbt = {
    'Orientação Sexual': ['Heterossexual', 'Recusou responder', 'Homossexual', 'Não Sabe', 'Bissexual', 'Outra orientação'],
    'Prevalência (%)': [10.1, 10.5, 13.2, 8.4, 21.1, 16.7]
}
df_saude_mental_lgbt = pd.DataFrame(data_saude_mental_lgbt)

# CONDIÇÕES DE SAÚDE - Frequência de Atividades Coletivas
data_atividades_coletivas = {
    'Frequência': ['Nenhuma vez', 'Uma vez ao ano', 'Algumas vezes no ano', '2 ou 3 ao Mês', '1 vez por semana', 'Mais de 1 vez na semana'],
    'Heterossexual (%)': [50, 2, 13, 6, 10, 18],
    'Recusou responder (%)': [47, 2, 14, 5, 14, 18],
    'Homossexual (%)': [31, 2, 15, 8, 17, 28],
    'Não sabe (%)': [52, 1, 14, 7, 11, 15],
    'Bissexual (%)': [21, 3, 17, 8, 22, 22],
    'Outra orientação (%)': [41, 0, 15, 19, 9, 16]
}
df_atividades_coletivas = pd.DataFrame(data_atividades_coletivas)
df_atividades_coletivas_melted = df_atividades_coletivas.melt(
    id_vars='Frequência',
    var_name='Orientação Sexual',
    value_name='Proporção (%)'
)

# NÍVEL EDUCACIONAL
fonte_educacao_lgbt = "Sistema de Avaliação da Educação Básica (SAEB) INEP 2019 e 2021"
data_perfil_estudantes = {
    'Nível Educacional': [
        'Sem instrução', 'Fundamental Incompleto', 'Fundamental Completo',
        'Médio Incompleto', 'Médio Completo', 'Superior Incompleto', 'Superior Completo'
    ],
    'Heterossexual (%)': [6, 29, 8, 6, 30, 5, 16],
    'Recusou (%)': [6, 29, 9, 10, 32, 3, 11],
    'Homossexual (%)': [1, 7, 7, 15, 3, 11, 30],
    'Não Sabe (%)': [11, 31, 13, 9, 31, 2, 3],
    'Bissexual (%)': [1, 9, 5, 6, 35, 16, 22],
    'Outra orientação (%)': [14, 18, 7, 2, 32, 11, 16]
}
df_perfil_estudantes = pd.DataFrame(data_perfil_estudantes)
df_perfil_estudantes_melted = df_perfil_estudantes.melt(
    id_vars='Nível Educacional',
    var_name='Orientação Sexual',
    value_name='Proporção (%)'
)

# SEGURANÇA
fonte_seguranca_lgbt = "Ouvidoria Nacional de Direitos Humanos 2022 / Sistema de Informação de Agravos de Notificação (SINAN) 2015-2022"
data_seguranca = {
    'Indicador': [
        'Municípios SEM conselhos específicos',
        'Municípios SEM programas de promoção de direitos',
        'Municípios SEM conferências municipais (2015-2019)',
        'Municípios SEM legislação específica de proteção ou reconhecimento de nome social'
    ],
    'Percentual (%)': [99.0, 98.0, 97.43, 98.0]
}
df_seguranca = pd.DataFrame(data_seguranca)

# RENDA FAMILIAR
fonte_renda_familiar_lgbt = "Pesquisa Nacional de Saúde (PNS) IBGE 2019"
data_renda_familiar = {
    'Faixa Salário-Mínimo': [
        'Sem renda a 1/2', 'De 1/2 a 1', 'De 1 a 3', 'De 3 a 5', 'Mais de 5'
    ],
    'Heterossexual (%)': [22.5, 29.1, 37.3, 6.4, 5.2],
    'Recusou (%)': [26.1, 28.9, 37.7, 4.7, 2.6],
    'Homossexual (%)': [13.1, 25.1, 40.1, 9.8, 12.0],
    'Não Sabe (%)': [34.3, 35.5, 26.8, 2.1, 1.3],
    'Bissexual (%)': [20.0, 23.8, 37.3, 12.3, 5.9],
    'Outra orientação (%)': [12.7, 50.7, 28.8, 7.8, 0.0]
}
df_renda_familiar = pd.DataFrame(data_renda_familiar)
df_renda_familiar_melted = df_renda_familiar.melt(
    id_vars='Faixa Salário-Mínimo',
    var_name='Orientação Sexual',
    value_name='Proporção (%)'
)

# SEGURIDADE SOCIAL - Acesso a Serviços
fonte_seguridade_social_lgbt = "Censo Sistema Único de Assistência Social (SUAS) 2022"
data_acesso_servicos_seg_social = {
    'Serviço': [
        'Acesso aos Centros POP', 'Acesso ao CREAS', 'Acesso ao CRAS (PAIF)',
        'Cadúnico (CRAS)', 'Centro de Convivência', 'Equipe Volante (CRAS)', 'PCF (CRAS)'
    ],
    'Percentual (%)': [97.5, 54.0, 45.7, 39.1, 13.2, 5.4, 4.0]
}
df_acesso_servicos_seg_social = pd.DataFrame(data_acesso_servicos_seg_social)

# SEGURIDADE SOCIAL - Centros de Convivência (Absolutos)
data_centros_convivencia_lgbt = {
    'Indicador': [
        'Total de Centro de Convivências',
        'Abordaram temas de Orientação Sexual e Identidade de Gênero',
        'Atenderam pessoas LGBTQIAP+ nos serviços de convivências e fortalecimentos de vínculos'
    ],
    'Número Absoluto': [73, 36, 13]
}
df_centros_convivencia_lgbt = pd.DataFrame(data_centros_convivencia_lgbt)

# NOVOS DADOS: SEGURIDADE SOCIAL - CRAS e CREAS Atendimentos
data_cras_atendimentos_lgbt = {
    'Tipo de Atendimento': [
        'Total de CRAS',
        'Serviços de proteção e atendimento integral a família (PAIF)',
        'Cadastro Único',
        'Outros atendimentos',
        'Não há presenças de pessoas LGBTQIAP+',
        'Atenderam na equipe volante',
        'Não atendem pessoas LGBTQIAP+',
        'Atenderam no Programa Criança Feliz (PCF)'
    ],
    'Número Absoluto': [266, 153, 116, 84, 52, 22, 19, 7]
}
df_cras_atendimentos_lgbt = pd.DataFrame(data_cras_atendimentos_lgbt)

data_paefi_ingressos_lgbt = {
    'Ano': [2017, 2018, 2019, 2020, 2021, 2022],
    'Número de Pessoas': [70, 53, 94, 68, 82, 62]
}
df_paefi_ingressos_lgbt = pd.DataFrame(data_paefi_ingressos_lgbt)

data_creas_atendimentos_grupo_etario_lgbt = {
    'Grupo Etário / Situação': [
        'Total de CREAS',
        'Não atende esse tipo de situação de discriminação em decorrência da orientação sexual e/ou da identidade de gênero',
        'Crianças e adolescentes vitimas',
        'Homens adultos vitimas',
        'Mulheres adultas vitimas',
        'Pessoas idosas vitimas'
    ],
    'Número Absoluto': [136, 64, 59, 49, 45, 25]
}
df_creas_atendimentos_grupo_etario_lgbt = pd.DataFrame(data_creas_atendimentos_grupo_etario_lgbt)


# VIOLÊNCIA - Quem são as vítimas
fonte_violencia_lgbt = "Ouvidoria Nacional de Direitos Humanos 2022 / Sistema de Informação de Agravos de Notificação (SINAN) 2015-2022"
data_quem_vitimas_lgbt = {
    'Gênero/Identidade': ['Feminino', 'Masculino', 'Intersexo', 'Famílias/comunidades'],
    'Proporção (%)': [50.0, 47.7, 0.7, 1.7]
}
df_quem_vitimas_lgbt = pd.DataFrame(data_quem_vitimas_lgbt)

# VIOLÊNCIA - Vítimas por Raça/Cor
data_vitimas_raca_lgbt = {
    'Raça/Cor': ['População Negra', 'População Branca', 'População Amarela', 'População Indígena'],
    'Proporção (%)': [55.4, 40.3, 0.7, 0.7]
}
df_vitimas_raca_lgbt = pd.DataFrame(data_vitimas_raca_lgbt)

# VIOLÊNCIA - Principais Agressores
data_principais_agressores_lgbt = {
    'Agressor': [
        'Vizinho', 'Pessoa desconhecida', 'Mãe', 'Companheiro ou Ex-Companheiro',
        'Irmão', 'Pai', 'Prestador de serviço', 'Tio', 'Filho'
    ],
    'Proporção (%)': [10.0, 9.6, 9.6, 6.9, 6.0, 5.6, 4.0, 3.5, 2.5]
}
df_principais_agressores_lgbt = pd.DataFrame(data_principais_agressores_lgbt)

# VIOLÊNCIA - Violência Associadas a LGBTQIfobia por Idade
data_violencia_lgbtfobia_idade = {
    'Tipo de Violência': ['Violência interpessoal', 'Violência autoprovocada', 'Violência interpessoal', 'Violência autoprovocada'],
    'Faixa Etária': ['10 a 19 Anos', '10 a 19 Anos', '20 a 29 Anos', '20 a 29 Anos'],
    'Proporção (%)': [24.6, 36.0, 35.3, 38.7]
}
df_violencia_lgbtfobia_idade = pd.DataFrame(data_violencia_lgbtfobia_idade)

# VIOLÊNCIA - Onde Ocorre a Violência (Local)
data_onde_violencia_local = {
    'Local': ['Ambiente Doméstico', 'Via Pública', 'Internet', 'Ambiente de trabalho'],
    'Proporção (%)': [55.3, 21.0, 11.8, 11.9]
}
df_onde_violencia_local = pd.DataFrame(data_onde_violencia_local)

# VIOLÊNCIA - Onde Ocorre a Violência (Tipo)
data_onde_violencia_tipo = {
    'Tipo': ['Violência autoprovocada', 'Violência interpessoal'],
    'Proporção (%)': [41.9, 58.1]
}
df_onde_violencia_tipo = pd.DataFrame(data_onde_violencia_tipo)


# --- Seções da Dashboard (Corpo Principal) ---

###############################################################################################################
st.markdown("---") # Separador inicial

# Seção Introdutória: População Total LGBTQIAP+
st.subheader("Total da População LGBTQIAP+ no Pará")

col_intro_lgbt, col_abs_lgbt, col_perc_lgbt = st.columns([3, 1, 1])

with col_intro_lgbt:
    st.markdown("###### Total da População LGBTQIAP+ no Pará")

with col_abs_lgbt:
    st.metric(
        label="Número de Pessoas",
        value=f"{total_pop_lgbt:,.0f}".replace(",", "."),
        delta=None
    )

with col_perc_lgbt:
    # A fonte é exibida nesta métrica, conforme o dado original
    st.metric(
        label="Fonte",
        value=f"{fonte_pop_lgbt}",
        delta=None
    )
st.markdown("---")


# 1. GÊNERO E SEXUALIDADE
st.subheader("1. GÊNERO E SEXUALIDADE")

# 1.1. Orientação Sexual
st.markdown("###### 1.1. Orientação Sexual") # Usar markdown para o subtítulo do gráfico
fig_orientacao_sexual = px.bar(
    df_orientacao_sexual,
    y="Orientação Sexual",
    x="Proporção (%)",
    orientation='h',
    title="Distribuição da População por Orientação Sexual",
    labels={"Proporção (%)": "Proporção (%)", "Orientação Sexual": "Orientação Sexual"},
    color="Proporção (%)",
    color_continuous_scale=px.colors.sequential.Plotly3,
    text="Proporção (%)"
)
fig_orientacao_sexual.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_orientacao_sexual.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_orientacao_sexual, use_container_width=True)
st.caption(f"Fonte: {fonte_genero_sexualidade}")
st.markdown("---")


# 2. CONTEXTO SOCIOECONÔMICO
st.subheader("2. CONTEXTO SOCIOECONÔMICO")

# 2.1. Perfil Étnico/Racial
st.markdown("###### 2.1. Perfil Étnico/Racial")
fig_perfil_etnico_racial = px.bar(
    df_perfil_etnico_racial_melted,
    x="Orientação Sexual",
    y="Proporção (%)",
    color="Raça/Cor",
    barmode="group",
    title="Perfil Étnico/Racial por Orientação Sexual",
    labels={"Proporção (%)": "Proporção (%)", "Orientação Sexual": "Orientação Sexual", "Raça/Cor": "Raça/Cor"},
    text="Proporção (%)"
)
fig_perfil_etnico_racial.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_perfil_etnico_racial.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_perfil_etnico_racial, use_container_width=True)
st.caption(f"Fonte: {fonte_genero_sexualidade}")
st.markdown("---")


# 2.2. Localidade
st.markdown("###### 2.2. Localidade")
fig_localidade_sexualidade = px.bar(
    df_localidade_sexualidade_melted,
    x="Orientação Sexual",
    y="Proporção (%)",
    color="Localidade",
    barmode="group", # ou "stack" se quiser ver a composição total
    title="Localidade por Orientação Sexual",
    labels={"Proporção (%)": "Proporção (%)", "Localidade": "Localidade"},
    text="Proporção (%)"
)
fig_localidade_sexualidade.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_localidade_sexualidade.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_localidade_sexualidade, use_container_width=True)
st.caption(f"Fonte: {fonte_genero_sexualidade}")
st.markdown("---")


# 2.3. Faixa Etária
st.markdown("###### 2.3. Faixa Etária")
fig_faixa_etaria_sexualidade = px.bar(
    df_faixa_etaria_sexualidade_melted,
    x="Orientação Sexual",
    y="Proporção (%)",
    color="Faixa Etária",
    barmode="stack", # Empilhado para mostrar a composição da idade dentro de cada orientação
    title="Faixa Etária por Orientação Sexual",
    labels={"Proporção (%)": "Proporção (%)", "Faixa Etária": "Faixa Etária"},
    text="Proporção (%)"
)
fig_faixa_etaria_sexualidade.update_traces(texttemplate='%{text:.1f}%', textposition='inside') # Texto dentro da barra para stack
fig_faixa_etaria_sexualidade.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_faixa_etaria_sexualidade, use_container_width=True)
st.caption(f"Fonte: {fonte_genero_sexualidade}")
st.markdown("---")


# 3. CONDIÇÕES DE SAÚDE
st.subheader("3. CONDIÇÕES DE SAÚDE")

# 3.1. Autoavaliação
st.markdown("###### 3.1. Autoavaliação")
fig_autoavaliacao_saude = px.bar(
    df_autoavaliacao_saude_melted,
    x="Orientação Sexual",
    y="Proporção (%)",
    color="Autoavaliação de Saúde",
    barmode="stack",
    title="Autoavaliação de Saúde por Orientação Sexual",
    labels={"Proporção (%)": "Proporção (%)", "Autoavaliação de Saúde": "Autoavaliação"},
    text="Proporção (%)"
)
fig_autoavaliacao_saude.update_traces(texttemplate='%{text:.0f}%', textposition='inside')
fig_autoavaliacao_saude.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_autoavaliacao_saude, use_container_width=True)
st.caption(f"Fonte: {fonte_condicoes_saude}")
st.markdown("---")


# 3.2. Unidades (Centros POP)
st.markdown("###### 3.2. Unidades (Centros POP)")
fig_centros_pop = px.bar(
    df_centros_pop,
    x="Indicador",
    y="Contagem",
    title="Atendimento de Centros POP à População LGBTQIAP+",
    labels={"Contagem": "Número de Unidades", "Indicador": "Tipo de Unidade/Serviço"},
    color="Contagem",
    color_continuous_scale=px.colors.sequential.Blues,
    text="Contagem"
)
fig_centros_pop.update_traces(texttemplate='%{text}', textposition='outside')
fig_centros_pop.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_centros_pop, use_container_width=True)
st.caption(f"Fonte: {fonte_condicoes_saude}")
st.markdown("---")


# 3.3. Saúde Mental
st.markdown("###### 3.3. Saúde Mental")
fig_saude_mental_lgbt = px.bar(
    df_saude_mental_lgbt,
    y="Orientação Sexual",
    x="Prevalência (%)",
    orientation='h',
    title="Prevalência de Saúde Mental por Orientação Sexual",
    labels={"Prevalência (%)": "Prevalência (%)", "Orientação Sexual": "Orientação Sexual"},
    color="Prevalência (%)",
    color_continuous_scale=px.colors.sequential.Greens,
    text="Prevalência (%)"
)
fig_saude_mental_lgbt.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_saude_mental_lgbt.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_saude_mental_lgbt, use_container_width=True)
st.caption(f"Fonte: {fonte_condicoes_saude}")
st.markdown("---")


# 3.4. Frequência de Atividades Coletivas
st.markdown("###### 3.4. Frequência de Atividades Coletivas")
fig_atividades_coletivas = px.bar(
    df_atividades_coletivas_melted,
    x="Orientação Sexual",
    y="Proporção (%)",
    color="Frequência",
    barmode="stack",
    title="Frequência de Atividades Coletivas por Orientação Sexual",
    labels={"Proporção (%)": "Proporção (%)", "Frequência": "Frequência"},
    text="Proporção (%)"
)
fig_atividades_coletivas.update_traces(texttemplate='%{text:.0f}%', textposition='inside')
fig_atividades_coletivas.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_atividades_coletivas, use_container_width=True)
st.caption(f"Fonte: {fonte_condicoes_saude}")
st.markdown("---")


# 4. NÍVEL EDUCACIONAL
st.subheader("4. NÍVEL EDUCACIONAL")

# 4.1. Perfil dos Estudantes
st.markdown("###### 4.1. Perfil dos Estudantes")
fig_perfil_estudantes = px.bar(
    df_perfil_estudantes_melted,
    x="Orientação Sexual",
    y="Proporção (%)",
    color="Nível Educacional",
    barmode="stack",
    title="Nível Educacional por Orientação Sexual",
    labels={"Proporção (%)": "Proporção (%)", "Nível Educacional": "Nível Educacional"},
    text="Proporção (%)"
)
fig_perfil_estudantes.update_traces(texttemplate='%{text:.0f}%', textposition='inside')
fig_perfil_estudantes.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_perfil_estudantes, use_container_width=True)
st.caption(f"Fonte: {fonte_educacao_lgbt}")
st.markdown("---")


# 5. SEGURANÇA
st.subheader("5. SEGURANÇA")

# 5.1. Indicadores de Segurança (consolidados como métricas)
st.markdown("###### 5.1. Indicadores de Segurança e Legislação")
col_seg_1, col_seg_2 = st.columns(2)
col_seg_3, col_seg_4 = st.columns(2) # Mais colunas para as métricas

with col_seg_1:
    st.metric(
        label=df_seguranca['Indicador'].iloc[0],
        value=f"{df_seguranca['Percentual (%)'].iloc[0]:.0f}%",
        delta=None
    )
with col_seg_2:
    st.metric(
        label=df_seguranca['Indicador'].iloc[1],
        value=f"{df_seguranca['Percentual (%)'].iloc[1]:.0f}%",
        delta=None
    )
with col_seg_3:
    st.metric(
        label=df_seguranca['Indicador'].iloc[2],
        value=f"{df_seguranca['Percentual (%)'].iloc[2]:.2f}%",
        delta=None
    )
with col_seg_4:
    st.metric(
        label=df_seguranca['Indicador'].iloc[3],
        value=f"{df_seguranca['Percentual (%)'].iloc[3]:.0f}%",
        delta=None
    )
st.caption(f"Fonte: {fonte_seguranca_lgbt}")
st.markdown("---")


# 6. RENDA FAMILIAR
st.subheader("6. RENDA FAMILIAR")

# 6.1. Renda Familiar por Salário-Mínimo e Orientação Sexual
st.markdown("###### 6.1. Renda Familiar por Faixa de Salário-Mínimo e Orientação Sexual")
fig_renda_familiar = px.bar(
    df_renda_familiar_melted,
    x="Orientação Sexual",
    y="Proporção (%)",
    color="Faixa Salário-Mínimo",
    barmode="stack",
    title="Renda Familiar por Salário-Mínimo e Orientação Sexual",
    labels={"Proporção (%)": "Proporção (%)", "Faixa Salário-Mínimo": "Faixa Salário-Mínimo"},
    text="Proporção (%)"
)
fig_renda_familiar.update_traces(texttemplate='%{text:.1f}%', textposition='inside')
fig_renda_familiar.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_renda_familiar, use_container_width=True)
st.caption(f"Fonte: {fonte_renda_familiar_lgbt}")
st.markdown("---")


# 7. SEGURIDADE SOCIAL
st.subheader("7. SEGURIDADE SOCIAL")

# 7.1. Acesso a Serviços
st.markdown("###### 7.1. Acesso a Serviços")
fig_acesso_servicos_seg_social = px.bar(
    df_acesso_servicos_seg_social,
    y="Serviço",
    x="Percentual (%)",
    orientation='h',
    title="Acesso a Serviços de Seguridade Social",
    labels={"Percentual (%)": "Percentual (%)", "Serviço": "Serviço"},
    color="Percentual (%)",
    color_continuous_scale=px.colors.sequential.Plotly3,
    text="Percentual (%)"
)
fig_acesso_servicos_seg_social.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_acesso_servicos_seg_social.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_acesso_servicos_seg_social, use_container_width=True)
st.caption(f"Fonte: {fonte_seguridade_social_lgbt}")
st.markdown("---")


# 7.2. Centros de Convivência (Absolutos)
st.markdown("###### 7.2. Centros de Convivência (Atendimento LGBTQIAP+)")
fig_centros_convivencia_lgbt = px.bar(
    df_centros_convivencia_lgbt,
    x="Indicador",
    y="Número Absoluto",
    title="Centros de Convivência: Atendimento a Pessoas LGBTQIAP+",
    labels={"Número Absoluto": "Número de Centros", "Indicador": "Indicador"},
    color="Número Absoluto",
    color_continuous_scale=px.colors.sequential.Blues,
    text="Número Absoluto"
)
fig_centros_convivencia_lgbt.update_traces(texttemplate='%{text}', textposition='outside')
fig_centros_convivencia_lgbt.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_centros_convivencia_lgbt, use_container_width=True)
st.caption(f"Fonte: {fonte_seguridade_social_lgbt}")
st.markdown("---")

# --- NOVAS ADIÇÕES (CRAS, PAEFI, CREAS) ---
# 7.3. Atendimentos de CRAS
st.markdown("###### 7.3. Atendimentos de CRAS a Pessoas LGBTQIAP+")
fig_cras_atendimentos_lgbt = px.bar(
    df_cras_atendimentos_lgbt,
    y="Tipo de Atendimento",
    x="Número Absoluto",
    orientation='h',
    title="Número de CRAS que realizaram atendimentos a pessoas LGBTQIAP+ por tipo de serviço",
    labels={"Número Absoluto": "Número de CRAS", "Tipo de Atendimento": "Tipo de Atendimento"},
    color="Número Absoluto",
    color_continuous_scale=px.colors.sequential.Viridis,
    text="Número Absoluto"
)
fig_cras_atendimentos_lgbt.update_traces(texttemplate='%{text}', textposition='outside')
fig_cras_atendimentos_lgbt.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_cras_atendimentos_lgbt, use_container_width=True)
st.caption(f"Fonte: {fonte_seguridade_social_lgbt}")
st.markdown("---")

# 7.4. Ingressos no PAEFI (2017-2022)
st.markdown("###### 7.4. Ingressos no PAEFI (2017-2022)")
fig_paefi_ingressos_lgbt = px.line(
    df_paefi_ingressos_lgbt,
    x="Ano",
    y="Número de Pessoas",
    title="Número de pessoas que ingressaram no PAEFI (Vítimas de discriminação por orientação sexual)",
    labels={"Número de Pessoas": "Número de Pessoas", "Ano": "Ano"},
    markers=True, # Adiciona marcadores nos pontos
    text="Número de Pessoas" # Mostra o valor em cada ponto
)
fig_paefi_ingressos_lgbt.update_traces(texttemplate='%{text}', textposition='top center')
fig_paefi_ingressos_lgbt.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_paefi_ingressos_lgbt, use_container_width=True)
st.caption(f"Fonte: {fonte_seguridade_social_lgbt}")
st.markdown("---")

# 7.5. Atendimentos de CREAS por Grupo Etário
st.markdown("###### 7.5. Atendimentos de CREAS por Grupo Etário")
fig_creas_atendimentos_grupo_etario_lgbt = px.bar(
    df_creas_atendimentos_grupo_etario_lgbt,
    y="Grupo Etário / Situação",
    x="Número Absoluto",
    orientation='h',
    title="Número de CREAS que realizaram atendimentos a vítimas de discriminação por Orientação Sexual e/ou Identidade de Gênero por grupo etário",
    labels={"Número Absoluto": "Número de CREAS", "Grupo Etário / Situação": "Grupo Etário / Situação"},
    color="Número Absoluto",
    color_continuous_scale=px.colors.sequential.Plasma,
    text="Número Absoluto"
)
fig_creas_atendimentos_grupo_etario_lgbt.update_traces(texttemplate='%{text}', textposition='outside')
fig_creas_atendimentos_grupo_etario_lgbt.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_creas_atendimentos_grupo_etario_lgbt, use_container_width=True)
st.caption(f"Fonte: {fonte_seguridade_social_lgbt}")
st.markdown("---")


# 8. VIOLÊNCIA
st.subheader("8. VIOLÊNCIA")

# 8.1. Quem são as vítimas (Gênero) e 8.2. Vítimas por Raça/Cor
col_vitimas_genero, col_vitimas_raca = st.columns(2)

with col_vitimas_genero:
    st.markdown("###### 8.1. Quem são as vítimas (Gênero)")
    fig_quem_vitimas_lgbt = px.pie(
        df_quem_vitimas_lgbt,
        values='Proporção (%)',
        names='Gênero/Identidade',
        title='Vítimas de Violência por Gênero/Identidade',
        hole=0.3
    )
    fig_quem_vitimas_lgbt.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_quem_vitimas_lgbt, use_container_width=True)

with col_vitimas_raca:
    st.markdown("###### 8.2. Vítimas por Raça/Cor")
    fig_vitimas_raca_lgbt = px.bar(
        df_vitimas_raca_lgbt,
        x="Raça/Cor",
        y="Proporção (%)",
        title="Vítimas de Violência por Raça/Cor",
        labels={"Proporção (%)": "Proporção (%)", "Raça/Cor": "Raça/Cor"},
        color="Proporção (%)",
        color_continuous_scale=px.colors.sequential.Purples,
        text="Proporção (%)"
    )
    fig_vitimas_raca_lgbt.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_vitimas_raca_lgbt.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_vitimas_raca_lgbt, use_container_width=True)
st.caption(f"Fonte: {fonte_violencia_lgbt}") # Uma fonte para ambos os gráficos acima
st.markdown("---")


# 8.3. Principais Agressores
st.markdown("###### 8.3. Principais Agressores")
fig_principais_agressores_lgbt = px.bar(
    df_principais_agressores_lgbt,
    y="Agressor",
    x="Proporção (%)",
    orientation='h',
    title="Principais Agressores (LGBTQIAP+)",
    labels={"Proporção (%)": "Proporção (%)", "Agressor": "Agressor"},
    color="Proporção (%)",
    color_continuous_scale=px.colors.sequential.Reds,
    text="Proporção (%)"
)
fig_principais_agressores_lgbt.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_principais_agressores_lgbt.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_principais_agressores_lgbt, use_container_width=True)
st.caption(f"Fonte: {fonte_violencia_lgbt}")
st.markdown("---")


# 8.4. Violência Associada a LGBTQIfobia por Idade
st.markdown("###### 8.4. Violência Associada a LGBTQIfobia por Idade")
fig_violencia_lgbtfobia_idade = px.bar(
    df_violencia_lgbtfobia_idade,
    x="Faixa Etária",
    y="Proporção (%)",
    color="Tipo de Violência",
    barmode="group",
    title="Violência Associada a LGBTQIfobia por Faixa Etária",
    labels={"Proporção (%)": "Proporção (%)", "Tipo de Violência": "Tipo de Violência"},
    text="Proporção (%)"
)
fig_violencia_lgbtfobia_idade.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_violencia_lgbtfobia_idade.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_violencia_lgbtfobia_idade, use_container_width=True)
st.caption(f"Fonte: {fonte_violencia_lgbt}")
st.markdown("---")


# 8.5. Onde Ocorre a Violência
col_local_violencia_lgbt, col_tipo_violencia_lgbt = st.columns(2)

with col_local_violencia_lgbt:
    st.markdown("###### 8.5.1. Local de Ocorrência")
    fig_onde_violencia_local = px.pie(
        df_onde_violencia_local,
        values='Proporção (%)',
        names='Local',
        title='Local de Ocorrência da Violência',
        hole=0.3
    )
    fig_onde_violencia_local.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_onde_violencia_local, use_container_width=True)

with col_tipo_violencia_lgbt:
    st.markdown("###### 8.5.2. Tipo de Violência (Autoprovocada vs Interpessoal)")
    fig_onde_violencia_tipo = px.pie(
        df_onde_violencia_tipo,
        values='Proporção (%)',
        names='Tipo',
        title='Tipo de Violência',
        hole=0.3
    )
    fig_onde_violencia_tipo.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_onde_violencia_tipo, use_container_width=True)
st.caption(f"Fonte: {fonte_violencia_lgbt}")
st.markdown("---") # Fim da seção LGBTQIAP+