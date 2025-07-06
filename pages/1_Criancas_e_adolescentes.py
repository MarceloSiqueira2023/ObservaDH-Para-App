import pandas as pd
import plotly.express as px
import streamlit as st

# --- Configuração da Página Streamlit ---
st.set_page_config(page_title="Crianças e Adolescentes", page_icon=":children_crossing:", layout="wide")

# --- Título Geral da Dashboard ---
st.title("Crianças e Adolescentes")

# --- 1. Definição Global de Variáveis e DataFrames ---

# População
populacao_total = 2431092
percentual_para = 29.94
fonte_populacao = "IBGE 2022"

# Saúde - Taxa de Mortalidade Juvenil
data_mortalidade_juvenil = {
    'Faixa Etária': ['0 a 5 anos', 'até 19 anos', '15 a 29 anos'],
    'Taxa de Mortalidade (%)': [17.79, 26.3, 50.6]
}
df_mortalidade_juvenil = pd.DataFrame(data_mortalidade_juvenil)
fonte_mortalidade = "FAPESPA 2024 / IPEA 2023"

# Saúde - Acesso a Serviços de Saúde Sexual e Reprodutiva
data_acesso_saude = {
    'Indicador': [
        'Tiveram relação sexual (geral)',
        'Tiveram relação sexual (Meninos)',
        'Tiveram relação sexual (Meninas)',
        'Receberam orientações sobre como adquirir preservativos gratuitos',
        'Obtiveram preservativos em serviços de saúde'
    ],
    'Valor (%)': [30.5, 43.7, 18.7, 67.6, 22.1]
}
df_acesso_saude = pd.DataFrame(data_acesso_saude)
fonte_acesso_saude = "IBGE 2019"

# Saúde - Gravidez na Adolescência
faixa_etaria_gravidez = "10 a 19 anos"
valor_percentual_gravidez = 20.38
fonte_gravidez = "SESPA 2022"

# Saúde - Prevalência de Doenças Crônicas Não Transmissíveis (DCNT)
faixa_etaria_dcnt = "13 a 17 anos"
valor_percentual_dcnt = 81.3
fonte_dcnt = "IBGE 2019" # Fonte comum para DCNT e fatores de risco

# Saúde - Fatores de riscos ao desenvolvimento de DCNT
data_fatores_risco = {
    'Fator de Risco': [
        'Falta de atividade física',
        'Ingestão inadequada de frutas e vegetais',
        'Sedentarismo (tempo excessivo em frente a telas)',
        'Consumo regular de doces',
        'Consumo de bebidas alcoólicas',
        'Consumo regular de refrigerantes',
        'Tabagismo'
    ],
    'Prevalência (%)': [71.5, 58.4, 54.1, 32.9, 28.1, 17.2, 6.8]
}
df_fatores_risco = pd.DataFrame(data_fatores_risco)

# Saúde - Índices de Saúde Mental
data_saude_mental = {
    'Faixa Etária': ['5 a 9 anos', '10 a 14 anos', '15 a 19 anos'],
    'Índice de Saúde Mental (%)': [6.8, 12.0, 30.0]
}
df_saude_mental = pd.DataFrame(data_saude_mental)
fonte_saude_mental = "(Informação faltante no CSV para esta seção, checar documento original)" # Manter a nota de fonte original

# Educação
fonte_educacao = "IBGE 2022 / INEP 2022"

# Educação - Taxa de Escolarização
data_escolarizacao = {
    'Faixa Etária': ['4 a 5 anos', '6 a 14 anos', '15 a 17 anos'],
    'Taxa de Escolarização (%)': [86.2, 96.7, 84.3]
}
df_escolarizacao = pd.DataFrame(data_escolarizacao)

# Educação - Abandono Escolar
data_abandono = {
    'Nível de Ensino': ['Ensino Fundamental (anos finais)', 'Ensino Médio'],
    'Taxa de Abandono (%)': [45.7, 45.9]
}
df_abandono = pd.DataFrame(data_abandono)

# Educação - Conclusão do Ensino Médio
data_conclusao = {
    'Indicador': [
        'Conclusão do Ensino Médio no tempo adequado',
        'Taxa de Distorção de Idade - Ensino Médio'
    ],
    'Percentual (%)': [58.4, 45.7]
}
df_conclusao = pd.DataFrame(data_conclusao)

# Educação - Acesso à Educação Profissionalizante
data_profissionalizante = {
    'Tipo de Educação Profissional': [
        'Educação Profissional Técnica',
        'Na Rede Federal de Educação Profissional',
        'Matrículas no Sistema (educação profissional)'
    ],
    'Número de Matrículas/Acessos': [45, 30, 25]
}
df_profissionalizante = pd.DataFrame(data_profissionalizante)

# Inclusão Digital
fonte_inclusao_digital = "FAPESPA 2023 / INEP 2022"

# Inclusão Digital - Acesso à Internet
valor_acesso_internet = 82.8

# Inclusão Digital - Posse de Dispositivos Digitais
data_posse_dispositivos = {
    'Faixa Etária': ['10 a 13 anos', '14 a 17 anos'],
    'Posse de Dispositivos Digitais (%)': [54.8, 84.7]
}
df_posse_dispositivos = pd.DataFrame(data_posse_dispositivos)

