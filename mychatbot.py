import streamlit as st

from utils_openai import retorna_resposta_modelo
from utils_file import *

# CONFIGURAÇÃO DA PAGINA ==================================================
def config_pag():
        st.set_page_config(
                page_title='J.A.R.V.I.S',
                page_icon='🤖'
            )
config_pag()

st.sidebar.markdown("<h2 style='color: #A67C52;'>J.A.R.V.I.S 🤖</h2>", unsafe_allow_html=True)


# OCULTAR MENUS ==================================================
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# INICIALIZAÇÃO ==================================================

def inicializacao():
    if not 'mensagens' in st.session_state:
        st.session_state.mensagens = []
    if not 'conversa_atual' in st.session_state:
        st.session_state.conversa_atual = ''
    if not 'modelo' in st.session_state:
        st.session_state.modelo = 'gpt-3.5-turbo'
    if not 'api_key' in st.session_state:
        st.session_state.api_key = le_chave()


# TABS ==================================================

def pagina_principal():
    
    mensagens = ler_mensagens(st.session_state['mensagens'])

    st.header('🤖 J.A.R.V.I.S', divider=True)

    for mensagem in mensagens:
        chat = st.chat_message(mensagem['role'])
        chat.markdown(mensagem['content'])
    
    prompt = st.chat_input('Faça sua pergunta aqui: ')
    if prompt:
        if st.session_state['api_key'] == '':
            st.error('Adicione uma chave de api na aba de configurações')
        else:
            nova_mensagem = {'role': 'user',
                             'content': prompt}
            chat = st.chat_message(nova_mensagem['role'])
            chat.markdown(nova_mensagem['content'])
            mensagens.append(nova_mensagem)

            chat = st.chat_message('assistant')
            placeholder = chat.empty()
            placeholder.markdown("▌")
            resposta_completa = ''
            respostas = retorna_resposta_modelo(mensagens,
                                                st.session_state['api_key'],
                                                modelo=st.session_state['modelo'],
                                                stream=True)
            
            for resposta in respostas:
                # Verifica se 'content' está presente dentro de 'delta'
                if 'content' in resposta.choices[0].delta:
                    resposta_completa += resposta.choices[0].delta['content'] or ''
                placeholder.markdown(resposta_completa + "▌")
            placeholder.markdown(resposta_completa)
            nova_mensagem = {'role': 'assistant',
                             'content': resposta_completa}
            mensagens.append(nova_mensagem)

            st.session_state['mensagens'] = mensagens
            salvar_mensagens(mensagens)


# PÁGINAS ==================================================


def tab_conversas(tab):

    tab.button('➕ Nova conversa',
                on_click=seleciona_conversa,
                args=('', ),
                use_container_width=True)
    tab.markdown('')
    conversas = listar_conversas()
    for nome_arquivo in conversas:
        nome_mensagem = desconverte_nome_mensagem(nome_arquivo).capitalize()
        if len(nome_mensagem) == 30:
            nome_mensagem += '...'
        tab.button(nome_mensagem,
            on_click=seleciona_conversa,
            args=(nome_arquivo, ),
            disabled=nome_arquivo==st.session_state['conversa_atual'],
            use_container_width=True)

def seleciona_conversa(nome_arquivo):
    if nome_arquivo == '':
        st.session_state['mensagens'] = []
    else:
        mensagem = ler_mensagem_por_nome_arquivo(nome_arquivo)
        st.session_state['mensagens'] = mensagem
    st.session_state['conversa_atual'] = nome_arquivo

def tab_configuracoes(tab):
    modelo_escolhido = tab.selectbox('Selecione o modelo',
                                     ['gpt-3.5-turbo', 'gpt-4'])
    st.session_state['modelo'] = modelo_escolhido

    chave = tab.text_input('Adicione sua api key', value=st.session_state['api_key'])
    if chave != st.session_state['api_key']:
        st.session_state['api_key'] = chave
        salva_chave(chave)
        tab.success('Chave salva com sucesso')
        
        
    # MAIN ==================================================

def explicacao():
    st.sidebar.divider()
    st.sidebar.markdown("""
    ## Bem-vindo ao J.A.R.V.I.S! 🤖  

    Esta aplicação permite interações com modelos de IA da OpenAI, proporcionando respostas inteligentes e contextualizadas para suas perguntas.  

    Para utilizar o chatbot, basta inserir sua **chave da API da OpenAI** e selecionar o modelo desejado (**GPT-3.5-Turbo** ou **GPT-4**). O chatbot armazena o histórico das conversas, permitindo que você acesse e continue interações anteriores a qualquer momento.  

    ### 🔹 Como funciona?  
    ✅ **Insira sua chave da API** na aba de **Configurações**.  
    ✅ **Escolha entre os modelos** GPT-3.5-Turbo e GPT-4.  
    ✅ **Inicie a conversa** digitando sua pergunta no chat.  
    ✅ **Acesse a aba Conversas** para visualizar ou continuar diálogos anteriores.  
    """)
    st.sidebar.divider()
    st.sidebar.markdown("""
    **Desenvolvido por Leandro Souza**  
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/leandro-souza-bi/)
    [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lsouzadasilva/chatbot_streamlit_openai)
    """)



def main():
    inicializacao()
    pagina_principal()
    tab1, tab2 = st.sidebar.tabs(['Conversas', 'Configurações'])
    tab_conversas(tab1)
    tab_configuracoes(tab2)
    explicacao()



if __name__ == '__main__':
    main()
