from imutils.video import VideoStream		# importado para captura de vídeo
from pyzbar import pyzbar					# importado para leitura de codigos de barra
import imutils								# módulo de processamento de imagem básico, utilizado para redimensionar o tamanho da saída da camera
import time									# tempo, usado para esperar 2 segundos para a lente da camera aquecer......
import cv2									# opencv, criação de linhas e textos no video
import mysql.connector						# importado para comunicação com o servidor sql
import tkinter								# importado para criaçao de uma rápida interface gráfica 
from tkinter import messagebox				# importado para mostrar caixas de mensangens

mydb = mysql.connector.connect(host="192.168.1.145",user="test",passwd="cerejinha123",database="cadastro")		# accesando o banco de dados
mycursor = mydb.cursor()
mycursor2=mydb.cursor()		# talvez n necessário, pois o alvo é o mesmo do de cima, mas funcionou

print("[INFO] Iniciando transmissão do video...")
vs = VideoStream(src=0).start()		# inicia a captura de frames de uma camera USB
#vs = VideoStream(usePiCamera=True).start() # quando estiver usando picamera
time.sleep(2.0)						# 2 segundos de parada para esquentar o sensor da camera, talvez n necessário...

while True:		# loopando
	frame = vs.read()								# pegando o frame da camera
	#frame = imutils.resize(frame, width=600)		# redimensionando a largura, funciona sem isso mas a janela terá a resolução nativa da camera...
	barcodes = pyzbar.decode(frame)					# acha os codigos nos frames e decodifica-os 

	for barcode in barcodes:			# loop nos códigos reconhecidos
		root = tkinter.Tk()				# criado para esconder janela do tkiner nas menssagebox
		root.withdraw()					# escondendo

		(x, y, w, h) = barcode.rect										# pegando as bordas do qr 
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)	# e desenhando em volta 
		
		barcodeData = barcode.data.decode("utf-8")	# o que foi lido é em bytes, transformando em texto
		barcodeType = barcode.type					# tipo do código reconhecido

		text = "{} ({})".format(barcodeData, barcodeType)	# transformando em uma string para ser mostrado

		#print(barcodeData) # esse é o que tem no qrcode

		cv2.putText(frame, text, (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)		# desenhando o código e o tipo dele na imagem 

#==================================== Analisando os dados obtidos ====================

		separar=barcodeData.split("\r\n")																# separando os dados lidos, é separado no \r\n de cada. exemplo TESTE3\r\n1\r\n1 ficará TESTE3,1,1 ---  rg=9 números ra=13 números
		print("Separando "+str(separar))																# mostrar no terminal como ficou a separação
		
		try:																							# tenta
			nome=separar[0]																				# pegar o nome da separação e também
			rg=str(separar[1])																			# rg
			ra=str(separar[2])																			# ra
			comando="select nome from pessoas where rg=md5('{}') and ra=md5('{}')".format(rg,ra)		# e prepará o envio da pergunta 'o rg e o ra estão no banco de dados?' e retorna o nome da pessoa ----- talvez vulnerável a sql injection

			mycursor.execute(comando)																	# executa a ação 
            
			myresult = mycursor.fetchall()																# terminado a execução do comando é necessário isso -- https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html

			if str(myresult) == "[]":																	# se o resultado do banco de dados estiver vazio significa que não foi encontrado------ talvez nao seguro....
				print("nao cadastrado, tentando cadastrar")												# mostra no terminal
				cadastrom=messagebox.askquestion(title="Cadastro", message="Usuário não encontrado, deseja iniciar cadastramento?")		# mostra uma janela de mensagem falando que o Usuário não está cadastrado e se deseja cadastrar
				if cadastrom=="yes":																									# se a resposta for sim
					def confirmar():																								# criando uma função confirmar para caso o botao 'confirmar' for pressionado
						print("confirmar")																							# mostra no terminal 'confirmar'
						cadastroc="insert into pessoas (nome, rg, ra) values ('{}', md5('{}'), md5('{}'))".format(nome,rg,ra)		# pega os dados de ra e ra lidos anteriormente e insere no banco de dados
						mycursor2.execute(cadastroc)																				# executando a ação 
						mydb.commit()																								# necessário para fazer as mudanças 
						
						messagebox.showinfo(title="Cadastro", message="Sucesso!")													# janela de mensagem escrito 'sucesso'
						cadastro.destroy()																							# destrói a janela cadastro

					def cancelar():																									# criando uma função cancelar para caso o botao 'cancelar' for pressionado			
						print("cancelar")																							# mostra no terminal 'cancelar'																					
						cadastro.destroy()																							# destrói a janela cadastro

#==================================== Interface de cadastro ====================

					root.destroy()																							# destruindo janela do mensagebox
					cadastro=tkinter.Tk()																					# crinando a janela de cadastro
					print("Usuário aceitou")																				# mostra no terminal que o usuário aceitou																		
					cadastro.title("Cadastro")																				# muda o titulo da janela para 'Cadastro'
					cadastro.geometry('800x400+1+1')																		# define o tamanho da janela em 800x400 pixels, +1 +1 é onde a janela irá aparecer.
					cadastro.configure(background='black')																	# fundo da janela na cor preto
					cadastro.overrideredirect(False)																		# "modo fullscreen"
					cadastro.resizable(0,0)																					# janela n pode ser redimensionada

					topo = tkinter.Frame (cadastro, width=800 , height=90 , bd=4 , relief ="groove")						# cria um frame chamado ""topo"" na janela ""cadastro"", com largura 800 e altura 90 pixels
					topo.place(x=0 , y=0)																					# posiciona ""topo"" em x=0 e y=0

					baixo = tkinter.Frame (cadastro, width=800 , height=310 , bd=4 , relief ="groove")						# cria um frame chamado ""baixo"" na janela ""cadastro"", com largura de 800 e altura de 310 pixels
					baixo.place(x=0 , y=90)																					# posiciona ""baixo"" em x=0 e y=90

					titulo= tkinter.Label(topo,font=('arial',32,'normal'),text="Cadastro",bd=8,width=30)					# cria uma label, tipo uma caixa de texto, chamada ""titulo"", no frame ""topo"", com o texto ''Cadastro'' e largura de 30 pixels
					titulo.place(x=0 , y=0)																					# posiciona ""titulo"" em x=0 e y=0

					info= tkinter.Label(baixo,font=('arial',16,'normal'),text="Informações",bd=8,width=30)					# cria uma label chamada ""info"", no frame ""baixo"", com o texto ''Informações'' e largura de 30 pixels
					info.place(x=0 , y=0)																					# posiciona ""info"" em x=0 e y=0
					
					nomel= tkinter.Label(baixo,font=('arial',16,'normal'),text=nome,bd=8,width=30)							# cria uma label chamada ""nomel"", no frame ""baixo"", com o texto da variável nome e largura de 30 pixels
					nomel.place(x=0 , y=50)																					# posiciona ""nomel"" em x=0 e y=50

					rgl= tkinter.Label(baixo,font=('arial',16,'normal'),text="RG={}".format(rg),bd=8,width=30)				# cria uma label chamada ""rg"", no frame ""baixo"", com o texto da variável rg e largura de 30 pixels
					rgl.place(x=0 , y=80)																					# posiciona ""rgl"" em x=0 e y=80

					ral= tkinter.Label(baixo,font=('arial',16,'normal'),text="RA={}".format(ra),bd=8,width=30)				# cria uma label chamada ""ra"", no frame ""baixo"", com o texto da variável ra e largura de 30 pixels
					ral.place(x=0 , y=110)																					# posiciona ""ral"" em x=0 e y=110

					confirmarb = tkinter.Button(baixo, width=20,height=3,bg="green",fg="black",text="Confirmar",command=confirmar)		# cria o botão confirmar, no frame 'baixo', com tamanho 20 pixels, altura 3 pixels, fundo verde, texto "Confirmar", e quando pressionado ativa a função ''confirmar''
					confirmarb.place(x=0, y=200)																						# coloca o botão nas cordenadas x=0 e y=200

					cancelarb = tkinter.Button(baixo, width=20,height=3,bg="red",fg="black",text="Cancelar",command=cancelar)			# cria o botão cancelar, no frame 'baixo', com tamanho 20 pixels, altura 3 pixels, fundo vermelho, texto "Cancelar", e quando pressionado ativa a função ''cancelar''
					cancelarb.place(x=400 , y=200)																						# coloca o botão nas cordenadas x=400 e y=200
					
					cadastro.mainloop()																									# loop da interface de cadastro

				else:									# usuário não aceitou a messagebox
					print("Usuário nao aceitou")		# mostra no terminal que a messagebox não foi aceita					
					root.destroy()						# destroi a messagebox								
                
			else:										# usuário foi encontrado no banco de dados
				print("usuario cadastrado")
				print("Bem Vindo {}".format(str(myresult).replace("[('","").replace("',)]","")))												# mostra no terminal a mensagem "Bem Vindo" + o nome do usuário formatado corretamente		
				messagebox.showinfo(title="Bem vindo", message="Bem Vindo {}".format(str(myresult).replace("[('","").replace("',)]","")))		# mostra uma menssagebox a mensagem "Bem Vindo" + o nome do usuário formatado corretamente
				root.destroy()																													# quando o usuário precionar ok messagebox é destruida


		except:																	# se o código qr não estiver no padrão da carteirinha da escola
			print("formato invalido")											# mostra no terminal que o formato é inválido
			messagebox.showinfo(title="Fomato", message="Formato invalido!")	# mostra uma mensagebox falando que o formato é inválido
			root.destroy()														# quando o usuário precionar ok a messagebox é destruida

	cv2.imshow("Barcode Scanner", frame)	# mostra a palavra 'barcode scanner' na tela de scanner do qr junto as outras informações
	key = cv2.waitKey(1) & 0xFF				# ??? usada para parar opencv https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1
 
	if key == ord("q"):						# se 'q' for pressionado
		break								# sair do loop

print("Saindo...")
cv2.destroyAllWindows()						# fechando as janelas criadas com o opencv
vs.stop()									# parando de receber frames