# Inclusão Digital - Participação em Programas de Inclusão Digital
data_participacao = {
    'Categoria': [
        '9 a 17 anos - Escola',
        'classes A e B',
        'classes D e E'
    ],
    'Participação (%)': [44.0, 71.0, 15.0]
}
df_participacao = pd.DataFrame(data_participacao)

# Trabalho
fonte_trabalho = "IBGE 2022"

# Trabalho - Taxa de Desemprego Juvenil
data_desemprego = {
    'Faixa Etária': ['14-17 anos', '18-24 anos', '14-29 anos'],
    'Taxa de Desemprego (%)': [41.2, 28.5, 23.7]
}
df_desemprego = pd.DataFrame(data_desemprego)

# Trabalho - Taxa de Informalidade no Trabalho Juvenil
data_informalidade = {
    'Faixa Etária': ['14-17 anos', '18-24 anos', '14-29 anos'],
    'Taxa de Informalidade (%)': [89.3, 71.5, 68.2]
}
df_informalidade = pd.DataFrame(data_informalidade)

# Trabalho - Taxa de Participação em Programas de Aprendizagem
valor_participacao_aprendizagem = 11.0

# Trabalho - Taxa do Nível de Remuneração dos Jovens Trabalhadores
data_remuneracao = {
    'Tipo de Rendimento': [
        'Rendimento médio mensal', 'Rendimento médio mensal',
        'Rendimento mediano mensal', 'Rendimento mediano mensal'
    ],
    'Faixa Etária': [
        '14-17 anos', '18-24 anos',
        '14-17 anos', '18-24 anos'
    ],
    'Valor (R$)': [
        65.00,
        1212.00,
        512.00,
        1045.00
    ]
}
df_remuneracao = pd.DataFrame(data_remuneracao)

# Violência Não Letal
fonte_violencia_nao_letal = "Fórum Brasileiro de Segurança Pública (FBSP) 2022"

# Violência Não Letal - Geral - Por Sexo
data_sexo_vnl = {
    'Gênero': ['Feminino', 'Masculino'],
    'Proporção (%)': [88.7, 11.3]
}
df_sexo_vnl = pd.DataFrame(data_sexo_vnl)

# Violência Não Letal - Geral - Raça/Cor
data_raca_vnl = {
    'Raça/Cor': ['Negra', 'Branca', 'Indígena', 'Amarela'],
    'Proporção (%)': [56.8, 42.3, 0.5, 0.4]
}
df_raca_vnl = pd.DataFrame(data_raca_vnl)

# Violência Não Letal - Geral - Local/Território
data_local_vnl = {
    'Local': ['Residência da Vítima', 'Vias Públicas'],
    'Proporção (%)': [68.3, 9.4]
}
df_local_vnl = pd.DataFrame(data_local_vnl)

# Violência Não Letal - Tipos Específicos
data_tipos_violencia_vnl = {
    'Tipo de Violência Geral': [
        'Física', 'Física',
        'Psicológica',
        'Sexual', 'Sexual',
        'Por Negligência', 'Por Negligência'
    ],
    'Subtipo de Violência': [
        'Maus-Tratos',
        'Lesão Corporal em Violência Doméstica',
        'Pornografia Infanto-Juvenil',
        'Estupro',
        'Exploração Sexual',
        'Abandono de Incapaz',
        'Abandono Material'
    ],
    'Prevalência (%)': [
        13.38, 3.46,
        7.03,
        15.3, 16.36,
        14.04, 1.85
    ]
}
df_tipos_violencia_vnl = pd.DataFrame(data_tipos_violencia_vnl)

# Letalidade Policial
fonte_letalidade_policial = "FBSP 2022"

# Letalidade Policial - Por Sexo
data_sexo_letalidade = {
    'Gênero': ['Masculino', 'Feminino'],
    'Proporção (%)': [98.4, 1.6]
}
df_sexo_letalidade = pd.DataFrame(data_sexo_letalidade)

# Letalidade Policial - Faixa Etária
data_faixa_etaria_letalidade = {
    'Faixa Etária': ['0 a 11 anos', '12 a 17 anos', '18 a 24 anos'],
    'Proporção (%)': [0.1, 7.5, 45.4]
}
df_faixa_etaria_letalidade = pd.DataFrame(data_faixa_etaria_letalidade)

# Letalidade Policial - Raça/Cor
data_raca_letalidade = {
    'Raça/Cor': ['Negro', 'Branco', 'Amarelo'],
    'Proporção (%)': [83.1, 16.6, 0.2]
}
df_raca_letalidade = pd.DataFrame(data_raca_letalidade)

# Letalidade Policial - Local/Território do Óbito
data_local_obito_letalidade = {
    'Local': ['Via pública', 'Residência', 'Outros Locais'],
    'Proporção (%)': [68.1, 15.8, 16.1]
}
df_local_obito_letalidade = pd.DataFrame(data_local_obito_letalidade)

# Letalidade Policial - Instrumento/Arma Utilizados (valor único)
valor_arma_letalidade = 76.5

# Violência Sexual
fonte_violencia_sexual = "ObservaDH 2022 / FBSP 2022"

# Violência Sexual - Por Idade (Vítimas Femininas)
data_idade_vsex = {
    'Faixa Etária': ['10 a 13 anos: feminino', '05 a 09 anos: feminino', '0 a 04 anos: feminino'],
    'Proporção (%)': [57.97, 26.5, 15.53]
}
df_idade_vsex = pd.DataFrame(data_idade_vsex)

