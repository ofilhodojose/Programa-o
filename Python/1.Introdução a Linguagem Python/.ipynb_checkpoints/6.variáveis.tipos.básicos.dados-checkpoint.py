nome = input("Digite seu nome: ")
print (nome)

#Modo 1 - usando formatadores de caracteres (igual na linguagem C) para imprimir variável e text
print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world!" % (nome))

#Modo 2 - usando a função format () para imprimir variável e texto
print ("Olá {}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world".format(nome))

#Modo 3 - usando strings formatadas
print (f"Olá {nome}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world")