##Ao iniciar um projeto novo utilizando esse codigo, instalar o seguinte pacote:
    ##pip3 install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
##Adicionar o credential.json

import os
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
import customtkinter as ctk
from tkinter import messagebox, filedialog
import pytz

# Configuração inicial do customtkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
thumbnail_path = None

# Helper: Obter nome do mês
def obter_nome_mes(mes):
    meses = [
        "JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO",
        "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"
    ]
    return meses[mes - 1]

# Helper: Converter data para formato ISO 8601
def converter_para_format_yt(data_hora_dd_mm_yyyy_hh_mm):
    data_hora = datetime.strptime(data_hora_dd_mm_yyyy_hh_mm, "%d-%m-%Y %H:%M")
    data_hora = pytz.utc.localize(data_hora)
    if data_hora < datetime.now(pytz.utc):
        data_hora += timedelta(minutes=15)
    return data_hora.isoformat()

# Gerar descrição da live
def descricao():
    descricao = """Bem vindo ao culto On Line CEIA CHURCH
    "Um Lugar Para Amar e Ser Amado"
    Através do nosso canal, temos a missão de "Evidenciar o Amor de Deus  a Todas as Pessoas", anunciar o evangelho, reunir pessoas que tem o propósito de adorar a Deus, de louvar a ELE e de ouvir a ministração de uma palavra para os corações aflitos e necessitados, transmitindo uma mensagem do Deus todo poderoso, para transformar vidas.

    Uma igreja cristã, que tem como missão "Evidenciar o Amor de Deus a Todas as Pessoas".
    Este canal   tem como objetivo levar a palavra de Deus, através do louvor e da adoração ao vivo.
    Alcançando almas que precisam ser abraçadas pelo Espirito Santo e sentir o grande amor de Deus. Por isso, mantemos 24h de louvor e adoração, e transmissão de nossos cultos todas as quintas-feiras, às 19:30​h, e todos os domingos, às 17h E 19h.
    Faça parte você também da nossa missão e se inscreva em nosso canal! Ative as notificações e compartilhe com seus amigos e familiares!
    Deus abençoe sua vida.

    Pastores Responsáveis:
    Pastor GILBERTO SERVO
    @CEIA TV / CEIA CHURCH CAMPINAS 


    Nos acompanhe nas rede sociais:
    Instagram: @CEIA TV / Campinas Canal CEIA church 
    Facebook: www.facebook.com.br/ceiachurch
    Site oficial: https://www.ceiachurch.com.br

    Entre em contato conosco:
    Pedido de oração: https://wa.me/5519981791596
    Precisa de visita: https://wa.me/5519981791596
             . ​

     Generosidade: CHAVE PIX  radiogospelcampinas@gmail.com

    Venha nos visitar:
    Rua VITÓRIO CHINÁGLIA 329 CAMPINAS-SP 
    Nossos cultos presenciais:
    Quinta feira as 19h30min
    Domingo: as 18:30



    A RÁDIO GOSPEL MAIS OUVIDA DO BRASIL NA INTERNET

    temos um compromisso com o reino de Deus, levando a pregação da palavra através do Pastor Gilberto Servo , o Pastor Gilberto Servo no programa bom dia com fé tem levado louvores e adoração e muita musica gospel. revelação da palavra e o desvendando os mistérios da Bíblia.


    *_Site Oficial_*
    https://www.radiogospelcampinas.com​

    *_Redes Sociais_*

    INSTAGRAM: https://www.instagram.com/radiogospel...
    FACEBOOK: https://www.facebook.com/radiogospelc...




    #OHgloria #ceiachurch #CULTOonline


    Observação: 
    **Direitos Autorais** 
    Eu não sou o autor dessa música. Todo material é de autoria e propriedade do seu respectivo dono(s).
    Srs. Cantores e Gravadoras, grande parte dos vídeos que divulgamos neste canal são autorizados por seus devidos proprietários. Se caso, exista algo em nosso canal que possam lhe causar algum dano ou prejuízo, peço que nos comunique para que possamos retirá-lo imediatamente!
    3 comentários
    COMPARTILHE NOSSO CULTO E SE INCREVA EM NOSSO CANAL

    #CeiaChurch
    #CultoAoVivo
    #PalavradeDeus
    #PastorMarcinho
    #Louvor
    #Adoração
    #Fé
    #Evangelho
    #JesusCristo
    #Cura
    #Milagre
    #Transformação
    #VidaComDeus
    #DeusÉFiel
    #Avivamento
    #Gospel
    #PregaçãoImpactante
    #Cristão
    #Igreja
    #PregaçãoTransformadora
    #JesusÉARespostas
    #RenovoEspiritual
    #MilagresHoje
    #FéQueMoveMontanhas
    #CoraçãoAlinhado
    #EspíritoSanto
    #PalavradeVida
    #OrandoJuntos
    #DeusNoControle
    #CeiaChurchAoVivo
    #DeusEstáAqui
    #TransformeSuaVida"""

    return descricao.strip()

