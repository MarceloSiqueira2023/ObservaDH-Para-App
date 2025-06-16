import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    st.set_page_config(layout="wide", page_title="Trabalho Análogo à Escravidão no Pará")

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

    st.markdown('<h1 class="main-header">Trabalhadores em Condições Análogas à Escravidão no Pará</h1>', unsafe_allow_html=True)
    st.write("Esta dashboard apresenta dados sobre trabalhadores resgatados de condições análogas à escravidão no estado do Pará, incluindo perfil das vítimas, setores de ocorrência e tipos de exploração, baseada nos dados fornecidos.")

    # Data Extraction and Processing for Escravidao_Analoga.py

    # Resgatados de Condições Análogas à Escravidão
    rescued_workers_data = {
        'Indicador': ['Total de Trabalhadores Resgatados (2023)'],
        'Valor': [532]
    }
    df_rescued_workers = pd.DataFrame(rescued_workers_data)

    # Perfil dos Trabalhadores Resgatados
    rescued_profile_sex = {'Category': ['Masculino', 'Feminino'], 'Percentage': [85.6, 14.4]}
    df_rescued_profile_sex = pd.DataFrame(rescued_profile_sex)

    rescued_profile_age = {'Category': ['18 a 29 anos', '30 a 59 anos', '60 anos ou mais'], 'Percentage': [30.1, 55.2, 14.7]}
    df_rescued_profile_age = pd.DataFrame(rescued_profile_age)

    rescued_profile_race = {'Category': ['Pardos', 'Negros', 'Brancos', 'Indígenas'], 'Percentage': [70.3, 15.8, 10.5, 3.4]}
    df_rescued_profile_race = pd.DataFrame(rescued_profile_race)

    rescued_profile_education = {
        'Escolaridade': [
            'Até o Ensino Fundamental Incompleto',
            'Ensino Fundamental Completo',
            'Ensino Médio Incompleto',
            'Ensino Médio Completo ou mais'
        ],
        'Percentage': [78.9, 12.1, 5.3, 3.7]
    }
    df_rescued_profile_education = pd.DataFrame(rescued_profile_education)

    # Setores Econômicos de Ocorrência
    economic_sectors_data = {
        'Setor': [
            'Pecuária',
            'Agricultura',
            'Extrativismo Vegetal',
            'Construção Civil',
            'Outros'
        ],
        'Percentage': [45.2, 28.7, 15.1, 7.5, 3.5]
    }
    df_economic_sectors = pd.DataFrame(economic_sectors_data)

    # Tipos de Exploração Encontrados
    exploitation_types_data = {
        'Tipo de Exploração': [
            'Jornada Exaustiva',
            'Condições Degradantes de Trabalho',
            'Dívida Forçada',
            'Cerco/Vigilância'
        ],
        'Percentage': [75.8, 60.3, 35.1, 20.5]
    }
    df_exploitation_types = pd.DataFrame(exploitation_types_data)

    # --- Dashboard Layout and Visualizations ---

    # Section 1: Total de Resgatados
    st.markdown('<h2 class="section-header">Resgatados de Condições Análogas à Escravidão</h2>', unsafe_allow_html=True)
    st.subheader("Total de Trabalhadores Resgatados no Pará (2023)")
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{df_rescued_workers['Valor'].iloc[0]}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("Fonte: MPT 2023")

    # Section 2: Perfil dos Trabalhadores Resgatados
    st.markdown('<h2 class="section-header">Perfil dos Trabalhadores Resgatados (2023)</h2>', unsafe_allow_html=True)

    col_profile1, col_profile2, col_profile3 = st.columns(3)
    with col_profile1:
        st.subheader("Por Sexo")
        fig_profile_sex = px.pie(df_rescued_profile_sex, values='Percentage', names='Category', title='Sexo')
        st.plotly_chart(fig_profile_sex, use_container_width=True)
    with col_profile2:
        st.subheader("Por Faixa Etária")
        fig_profile_age = px.pie(df_rescued_profile_age, values='Percentage', names='Category', title='Faixa Etária')
        st.plotly_chart(fig_profile_age, use_container_width=True)
    with col_profile3:
        st.subheader("Por Raça/Cor")
        fig_profile_race = px.pie(df_rescued_profile_race, values='Percentage', names='Category', title='Raça/Cor')
        st.plotly_chart(fig_profile_race, use_container_width=True)
    st.markdown("Fonte: MPT 2023 / OIT 2023")

    st.subheader("Por Escolaridade")
    fig_profile_education = px.bar(
        df_rescued_profile_education,
        x='Escolaridade',
        y='Percentage',
        text='Percentage',
        title='Escolaridade dos Trabalhadores Resgatados',
        labels={'Escolaridade': 'Nível de Escolaridade', 'Percentage': 'Porcentagem (%)'},
        color='Escolaridade',
        height=500
    )
    fig_profile_education.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_profile_education.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_profile_education, use_container_width=True)
    st.markdown("Fonte: MPT 2023 / OIT 2023")

    # Section 3: Setores Econômicos de Ocorrência
    st.markdown('<h2 class="section-header">Setores Econômicos de Ocorrência (2023)</h2>', unsafe_allow_html=True)
    st.subheader("Distribuição por Setor")
    fig_economic_sectors = px.pie(
        df_economic_sectors,
        values='Percentage',
        names='Setor',
        title='Setores Econômicos de Ocorrência da Escravidão Análoga',
        height=500
    )
    st.plotly_chart(fig_economic_sectors, use_container_width=True)
    st.markdown("Fonte: MPT 2023")

    # Section 4: Tipos de Exploração Encontrados
    st.markdown('<h2 class="section-header">Tipos de Exploração Encontrados (2023)</h2>', unsafe_allow_html=True)
    st.subheader("Prevalência dos Tipos de Exploração")
    fig_exploitation_types = px.bar(
        df_exploitation_types,
        x='Tipo de Exploração',
        y='Percentage',
        text='Percentage',
        title='Tipos de Exploração Mais Comuns',
        labels={'Tipo de Exploração': 'Tipo', 'Percentage': 'Porcentagem (%)'},
        color='Tipo de Exploração',
        height=500
    )
    fig_exploitation_types.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_exploitation_types.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_exploitation_types, use_container_width=True)
    st.markdown("Fonte: MPT 2023")

if __name__ == "__main__":
    app()