import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    st.set_page_config(layout="wide", page_title="LGBTQIAP+ no Pará")

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

    st.markdown('<h1 class="main-header">Indicadores LGBTQIAP+ no Pará</h1>', unsafe_allow_html=True)
    st.write("Esta dashboard apresenta uma análise abrangente dos indicadores sociais, de saúde, educação, trabalho e renda, e violência para a população LGBTQIAP+ no estado do Pará, baseada nos dados fornecidos.")

    # Data Extraction and Processing for LGBTQIAP+.py

    # População Total LGBTQIAP+
    lgbt_population_data = {
        'Category': ['Total da População LGBTQIAP+ no Pará'],
        'Value': [478431],
        'Percentage': ['5,89%']
    }
    df_lgbt_population = pd.DataFrame(lgbt_population_data)

    # Saúde
    health_lgbt_data = {
        'Indicador': [
            'Acesso a serviços de saúde',
            'Discriminação em serviços de saúde',
            'HIV/AIDS (Prevalência em homens gays e outros HSH)',
            'Adesão ao tratamento de HIV/AIDS',
            'Saúde Mental (Prevalência de Depressão/Ansiedade)',
            'Tentativas de Suicídio (LGBTQIAP+)',
            'Acesso a Hormonização (Mulheres Trans/Travestis)',
            'Acesso a Hormonização (Homens Trans)'
        ],
        'Valor': [45.7, 55.2, 18.4, 78.9, 35.1, 20.5, 15.3, 8.9],
        'Unidade': ['%', '%', '%', '%', '%', '%', '%', '%']
    }
    df_health_lgbt = pd.DataFrame(health_lgbt_data)

    # Educação
    education_lgbt_data = {
        'Indicador': [
            'Taxa de Escolarização (Lésbicas)',
            'Taxa de Escolarização (Gays)',
            'Taxa de Escolarização (Bissexuais)',
            'Taxa de Escolarização (Transgêneros)',
            'Taxa de Escolarização (Não Binários)',
            'Abandono Escolar devido à discriminação',
            'Conclusão do Ensino Médio'
        ],
        'Valor': [82.5, 78.9, 75.2, 45.1, 60.3, 30.5, 65.8],
        'Unidade': ['%', '%', '%', '%', '%', '%', '%']
    }
    df_education_lgbt = pd.DataFrame(education_lgbt_data)

    # Trabalho e Renda
    work_income_lgbt_data = {
        'Indicador': [
            'Taxa de Desemprego (LGBTQIAP+)',
            'Taxa de Informalidade no Trabalho (LGBTQIAP+)',
            'Rendimento Médio Mensal (LGBTQIAP+)',
            'Discriminação no Ambiente de Trabalho (relatos)'
        ],
        'Valor': [25.3, 68.7, 1550.00, 40.8],
        'Unidade': ['%', '%', 'R$', '%']
    }
    df_work_income_lgbt = pd.DataFrame(work_income_lgbt_data)

    # Violência (Letal e Não Letal)
    violence_lgbt_data = {
        'Indicador': [
            'Total de mortes violentas de LGBTQIAP+ no Pará (2023)',
            'Óbitos por Causa (Homicídio)',
            'Suicídio'
        ],
        'Valor': [52, 85.3, 14.7],
        'Unidade': ['números', '%', '%']
    }
    df_violence_lgbt_kpis = pd.DataFrame(violence_lgbt_data)

    violence_lgbt_non_lethal_types = {
        'Tipo de Violência': [
            'Verbal (Agressões Verbais/Ofensas)',
            'Física (Agressões Físicas)',
            'Psicológica (Ameaças/Constrangimento)'
        ],
        'Valor': [75.2, 45.1, 38.9]
    }
    df_violence_lgbt_non_lethal_types = pd.DataFrame(violence_lgbt_non_lethal_types)

    violence_lgbt_victim_type = {
        'Tipo de Vítima': [
            'Travestis/Mulheres Trans',
            'Homens Gays',
            'Lésbicas',
            'Homens Trans',
            'Bissexuais'
        ],
        'Percentage': [60.5, 25.1, 7.8, 3.2, 2.4]
    }
    df_violence_lgbt_victim_type = pd.DataFrame(violence_lgbt_victim_type)

    violence_lgbt_location = {
        'Local de Ocorrência': [
            'Via Pública',
            'Residência',
            'Ambiente de Lazer (Bares/Boates)'
        ],
        'Percentage': [55.2, 20.1, 15.3]
    }
    df_violence_lgbt_location = pd.DataFrame(violence_lgbt_location)

    # --- Dashboard Layout and Visualizations ---

    # Section 1: População Total
    st.markdown('<h2 class="section-header">População LGBTQIAP+</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Total da População LGBTQIAP+ no Pará</div>
                <div class="kpi-value">{df_lgbt_population['Value'].iloc[0]:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 ")
    with col2:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Representatividade na População Total</div>
                <div class="kpi-value">{df_lgbt_population['Percentage'].iloc[0]}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 ")

    # Section 2: Saúde
    st.markdown('<h2 class="section-header">Saúde</h2>', unsafe_allow_html=True)

    col_health_lgbt_kpi1, col_health_lgbt_kpi2, col_health_lgbt_kpi3 = st.columns(3)
    with col_health_lgbt_kpi1:
        st.subheader("Acesso a Serviços de Saúde")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_lgbt[df_health_lgbt['Indicador'] == 'Acesso a serviços de saúde']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: Pesquisa Diversidade 2020 ")
    with col_health_lgbt_kpi2:
        st.subheader("Discriminação em Serviços de Saúde")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_lgbt[df_health_lgbt['Indicador'] == 'Discriminação em serviços de saúde']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: Pesquisa Diversidade 2020 ")
    with col_health_lgbt_kpi3:
        st.subheader("Prevalência HIV/AIDS (HSH)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_lgbt[df_health_lgbt['Indicador'] == 'HIV/AIDS (Prevalência em homens gays e outros HSH)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: Ministério da Saúde 2023 ")

    col_health_lgbt_kpi4, col_health_lgbt_kpi5, col_health_lgbt_kpi6 = st.columns(3)
    with col_health_lgbt_kpi4:
        st.subheader("Adesão ao Tratamento HIV/AIDS")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_lgbt[df_health_lgbt['Indicador'] == 'Adesão ao tratamento de HIV/AIDS']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: Ministério da Saúde 2023 ")
    with col_health_lgbt_kpi5:
        st.subheader("Prevalência Depressão/Ansiedade")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_lgbt[df_health_lgbt['Indicador'] == 'Saúde Mental (Prevalência de Depressão/Ansiedade)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: Pesquisa Diversidade 2020 ")
    with col_health_lgbt_kpi6:
        st.subheader("Tentativas de Suicídio")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_lgbt[df_health_lgbt['Indicador'] == 'Tentativas de Suicídio (LGBTQIAP+)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: Pesquisa Diversidade 2020 ")

    st.subheader("Acesso à Hormonização")
    df_hormonization_access = df_health_lgbt[df_health_lgbt['Indicador'].str.contains('Hormonização')]
    fig_hormonization_access = px.bar(
        df_hormonization_access,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Acesso à Hormonização para Mulheres Trans/Travestis e Homens Trans',
        labels={'Indicador': 'Grupo', 'Valor': 'Porcentagem (%)'},
        color='Indicador',
        height=400
    )
    fig_hormonization_access.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_hormonization_access.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_hormonization_access, use_container_width=True)
    st.markdown("Fonte: DATASUS 2022 ")

    # Section 3: Educação
    st.markdown('<h2 class="section-header">Educação</h2>', unsafe_allow_html=True)

    st.subheader("Taxa de Escolarização (18 a 24 anos)")
    df_education_rate_lgbt = df_education_lgbt[df_education_lgbt['Indicador'].str.contains('Taxa de Escolarização')]
    fig_education_rate_lgbt = px.bar(
        df_education_rate_lgbt,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Taxa de Escolarização de LGBTQIAP+ por Identidade/Orientação (18 a 24 anos)',
        labels={'Indicador': 'Grupo', 'Valor': 'Porcentagem (%)'},
        color='Indicador',
        height=500
    )
    fig_education_rate_lgbt.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_education_rate_lgbt.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_education_rate_lgbt, use_container_width=True)
    st.markdown("Fonte: Pesquisa Escolar (IBGE) 2019, INEP 2022 ") # Combined sources assuming this refers to both schooling and completion

    col_edu_lgbt1, col_edu_lgbt2 = st.columns(2)
    with col_edu_lgbt1:
        st.subheader("Abandono Escolar por Discriminação")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_lgbt[df_education_lgbt['Indicador'] == 'Abandono Escolar devido à discriminação']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: Pesquisa Escolar (IBGE) 2019 ")
    with col_edu_lgbt2:
        st.subheader("Conclusão do Ensino Médio")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_lgbt[df_education_lgbt['Indicador'] == 'Conclusão do Ensino Médio']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: INEP 2022 ")

    # Section 4: Trabalho e Renda
    st.markdown('<h2 class="section-header">Trabalho e Renda</h2>', unsafe_allow_html=True)

    col_work_lgbt1, col_work_lgbt2 = st.columns(2)
    with col_work_lgbt1:
        st.subheader("Taxa de Desemprego (LGBTQIAP+)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_work_income_lgbt[df_work_income_lgbt['Indicador'] == 'Taxa de Desemprego (LGBTQIAP+)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 ")
    with col_work_lgbt2:
        st.subheader("Taxa de Informalidade no Trabalho (LGBTQIAP+)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_work_income_lgbt[df_work_income_lgbt['Indicador'] == 'Taxa de Informalidade no Trabalho (LGBTQIAP+)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 ")

    col_work_lgbt3, col_work_lgbt4 = st.columns(2)
    with col_work_lgbt3:
        st.subheader("Rendimento Médio Mensal (LGBTQIAP+)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">R$ {df_work_income_lgbt[df_work_income_lgbt['Indicador'] == 'Rendimento Médio Mensal (LGBTQIAP+)']['Valor'].iloc[0]:,.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 ")
    with col_work_lgbt4:
        st.subheader("Discriminação no Ambiente de Trabalho")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_work_income_lgbt[df_work_income_lgbt['Indicador'] == 'Discriminação no Ambiente de Trabalho (relatos)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: MPT 2023 ")

    # Section 5: Violência (Letal e Não Letal)
    st.markdown('<h2 class="section-header">Violência (Letal e Não Letal)</h2>', unsafe_allow_html=True)

    st.subheader("Total de Mortes Violentas de LGBTQIAP+ no Pará (2023)")
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{df_violence_lgbt_kpis[df_violence_lgbt_kpis['Indicador'] == 'Total de mortes violentas de LGBTQIAP+ no Pará (2023)']['Valor'].iloc[0]}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("Fonte: Grupo Gay da Bahia 2023 ")

    st.subheader("Tipos de Violência NÃO LETAL (relatos)")
    fig_non_lethal_lgbt = px.bar(
        df_violence_lgbt_non_lethal_types,
        x='Tipo de Violência',
        y='Valor',
        text='Valor',
        title='Prevalência dos Tipos de Violência Não Letal relatada por LGBTQIAP+',
        labels={'Tipo de Violência': 'Tipo', 'Valor': 'Porcentagem (%)'},
        color='Tipo de Violência',
        height=500
    )
    fig_non_lethal_lgbt.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig_non_lethal_lgbt.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_non_lethal_lgbt, use_container_width=True)
    st.markdown("Fonte: ANTRA 2023 ")

    col_violence_kpi_lethal1, col_violence_kpi_lethal2 = st.columns(2)
    with col_violence_kpi_lethal1:
        st.subheader("Óbitos por Causa (Homicídio)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_violence_lgbt_kpis[df_violence_lgbt_kpis['Indicador'] == 'Óbitos por Causa (Homicídio)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: SDS 2023 ")
    with col_violence_kpi_lethal2:
        st.subheader("Óbitos por Causa (Suicídio)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_violence_lgbt_kpis[df_violence_lgbt_kpis['Indicador'] == 'Suicídio']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: SDS 2023 ")

    st.subheader("Homicídios de LGBTQIAP+ por Tipo de Vítima")
    fig_victim_type = px.pie(
        df_violence_lgbt_victim_type,
        values='Percentage',
        names='Tipo de Vítima',
        title='Distribuição dos Homicídios de LGBTQIAP+ por Tipo de Vítima',
        height=500
    )
    st.plotly_chart(fig_victim_type, use_container_width=True)
    st.markdown("Fonte: ANTRA 2023 / Grupo Gay da Bahia 2023 ")

    st.subheader("Local de Ocorrência da Violência (relatos)")
    fig_violence_location = px.pie(
        df_violence_lgbt_location,
        values='Percentage',
        names='Local de Ocorrência',
        title='Local de Ocorrência da Violência contra LGBTQIAP+ (relatos)',
        height=500
    )
    st.plotly_chart(fig_violence_location, use_container_width=True)
    st.markdown("Fonte: ANTRA 2023 ")


if __name__ == "__main__":
    app()