# Gerar título da live
def gerar_titulo_live():
    hoje = datetime.now()
    nome_mes = obter_nome_mes(hoje.month)
    dia_semana = hoje.weekday()
    if dia_semana == 6:
        return f"DOMINGO NA CEIA 🔥 {hoje.day} DE {nome_mes} DE {hoje.year} 🔥"
    elif dia_semana == 3:
        return f"QUINTA NA CEIA 🔥 {hoje.day} DE {nome_mes} DE {hoje.year} 🔥"
    return f"TRANSMISSÃO AO VIVO 🔥 {hoje.day} DE {nome_mes} DE {hoje.year} 🔥"

# Upload de miniatura
def upload_thumbnail(youtube_service, broadcast_id, thumbnail_path):
    try:
        response = youtube_service.thumbnails().set(
            videoId=broadcast_id,
            media_body=MediaFileUpload(thumbnail_path, resumable=False)
        ).execute()
        return "Miniatura enviada com sucesso!"
    except HttpError as e:
        return f"Erro ao enviar miniatura: {e}"

# Selecionar imagem
def selecionar_imagem():
    global thumbnail_path
    file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.png")])
    if file_path:
        thumbnail_path = file_path
        thumbnail_label.configure(text=thumbnail_path)

# Autenticação com o YouTube
def autenticar_youtube():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)

# Criar transmissão
def criar_transmissao():
    try:
        youtube_service = autenticar_youtube()
        horario = entry_horario.get()
        if not horario:
            messagebox.showwarning("Aviso", "Por favor, insira um horário válido!")
            return

        horario_formatado = converter_para_format_yt(horario)
        request = youtube_service.liveBroadcasts().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": gerar_titulo_live(),
                    "description": descricao(),
                    "scheduledStartTime": horario_formatado,
                    "categoryId" : "10"
                },
                "status": {
                    "privacyStatus": "public"
                }
            }
        )
        response = request.execute()
        broadcast_id = response["id"]

        if thumbnail_path:
            resultado = upload_thumbnail(youtube_service, broadcast_id, thumbnail_path)
            messagebox.showinfo("Resultado do Upload", resultado)

        messagebox.showinfo("Sucesso", "Transmissão criada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao criar transmissão: {e}")

# Interface gráfica
app = ctk.CTk()
app.geometry("400x500")
app.title("Criador de Lives")

ctk.CTkLabel(app, text="Horário (DD-MM-YYYY HH:MM)").pack(pady=10)
entry_horario = ctk.CTkEntry(app)
entry_horario.pack(pady=5)

thumbnail_label = ctk.CTkLabel(app, text="Selecione uma miniatura")
thumbnail_label.pack(pady=5)

ctk.CTkButton(app, text="Selecionar Miniatura", command=selecionar_imagem).pack(pady=10)
ctk.CTkButton(app, text="Criar Transmissão", command=criar_transmissao).pack(pady=20)

app.mainloop()
