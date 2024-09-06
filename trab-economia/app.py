import streamlit as st

# Definir a configuração da página
st.set_page_config(page_title="Teoria dos Jogos para Oligopólios", layout="centered")

# Inicializar controle de estado para navegação
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# Função para trocar a página
def change_page(page_name):
    st.session_state['page'] = page_name

# Tela inicial
if st.session_state['page'] == 'home':
    st.title("Teoria dos Jogos para Oligopólios")
    st.write("Trabalho de Economia")
    st.write("Autores: ")
    
    # Botão para ir para o menu de modelos
    if st.button("Começar"):
        change_page('menu')

# Menu de seleção de modelos
elif st.session_state['page'] == 'menu':
    st.title("Escolha um Modelo para Explorar")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Modelo de Cournot"):
            change_page('cournot')
    with col2:
        if st.button("Modelo de Bertrand"):
            change_page('bertrand')
    with col3:
        if st.button("Modelo de Stackelberg"):
            change_page('stackelberg')
    with col4:
        if st.button("Comparação"):
            change_page('comparacao')

# Páginas dos modelos
elif st.session_state['page'] == 'cournot':
    import pages.cournot as cournot
    cournot.show()
elif st.session_state['page'] == 'bertrand':
    import pages.bertrand as bertrand
    bertrand.show()
elif st.session_state['page'] == 'stackelberg':
    import pages.stackelberg as stackelberg
    stackelberg.show()
elif st.session_state['page'] == 'comparacao':
    import pages.comparacao as comparacao
    comparacao.show()

# Rodapé com botão "Voltar"
if st.session_state['page'] != 'home':
    st.markdown("---")
    if st.button("Voltar ao Início"):
        change_page('home')