# Violência Sexual - Por Sexo
data_sexo_vsex = {
    'Gênero': ['Feminino', 'Masculino'],
    'Proporção (%)': [85.98, 14.02]
}
df_sexo_vsex = pd.DataFrame(data_sexo_vsex)

# Violência Sexual - Por Local/Território
data_local_vsex = {
    'Local': ['Residência da Vítima', 'Vias Públicas'],
    'Proporção (%)': [68.3, 9.4]
}
df_local_vsex = pd.DataFrame(data_local_vsex)

# Violência Sexual - Número de Vítimas por Raça/Cor
data_vitimas_raca_vsex = {
    'Raça/Cor': ['Negro', 'Branco', 'Indígena', 'Amarelo'],
    'Número de Vítimas': [12452, 9516, 101, 69]
}
df_vitimas_raca_vsex = pd.DataFrame(data_vitimas_raca_vsex)

# Violência Sexual - Estupro
data_estupro_vsex = {
    'Gênero (Até 13 anos)': ['Meninas', 'Meninos'],
    'Proporção (%)': [85.98, 14.02]
}
df_estupro_vsex = pd.DataFrame(data_estupro_vsex)

# Violência Sexual - Exploração Sexual (valor único)
valor_exploracao_sexual = 16.4

# Violência Sexual - Pedofilia
data_pedofilia_vsex = {
    'Relação com Agressor': [
        'Pai /Padrasto', 'Conhecido', 'Tio', 'Avô/Avó', 'Vizinho',
        'Outro familiar', 'Desconhecido', 'Primo', 'Irmão/irmã'
    ],
    'Proporção (%)': [44.4, 18.0, 7.7, 7.4, 6.4, 4.8, 4.1, 3.8, 3.4]
}
df_pedofilia_vsex = pd.DataFrame(data_pedofilia_vsex)

# Violência Letal: Homicídios
fonte_homicidios = "ObservaDH 2022"

# Violência Letal: Homicídios - Por Sexo
data_homicidios_sexo = {
    'Gênero': ['Masculino', 'Feminino', 'Masculino', 'Feminino'],
    'Faixa Etária': ['0 a 11 anos', '0 a 11 anos', '12 a 17 anos', '12 a 17 anos'],
    'Proporção (%)': [37.60, 81.71, 62.40, 18.29]
}
df_homicidios_sexo = pd.DataFrame(data_homicidios_sexo)

# Violência Letal: Homicídios - Raça/Cor
data_homicidios_raca = {
    'Raça/Cor': ['Negros', 'Brancos', 'Negros', 'Brancos'],
    'Faixa Etária': ['0 a 11 anos', '0 a 11 anos', '12 a 17 anos', '12 a 17 anos'],
    'Proporção (%)': [44.08, 69.10, 55.92, 30.90]
}
df_homicidios_raca = pd.DataFrame(data_homicidios_raca)

# Violência Letal: Homicídios - Local/Território do Óbito
data_homicidios_local = {
    'Local': ['Via pública', 'Residência', 'Outros', 'Via pública', 'Residência', 'Outros'],
    'Faixa Etária': ['0 a 11 anos', '0 a 11 anos', '0 a 11 anos', '12 a 17 anos', '12 a 17 anos', '12 a 17 anos'],
    'Proporção (%)': [15.38, 65.38, 19.23, 59.41, 15.84, 24.75]
}
df_homicidios_local = pd.DataFrame(data_homicidios_local)

# Violência Letal: Homicídios - Instrumento ou Arma Utilizados
data_homicidios_arma = {
    'Arma': ['Agressão', 'Arma branca', 'Arma de fogo', 'Arma de fogo', 'Arma branca'],
    'Faixa Etária': ['0 a 11 anos', '0 a 11 anos', '0 a 11 anos', '12 a 17 anos', '12 a 17 anos'],
    'Proporção (%)': [21.15, 23.08, 55.77, 90.76, 8.87]
}
df_homicidios_arma = pd.DataFrame(data_homicidios_arma)

# Violência Letal: Homicídios - Causa
data_homicidios_causa = {
    'Causa': [
        'Homicídio doloso', 'Feminicídio', 'Lesão corporal seguida de morte',
        'Morte decorrente de lesão corporal', 'Latrocínio',
        'Homicídio doloso', 'Morte decorrente de intervenção policial',
        'Feminicídio', 'Latrocínio', 'Lesão corporal seguida de morte'
    ],
    'Faixa Etária': [
        '0 a 11 anos', '0 a 11 anos', '0 a 11 anos',
        '0 a 11 anos', '0 a 11 anos',
        '12 a 17 anos', '12 a 17 anos',
        '12 a 17 anos', '12 a 17 anos', '12 a 17 anos'
    ],
    'Proporção (%)': [
        84.8, 11.4, 1.9,
        1.4, 0.5,
        80.4, 15.7,
        2.2, 0.8, 0.8
    ]
}
df_homicidios_causa = pd.DataFrame(data_homicidios_causa)


# --- Seções da Dashboard (Corpo Principal) ---

###############################################################################################################
st.markdown("---") # Separador para a próxima seção

# População Geral
col_title, col_absolutos, col_percentual = st.columns([3, 1, 1])

with col_title:
    st.subheader("Total da População de Crianças e Adolescentes no Pará")

