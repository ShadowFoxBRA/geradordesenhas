#importando tkinter
from tkinter import *
import random

#root e nome da janela
root=Tk()
root.title('Senha aleatória')

#caracteres a serem utilizados no random
dicionario=['a','b','c','d','e','f','g','h','i','j'
,'k','l','m','n','o','p','q','r','s','t','u','v','w'
,'x','y','z','0','1','2','3','4','5','6','7','8','9'
,'A','B','C','D','E','F','G','H','I','J','K','L','M'
,'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
,'!','@','#','$','%','&','*']

#definindo a senha aleatoriamente e com o tamanho definido pelo slider
def gerar():
	senha=random.choices(dicionario,k=slider.get())
	resultado.delete(0,END)
	resultado.insert(0,''.join(senha))
	
#TELA
tamanho = LabelFrame(root, text='Tamanho')
output=LabelFrame(root, text='Password')
botao=Button(root, text='Gerar senha', command=gerar)
#definindo tamanho do slider e da senha
slider=Scale(tamanho, from_=8, to=20, orient=HORIZONTAL)
resultado=Entry(output)

#Empacotando
tamanho.pack()
slider.pack()
botao.pack()
output.pack()
resultado.pack()

#Loop para execução
root.mainloop()