import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    st.set_page_config(layout="wide", page_title="Crianças e Adolescentes no Pará")

    st.markdown("""
        <style>
            .main-header {
                font-size: 3em;
                color: #2F4F4F;
                text-align: center;
                margin-bottom: 30px;
            }
            .section-header {
                font-size: 2em;
                color: #4682B4;
                border-bottom: 2px solid #4682B4;
                padding-bottom: 10px;
                margin-top: 40px;
                margin-bottom: 20px;
            }
            .kpi-card {
                background-color: #F0F8FF;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
                margin-bottom: 20px;
            }
            .kpi-value {
                font-size: 2.5em;
                font-weight: bold;
                color: #008B8B;
            }
            .kpi-title {
                font-size: 1.2em;
                color: #555555;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-header">Indicadores de Crianças e Adolescentes no Pará</h1>', unsafe_allow_html=True)
    st.write("Esta dashboard apresenta uma análise abrangente dos indicadores sociais, de saúde, educação, inclusão digital, trabalho e violência para crianças e adolescentes no estado do Pará, baseada nos dados fornecidos.")

    # Data extraction and processing
    # Total Population
    total_population_data = {
        'Category': ['Total da População de Crianças e Adolescentes no Pará'],
        'Value': [2431092],
        'Percentage': ['29,94%']
    }
    df_total_population = pd.DataFrame(total_population_data)

    # Health Data
    health_data = {
        'Indicador': [
            'Taxa de Mortalidade Juvenil (0 a 5 anos)',
            'Taxa de Mortalidade Juvenil (até 19 anos)',
            'Taxa de Mortalidade Juvenil (15 a 29 anos)',
            'Acesso a Serviços de Saúde Sexual e Reprodutiva (Tiveram relação sexual)',
            'Acesso a Serviços de Saúde Sexual e Reprodutiva (Meninos)',
            'Acesso a Serviços de Saúde Sexual e Reprodutiva (Meninas)',
            'Acesso a Serviços de Saúde Sexual e Reprodutiva (Receberam orientações sobre como adquirir preservativos gratuitos)',
            'Acesso a Serviços de Saúde Sexual e Reprodutiva (Obtiveram preservativos em serviços de saúde)',
            'Gravidez na Adolescência (10 a 19 anos)',
            'Prevalência de Doenças Crônicas Não Transmissíveis (13 a 17 anos)',
            'Fatores de riscos ao desenvolvimento de DCNT (Falta de atividade física)',
            'Fatores de riscos ao desenvolvimento de DCNT (Ingestão inadequada de frutas e vegetais)',
            'Fatores de riscos ao desenvolvimento de DCNT (Sedentarismo)',
            'Fatores de riscos ao desenvolvimento de DCNT (Consumo regular de doces)',
            'Fatores de riscos ao desenvolvimento de DCNT (Consumo de bebidas alcoólicas)',
            'Fatores de riscos ao desenvolvimento de DCNT (Consumo regular de refrigerantes)',
            'Fatores de riscos ao desenvolvimento de DCNT (Tabagismo)',
            'Índices de Saúde Mental (5 a 9 anos)',
            'Índices de Saúde Mental (10 a 14 anos)',
            'Índices de Saúde Mental (15 a 19 anos)'
        ],
        'Valor': [
            17.79, 26.3, 50.6, 30.5, 43.7, 18.7, 67.6, 22.1, 20.38, 81.3,
            71.5, 58.4, 54.1, 32.9, 28.1, 17.2, 6.8, 6.8, 12.0, 30.0
        ],
        'Unidade': [
            '%', '%', '%', '%', '%', '%', '%', '%', '%', '%',
            '%', '%', '%', '%', '%', '%', '%', '%', '%', '%'
        ]
    }
    df_health = pd.DataFrame(health_data)

    # Education Data
    education_data = {
        'Indicador': [
            'Taxa de Escolarização (4 a 5 anos)',
            'Taxa de Escolarização (6 a 14 anos)',
            'Taxa de Escolarização (15 a 17 anos)',
            'Abandono Escolar (Ensino Fundamental - anos finais)',
            'Abandono Escolar (Ensino Médio)',
            'Conclusão do Ensino Médio no tempo adequado',
            'Taxa de Distorção de Idade - Ensino Médio',
            'Educação Profissional Técnica',
            'Na Rede Federal de Educação Profissional',
            'Matrículas no Sistema (educação profissional)'
        ],
        'Valor': [86.2, 96.7, 84.3, 45.7, 45.9, 58.4, 45.7, 45.0, 30.0, 25.0],
        'Unidade': ['%', '%', '%', '%', '%', '%', '%', '%', '%', '%']
    }
    df_education = pd.DataFrame(education_data)

    # Digital Inclusion Data
    digital_inclusion_data = {
        'Indicador': [
            'Acesso à Internet',
            'Posse de Dispositivos Digitais (10 a 13 anos)',
            'Posse de Dispositivos Digitais (14 a 17 anos)',
            'Participação em Programas de Inclusão Digital (9 a 17 anos - Escola)',
            'Participação em Programas de Inclusão Digital (classes A e B)',
            'Participação em Programas de Inclusão Digital (classes D e E)'
        ],
        'Valor': [82.8, 54.8, 84.7, 44.0, 71.0, 15.0],
        'Unidade': ['%', '%', '%', '%', '%', '%']
    }
    df_digital_inclusion = pd.DataFrame(digital_inclusion_data)

    # Work Data (Rates)
    work_rates_data = {
        'Indicador': [
            'Taxa de Desemprego Juvenil (14-17 anos)',
            'Taxa de Desemprego Juvenil (18-24 anos)',
            'Taxa de Desemprego Juvenil (14-29 anos)',
            'Taxa de Informalidade no Trabalho Juvenil (14-17 anos)',
            'Taxa de Informalidade no Trabalho Juvenil (18-24 anos)',
            'Taxa de Informalidade no Trabalho Juvenil (14-29 anos)',
            'Taxa de Participação em Programas de Aprendizagem (15-24 anos)'
        ],
        'Valor': [41.2, 28.5, 23.7, 89.3, 71.5, 68.2, 11.0],
        'Unidade': ['%', '%', '%', '%', '%', '%', '%']
    }
    df_work_rates = pd.DataFrame(work_rates_data)

    # Work Data (Remuneration)
    work_remuneration_data = {
        'Tipo': [
            'Rendimento médio mensal',
            'Rendimento médio mensal',
            'Rendimento mediano mensal',
            'Rendimento mediano mensal'
        ],
        'Faixa Etária': [
            '14-17 anos',
            '18-24 anos',
            '14-17 anos',
            '18-24 anos'
        ],
        'Valor': [65.00, 1212.00, 512.00, 1045.00],
        'Unidade': ['R$', 'R$', 'R$', 'R$']
    }
    df_work_remuneration = pd.DataFrame(work_remuneration_data)

    # Non-Lethal Violence Data
    non_lethal_violence_data_sex = {'Category': ['Feminino', 'Masculino'], 'Percentage': [88.7, 11.3]}
    df_non_lethal_sex = pd.DataFrame(non_lethal_violence_data_sex)

    non_lethal_violence_data_race = {'Category': ['Negra', 'Branca', 'Indígena', 'Amarela'], 'Percentage': [56.8, 42.3, 0.5, 0.4]}
    df_non_lethal_race = pd.DataFrame(non_lethal_violence_data_race)

    non_lethal_violence_data_location = {'Category': ['Residência da Vítima', 'Vias Públicas'], 'Percentage': [68.3, 9.4]}
    df_non_lethal_location = pd.DataFrame(non_lethal_violence_data_location)

    non_lethal_violence_data_type = {
        'Tipo de Violência': [
            'Maus-Tratos', 'Lesão Corporal em Violência Doméstica',
            'Pornografia Infanto-Juvenil',
            'Estupro', 'Exploração Sexual',
            'Abandono de Incapaz', 'Abandono Material'
        ],
        'Valor': [13.38, 3.46, 7.03, 15.3, 16.36, 14.04, 1.85]
    }
    df_non_lethal_type = pd.DataFrame(non_lethal_violence_data_type)

    # Police Lethality Data
    police_lethality_sex = {'Category': ['Masculino', 'Feminino'], 'Percentage': [98.4, 1.6]}
    df_police_lethality_sex = pd.DataFrame(police_lethality_sex)

    police_lethality_age = {'Category': ['0 a 11 anos', '12 a 17 anos', '18 a 24 anos'], 'Percentage': [0.1, 7.5, 45.4]}
    df_police_lethality_age = pd.DataFrame(police_lethality_age)

    police_lethality_race = {'Category': ['Negro', 'Branco', 'Amarelo'], 'Percentage': [83.1, 16.6, 0.2]}
    df_police_lethality_race = pd.DataFrame(police_lethality_race)

    police_lethality_location = {'Category': ['Via pública', 'Residência', 'Outros Locais'], 'Percentage': [68.1, 15.8, 16.1]}
    df_police_lethality_location = pd.DataFrame(police_lethality_location)

    police_lethality_weapon = {'Category': ['Arma de fogo'], 'Percentage': [76.5]}
    df_police_lethality_weapon = pd.DataFrame(police_lethality_weapon)

    # Sexual Violence Data
    sexual_violence_age_female = {'Age Group': ['10 a 13 anos: feminino', '05 a 09 anos: feminino', '0 a 04 anos: feminino'], 'Percentage': [57.97, 26.5, 15.53]}
    df_sexual_violence_age_female = pd.DataFrame(sexual_violence_age_female)

    sexual_violence_sex = {'Category': ['Feminino', 'Masculino'], 'Percentage': [85.98, 14.02]}
    df_sexual_violence_sex = pd.DataFrame(sexual_violence_sex)

    sexual_violence_location = {'Category': ['Residência da Vítima', 'Vias Públicas'], 'Percentage': [68.3, 9.4]}
    df_sexual_violence_location = pd.DataFrame(sexual_violence_location)

    sexual_violence_victims_race = {'Race/Color': ['Negro', 'Branco', 'Indígena', 'Amarelo'], 'Número de Vítimas': [12452, 9516, 101, 69]}
    df_sexual_violence_victims_race = pd.DataFrame(sexual_violence_victims_race)

    sexual_violence_rape = {'Category': ['Até 13 anos Meninas', 'Até 13 anos Meninos'], 'Percentage': [85.98, 14.02]}
    df_sexual_violence_rape = pd.DataFrame(sexual_violence_rape)

    sexual_violence_pedophilia = {
        'Relationship': [
            'Pai /Padrasto', 'Conhecido', 'Tio', 'Avô/Avó', 'Vizinho',
            'Outro familiar', 'Desconhecido', 'Primo', 'Irmão/irmã'
        ],
        'Percentage': [44.4, 18.0, 7.7, 7.4, 6.4, 4.8, 4.1, 3.8, 3.4]
    }
    df_sexual_violence_pedophilia = pd.DataFrame(sexual_violence_pedophilia)

    sexual_violence_exploitation = {'Category': ['Exploração Sexual'], 'Percentage': [16.4]}
    df_sexual_violence_exploitation = pd.DataFrame(sexual_violence_exploitation)

    # Lethal Violence - Homicides Data
    homicides_sex_0_11 = {'Category': ['Masculino', 'Feminino'], 'Percentage': [37.60, 81.71]}
    df_homicides_sex_0_11 = pd.DataFrame(homicides_sex_0_11)

    homicides_sex_12_17 = {'Category': ['Masculino', 'Feminino'], 'Percentage': [62.40, 18.29]}
    df_homicides_sex_12_17 = pd.DataFrame(homicides_sex_12_17)

    homicides_race_0_11 = {'Category': ['Negros', 'Brancos'], 'Percentage': [44.08, 69.10]}
    df_homicides_race_0_11 = pd.DataFrame(homicides_race_0_11)

    homicides_race_12_17 = {'Category': ['Negros', 'Brancos'], 'Percentage': [55.92, 30.90]}
    df_homicides_race_12_17 = pd.DataFrame(homicides_race_12_17)

    homicides_location_0_11 = {'Category': ['via pública', 'residência', 'outros'], 'Percentage': [15.38, 65.38, 19.23]}
    df_homicides_location_0_11 = pd.DataFrame(homicides_location_0_11)

    homicides_location_12_17 = {'Category': ['via pública', 'residência', 'outros'], 'Percentage': [59.41, 15.84, 24.75]}
    df_homicides_location_12_17 = pd.DataFrame(homicides_location_12_17)

    homicides_weapon_0_11 = {'Category': ['agressão', 'arma branca', 'arma de fogo'], 'Percentage': [21.15, 23.08, 55.77]}
    df_homicides_weapon_0_11 = pd.DataFrame(homicides_weapon_0_11)

    homicides_weapon_12_17 = {'Category': ['arma de fogo', 'arma branca'], 'Percentage': [90.76, 8.87]}
    df_homicides_weapon_12_17 = pd.DataFrame(homicides_weapon_12_17)

    homicides_cause_0_11 = {'Category': ['homicídio doloso', 'feminicídio', 'lesão corporal seguida de morte', 'morte decorrente de lesão corporal', 'latrocínio'], 'Percentage': [84.8, 11.4, 1.9, 1.4, 0.5]}
    df_homicides_cause_0_11 = pd.DataFrame(homicides_cause_0_11)

    homicides_cause_12_17 = {'Category': ['homicídio doloso', 'morte decorrente de intervenção policial', 'feminicídio', 'latrocínio', 'lesão corporal seguida de morte'], 'Percentage': [80.4, 15.7, 2.2, 0.8, 0.8]}
    df_homicides_cause_12_17 = pd.DataFrame(homicides_cause_12_17)

    # --- Dashboard Layout and Visualizations ---

    # Section 1: População Total
    st.markdown('<h2 class="section-header">População Total</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Total da População de Crianças e Adolescentes no Pará</div>
                <div class="kpi-value">{df_total_population['Value'].iloc[0]:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Representatividade na População Total</div>
                <div class="kpi-value">{df_total_population['Percentage'].iloc[0]}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("Fonte: IBGE 2022 ")

    # Section 2: Saúde
    st.markdown('<h2 class="section-header">Saúde</h2>', unsafe_allow_html=True)

    st.subheader("Taxa de Mortalidade Juvenil")
    df_mortality = df_health[df_health['Indicador'].str.contains('Mortalidade Juvenil')]
    fig_mortality = px.bar(
        df_mortality,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Taxa de Mortalidade Juvenil por Faixa Etária',
        labels={'Indicador': 'Faixa Etária', 'Valor': 'Taxa (%)'},
        color='Indicador',
        height=400
    )
    fig_mortality.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_mortality.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_mortality, use_container_width=True)
    st.markdown("Fonte: FAPESPA 2024, IPEA 2023 ")

    st.subheader("Acesso a Serviços de Saúde Sexual e Reprodutiva")
    df_sexual_health = df_health[df_health['Indicador'].str.contains('Saúde Sexual e Reprodutiva')]
    fig_sexual_health = px.bar(
        df_sexual_health,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Acesso a Serviços de Saúde Sexual e Reprodutiva',
        labels={'Indicador': 'Tipo de Acesso', 'Valor': 'Porcentagem (%)'},
        color='Indicador',
        height=500
    )
    fig_sexual_health.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_sexual_health.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_sexual_health, use_container_width=True)
    st.markdown("Fonte: IBGE 2019 ")

    col_health1, col_health2 = st.columns(2)
    with col_health1:
        st.subheader("Gravidez na Adolescência (10 a 19 anos)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health[df_health['Indicador'] == 'Gravidez na Adolescência (10 a 19 anos)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: SESPA 2022 ")
    with col_health2:
        st.subheader("Prevalência de Doenças Crônicas Não Transmissíveis (13 a 17 anos)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health[df_health['Indicador'] == 'Prevalência de Doenças Crônicas Não Transmissíveis (13 a 17 anos)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2019 ")

    st.subheader("Fatores de Riscos ao Desenvolvimento de DCNT")
    df_risk_factors = df_health[df_health['Indicador'].str.contains('Fatores de riscos ao desenvolvimento de DCNT')]
    fig_risk_factors = px.bar(
        df_risk_factors,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Fatores de Riscos para Doenças Crônicas Não Transmissíveis',
        labels={'Indicador': 'Fator de Risco', 'Valor': 'Porcentagem (%)'},
        color='Indicador',
        height=500
    )
    fig_risk_factors.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_risk_factors.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_risk_factors, use_container_width=True)
    st.markdown("Fonte: IBGE 2019 ")

    st.subheader("Índices de Saúde Mental")
    df_mental_health = df_health[df_health['Indicador'].str.contains('Índices de Saúde Mental')]
    fig_mental_health = px.bar(
        df_mental_health,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Índices de Saúde Mental por Faixa Etária',
        labels={'Indicador': 'Faixa Etária', 'Valor': 'Porcentagem (%)'},
        color='Indicador',
        height=400
    )
    fig_mental_health.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_mental_health.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_mental_health, use_container_width=True)
    st.markdown("Fonte: IBGE 2019 ")

    # Section 3: Educação
    st.markdown('<h2 class="section-header">Educação</h2>', unsafe_allow_html=True)

    st.subheader("Taxa de Escolarização")
    df_schooling_rate = df_education[df_education['Indicador'].str.contains('Taxa de Escolarização')]
    fig_schooling_rate = px.bar(
        df_schooling_rate,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Taxa de Escolarização por Faixa Etária',
        labels={'Indicador': 'Faixa Etária', 'Valor': 'Taxa (%)'},
        color='Indicador',
        height=400
    )
    fig_schooling_rate.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_schooling_rate.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_schooling_rate, use_container_width=True)
    st.markdown("Fonte: IBGE 2022 / INEP 2022 ")

    st.subheader("Abandono Escolar")
    df_dropout_rate = df_education[df_education['Indicador'].str.contains('Abandono Escolar')]
    fig_dropout_rate = px.bar(
        df_dropout_rate,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Taxa de Abandono Escolar por Nível de Ensino',
        labels={'Indicador': 'Nível de Ensino', 'Valor': 'Taxa (%)'},
        color='Indicador',
        height=400
    )
  
    fig_dropout_rate.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_dropout_rate.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_dropout_rate, use_container_width=True)
    st.markdown("Fonte: IBGE 2022 / INEP 2022 ")

    col_edu1, col_edu2 = st.columns(2)
    with col_edu1:
        st.subheader("Conclusão do Ensino Médio no tempo adequado")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education[df_education['Indicador'] == 'Conclusão do Ensino Médio no tempo adequado']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 / INEP 2022 ")
    with col_edu2:
        st.subheader("Taxa de Distorção de Idade - Ensino Médio")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education[df_education['Indicador'] == 'Taxa de Distorção de Idade - Ensino Médio']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 / INEP 2022 ")

    st.subheader("Acesso à Educação Profissionalizante")
    df_vocational_education = df_education[df_education['Indicador'].str.contains('Educação Profissional')]
    fig_vocational_education = px.bar(
        df_vocational_education,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Acesso à Educação Profissionalizante',
        labels={'Indicador': 'Tipo de Acesso', 'Valor': 'Porcentagem (%)'},
        color='Indicador',
        height=400
    )
    fig_vocational_education.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_vocational_education.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_vocational_education, use_container_width=True)
    st.markdown("Fonte: IBGE 2022 / INEP 2022 ")

    # Section 4: Inclusão Digital
    st.markdown('<h2 class="section-header">Inclusão Digital</h2>', unsafe_allow_html=True)

    col_dig1, col_dig2 = st.columns(2)
    with col_dig1:
        st.subheader("Acesso à Internet")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_digital_inclusion[df_digital_inclusion['Indicador'] == 'Acesso à Internet']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: FAPESPA 2023 / INEP 2022 ")
    with col_dig2:
        st.subheader("Posse de Dispositivos Digitais")
        df_device_ownership = df_digital_inclusion[df_digital_inclusion['Indicador'].str.contains('Posse de Dispositivos Digitais')]
        fig_device_ownership = px.bar(
            df_device_ownership,
            x='Indicador',
            y='Valor',
            text='Valor',
            title='Posse de Dispositivos Digitais por Faixa Etária',
            labels={'Indicador': 'Faixa Etária', 'Valor': 'Porcentagem (%)'},
            color='Indicador',
            height=300
        )
        fig_device_ownership.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
        fig_device_ownership.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_device_ownership, use_container_width=True)
        st.markdown("Fonte: FAPESPA 2023 / INEP 2022 ")

    st.subheader("Participação em Programas de Inclusão Digital")
    df_digital_inclusion_programs = df_digital_inclusion[df_digital_inclusion['Indicador'].str.contains('Participação em Programas de Inclusão Digital')]
    fig_digital_inclusion_programs = px.bar(
        df_digital_inclusion_programs,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Participação em Programas de Inclusão Digital',
        labels={'Indicador': 'Grupo', 'Valor': 'Porcentagem (%)'},
        color='Indicador',
        height=400
    )
    fig_digital_inclusion_programs.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_digital_inclusion_programs.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_digital_inclusion_programs, use_container_width=True)
    st.markdown("Fonte: FAPESPA 2023 / INEP 2022 ")

    # Section 5: Trabalho
    st.markdown('<h2 class="section-header">Trabalho</h2>', unsafe_allow_html=True)

    st.subheader("Taxas de Desemprego e Informalidade Juvenil")
    df_unemployment_informality = df_work_rates[df_work_rates['Indicador'].str.contains('Desemprego Juvenil|Informalidade no Trabalho Juvenil')]
    fig_unemployment_informality = px.bar(
        df_unemployment_informality,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Taxas de Desemprego e Informalidade Juvenil por Faixa Etária',
        labels={'Indicador': 'Indicador e Faixa Etária', 'Valor': 'Taxa (%)'},
        color='Indicador',
        height=500
    )
    fig_unemployment_informality.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_unemployment_informality.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_unemployment_informality, use_container_width=True)
    st.markdown("Fonte: IBGE 2022 ")

    col_work1, col_work2 = st.columns(2)
    with col_work1:
        st.subheader("Taxa de Participação em Programas de Aprendizagem (15-24 anos)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_work_rates[df_work_rates['Indicador'] == 'Taxa de Participação em Programas de Aprendizagem (15-24 anos)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 ")

    with col_work2:
        st.subheader("Rendimento Mensal de Jovens Trabalhadores")
        fig_remuneration = px.bar(
            df_work_remuneration,
            x='Faixa Etária',
            y='Valor',
            color='Tipo',
            barmode='group',
            text='Valor',
            title='Rendimento Médio e Mediano Mensal por Faixa Etária',
            labels={'Faixa Etária': 'Faixa Etária', 'Valor': 'Rendimento (R$)'},
            height=400
        )
        fig_remuneration.update_traces(texttemplate='R$ %{text:,.2f}', textposition='outside')
        st.plotly_chart(fig_remuneration, use_container_width=True)
        st.markdown("Fonte: IBGE 2022 ")

    # Section 6: Violência Não Letal
    st.markdown('<h2 class="section-header">Violência Não Letal</h2>', unsafe_allow_html=True)

    col_vnl1, col_vnl2, col_vnl3 = st.columns(3)
    with col_vnl1:
        st.subheader("Por Sexo")
        fig_vnl_sex = px.pie(df_non_lethal_sex, values='Percentage', names='Category', title='Violência Não Letal por Sexo')
        st.plotly_chart(fig_vnl_sex, use_container_width=True)
        st.markdown("Fonte: Fórum Brasileiro de Segurança Pública (FBSP) 2022 ")
    with col_vnl2:
        st.subheader("Por Raça/Cor")
        fig_vnl_race = px.pie(df_non_lethal_race, values='Percentage', names='Category', title='Violência Não Letal por Raça/Cor')
        st.plotly_chart(fig_vnl_race, use_container_width=True)
        st.markdown("Fonte: Fórum Brasileiro de Segurança Pública (FBSP) 2022 ")
    with col_vnl3:
        st.subheader("Por Local/Território")
        fig_vnl_location = px.pie(df_non_lethal_location, values='Percentage', names='Category', title='Violência Não Letal por Local/Território')
        st.plotly_chart(fig_vnl_location, use_container_width=True)
        st.markdown("Fonte: Fórum Brasileiro de Segurança Pública (FBSP) 2022 ")

    st.subheader("Tipos de Violência Não Letal")
    fig_vnl_type = px.bar(
        df_non_lethal_type,
        x='Tipo de Violência',
        y='Valor',
        text='Valor',
        title='Prevalência dos Tipos de Violência Não Letal',
        labels={'Tipo de Violência': 'Tipo', 'Valor': 'Porcentagem (%)'},
        color='Tipo de Violência',
        height=500
    )
    fig_vnl_type.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_vnl_type.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_vnl_type, use_container_width=True)
    st.markdown("Fonte: FBSP 2022 ")

    # Section 7: Letalidade Policial
    st.markdown('<h2 class="section-header">Letalidade Policial</h2>', unsafe_allow_html=True)

    col_pol1, col_pol2, col_pol3 = st.columns(3)
    with col_pol1:
        st.subheader("Por Sexo")
        fig_pol_sex = px.pie(df_police_lethality_sex, values='Percentage', names='Category', title='Letalidade Policial por Sexo')
        st.plotly_chart(fig_pol_sex, use_container_width=True)
        st.markdown("Fonte: FBSP 2022 ")
    with col_pol2:
        st.subheader("Por Faixa Etária")
        fig_pol_age = px.bar(df_police_lethality_age, x='Category', y='Percentage', text='Percentage', title='Letalidade Policial por Faixa Etária', labels={'Category': 'Faixa Etária', 'Percentage': 'Porcentagem (%)'}, color='Category')
        fig_pol_age.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
        fig_pol_age.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_pol_age, use_container_width=True)
        st.markdown("Fonte: FBSP 2022 ")
    with col_pol3:
        st.subheader("Por Raça/Cor")
        fig_pol_race = px.pie(df_police_lethality_race, values='Percentage', names='Category', title='Letalidade Policial por Raça/Cor')
        st.plotly_chart(fig_pol_race, use_container_width=True)
        st.markdown("Fonte: FBSP 2022 ")

    col_pol4, col_pol5 = st.columns(2)
    with col_pol4:
        st.subheader("Local/Território do Óbito")
        fig_pol_location = px.pie(df_police_lethality_location, values='Percentage', names='Category', title='Letalidade Policial por Local do Óbito')
        st.plotly_chart(fig_pol_location, use_container_width=True)
        st.markdown("Fonte: FBSP 2022 ")
    with col_pol5:
        st.subheader("Instrumento/Arma Utilizados")
        fig_pol_weapon = px.pie(df_police_lethality_weapon, values='Percentage', names='Category', title='Instrumento/Arma Utilizados na Letalidade Policial')
        st.plotly_chart(fig_pol_weapon, use_container_width=True)
        st.markdown("Fonte: FBSP 2022 ")

    # Section 8: Violência Sexual
    st.markdown('<h2 class="section-header">Violência Sexual</h2>', unsafe_allow_html=True)

    col_vs1, col_vs2 = st.columns(2)
    with col_vs1:
        st.subheader("Vítimas do Sexo Feminino por Idade")
        fig_vs_age_female = px.pie(df_sexual_violence_age_female, values='Percentage', names='Age Group', title='Violência Sexual: Vítimas Femininas por Idade')
        st.plotly_chart(fig_vs_age_female, use_container_width=True)
        st.markdown("Fonte: ObservaDH 2022 / FBSP 2022 ")
    with col_vs2:
        st.subheader("Por Sexo")
        fig_vs_sex = px.pie(df_sexual_violence_sex, values='Percentage', names='Category', title='Violência Sexual por Sexo')
        st.plotly_chart(fig_vs_sex, use_container_width=True)
        st.markdown("Fonte: ObservaDH 2022 / FBSP 2022 ")

    col_vs3, col_vs4 = st.columns(2)
    with col_vs3:
        st.subheader("Por Local/Território")
        fig_vs_location = px.pie(df_sexual_violence_location, values='Percentage', names='Category', title='Violência Sexual por Local/Território')
        st.plotly_chart(fig_vs_location, use_container_width=True)
        st.markdown("Fonte: ObservaDH 2022 / FBSP 2022 ")
    with col_vs4:
        st.subheader("Número de Vítimas por Raça/Cor")
        fig_vs_race_victims = px.bar(df_sexual_violence_victims_race, x='Race/Color', y='Número de Vítimas', text='Número de Vítimas', title='Violência Sexual: Vítimas por Raça/Cor', labels={'Race/Color': 'Raça/Cor', 'Número de Vítimas': 'Número de Vítimas'}, color='Race/Color')
        fig_vs_race_victims.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
        fig_vs_race_victims.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_vs_race_victims, use_container_width=True)
        st.markdown("Fonte: ObservaDH 2022 / FBSP 2022 ")

    st.subheader("Estupro por Sexo (Até 13 anos)")
    fig_vs_rape = px.pie(df_sexual_violence_rape, values='Percentage', names='Category', title='Estupro: Vítimas até 13 anos por Sexo')
    st.plotly_chart(fig_vs_rape, use_container_width=True)
    st.markdown("Fonte: ObservaDH 2022 / FBSP 2022 ")

    st.subheader("Pedofilia por Relação com a Vítima")
    fig_vs_pedophilia = px.bar(
        df_sexual_violence_pedophilia,
        x='Relationship',
        y='Percentage',
        text='Percentage',
        title='Pedofilia: Relação do Agressor com a Vítima',
        labels={'Relationship': 'Relação', 'Percentage': 'Porcentagem (%)'},
        color='Relationship',
        height=500
    )
    fig_vs_pedophilia.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_vs_pedophilia.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_vs_pedophilia, use_container_width=True)
    st.markdown("Fonte: ObservaDH 2022 / FBSP 2022 ")

    st.subheader("Exploração Sexual")
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{df_sexual_violence_exploitation['Percentage'].iloc[0]}%</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("Fonte: ObservaDH 2022 / FBSP 2022 ")

    # Section 9: Violência Letal: Homicídios
    st.markdown('<h2 class="section-header">Violência Letal: Homicídios</h2>', unsafe_allow_html=True)

    st.subheader("Homicídios por Sexo")
    col_hom_sex1, col_hom_sex2 = st.columns(2)
    with col_hom_sex1:
        fig_hom_sex_0_11 = px.pie(df_homicides_sex_0_11, values='Percentage', names='Category', title='0 a 11 anos')
        st.plotly_chart(fig_hom_sex_0_11, use_container_width=True)
    with col_hom_sex2:
        fig_hom_sex_12_17 = px.pie(df_homicides_sex_12_17, values='Percentage', names='Category', title='12 a 17 anos')
        st.plotly_chart(fig_hom_sex_12_17, use_container_width=True)
    st.markdown("Fonte: ObservaDH 2022 ")

    st.subheader("Homicídios por Raça/Cor")
    col_hom_race1, col_hom_race2 = st.columns(2)
    with col_hom_race1:
        fig_hom_race_0_11 = px.pie(df_homicides_race_0_11, values='Percentage', names='Category', title='0 a 11 anos')
        st.plotly_chart(fig_hom_race_0_11, use_container_width=True)
    with col_hom_race2:
        fig_hom_race_12_17 = px.pie(df_homicides_race_12_17, values='Percentage', names='Category', title='12 a 17 anos')
        st.plotly_chart(fig_hom_race_12_17, use_container_width=True)
    st.markdown("Fonte: ObservaDH 2022 ")

    st.subheader("Homicídios por Local/Território do Óbito")
    col_hom_loc1, col_hom_loc2 = st.columns(2)
    with col_hom_loc1:
        fig_hom_loc_0_11 = px.pie(df_homicides_location_0_11, values='Percentage', names='Category', title='0 a 11 anos')
        st.plotly_chart(fig_hom_loc_0_11, use_container_width=True)
    with col_hom_loc2:
        fig_hom_loc_12_17 = px.pie(df_homicides_location_12_17, values='Percentage', names='Category', title='12 a 17 anos')
        st.plotly_chart(fig_hom_loc_12_17, use_container_width=True)
    st.markdown("Fonte: ObservaDH 2022 ")

    st.subheader("Homicídios por Instrumento ou Arma Utilizados")
    col_hom_weapon1, col_hom_weapon2 = st.columns(2)
    with col_hom_weapon1:
        fig_hom_weapon_0_11 = px.pie(df_homicides_weapon_0_11, values='Percentage', names='Category', title='0 a 11 anos')
        st.plotly_chart(fig_hom_weapon_0_11, use_container_width=True)
    with col_hom_weapon2:
        fig_hom_weapon_12_17 = px.pie(df_homicides_weapon_12_17, values='Percentage', names='Category', title='12 a 17 anos')
        st.plotly_chart(fig_hom_weapon_12_17, use_container_width=True)
    st.markdown("Fonte: ObservaDH 2022 ")

    st.subheader("Homicídios por Causa")
    col_hom_cause1, col_hom_cause2 = st.columns(2)
    with col_hom_cause1:
        fig_hom_cause_0_11 = px.pie(df_homicides_cause_0_11, values='Percentage', names='Category', title='0 a 11 anos')
        st.plotly_chart(fig_hom_cause_0_11, use_container_width=True)
    with col_hom_cause2:
        fig_hom_cause_12_17 = px.pie(df_homicides_cause_12_17, values='Percentage', names='Category', title='12 a 17 anos')
        st.plotly_chart(fig_hom_cause_12_17, use_container_width=True)
    st.markdown("Fonte: ObservaDH 2022 ")

if __name__ == "__main__":
    app()