with col_absolutos:
    st.metric(
        label="População Total",
        value=f"{populacao_total:,.0f}".replace(",", "."),
        delta=None
    )

with col_percentual:
    st.metric(
        label="Percentual no Pará",
        value=f"{percentual_para:.2f}%",
        delta=None
    )
st.caption(f"Fonte: {fonte_populacao}")

###############################################################################################################
st.markdown("---") # Separador para a próxima seção

st.header("1. Saúde")

# 1.1. Taxa de Mortalidade Juvenil e 1.2. Acesso a Serviços de Saúde Sexual e Reprodutiva
col_tx_mortalidade, col_acesso_saude = st.columns(2)

with col_tx_mortalidade:
    st.subheader("1.1. Taxa de Mortalidade Juvenil")
    fig_mortalidade = px.bar(
        df_mortalidade_juvenil,
        x="Faixa Etária",
        y="Taxa de Mortalidade (%)",
        labels={
            "Taxa de Mortalidade (%)": "Taxa (%)",
            "Faixa Etária": "Faixa Etária"
        },
        color="Taxa de Mortalidade (%)",
        color_continuous_scale=px.colors.sequential.Plasma,
        text="Taxa de Mortalidade (%)"
    )
    fig_mortalidade.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig_mortalidade.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_mortalidade, use_container_width=True)
    st.caption(f"Fonte: {fonte_mortalidade}")

with col_acesso_saude:
    st.subheader("1.2. Acesso a Serviços de Saúde Sexual e Reprodutiva")

    col_metricas_1, col_metricas_2 = st.columns(2)

    with col_metricas_1:
        st.metric(
            label="Tiveram Relação Sexual",
            value=f"{df_acesso_saude[df_acesso_saude['Indicador'] == 'Tiveram relação sexual (geral)']['Valor (%)'].iloc[0]:.1f}%"
        )
        df_sexo_relacao = df_acesso_saude[
            (df_acesso_saude['Indicador'] == 'Tiveram relação sexual (Meninos)') |
            (df_acesso_saude['Indicador'] == 'Tiveram relação sexual (Meninas)')
        ].copy()
        df_sexo_relacao['Gênero'] = df_sexo_relacao['Indicador'].apply(lambda x: x.split('(')[1].replace(')', ''))
        
        fig_sexo_relacao = px.bar(
            df_sexo_relacao,
            x="Gênero",
            y="Valor (%)",
            title="Relação Sexual por Gênero",
            labels={
                "Valor (%)": "Percentual (%)",
                "Gênero": "Gênero"
            },
            color="Gênero",
            color_discrete_map={'Meninos': 'blue', 'Meninas': 'pink'},
            text="Valor (%)"
        )
        fig_sexo_relacao.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig_sexo_relacao.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig_sexo_relacao, use_container_width=True)
        
    with col_metricas_2:
        st.metric(
            label="Receberam Orientações sobre Preservativos Gratuitos",
            value=f"{df_acesso_saude[df_acesso_saude['Indicador'] == 'Receberam orientações sobre como adquirir preservativos gratuitos']['Valor (%)'].iloc[0]:.1f}%"
        )
        st.metric(
            label="Obtiveram Preservativos em Serviços de Saúde",
            value=f"{df_acesso_saude[df_acesso_saude['Indicador'] == 'Obtiveram preservativos em serviços de saúde']['Valor (%)'].iloc[0]:.1f}%"
        )
    st.caption(f"Fonte: {fonte_acesso_saude}")

###############################################################################################################
st.markdown("---") # Separador para a próxima seção

# 1.3. Gravidez na Adolescência e 1.4. Prevalência de Doenças Crônicas Não Transmissíveis (DCNT)
col_gravidez, col_dcnt = st.columns([2, 1]) 

with col_gravidez:
    st.subheader("1.3. Gravidez na Adolescência")
    st.metric(
        label=f"Taxa de Gravidez na Adolescência ({faixa_etaria_gravidez})",
        value=f"{valor_percentual_gravidez:.2f}%",
        delta=None
    )
    st.caption(f"Fonte: {fonte_gravidez}")

with col_dcnt:
    st.subheader("1.4. Prevalência de Doenças Crônicas Não Transmissíveis (DCNT)")
    st.metric(
        label=f"Prevalência de DCNT ({faixa_etaria_dcnt})",
        value=f"{valor_percentual_dcnt:.1f}%",
        delta=None
    )
    st.caption(f"Fonte: {fonte_dcnt}")

###############################################################################################################
st.markdown("---") # Separador para a próxima seção

# 1.5. Fatores de riscos ao desenvolvimento de DCNT e 1.6. Índices de Saúde Mental
col_fatores_risco, col_saude_mental = st.columns([2, 1])

with col_fatores_risco:
    st.subheader("1.5. Fatores de riscos ao desenvolvimento de DCNT") # MOVIDO PARA AQUI
    fig_fatores = px.bar(
        df_fatores_risco,
        y="Fator de Risco",
        x="Prevalência (%)",
        orientation='h',
        labels={
            "Prevalência (%)": "Prevalência (%)",
            "Fator de Risco": "Fator de Risco"
        },
        color="Prevalência (%)",
        color_continuous_scale=px.colors.sequential.Sunset,
        text="Prevalência (%)"
    )
    fig_fatores.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_fatores.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_fatores, use_container_width=True)
    st.caption(f"Fonte: {fonte_dcnt}")

