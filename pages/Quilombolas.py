import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    st.set_page_config(layout="wide", page_title="População Quilombola no Pará")

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

    st.markdown('<h1 class="main-header">Indicadores da População Quilombola no Pará</h1>', unsafe_allow_html=True)
    st.write("Esta dashboard apresenta uma análise abrangente dos indicadores de saúde, educação, saneamento básico, trabalho e renda, e violência/conflitos territoriais que afetam a população quilombola no estado do Pará, baseada nos dados fornecidos.")

    # Data Extraction and Processing for Quilombolas.py

    # População Total Quilombola
    quilombola_population_data = {
        'Category': ['Total da População Quilombola no Pará'],
        'Value': [279799],
        'Percentage': ['3,44%']
    }
    df_quilombola_population = pd.DataFrame(quilombola_population_data)

    # Saúde
    health_quilombola_data = {
        'Indicador': [
            'Acesso a serviços de saúde (percepção de dificuldade)',
            'Cobertura Vacinal (todas as vacinas do calendário básico)',
            'Mortalidade Infantil (em comunidades quilombolas)',
            'Prevalência de Doenças Infecciosas (ex: malária, hanseníase)'
        ],
        'Valor': [65.2, 55.8, 25.7, 18.3],
        'Unidade': ['%', '%', 'por mil nascidos vivos', '%']
    }
    df_health_quilombola = pd.DataFrame(health_quilombola_data)

    # Educação
    education_quilombola_data = {
        'Indicador': [
            'Taxa de Analfabetismo (15 anos ou mais)',
            'Anos de Estudo (Média)',
            'Acesso à Escola (6 a 17 anos)',
            'Conclusão do Ensino Médio (18 a 24 anos)'
        ],
        'Valor': [28.9, 5.3, 78.1, 32.5],
        'Unidade': ['%', 'anos', '%', '%']
    }
    df_education_quilombola = pd.DataFrame(education_quilombola_data)

    # Saneamento Básico
    sanitation_quilombola_data = {
        'Indicador': [
            'Acesso à água potável (rede geral)',
            'Acesso a esgotamento sanitário (rede geral)',
            'Coleta de lixo regular'
        ],
        'Valor': [40.5, 15.2, 30.1],
        'Unidade': ['%', '%', '%']
    }
    df_sanitation_quilombola = pd.DataFrame(sanitation_quilombola_data)

    # Trabalho e Renda
    work_income_quilombola_data = {
        'Indicador': [
            'Taxa de Ocupação (14 anos ou mais)',
            'Rendimento Médio Mensal (Pessoas Ocupadas)'
        ],
        'Valor': [45.7, 890.00],
        'Unidade': ['%', 'R$']
    }
    df_work_income_quilombola = pd.DataFrame(work_income_quilombola_data)

    main_economic_activities = {
        'Atividade Econômica': [
            'Agricultura Familiar',
            'Extrativismo',
            'Artesanato/Turismo',
            'Outros'
        ],
        'Percentage': [70.3, 15.8, 8.5, 5.4]
    }
    df_main_economic_activities = pd.DataFrame(main_economic_activities)

    # Violência e Conflitos Territoriais
    violence_quilombola_data = {
        'Indicador': [
            'Total de Conflitos por Terra/Território (2023)',
            'Assassinatos (relacionados a conflitos por terra)'
        ],
        'Valor': [55, 12],
        'Unidade': ['números', 'números']
    }
    df_violence_quilombola_kpis = pd.DataFrame(violence_quilombola_data)

    violence_quilombola_types = {
        'Tipo de Conflito/Violência': [
            'Ameaças de morte (relatos)',
            'Agressão física (relatos)',
            'Invasão/Grilagem de Terras (relatos)'
        ],
        'Valor': [12.8, 8.1, 40.5]
    }
    df_violence_quilombola_types = pd.DataFrame(violence_quilombola_types)

    # --- Dashboard Layout and Visualizations ---

    # Section 1: População Total Quilombola
    st.markdown('<h2 class="section-header">População Quilombola</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Total da População Quilombola no Pará</div>
                <div class="kpi-value">{df_quilombola_population['Value'].iloc[0]:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022")
    with col2:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Representatividade na População Total</div>
                <div class="kpi-value">{df_quilombola_population['Percentage'].iloc[0]}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: IBGE 2022")

    # Section 2: Saúde
    st.markdown('<h2 class="section-header">Saúde</h2>', unsafe_allow_html=True)

    col_health_quilombola1, col_health_quilombola2 = st.columns(2)
    with col_health_quilombola1:
        st.subheader("Acesso a serviços de saúde (percepção de dificuldade)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_quilombola[df_health_quilombola['Indicador'] == 'Acesso a serviços de saúde (percepção de dificuldade)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: Pesquisa Quilombola (Fiocruz) 2021")
    with col_health_quilombola2:
        st.subheader("Cobertura Vacinal (todas as vacinas do calendário básico)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_quilombola[df_health_quilombola['Indicador'] == 'Cobertura Vacinal (todas as vacinas do calendário básico)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: Ministério da Saúde 2023")

    col_health_quilombola3, col_health_quilombola4 = st.columns(2)
    with col_health_quilombola3:
        st.subheader("Mortalidade Infantil (em comunidades quilombolas)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_quilombola[df_health_quilombola['Indicador'] == 'Mortalidade Infantil (em comunidades quilombolas)']['Valor'].iloc[0]}</div>
                <div class="kpi-title">por mil nascidos vivos</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: SESPA 2022")
    with col_health_quilombola4:
        st.subheader("Prevalência de Doenças Infecciosas")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_health_quilombola[df_health_quilombola['Indicador'] == 'Prevalência de Doenças Infecciosas (ex: malária, hanseníase)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: Fiocruz 2021")

    # Section 3: Educação
    st.markdown('<h2 class="section-header">Educação</h2>', unsafe_allow_html=True)

    col_edu_quilombola1, col_edu_quilombola2 = st.columns(2)
    with col_edu_quilombola1:
        st.subheader("Taxa de Analfabetismo (15 anos ou mais)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_quilombola[df_education_quilombola['Indicador'] == 'Taxa de Analfabetismo (15 anos ou mais)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD 2022")
    with col_edu_quilombola2:
        st.subheader("Anos de Estudo (Média)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_quilombola[df_education_quilombola['Indicador'] == 'Anos de Estudo (Média)']['Valor'].iloc[0]} anos</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD 2022")

    col_edu_quilombola3, col_edu_quilombola4 = st.columns(2)
    with col_edu_quilombola3:
        st.subheader("Acesso à Escola (6 a 17 anos)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_quilombola[df_education_quilombola['Indicador'] == 'Acesso à Escola (6 a 17 anos)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD 2022")
    with col_edu_quilombola4:
        st.subheader("Conclusão do Ensino Médio (18 a 24 anos)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_education_quilombola[df_education_quilombola['Indicador'] == 'Conclusão do Ensino Médio (18 a 24 anos)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD 2022")

    # Section 4: Saneamento Básico
    st.markdown('<h2 class="section-header">Saneamento Básico</h2>', unsafe_allow_html=True)
    st.subheader("Acesso a Serviços de Saneamento Básico")
    fig_sanitation_quilombola = px.bar(
        df_sanitation_quilombola,
        x='Indicador',
        y='Valor',
        text='Valor',
        title='Acesso a Serviços de Saneamento Básico em Comunidades Quilombolas',
        labels={'Indicador': 'Serviço', 'Valor': 'Porcentagem (%)'},
        color='Indicador',
        height=400
    )
    fig_sanitation_quilombola.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_sanitation_quilombola.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_sanitation_quilombola, use_container_width=True)
    st.markdown("Fonte: IBGE 2022")

    # Section 5: Trabalho e Renda
    st.markdown('<h2 class="section-header">Trabalho e Renda</h2>', unsafe_allow_html=True)

    col_work_quilombola1, col_work_quilombola2 = st.columns(2)
    with col_work_quilombola1:
        st.subheader("Taxa de Ocupação (14 anos ou mais)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_work_income_quilombola[df_work_income_quilombola['Indicador'] == 'Taxa de Ocupação (14 anos ou mais)']['Valor'].iloc[0]}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD Contínua 2023")
    with col_work_quilombola2:
        st.subheader("Rendimento Médio Mensal (Pessoas Ocupadas)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">R$ {df_work_income_quilombola[df_work_income_quilombola['Indicador'] == 'Rendimento Médio Mensal (Pessoas Ocupadas)']['Valor'].iloc[0]:,.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: PNAD Contínua 2023")

    st.subheader("Principais Atividades Econômicas")
    fig_economic_activities = px.pie(
        df_main_economic_activities,
        values='Percentage',
        names='Atividade Econômica',
        title='Principais Atividades Econômicas em Comunidades Quilombolas',
        height=500
    )
    st.plotly_chart(fig_economic_activities, use_container_width=True)
    st.markdown("Fonte: INCRA 2022")

    # Section 6: Violência e Conflitos Territoriais
    st.markdown('<h2 class="section-header">Violência e Conflitos Territoriais</h2>', unsafe_allow_html=True)

    col_violence_quilombola1, col_violence_quilombola2 = st.columns(2)
    with col_violence_quilombola1:
        st.subheader("Total de Conflitos por Terra/Território (2023)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_violence_quilombola_kpis[df_violence_quilombola_kpis['Indicador'] == 'Total de Conflitos por Terra/Território (2023)']['Valor'].iloc[0]}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: CPT 2023")
    with col_violence_quilombola2:
        st.subheader("Assassinatos (relacionados a conflitos por terra)")
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{df_violence_quilombola_kpis[df_violence_quilombola_kpis['Indicador'] == 'Assassinatos (relacionados a conflitos por terra)']['Valor'].iloc[0]}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("Fonte: CPT 2023")

    st.subheader("Tipos de Conflitos e Violência Relatados")
    fig_violence_types_quilombola = px.bar(
        df_violence_quilombola_types,
        x='Tipo de Conflito/Violência',
        y='Valor',
        text='Valor',
        title='Tipos de Conflitos e Violência Relatados em Comunidades Quilombolas',
        labels={'Tipo de Conflito/Violência': 'Tipo', 'Valor': 'Porcentagem (%)'},
        color='Tipo de Conflito/Violência',
        height=500
    )
    fig_violence_types_quilombola.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_violence_types_quilombola.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_violence_types_quilombola, use_container_width=True)
    st.markdown("Fonte: CPT 2023")


if __name__ == "__main__":
    app()