import streamlit as st

def main_page_content():
    st.set_page_config(layout="wide", page_title="ObservaDH-Pará") # Configuração da página inicial

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
            /* Estilo para a barra lateral automática do Streamlit */
            .sidebar .sidebar-content {
                background-color: #f0f8ff; /* Cor de fundo para combinar com os KPI cards */
            }
            .st-emotion-cache-1rxv3a6 { /* Esta classe pode variar, é para o container da sidebar */
                background-color: #f0f8ff; /* Cor de fundo para a sidebar */
                border-right: 1px solid #4682B4;
            }
            /* O Streamlit gerencia os estilos dos links de navegação automaticamente */
            /* Se precisar de mais personalização para os links da sidebar, seria via .streamlit/config.toml ou JS */
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 6, 1]) # Ajuste os pesos das colunas conforme necessário

    with col2:
        st.image("logo_ObservaDHPA.png", width=1000) # Logo do ObservaDH-Pará
    
    #st.image("logo_ObservaDHPA.png", width=1200)  # Logo do ObservaDH-Pará

    st.markdown('<h1 class="main-header">Bem-vindos(as) ao ObservaDH-Pará: Indicadores Sociais e de Direitos Humanos</h1>', unsafe_allow_html=True)

    st.markdown("""
        <p style='font-size: 1.1em; line-height: 1.6;'>
            Este dashboard interativo foi desenvolvido para oferecer uma visão abrangente sobre a situação social e os desafios relacionados aos Direitos Humanos de diversos grupos populacionais no estado do Pará.
            Aqui, você encontrará dados cruciais sobre:
        </p>
        <ul>
            <li><b>Crianças e Adolescentes:</b> Indicadores de saúde, educação, inclusão digital, trabalho e violência.</li>
            <li><b>Idosos:</b> Dados sobre esperança de vida, saúde, educação, inclusão digital, trabalho e renda, e violência.</li>
            <li><b>LGBTQIAP+:</b> Informações sobre saúde, educação, trabalho e renda, e diferentes formas de violência.</li>
            <li><b>Pessoas com Deficiência (PCD):</b> Análise de saúde, educação, inclusão no mercado de trabalho e violência.</li>
            <li><b>População Negra:</b> Indicadores de saúde, educação, trabalho e renda, e violência, com foco nas desigualdades.</li>
            <li><b>População Quilombola:</b> Dados sobre saúde, educação, saneamento básico, trabalho e renda, e conflitos territoriais.</li>
            <li><b>Trabalhadores em Condições Análogas à Escravidão:</b> Detalhes sobre o perfil dos resgatados, setores econômicos e tipos de exploração.</li>
        </ul>
        <p style='font-size: 1.1em; line-height: 1.6;'>
            Os dados apresentados são provenientes de fontes oficiais e reconhecidas, como IBGE, PNAD, SISAB, DATASUS, MPT, CPT, SDS, INEP, entre outras.
            É fundamental compreender que estes dados representam recortes da realidade e são essenciais para a formulação de políticas públicas mais eficazes e para a promoção da justiça social no Pará.
        </p>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Como Navegar:")
    st.write("Utilize a barra lateral esquerda para escolher o grupo populacional que deseja analisar. Cada seleção o levará a uma página dedicada com gráficos e informações específicas.")
    st.info("Explore os dados e contribua para um Pará mais equitativo e justo.")


def main():
    # Streamlit automaticamente detecta os arquivos na pasta 'pages'
    # e cria a navegação na barra lateral. O 'main_app.py' será a página inicial.
    # Não é necessário importar as páginas aqui nem usar st.sidebar.selectbox/radio.
    
    main_page_content()

if __name__ == "__main__":
    main()