with col_saude_mental:
    st.subheader("1.6. Índices de Saúde Mental") # MOVIDO PARA AQUI
    fig_saude_mental = px.bar(
        df_saude_mental,
        x="Faixa Etária",
        y="Índice de Saúde Mental (%)",
        labels={
            "Índice de Saúde Mental (%)": "Índice (%)",
            "Faixa Etária": "Faixa Etária"
        },
        color="Índice de Saúde Mental (%)",
        color_continuous_scale=px.colors.sequential.Viridis,
        text="Índice de Saúde Mental (%)"
    )
    fig_saude_mental.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_saude_mental.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_saude_mental, use_container_width=True)
    st.caption(f"Fonte: {fonte_saude_mental}")

###############################################################################################################
st.markdown("---") # Separador para a próxima seção

st.header("2. Educação")

# 2.1. Taxa de Escolarização e 2.2. Abandono Escolar
col_escolarizacao, col_abandono = st.columns([1, 1])

with col_escolarizacao:
    st.subheader("2.1. Taxa de Escolarização")
    fig_escolarizacao = px.bar(
        df_escolarizacao,
        x="Faixa Etária",
        y="Taxa de Escolarização (%)",
        labels={"Taxa de Escolarização (%)": "Taxa (%)"},
        color="Taxa de Escolarização (%)",
        color_continuous_scale=px.colors.sequential.Plotly3,
        text="Taxa de Escolarização (%)"
    )
    fig_escolarizacao.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_escolarizacao.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_escolarizacao, use_container_width=True)
    st.caption(f"Fonte: {fonte_educacao}")

with col_abandono:
    st.subheader("2.2. Abandono Escolar")
    fig_abandono = px.bar(
        df_abandono,
        x="Nível de Ensino",
        y="Taxa de Abandono (%)",
        labels={"Taxa de Abandono (%)": "Taxa (%)"},
        color="Taxa de Abandono (%)",
        color_continuous_scale=px.colors.sequential.Reds,
        text="Taxa de Abandono (%)"
    )
    fig_abandono.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_abandono.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_abandono, use_container_width=True)
    st.caption(f"Fonte: {fonte_educacao}")

################################################################################################################
st.markdown("---") # Separador para a próxima seção

# 2.3. Conclusão do Ensino Médio e 2.4. Acesso à Educação Profissionalizante
col_conclusao, col_profissionalizante = st.columns([1, 1])

with col_conclusao:
    st.subheader("2.3. Conclusão do Ensino Médio")
    fig_conclusao = px.bar(
        df_conclusao,
        x="Indicador",
        y="Percentual (%)",
        title="Conclusão do Ensino Médio e Distorção de Idade",
        labels={"Percentual (%)": "Percentual (%)"},
        color="Percentual (%)",
        color_continuous_scale=px.colors.sequential.Blues,
        text="Percentual (%)"
    )
    fig_conclusao.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_conclusao.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_conclusao, use_container_width=True)
    st.caption(f"Fonte: {fonte_educacao}")

with col_profissionalizante:
    st.subheader("2.4. Acesso à Educação Profissionalizante")
    fig_profissionalizante = px.bar(
        df_profissionalizante,
        y="Tipo de Educação Profissional",
        x="Número de Matrículas/Acessos",
        orientation='h',
        title="Acesso e Matrículas na Educação Profissionalizante",
        labels={"Número de Matrículas/Acessos": "Número de Matrículas/Acessos"},
        color="Número de Matrículas/Acessos",
        color_continuous_scale=px.colors.sequential.Greens,
        text="Número de Matrículas/Acessos"
    )
    fig_profissionalizante.update_traces(texttemplate='%{text}', textposition='outside')
    fig_profissionalizante.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_profissionalizante, use_container_width=True)
    st.caption(f"Fonte: {fonte_educacao}")

#################################################################################################################
st.markdown("---") # Separador para a próxima seção

st.header("3. Inclusão Digital")   

# 3.1. Acesso à Internet
st.subheader("3.1. Acesso à Internet")
st.metric(
    label="Percentual da População com Acesso à Internet",
    value=f"{valor_acesso_internet:.1f}%",
    delta=None
)
st.caption(f"Fonte: {fonte_inclusao_digital}")
st.markdown("---")

# 3.2. Posse de Dispositivos Digitais e 3.3. Participação em Programas de Inclusão Digital
col_posse_dispositivos, col_participacao = st.columns([1, 1])

with col_posse_dispositivos:
    st.subheader("3.2. Posse de Dispositivos Digitais")
    fig_posse_dispositivos = px.bar(
        df_posse_dispositivos,
        x="Faixa Etária",
        y="Posse de Dispositivos Digitais (%)",
        labels={"Posse de Dispositivos Digitais (%)": "Percentual (%)"},
        color="Posse de Dispositivos Digitais (%)",
        color_continuous_scale=px.colors.sequential.Teal,
        text="Posse de Dispositivos Digitais (%)"
    )
    fig_posse_dispositivos.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_posse_dispositivos.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_posse_dispositivos, use_container_width=True)
    st.caption(f"Fonte: {fonte_inclusao_digital}")

