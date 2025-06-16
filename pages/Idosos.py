import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    st.set_page_config(layout="wide", page_title="Idosos no Pará")

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

    st.markdown('<h1 class="main-header">Indicadores de Idosos no Pará</h1>', unsafe_allow_html=True)
    st.write("Esta dashboard apresenta uma análise abrangente dos indicadores sociais, de saúde, educação, inclusão digital, trabalho e renda, e violência para a população idosa no estado do Pará, baseada nos dados fornecidos.")

    # Data Extraction and Processing for IDOSOS.py

    # População Total de Idosos
    elderly_population_data = {
        'Category': ['Total da População de Idosos no Pará'],
        'Value': [978751],
        'Percentage': ['12,04%']
    }
    df_elderly_population = pd.DataFrame(elderly_population_data)

    # Saúde
    health_elderly_data = {
        'Indicador': [
            'Esperança de vida ao nascer (Pará)',
            'Esperança de vida ao nascer (Brasil)',
            'Prevalência de DCNT (Hipertensão Arterial)',
            'Prevalência de DCNT (Diabetes)',
            'Prevalência de DCNT (Doenças Cardíacas)',
            'Prevalência de DCNT (Doenças Respiratórias)',
            'Prevalência de DCNT (Câncer)',
            'Cobertura Vacinal (Influenza)',
            'Acesso a Serviços de Saúde (Consultou Médico/Enfermeiro)',
            'Acesso a Serviços de Saúde (Fez exame laboratorial/de imagem)',
            'Acesso a Serviços de Saúde (Internação Hospitalar)',
            'Saúde Mental (60 a 69 anos)',
            'Saúde Mental (70 a 79 anos)',
            'Saúde Mental (80 anos ou mais)'
        ],
        'Valor': [
            73.08, 75.5, 58.3, 25.7, 15.8, 12.4, 4.2, 75.8, 85.6, 70.3, 12.5,
            18.5, 23.1, 28.9
        ],
        'Unidade': [
            'anos', 'anos', '%', '%', '%', '%', '%', '%', '%', '%', '%',
            '%', '%', '%'
        ]
    }
    df_health_elderly = pd.DataFrame(health_elderly_data)

    # Educação
    education_elderly_data = {
        'Indicador': [
            'Taxa de Analfabetismo (60 a 69 anos)',
            'Taxa de Analfabetismo (70 a 79 anos)',
            'Taxa de Analfabetismo (80 anos ou mais)',
            'Anos de Estudo (Média)',
            'Participação em Atividades Educacionais/Culturais'
        ],
        'Valor': [18.9, 28.4, 40.1, 7.8, 15.2],
        'Unidade': ['%', '%', '%', 'anos', '%']
    }
    df_education_elderly = pd.DataFrame(education_elderly_data)

    # Inclusão Digital
    digital_inclusion_elderly_data = {
        'Indicador': [
            'Acesso à Internet',
            'Posse de Dispositivos Digitais (Smartphone)',
            'Posse de Dispositivos Digitais (Computador)'
        ],
        'Valor': [65.3, 88.1, 30.5],
        'Unidade': ['%', '%', '%']
    }
    df_digital_inclusion_elderly = pd.DataFrame(digital_inclusion_elderly_data)

    # Trabalho e Renda
    work_income_elderly_data = {
        'Indicador': [
            'Taxa de Participação na Força de Trabalho',
            'Taxa de Ocupação',
            'Taxa de Informalidade',
            'Rendimento Médio Mensal (Idosos Ocupados)',
            'Rendimento Médio Mensal (Beneficiários de Previdência/Assistência)'
        ],
        'Valor': [18.7, 17.1, 72.1, 1980.00, 1350.00],
        'Unidade': ['%', '%', '%', 'R$', 'R$']
    }
    df_work_income_elderly = pd.DataFrame(work_income_elderly_data)

    # Violência Não Letal
    non_lethal_violence_elderly_sex = {'Category': ['Feminino', 'Masculino'], 'Percentage': [70.5, 29.5]}
    df_non_lethal_elderly_sex = pd.DataFrame(non_lethal_violence_elderly_sex)

    non_lethal_violence_elderly_race = {'Category': ['Negra', 'Branca', 'Indígena', 'Amarela'], 'Percentage': [58.1, 40.2, 0.8, 0.9]}
    df_non_lethal_elderly_race = pd.DataFrame(non_lethal_violence_elderly_race)

    non_lethal_violence_elderly_location = {'Category': ['Residência da Vítima', 'Vias Públicas'], 'Percentage': [75.2, 10.1]}
    df_non_lethal_elderly_location = pd.DataFrame(non_lethal_violence_elderly_location)

    non_lethal_violence_elderly_type = {
        'Tipo de Violência': [
            'Agressão (Física)',
            'Lesão Corporal em Violência Doméstica (Física)',
            'Ameaça/Constrangimento (Psicológica)',
            'Extorsão/Apropriação Indébita (Patrimonial)',
            'Negligência/Abandono',
            'Sexual'
        ],
        'Valor': [25.3, 10.7, 18.2, 14.5, 12.1, 3.8]
    }
    df_non_lethal_elderly_type = pd.DataFrame(non_lethal_violence_elderly_type)

    # Violência Letal: Homicídios
    lethal_violence_elderly_data = {
        'Indicador': ['Total de Homicídios de Idosos (2022)'],
        'Valor': [213]
    }
    df_lethal_violence_elderly = pd.DataFrame(lethal_violence_elderly_data)

    lethal_violence_elderly_sex = {'Category': ['Masculino', 'Feminino'], 'Percentage': [85.6, 14.4]}
    df_lethal_elderly_sex = pd.DataFrame(lethal_violence_elderly_sex)

    lethal_violence_elderly_age = {'Category': ['60 a 69 anos', '70 a 79 anos', '80 anos ou mais'], 'Percentage': [45.1, 30.2, 24.7]}
    df_lethal_elderly_age = pd.DataFrame(lethal_violence_elderly_age)

    lethal_violence_elderly_race = {'Category': ['Negra', 'Branca', 'Indígena', 'Amarela'], 'Percentage': [62.5, 35.1, 1.5, 0.9]}
    df_lethal_elderly_race = pd.DataFrame(lethal_violence_elderly_race)

    lethal_violence_elderly_location = {'Category': ['Residência', 'Via pública', 'Outros locais'], 'Percentage': [55.8, 28.3, 15.9]}
    df_lethal_elderly_location = pd.DataFrame(lethal_violence_elderly_location)

    lethal_violence_elderly_weapon = {'Category': ['Arma de fogo', 'Arma branca', 'Agressão'], 'Percentage': [68.2, 18.5, 13.3]}
    df_lethal_elderly_weapon = pd.DataFrame(lethal_violence_elderly_weapon)

    # --- Dashboard Layout and Visualizations ---

    # Section 1: População Total
    st.markdown('<h2 class="section-header">População Total</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Total da População de Idosos no Pará</div>
                <div class="kpi-value">{df_elderly_population['Value'].iloc[0]:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 ")
    with col2:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Representatividade na População Total</div>
                <div class="kpi-value">{df_elderly_population['Percentage'].iloc[0]}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 ")

    # Section 2: Saúde
    st.markdown('<h2 class="section-header">Saúde</h2>', unsafe_allow_html=True)

    st.subheader("Esperança de Vida ao Nascer")
    df_life_expectancy = df_health_elderly[df_health_elderly['Indicador'].str.contains('Esperança de vida')]
    fig_life_expectancy = px.bar(
        df_life_expectancy,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Esperança de Vida ao Nascer (Pará vs. Brasil)',
        labels={'Indicador': 'Localidade', 'Valor': 'Anos'},
        color='Indicador',
        height=400
    )
    fig_life_expectancy.update_traces(texttemplate='%{text:.2f} anos', textposition='outside')
    st.plotly_chart(fig_life_expectancy, use_container_width=True)
    st.markdown("Fonte: IBGE 2022, IPEA 2023 ")

    st.subheader("Prevalência de Doenças Crônicas Não Transmissíveis (DCNT)")
    df_dcn_prevalence = df_health_elderly[df_health_elderly['Indicador'].str.contains('Prevalência de DCNT')]
    fig_dcn_prevalence = px.bar(
        df_dcn_prevalence,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Prevalência de DCNT em Idosos',
        labels={'Indicador': 'Doença', 'Valor': 'Prevalência (%)'},
        color='Indicador',
        height=500
    )
    fig_dcn_prevalence.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_dcn_prevalence.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_dcn_prevalence, use_container_width=True)
    st.markdown("Fonte: SISAB 2022 ")

    st.subheader("Cobertura Vacinal (Influenza)")
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{df_health_elderly[df_health_elderly['Indicador'] == 'Cobertura Vacinal (Influenza)']['Valor'].iloc[0]}%</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("Fonte: SESPA 2023 ")

    st.subheader("Acesso a Serviços de Saúde (últimos 12 meses)")
    df_health_access = df_health_elderly[df_health_elderly['Indicador'].str.contains('Acesso a Serviços de Saúde')]
    fig_health_access = px.bar(
        df_health_access,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Acesso a Serviços de Saúde em Idosos',
        labels={'Indicador': 'Serviço', 'Valor': 'Porcentagem (%)'},
        color='Indicador',
        height=400
    )
    fig_health_access.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_health_access.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_health_access, use_container_width=True)
    st.markdown("Fonte: PNS 2019 ")

    st.subheader("Índices de Saúde Mental (Depressão, Ansiedade, etc.)")
    df_mental_health_elderly = df_health_elderly[df_health_elderly['Indicador'].str.contains('Saúde Mental')]
    fig_mental_health_elderly = px.bar(
        df_mental_health_elderly,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Índices de Saúde Mental em Idosos por Faixa Etária',
        labels={'Indicador': 'Faixa Etária', 'Valor': 'Porcentagem (%)'},
        color='Indicador',
        height=400
    )
    fig_mental_health_elderly.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_mental_health_elderly.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_mental_health_elderly, use_container_width=True)
    st.markdown("Fonte: IBGE 2019 ")

    # Section 3: Educação
    st.markdown('<h2 class="section-header">Educação</h2>', unsafe_allow_html=True)

    st.subheader("Taxa de Analfabetismo por Faixa Etária")
    df_illiteracy = df_education_elderly[df_education_elderly['Indicador'].str.contains('Analfabetismo')]
    fig_illiteracy = px.bar(
        df_illiteracy,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Taxa de Analfabetismo em Idosos por Faixa Etária',
        labels={'Indicador': 'Faixa Etária', 'Valor': 'Taxa (%)'},
        color='Indicador',
        height=400
    )
    fig_illiteracy.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_illiteracy.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_illiteracy, use_container_width=True)
    st.markdown("Fonte: PNAD 2022 ")

    col_edu_eld1, col_edu_eld2 = st.columns(2)
    with col_edu_eld1:
        st.subheader("Média de Anos de Estudo")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_elderly[df_education_elderly['Indicador'] == 'Anos de Estudo (Média)']['Valor'].iloc[0]} anos</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD 2022 ")
    with col_edu_eld2:
        st.subheader("Participação em Atividades Educacionais/Culturais")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_elderly[df_education_elderly['Indicador'] == 'Participação em Atividades Educacionais/Culturais']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2019 ")

    # Section 4: Inclusão Digital
    st.markdown('<h2 class="section-header">Inclusão Digital</h2>', unsafe_allow_html=True)

    col_dig_eld1, col_dig_eld2 = st.columns(2)
    with col_dig_eld1:
        st.subheader("Acesso à Internet")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_digital_inclusion_elderly[df_digital_inclusion_elderly['Indicador'] == 'Acesso à Internet']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 ")
    with col_dig_eld2:
        st.subheader("Posse de Dispositivos Digitais")
        df_device_ownership_elderly = df_digital_inclusion_elderly[df_digital_inclusion_elderly['Indicador'].str.contains('Posse de Dispositivos')]
        fig_device_ownership_elderly = px.bar(
            df_device_ownership_elderly,
            x='Indicador',
            y='Valor',
            text='Valor',
            title='Posse de Dispositivos Digitais por Idosos',
            labels={'Indicador': 'Tipo de Dispositivo', 'Valor': 'Porcentagem (%)'},
            color='Indicador',
            height=300
        )
        fig_device_ownership_elderly.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
        fig_device_ownership_elderly.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_device_ownership_elderly, use_container_width=True)
        st.markdown("Fonte: IBGE 2022 ")

    # Section 5: Trabalho e Renda
    st.markdown('<h2 class="section-header">Trabalho e Renda</h2>', unsafe_allow_html=True)

    st.subheader("Taxas de Trabalho e Informalidade")
    df_work_rates_elderly = df_work_income_elderly[df_work_income_elderly['Indicador'].str.contains('Taxa')]
    fig_work_rates_elderly = px.bar(
        df_work_rates_elderly,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Taxas de Participação, Ocupação e Informalidade de Idosos',
        labels={'Indicador': 'Tipo de Taxa', 'Valor': 'Porcentagem (%)'},
        color='Indicador',
        height=400
    )
    fig_work_rates_elderly.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_work_rates_elderly.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_work_rates_elderly, use_container_width=True)
    st.markdown("Fonte: PNAD Contínua 2023 ")

    st.subheader("Rendimento Médio Mensal")
    df_income_elderly = df_work_income_elderly[df_work_income_elderly['Indicador'].str.contains('Rendimento Médio Mensal')]
    fig_income_elderly = px.bar(
        df_income_elderly,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Rendimento Médio Mensal de Idosos',
        labels={'Indicador': 'Fonte de Renda', 'Valor': 'Rendimento Médio (R$)'},
        color='Indicador',
        height=400
    )
    fig_income_elderly.update_traces(texttemplate='R$ %{text:,.2f}', textposition='outside')
    fig_income_elderly.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_income_elderly, use_container_width=True)
    st.markdown("Fonte: PNAD Contínua 2023 ")

    # Section 6: Violência Não Letal
    st.markdown('<h2 class="section-header">Violência Não Letal</h2>', unsafe_allow_html=True)

    col_vnl_eld1, col_vnl_eld2, col_vnl_eld3 = st.columns(3)
    with col_vnl_eld1:
        st.subheader("Por Sexo")
        fig_vnl_eld_sex = px.pie(df_non_lethal_elderly_sex, values='Percentage', names='Category', title='Violência Não Letal de Idosos por Sexo')
        st.plotly_chart(fig_vnl_eld_sex, use_container_width=True)
        st.markdown("Fonte: Fórum Brasileiro de Segurança Pública (FBSP) 2022 ")
    with col_vnl_eld2:
        st.subheader("Por Raça/Cor")
        fig_vnl_eld_race = px.pie(df_non_lethal_elderly_race, values='Percentage', names='Category', title='Violência Não Letal de Idosos por Raça/Cor')
        st.plotly_chart(fig_vnl_eld_race, use_container_width=True)
        st.markdown("Fonte: Fórum Brasileiro de Segurança Pública (FBSP) 2022 ")
    with col_vnl_eld3:
        st.subheader("Por Local/Território")
        fig_vnl_eld_location = px.pie(df_non_lethal_elderly_location, values='Percentage', names='Category', title='Violência Não Letal de Idosos por Local/Território')
        st.plotly_chart(fig_vnl_eld_location, use_container_width=True)
        st.markdown("Fonte: Fórum Brasileiro de Segurança Pública (FBSP) 2022 ")

    st.subheader("Tipos de Violência Não Letal")
    fig_vnl_eld_type = px.bar(
        df_non_lethal_elderly_type,
        x='Tipo de Violência',
        y='Valor',
        text='Valor',
        title='Prevalência dos Tipos de Violência Não Letal contra Idosos',
        labels={'Tipo de Violência': 'Tipo', 'Valor': 'Porcentagem (%)'},
        color='Tipo de Violência',
        height=500
    )
    fig_vnl_eld_type.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_vnl_eld_type.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_vnl_eld_type, use_container_width=True)
    st.markdown("Fonte: FBSP 2022 ")

    # Section 7: Violência Letal: Homicídios
    st.markdown('<h2 class="section-header">Violência Letal: Homicídios</h2>', unsafe_allow_html=True)

    st.subheader("Total de Homicídios de Idosos (2022)")
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{df_lethal_violence_elderly['Valor'].iloc[0]}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("Fonte: ObservaDH 2022 ")

    col_homicides_eld1, col_homicides_eld2 = st.columns(2)
    with col_homicides_eld1:
        st.subheader("Por Sexo")
        fig_hom_eld_sex = px.pie(df_lethal_elderly_sex, values='Percentage', names='Category', title='Homicídios de Idosos por Sexo')
        st.plotly_chart(fig_hom_eld_sex, use_container_width=True)
        st.markdown("Fonte: ObservaDH 2022 ")
    with col_homicides_eld2:
        st.subheader("Por Faixa Etária")
        fig_hom_eld_age = px.pie(df_lethal_elderly_age, values='Percentage', names='Category', title='Homicídios de Idosos por Faixa Etária')
        st.plotly_chart(fig_hom_eld_age, use_container_width=True)
        st.markdown("Fonte: ObservaDH 2022 ")

    col_homicides_eld3, col_homicides_eld4 = st.columns(2)
    with col_homicides_eld3:
        st.subheader("Por Raça/Cor")
        fig_hom_eld_race = px.pie(df_lethal_elderly_race, values='Percentage', names='Category', title='Homicídios de Idosos por Raça/Cor')
        st.plotly_chart(fig_hom_eld_race, use_container_width=True)
        st.markdown("Fonte: ObservaDH 2022 ")
    with col_homicides_eld4:
        st.subheader("Por Local/Território do Óbito")
        fig_hom_eld_location = px.pie(df_lethal_elderly_location, values='Percentage', names='Category', title='Homicídios de Idosos por Local do Óbito')
        st.plotly_chart(fig_hom_eld_location, use_container_width=True)
        st.markdown("Fonte: ObservaDH 2022 ")

    st.subheader("Por Instrumento/Arma Utilizados")
    fig_hom_eld_weapon = px.pie(df_lethal_elderly_weapon, values='Percentage', names='Category', title='Homicídios de Idosos por Instrumento/Arma')
    st.plotly_chart(fig_hom_eld_weapon, use_container_width=True)
    st.markdown("Fonte: ObservaDH 2022 ")

if __name__ == "__main__":
    app()