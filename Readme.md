# :paperclip: Anotações gerais sobre o uso do Git 

<img src = https://git-scm.com/images/logos/downloads/Git-Logo-2Color.png width = '300'>

## ⏬ Download:
Disponivel para:  
* :apple: [MacOS](https://git-scm.com/download/mac)
* :penguin: [Linux](https://git-scm.com/download/linux)
* :window: [Windows (32/64 bits)](https://git-scm.com/download/win)


## :hammer_and_wrench: Instruções de instalação - Windows

O processo de instalação no windows é bastante simples, segue o conceito next-next-finish.

### Primeiros comandos

Apos a instalção do git, abrir o pront de comando (CMD)

Verifique se a instalação foi bem sucedida

```
git --version
```
Deve retornar como resultado a versão do git instalado na maquina

Defina seu nome de usuario e email, atraves do comandos  

```
git config --global user.name "Seu nome"
```
* Escreva seu nome dentro das aspas

```
git config --glonal user.email seu_email@email.com
```
* O comando --global, serve para indicar que os dados informados devem ser usados como config padrão

Para verificar se os dados foram gravados com sucesso, utilize o comando
```
git config -l
ou
git config --list
```

## :file_folder: Criando repositorio

Um repositorio pode ser criado de duas formas

### Atraves da clonagem de um repositorio remoto, já existente e disponivel na internet

Crie uma pasta vazia em seu local de preferencia  

Abra o pront de comando
1. Dentro da pasta, clique com o botão direto do mouse e selecione a opção "Abrir no terminal"  
ou
2. Abra o Pront de comando e digite o comando:  
`cd caminho\da\pasta`  

Realize o clone do repositorio desejado, com o comando:  
`git clone https://linkDoRepositorio.com`  

:warning:Use o link Https do repositorio para realizar a clonagem

✅ Aguarde o download dos arquivos disponiveis no repositorio e esta pronto o seu repositorio 
   
### Apartir de uma pasta local do dispositivo

Crie uma pasta vazia no seu diretorio de preferencia

Abra o promt de comando, utilizando uma das duas formas citadas acima  

Digite o comando:  
`git init`

✅ Pronto, seu repositorio esta criado!  

## Gravando as mudanças em seu repositorio Git

O Git classifica os arquivos em quatro estagios  
* Untracked = Arquivo não monitorado, que ainda não foi registrado no Git
* Unmodified = arquivo monitorado e que não teve nenhuma modificação
* Modified = Arquivo que contem modificações e que ainda não foi atualizado no Git
* Staged = arquivo pronto para ser 'commitado' no Git

A movimentação de estagios se da das seguintes formas  
* Untracked -> Staged = Arquivo foi criado e esta pronto para ser adicionado ao Git
* Unmodified -> Modified = Quando um arquivo sofre alterações no seu conteudo
* Modified -> Staged = Arquivo foi modificado e esta pronto para ser 'commitado'
* Unmodified -> Untracked = Quando o arquivo é excluido
* Staged -> Unmodified = Todas as alterações foram 'commitadas' no Git