with col_participacao:
    st.subheader("3.3. Participação em Programas de Inclusão Digital")
    fig_participacao = px.bar(
        df_participacao,
        y="Categoria",
        x="Participação (%)",
        orientation='h',
        labels={"Participação (%)": "Percentual (%)"},
        color="Participação (%)",
        color_continuous_scale=px.colors.sequential.Plotly3,
        text="Participação (%)"
    )
    fig_participacao.update_traces(texttemplate='%{text:.0f}%', textposition='outside')
    fig_participacao.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_participacao, use_container_width=True)
    st.caption(f"Fonte: {fonte_inclusao_digital}")

#################################################################################################################
st.markdown("---") # Separador para a próxima seção

st.header("4. TRABALHO")

# 4.1. Taxa de Desemprego Juvenil e 4.2. Taxa de Informalidade no Trabalho Juvenil
col_desemprego, col_informalidade = st.columns([1, 1])

with col_desemprego:
    st.subheader("4.1. Taxa de Desemprego Juvenil")
    fig_desemprego = px.bar(
        df_desemprego,
        x="Faixa Etária",
        y="Taxa de Desemprego (%)",
        labels={"Taxa de Desemprego (%)": "Taxa (%)"},
        color="Taxa de Desemprego (%)",
        color_continuous_scale=px.colors.sequential.Oranges,
        text="Taxa de Desemprego (%)"
    )
    fig_desemprego.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_desemprego.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_desemprego, use_container_width=True)
    st.caption(f"Fonte: {fonte_trabalho}")

with col_informalidade:
    st.subheader("4.2. Taxa de Informalidade no Trabalho Juvenil")
    fig_informalidade = px.bar(
        df_informalidade,
        x="Faixa Etária",
        y="Taxa de Informalidade (%)",
        labels={"Taxa de Informalidade (%)": "Taxa (%)"},
        color="Taxa de Informalidade (%)",
        color_continuous_scale=px.colors.sequential.Greys,
        text="Taxa de Informalidade (%)"
    )
    fig_informalidade.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_informalidade.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_informalidade, use_container_width=True)
    st.caption(f"Fonte: {fonte_trabalho}")

st.markdown("---") # Separador entre as seções em coluna e a próxima individual

# 4.3. Taxa de Participação em Programas de Aprendizagem
st.subheader("4.3. Taxa de Participação em Programas de Aprendizagem")
st.metric(
    label="Taxa de Participação em Programas de Aprendizagem (15-24 anos)",
    value=f"{valor_participacao_aprendizagem:.0f}%",
    delta=None
)
st.caption(f"Fonte: {fonte_trabalho}")

# 4.4. Taxa do Nível de Remuneração dos Jovens Trabalhadores
st.subheader("4.4. Taxa do Nível de Remuneração dos Jovens Trabalhadores")
st.markdown(
    """
    Este gráfico ilustra o **rendimento médio** (total dividido pelo número) e **rendimento mediano** (valor central)
    mensal dos jovens trabalhadores por faixa etária. O rendimento mediano é geralmente uma melhor indicação da renda típica, pois é menos distorcido por valores extremos.
    """
)
fig_remuneracao = px.bar(
    df_remuneracao,
    x="Faixa Etária",
    y="Valor (R$)",
    color="Tipo de Rendimento",
    barmode="group",
    labels={
        "Valor (R$)": "Rendimento (R$)",
        "Faixa Etária": "Faixa Etária"
    },
    color_discrete_map={
        'Rendimento médio mensal': px.colors.qualitative.Plotly[0],
        'Rendimento mediano mensal': px.colors.qualitative.Plotly[1]
    },
    text="Valor (R$)"
)
fig_remuneracao.update_traces(texttemplate='R$ %{text:,.2f}', textposition='outside')
fig_remuneracao.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_remuneracao, use_container_width=True)
st.caption(f"Fonte: {fonte_trabalho}")

###################################################################################################################
st.markdown("---") # Separador para a próxima seção principal

st.header("5. Violência não-letal")

# 5.1. Visão Geral da Violência Não Letal (organizada em 3 colunas)
col1_geral, col2_geral, col3_geral = st.columns(3)

with col1_geral:
    st.subheader("5.1. Por Sexo")
    fig_sexo = px.pie(
        df_sexo_vnl,
        values='Proporção (%)',
        names='Gênero',
        title='Violência Não Letal por Sexo',
        hole=0.3
    )
    fig_sexo.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_sexo, use_container_width=True)

with col2_geral:
    st.subheader("5.2. Por Raça/Cor")
    fig_raca = px.pie(
        df_raca_vnl,
        values='Proporção (%)',
        names='Raça/Cor',
        title='Violência Não Letal por Raça/Cor',
        hole=0.3
    )
    fig_raca.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_raca, use_container_width=True)

with col3_geral:
    st.subheader("5.3. Por Local/Território")
    fig_local = px.bar(
        df_local_vnl,
        x="Local",
        y="Proporção (%)",
        title="Violência Não Letal por Local/Território",
        labels={"Proporção (%)": "Percentual (%)"},
        color="Proporção (%)",
        color_continuous_scale=px.colors.sequential.Plotly3,
        text="Proporção (%)"
    )
    fig_local.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_local.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_local, use_container_width=True)

st.caption(f"Fonte: {fonte_violencia_nao_letal}")

########################################################################################################################################
st.markdown("---")

# 5.4. Tipos Específicos de Violência Não Letal
st.subheader("5.4. Tipos Específicos de Violência Não Letal")

