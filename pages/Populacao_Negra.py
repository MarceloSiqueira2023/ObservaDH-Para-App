import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    st.set_page_config(layout="wide", page_title="População Negra no Pará")

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

    st.markdown('<h1 class="main-header">Indicadores da População Negra no Pará</h1>', unsafe_allow_html=True)
    st.write("Esta dashboard apresenta uma análise abrangente dos indicadores de saúde, educação, trabalho e renda, e violência que afetam a população negra no estado do Pará, baseada nos dados fornecidos.")

    # Data Extraction and Processing for População Negra.py

    # População Total Negra
    black_population_data = {
        'Category': ['Total da População Negra no Pará'],
        'Value': [5761642],
        'Percentage': ['70,95%']
    }
    df_black_population = pd.DataFrame(black_population_data)

    # Saúde
    health_black_data = {
        'Indicador': [
            'Taxa de Mortalidade Materna (Mulheres Negras)',
            'Prevalência de Doenças Crônicas (Anemia Falciforme)',
            'Prevalência de Doenças Crônicas (Hipertensão Arterial)',
            'Prevalência de Doenças Crônicas (Diabetes)',
            'Acesso a serviços de saúde (Percepção de discriminação)'
        ],
        'Valor': [68.3, 8.5, 32.1, 15.4, 40.2],
        'Unidade': ['%', '%', '%', '%', '%']
    }
    df_health_black = pd.DataFrame(health_black_data)

    # Educação
    education_black_data = {
        'Indicador': [
            'Taxa de Analfabetismo (15 anos ou mais)',
            'Anos de Estudo (Média)',
            'Conclusão do Ensino Médio (18 a 24 anos)',
            'Acesso ao Ensino Superior (18 a 24 anos)'
        ],
        'Valor': [12.1, 8.5, 55.8, 20.3],
        'Unidade': ['%', 'anos', '%', '%']
    }
    df_education_black = pd.DataFrame(education_black_data)

    # Trabalho e Renda
    work_income_black_data = {
        'Indicador': [
            'Taxa de Desemprego (População Negra)',
            'Taxa de Informalidade no Trabalho (População Negra)',
            'Rendimento Médio Mensal (População Negra Ocupada)',
            'Rendimento Médio Mensal (População Branca Ocupada)',
            'Discriminação no ambiente de trabalho (relatos)'
        ],
        'Valor': [18.5, 65.3, 1300.00, 2100.00, 48.2],
        'Unidade': ['%', '%', 'R$', 'R$', '%']
    }
    df_work_income_black = pd.DataFrame(work_income_black_data)

    # Violência
    violence_black_homicide_rates = {
        'População': ['Negra', 'Branca'],
        'Taxa de Homicídios (por 100 mil hab.)': [35.6, 15.2]
    }
    df_violence_black_homicide_rates = pd.DataFrame(violence_black_homicide_rates)

    violence_black_denuncias = {
        'Indicador': ['Total de Denúncias de Racismo/Injúria Racial (2023)'],
        'Valor': [1250]
    }
    df_violence_black_denuncias = pd.DataFrame(violence_black_denuncias)

    violence_black_types = {
        'Tipo de Agressão/Discriminação': [
            'Agressão Física (relatos)',
            'Agressão Verbal/Moral (relatos)',
            'Discriminação no Comércio/Serviços (relatos)'
        ],
        'Valor': [28.7, 60.5, 35.1]
    }
    df_violence_black_types = pd.DataFrame(violence_black_types)


    # --- Dashboard Layout and Visualizations ---

    # Section 1: População Total Negra
    st.markdown('<h2 class="section-header">População Negra</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Total da População Negra no Pará </div>
                <div class="kpi-value">{df_black_population['Value'].iloc[0]:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 ")
    with col2:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Representatividade na População Total </div>
                <div class="kpi-value">{df_black_population['Percentage'].iloc[0]}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022 ")

    # Section 2: Saúde
    st.markdown('<h2 class="section-header">Saúde</h2>', unsafe_allow_html=True)

    col_health_black1, col_health_black2 = st.columns(2)
    with col_health_black1:
        st.subheader("Taxa de Mortalidade Materna (Mulheres Negras) ")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_black[df_health_black['Indicador'] == 'Taxa de Mortalidade Materna (Mulheres Negras)']['Valor'].iloc[0]}</div>
                <div class="kpi-title">por 100 mil nascidos vivos</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: Ministério da Saúde 2023 ")
    with col_health_black2:
        st.subheader("Acesso a serviços de saúde (Percepção de discriminação) ")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_black[df_health_black['Indicador'] == 'Acesso a serviços de saúde (Percepção de discriminação)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: Pesquisa Saúde 2020 ")

    st.subheader("Prevalência de Doenças Crônicas (População Negra) ")
    df_chronic_diseases_black = df_health_black[df_health_black['Indicador'].str.contains('Prevalência de Doenças Crônicas')]
    fig_chronic_diseases_black = px.bar(
        df_chronic_diseases_black,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Prevalência de Doenças Crônicas na População Negra',
        labels={'Indicador': 'Doença Crônica', 'Valor': 'Prevalência (%)'},
        color='Indicador',
        height=500
    )
    fig_chronic_diseases_black.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_chronic_diseases_black.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_chronic_diseases_black, use_container_width=True)
    st.markdown("Fonte: SISAB 2022 ")

    # Section 3: Educação
    st.markdown('<h2 class="section-header">Educação</h2>', unsafe_allow_html=True)

    col_edu_black1, col_edu_black2 = st.columns(2)
    with col_edu_black1:
        st.subheader("Taxa de Analfabetismo (15 anos ou mais) ")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_black[df_education_black['Indicador'] == 'Taxa de Analfabetismo (15 anos ou mais)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD 2022 ")
    with col_edu_black2:
        st.subheader("Anos de Estudo (Média) ")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_black[df_education_black['Indicador'] == 'Anos de Estudo (Média)']['Valor'].iloc[0]} anos</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD 2022 ")

    col_edu_black3, col_edu_black4 = st.columns(2)
    with col_edu_black3:
        st.subheader("Conclusão do Ensino Médio (18 a 24 anos) ")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_black[df_education_black['Indicador'] == 'Conclusão do Ensino Médio (18 a 24 anos)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD 2022 ")
    with col_edu_black4:
        st.subheader("Acesso ao Ensino Superior (18 a 24 anos) ")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_black[df_education_black['Indicador'] == 'Acesso ao Ensino Superior (18 a 24 anos)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD 2022 ")

    # Section 4: Trabalho e Renda
    st.markdown('<h2 class="section-header">Trabalho e Renda</h2>', unsafe_allow_html=True)

    st.subheader("Taxas de Desemprego e Informalidade (População Negra) ")
    df_work_rates_black = df_work_income_black[df_work_income_black['Indicador'].str.contains('Taxa de Desemprego|Taxa de Informalidade')]
    fig_work_rates_black = px.bar(
        df_work_rates_black,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Taxas de Desemprego e Informalidade da População Negra',
        labels={'Indicador': 'Tipo de Taxa', 'Valor': 'Porcentagem (%)'},
        color='Indicador',
        height=400
    )
    fig_work_rates_black.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_work_rates_black.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_work_rates_black, use_container_width=True)
    st.markdown("Fonte: PNAD Contínua 2023 ")

    st.subheader("Rendimento Médio Mensal Comparativo ")
    df_income_comparison = df_work_income_black[df_work_income_black['Indicador'].str.contains('Rendimento Médio Mensal')]
    fig_income_comparison = px.bar(
        df_income_comparison,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Rendimento Médio Mensal da População Negra vs. Branca Ocupada',
        labels={'Indicador': 'População', 'Valor': 'Rendimento (R$)'},
        color='Indicador',
        height=400
    )
    fig_income_comparison.update_traces(texttemplate='R$ %{text:,.2f}', textposition='outside')
    fig_income_comparison.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_income_comparison, use_container_width=True)
    st.markdown("Fonte: PNAD Contínua 2023 ")

    st.subheader("Discriminação no Ambiente de Trabalho (relatos) ")
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{df_work_income_black[df_work_income_black['Indicador'] == 'Discriminação no ambiente de trabalho (relatos)']['Valor'].iloc[0]}%</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("Fonte: MPT 2023 ")

    # Section 5: Violência
    st.markdown('<h2 class="section-header">Violência</h2>', unsafe_allow_html=True)

    st.subheader("Taxa de Homicídios por População ")
    fig_homicide_rates = px.bar(
        df_violence_black_homicide_rates,
        x='População',
        y='Taxa de Homicídios (por 100 mil hab.)',
        text='Taxa de Homicídios (por 100 mil hab.)',
        title='Taxa de Homicídios da População Negra vs. Branca (por 100 mil habitantes)',
        labels={'População': 'Grupo Racial', 'Taxa de Homicídios (por 100 mil hab.)': 'Taxa de Homicídios'},
        color='População',
        height=400
    )
    fig_homicide_rates.update_traces(texttemplate='%{text:.1f}', textposition='outside')
    st.plotly_chart(fig_homicide_rates, use_container_width=True)
    st.markdown("Fonte: Atlas da Violência 2023 ")

    st.subheader("Total de Denúncias de Racismo/Injúria Racial (2023) ")
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{df_violence_black_denuncias['Valor'].iloc[0]:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("Fonte: Ministério Público do Pará 2023 ")

    st.subheader("Tipos de Agressão e Discriminação Relatados ")
    fig_violence_types_black = px.bar(
        df_violence_black_types,
        x='Tipo de Agressão/Discriminação',
        y='Valor',
        text='Valor',
        title='Tipos de Agressão e Discriminação Relatados pela População Negra',
        labels={'Tipo de Agressão/Discriminação': 'Tipo', 'Valor': 'Porcentagem (%)'},
        color='Tipo de Agressão/Discriminação',
        height=500
    )
    fig_violence_types_black.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_violence_types_black.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_violence_types_black, use_container_width=True)
    st.markdown("Fonte: Pesquisa Percepção de Racismo 2021 ")

if __name__ == "__main__":
    app()