import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    st.set_page_config(layout="wide", page_title="Pessoas com Deficiência no Pará")

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

    st.markdown('<h1 class="main-header">Indicadores de Pessoas com Deficiência (PCD) no Pará</h1>', unsafe_allow_html=True)
    st.write("Esta dashboard apresenta uma análise abrangente dos indicadores sociais, de saúde, educação, inclusão no mercado de trabalho e violência para a população de Pessoas com Deficiência no estado do Pará, baseada nos dados fornecidos.")

    # Data Extraction and Processing for PCD.py

    # População Total de PCD
    pcd_population_data = {
        'Category': ['Total da População de Pessoas com Deficiência no Pará'],
        'Value': [1554499],
        'Percentage': ['19,13%']
    }
    df_pcd_population = pd.DataFrame(pcd_population_data)

    # Saúde
    health_pcd_data = {
        'Indicador': [
            'Acesso a serviços de saúde (últimos 12 meses)',
            'Dificuldade de acesso a serviços de saúde',
            'Reabilitação/Terapias (Pessoas que necessitam e recebem)',
            'Prevalência de Condições Crônicas (Diabetes)',
            'Prevalência de Condições Crônicas (Hipertensão Arterial)',
            'Prevalência de Condições Crônicas (Doenças Cardíacas)',
            'Prevalência de Condições Crônicas (Doenças Respiratórias)'
        ],
        'Valor': [70.1, 25.8, 35.2, 15.3, 35.7, 10.2, 8.9],
        'Unidade': ['%', '%', '%', '%', '%', '%', '%']
    }
    df_health_pcd = pd.DataFrame(health_pcd_data)

    # Educação
    education_pcd_data = {
        'Indicador': [
            'Taxa de Escolarização (6 a 17 anos)',
            'Inclusão em Escolas Regulares',
            'Apoio Educacional Especializado (recebem)',
            'Taxa de Analfabetismo (15 anos ou mais)',
            'Conclusão do Ensino Médio (PCD 18+)'
        ],
        'Valor': [68.4, 85.6, 40.1, 28.7, 35.9],
        'Unidade': ['%', '%', '%', '%', '%']
    }
    df_education_pcd = pd.DataFrame(education_pcd_data)

    # Inclusão no Mercado de Trabalho
    work_pcd_data = {
        'Indicador': [
            'Taxa de Ocupação (14 anos ou mais)',
            'Salário Médio Mensal (PCD Ocupadas)',
            'Contratações via Lei de Cotas (2023)',
            'Discriminação no ambiente de trabalho (relatos)'
        ],
        'Valor': [18.2, 1250.00, 5210, 55.7],
        'Unidade': ['%', 'R$', 'números', '%']
    }
    df_work_pcd = pd.DataFrame(work_pcd_data)

    # Violência
    violence_pcd_data = {
        'Indicador': ['Total de denúncias de violência contra PCD no Pará (2023)'],
        'Valor': [850]
    }
    df_violence_pcd_kpis = pd.DataFrame(violence_pcd_data)

    violence_pcd_types = {
        'Tipo de Violência': [
            'Negligência/Abandono',
            'Violência Psicológica',
            'Violência Física',
            'Violência Sexual'
        ],
        'Valor': [45.8, 25.1, 20.5, 8.6]
    }
    df_violence_pcd_types = pd.DataFrame(violence_pcd_types)

    violence_pcd_location = {
        'Local de Ocorrência': [
            'Residência da Vítima',
            'Instituições/Serviços',
            'Via Pública'
        ],
        'Percentage': [78.2, 10.1, 7.5]
    }
    df_violence_pcd_location = pd.DataFrame(violence_pcd_location)

    violence_pcd_aggressor = {
        'Perfil do Agressor': [
            'Familiar (pais, irmãos, filhos)',
            'Cuidadores/Profissionais',
            'Desconhecido'
        ],
        'Percentage': [65.3, 15.8, 10.2]
    }
    df_violence_pcd_aggressor = pd.DataFrame(violence_pcd_aggressor)

    # --- Dashboard Layout and Visualizations ---

    # Section 1: População Total de Pessoas com Deficiência
    st.markdown('<h2 class="section-header">População de Pessoas com Deficiência (PCD)</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Total da População de PCD no Pará</div>
                <div class="kpi-value">{df_pcd_population['Value'].iloc[0]:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 ")
    with col2:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Representatividade na População Total</div>
                <div class="kpi-value">{df_pcd_population['Percentage'].iloc[0]}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 ")

    # Section 2: Saúde
    st.markdown('<h2 class="section-header">Saúde</h2>', unsafe_allow_html=True)

    col_health_pcd1, col_health_pcd2, col_health_pcd3 = st.columns(3)
    with col_health_pcd1:
        st.subheader("Acesso a Serviços de Saúde")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_pcd[df_health_pcd['Indicador'] == 'Acesso a serviços de saúde (últimos 12 meses)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNS 2019 ")
    with col_health_pcd2:
        st.subheader("Dificuldade de Acesso a Serviços de Saúde")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_pcd[df_health_pcd['Indicador'] == 'Dificuldade de acesso a serviços de saúde']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNS 2019 ")
    with col_health_pcd3:
        st.subheader("Reabilitação/Terapias (Necessidade e Recebimento)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_pcd[df_health_pcd['Indicador'] == 'Reabilitação/Terapias (Pessoas que necessitam e recebem)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: Pesquisa Saúde 2020 ")

    st.subheader("Prevalência de Condições Crônicas")
    df_chronic_conditions_pcd = df_health_pcd[df_health_pcd['Indicador'].str.contains('Prevalência de Condições Crônicas')]
    fig_chronic_conditions_pcd = px.bar(
        df_chronic_conditions_pcd,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Prevalência de Condições Crônicas em Pessoas com Deficiência',
        labels={'Indicador': 'Condição Crônica', 'Valor': 'Porcentagem (%)'},
        color='Indicador',
        height=500
    )
    fig_chronic_conditions_pcd.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_chronic_conditions_pcd.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_chronic_conditions_pcd, use_container_width=True)
    st.markdown("Fonte: PNS 2019 ")

    # Section 3: Educação
    st.markdown('<h2 class="section-header">Educação</h2>', unsafe_allow_html=True)

    col_edu_pcd1, col_edu_pcd2, col_edu_pcd3 = st.columns(3)
    with col_edu_pcd1:
        st.subheader("Taxa de Escolarização (6 a 17 anos)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_pcd[df_education_pcd['Indicador'] == 'Taxa de Escolarização (6 a 17 anos)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD 2022 ")
    with col_edu_pcd2:
        st.subheader("Inclusão em Escolas Regulares")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_pcd[df_education_pcd['Indicador'] == 'Inclusão em Escolas Regulares']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: INEP 2022 ")
    with col_edu_pcd3:
        st.subheader("Apoio Educacional Especializado (recebem)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_pcd[df_education_pcd['Indicador'] == 'Apoio Educacional Especializado (recebem)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: INEP 2022 ")

    col_edu_pcd4, col_edu_pcd5 = st.columns(2)
    with col_edu_pcd4:
        st.subheader("Taxa de Analfabetismo (15 anos ou mais)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_pcd[df_education_pcd['Indicador'] == 'Taxa de Analfabetismo (15 anos ou mais)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD 2022 ")
    with col_edu_pcd5:
        st.subheader("Conclusão do Ensino Médio (PCD 18+)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_pcd[df_education_pcd['Indicador'] == 'Conclusão do Ensino Médio (PCD 18+)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: INEP 2022 ")

    # Section 4: Inclusão no Mercado de Trabalho
    st.markdown('<h2 class="section-header">Inclusão no Mercado de Trabalho</h2>', unsafe_allow_html=True)

    col_work_pcd1, col_work_pcd2 = st.columns(2)
    with col_work_pcd1:
        st.subheader("Taxa de Ocupação (14 anos ou mais)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_work_pcd[df_work_pcd['Indicador'] == 'Taxa de Ocupação (14 anos ou mais)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD Contínua 2023 ")
    with col_work_pcd2:
        st.subheader("Salário Médio Mensal (PCD Ocupadas)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">R$ {df_work_pcd[df_work_pcd['Indicador'] == 'Salário Médio Mensal (PCD Ocupadas)']['Valor'].iloc[0]:,.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD Contínua 2023 ")

    col_work_pcd3, col_work_pcd4 = st.columns(2)
    with col_work_pcd3:
        st.subheader("Contratações via Lei de Cotas (2023)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_work_pcd[df_work_pcd['Indicador'] == 'Contratações via Lei de Cotas (2023)']['Valor'].iloc[0]:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: MTE 2023 ")
    with col_work_pcd4:
        st.subheader("Discriminação no Ambiente de Trabalho (relatos)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_work_pcd[df_work_pcd['Indicador'] == 'Discriminação no ambiente de trabalho (relatos)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: MPT 2023 ")

    # Section 5: Violência
    st.markdown('<h2 class="section-header">Violência</h2>', unsafe_allow_html=True)

    st.subheader("Total de Denúncias de Violência contra PCD no Pará (2023)")
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{df_violence_pcd_kpis['Valor'].iloc[0]:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("Fonte: Disque 100 2023 ")

    st.subheader("Tipos de Violência (principais denúncias)")
    fig_violence_types_pcd = px.bar(
        df_violence_pcd_types,
        x='Tipo de Violência',
        y='Valor',
        text='Valor',
        title='Principais Tipos de Violência contra Pessoas com Deficiência (Denúncias)',
        labels={'Tipo de Violência': 'Tipo', 'Valor': 'Porcentagem (%)'},
        color='Tipo de Violência',
        height=500
    )
    fig_violence_types_pcd.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_violence_types_pcd.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_violence_types_pcd, use_container_width=True)
    st.markdown("Fonte: Disque 100 2023 ")

    col_violence_pcd1, col_violence_pcd2 = st.columns(2)
    with col_violence_pcd1:
        st.subheader("Local de Ocorrência da Violência")
        fig_violence_location_pcd = px.pie(
            df_violence_pcd_location,
            values='Percentage',
            names='Local de Ocorrência',
            title='Local de Ocorrência da Violência contra PCD',
            height=400
        )
        st.plotly_chart(fig_violence_location_pcd, use_container_width=True)
        st.markdown("Fonte: Disque 100 2023 ")
    with col_violence_pcd2:
        st.subheader("Perfil do Agressor")
        fig_violence_aggressor_pcd = px.pie(
            df_violence_pcd_aggressor,
            values='Percentage',
            names='Perfil do Agressor',
            title='Perfil do Agressor em Denúncias de Violência contra PCD',
            height=400
        )
        st.plotly_chart(fig_violence_aggressor_pcd, use_container_width=True)
        st.markdown("Fonte: Disque 100 2023 ")


if __name__ == "__main__":
    app()