fig_tipos = px.bar(
    df_tipos_violencia_vnl,
    y="Subtipo de Violência",
    x="Prevalência (%)",
    orientation='h',
    color="Tipo de Violência Geral",
    title="Prevalência de Tipos Específicos de Violência Não Letal",
    labels={
        "Prevalência (%)": "Prevalência (%)",
        "Subtipo de Violência": "Subtipo"
    },
    text="Prevalência (%)"
)
fig_tipos.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
fig_tipos.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_tipos, use_container_width=True)

st.caption(f"Fonte: {fonte_violencia_nao_letal}")

#########################################################################################################################################
st.markdown("---")

st.header("6. LETALIDADE POLICIAL")

# 6.1. Por Sexo e 6.2. Por Faixa Etária
col_sexo_letalidade, col_faixa_etaria_letalidade = st.columns(2)

with col_sexo_letalidade:
    st.subheader("6.1. Por Sexo")
    fig_sexo_letalidade = px.pie(
        df_sexo_letalidade,
        values='Proporção (%)',
        names='Gênero',
        title='Letalidade Policial por Sexo',
        hole=0.3
    )
    fig_sexo_letalidade.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_sexo_letalidade, use_container_width=True)

with col_faixa_etaria_letalidade:
    st.subheader("6.2. Por Faixa Etária")
    fig_faixa_etaria_letalidade = px.bar(
        df_faixa_etaria_letalidade,
        x="Faixa Etária",
        y="Proporção (%)",
        title="Letalidade Policial por Faixa Etária",
        labels={"Proporção (%)": "Percentual (%)"},
        color="Proporção (%)",
        color_continuous_scale=px.colors.sequential.Oranges,
        text="Proporção (%)"
    )
    fig_faixa_etaria_letalidade.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_faixa_etaria_letalidade.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_faixa_etaria_letalidade, use_container_width=True)

# 6.3. Por Raça/Cor e 6.4. Por Local/Território do Óbito
col_raca_letalidade, col_local_obito_letalidade = st.columns(2)

with col_raca_letalidade:
    st.subheader("6.3. Por Raça/Cor")
    fig_raca_letalidade = px.pie(
        df_raca_letalidade,
        values='Proporção (%)',
        names='Raça/Cor',
        title='Letalidade Policial por Raça/Cor',
        hole=0.3
    )
    fig_raca_letalidade.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_raca_letalidade, use_container_width=True)

with col_local_obito_letalidade:
    st.subheader("6.4. Por Local/Território do Óbito")
    fig_local_obito_letalidade = px.pie(
        df_local_obito_letalidade,
        values='Proporção (%)',
        names='Local',
        title='Letalidade Policial por Local/Território do Óbito',
        hole=0.3
    )
    fig_local_obito_letalidade.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_local_obito_letalidade, use_container_width=True)

# 6.5. Instrumento/Arma Utilizados
st.subheader("6.5. Instrumento/Arma Utilizados")
st.metric(
    label="Letalidade Policial: Uso de Arma de Fogo (%)",
    value=f"{valor_arma_letalidade:.1f}%",
    delta=None
)
st.caption(f"Fonte: {fonte_letalidade_policial}")

####################################################################################################################
st.markdown("---")

st.header("7. VIOLÊNCIA SEXUAL")

# 7.1. Por Idade (Vítimas Femininas) e 7.2. Por Sexo
col_idade_vsex, col_sexo_vsex = st.columns(2)

with col_idade_vsex:
    st.subheader("7.1. Por Idade (Vítimas Femininas)")
    fig_idade_vsex = px.pie(
        df_idade_vsex,
        values='Proporção (%)',
        names='Faixa Etária',
        title='Vítimas de Violência Sexual por Idade (Feminino)',
        hole=0.3
    )
    fig_idade_vsex.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_idade_vsex, use_container_width=True)

with col_sexo_vsex:
    st.subheader("7.2. Por Sexo")
    fig_sexo_vsex = px.pie(
        df_sexo_vsex,
        values='Proporção (%)',
        names='Gênero',
        title='Vítimas de Violência Sexual por Sexo',
        hole=0.3
    )
    fig_sexo_vsex.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_sexo_vsex, use_container_width=True)

# 7.3. Por Local/Território
st.subheader("7.3. Por Local/Território")
fig_local_vsex = px.bar(
    df_local_vsex,
    x="Local",
    y="Proporção (%)",
    title="Violência Sexual por Local/Território",
    labels={"Proporção (%)": "Percentual (%)"},
    color="Proporção (%)",
    color_continuous_scale=px.colors.sequential.Plotly3,
    text="Proporção (%)"
)
fig_local_vsex.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_local_vsex.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_local_vsex, use_container_width=True)
st.caption(f"Fonte: {fonte_violencia_sexual}")

# 7.4. Número de Vítimas por Raça/Cor
st.subheader("7.4. Número de Vítimas por Raça/Cor")
fig_vitimas_raca_vsex = px.bar(
    df_vitimas_raca_vsex,
    x="Raça/Cor",
    y="Número de Vítimas",
    title="Número de Vítimas de Violência Sexual por Raça/Cor",
    labels={"Número de Vítimas": "Número de Vítimas"},
    color="Número de Vítimas",
    color_continuous_scale=px.colors.sequential.Purples,
    text="Número de Vítimas"
)
fig_vitimas_raca_vsex.update_traces(texttemplate='%{text}', textposition='outside')
fig_vitimas_raca_vsex.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_vitimas_raca_vsex, use_container_width=True)
st.caption(f"Fonte: {fonte_violencia_sexual}")

# 7.5. Estupro e 7.6. Exploração Sexual
col_estupro_vsex, col_exploracao_vsex = st.columns([1, 1])

with col_estupro_vsex:
    st.subheader("7.5. Estupro")
    fig_estupro_vsex = px.pie(
        df_estupro_vsex,
        values='Proporção (%)',
        names='Gênero (Até 13 anos)',
        title='Estupro (Vítimas Até 13 Anos)',
        hole=0.3
    )
    fig_estupro_vsex.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
    st.plotly_chart(fig_estupro_vsex, use_container_width=True)

with col_exploracao_vsex:
    st.subheader("7.6. Exploração Sexual")
    st.metric(
        label="Prevalência de Exploração Sexual",
        value=f"{valor_exploracao_sexual:.1f}%",
        delta=None
    )
st.caption(f"Fonte: {fonte_violencia_sexual}") # Caption para o bloco de Estupro/Exploração

# 7.7. Pedofilia
st.subheader("7.7. Pedofilia")
fig_pedofilia_vsex = px.bar(
    df_pedofilia_vsex,
    y="Relação com Agressor",
    x="Proporção (%)",
    orientation='h',
    title="Relação do Agressor em Casos de Pedofilia",
    labels={"Proporção (%)": "Percentual (%)", "Relação com Agressor": "Relação com Agressor"},
    color="Proporção (%)",
    color_continuous_scale=px.colors.sequential.Plotly3,
    text="Proporção (%)"
)
fig_pedofilia_vsex.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_pedofilia_vsex.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_pedofilia_vsex, use_container_width=True)
st.caption(f"Fonte: {fonte_violencia_sexual}")

####################################################################################################################
st.markdown("---")

st.header("8. VIOLÊNCIA LETAL: HOMICÍDIOS")

# 8.1. Por Sexo
st.subheader("8.1. Por Sexo")
fig_homicidios_sexo = px.bar(
    df_homicidios_sexo,
    x="Gênero",
    y="Proporção (%)",
    color="Faixa Etária",
    barmode="group",
    title="Homicídios por Sexo e Faixa Etária",
    labels={"Proporção (%)": "Percentual (%)", "Gênero": "Gênero"},
    text="Proporção (%)"
)
fig_homicidios_sexo.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
fig_homicidios_sexo.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_homicidios_sexo, use_container_width=True)
st.caption(f"Fonte: {fonte_homicidios}")
st.markdown("---")

# 8.2. Raça/Cor
st.subheader("8.2. Por Raça/Cor")
fig_homicidios_raca = px.bar(
    df_homicidios_raca,
    x="Raça/Cor",
    y="Proporção (%)",
    color="Faixa Etária",
    barmode="group",
    title="Homicídios por Raça/Cor e Faixa Etária",
    labels={"Proporção (%)": "Percentual (%)", "Raça/Cor": "Raça/Cor"},
    text="Proporção (%)"
)
fig_homicidios_raca.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
fig_homicidios_raca.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_homicidios_raca, use_container_width=True)
st.caption(f"Fonte: {fonte_homicidios}")
st.markdown("---")

# 8.3. Local/Território do Óbito
st.subheader("8.3. Local/Território do Óbito")
fig_homicidios_local = px.bar(
    df_homicidios_local,
    x="Local",
    y="Proporção (%)",
    color="Faixa Etária",
    barmode="group",
    title="Homicídios por Local/Território do Óbito e Faixa Etária",
    labels={"Proporção (%)": "Percentual (%)", "Local": "Local"},
    text="Proporção (%)"
)
fig_homicidios_local.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
fig_homicidios_local.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_homicidios_local, use_container_width=True)
st.caption(f"Fonte: {fonte_homicidios}")
st.markdown("---")

# 8.4. Instrumento ou Arma Utilizados
st.subheader("8.4. Instrumento ou Arma Utilizados")
fig_homicidios_arma = px.bar(
    df_homicidios_arma,
    y="Arma",
    x="Proporção (%)",
    orientation='h',
    color="Faixa Etária",
    barmode="group",
    title="Homicídios por Instrumento ou Arma Utilizados e Faixa Etária",
    labels={"Proporção (%)": "Percentual (%)", "Arma": "Instrumento/Arma"},
    text="Proporção (%)"
)
fig_homicidios_arma.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
fig_homicidios_arma.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_homicidios_arma, use_container_width=True)
st.caption(f"Fonte: {fonte_homicidios}")
st.markdown("---")

# 8.5. Causa
st.subheader("8.5. Causa")
fig_homicidios_causa = px.bar(
    df_homicidios_causa,
    y="Causa",
    x="Proporção (%)",
    orientation='h',
    color="Faixa Etária",
    barmode="group",
    title="Homicídios por Causa e Faixa Etária",
    labels={"Proporção (%)": "Percentual (%)", "Causa": "Causa"},
    text="Proporção (%)"
)
fig_homicidios_causa.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_homicidios_causa.update_layout(yaxis={'categoryorder':'total ascending'}, uniformtext_minsize=8, uniformtext_mode='hide')
st.plotly_chart(fig_homicidios_causa, use_container_width=True)
st.caption(f"Fonte: {fonte_homicidios}")
st.markdown("---")