# Gerenciador de Favoritos em Python
Trata-se de um aplicativo desktop para gerenciamento de favoritos escrito em Python. Eu já tinha esse aplicativo escrito em Java. Eu escrevi este programa quando eu estava utilizando um computador antigo e lento no qual o navegador estava demorando para abrir a página inicial. Então pensei: consigo escrever uma aplicação que consegue o navegador diretamente no site que eu quero abrir, sem necessidade de abrir a página inicial? Pode haver soluções melhores, mas preferi aproveitar para testar minhas habilidades como programador.<br>

## Telas
* <b>Lista de Assuntos:</b> <br>
  * Mostra os assuntos salvos no banco de dados. <br>
  * Dá acesso à tela de correção do nome do assunto. <br>
  * Dá acesso à tela de listagem dos favoritos de determinado assunto. <br>
  * Dá acesso à tela de inclusão de um novo favorito. Se não houver nada salvo no banco de dados, O botão para este acesso é o único componente que vai aparecer na tela. <br>
* <b>Inclusão de Favorito:</b> <br>
  * Tem campo para digitação do nome e da URL. O assunto pode ser selecionado no campo de seleção ou digitado manualmente. <br>
* <b>Atualização de assunto:</b> <br>
  * Permite alteração do nome do assunto. <br>
* <b>Listagem de Favoritos:</b> <br>
  * Mostra os favoritos de determinado assunto salvos no banco de dados. <br>
  * Permite abrir o favorito no navegador de internet configurado como padrão no sistema operacional <br>
  * Permite exibir no navegador de internet uma pesquisa de um conteúdo digitado pelo usuário no site favorito. Basicamente, o botão com esta funcionalidade vai abrir o site da Google no navegador com a pesquisa: "<conteúdo a ser pesquisado> site:\<url-do-site-favorito\>". <br>
  * Dá acesso à tela de correção de dados do favorito. <br>
  * Dá acesso à tela de exclusão do favorito. <br>
* <b>Atualização de Favorito</b> <br>
  * É uma tela parecida com a de inclusão de favorito, mas aparecem os dados do favorito a ter dados corrigidos ou atualizados e não cria um favorito novo - só atualiza. <br>
* <b>Exclusão de Favorito:</b> <br>
  * Mostra os dados do favorito a ser excluído e pergunta se o usuário deseja mesmo a exclusão. <br>
* <b>Erro:</b> <br>
  * Aparece se qualquer erro ocorrer na execução do programa. Permite a listagem dos assuntos e tem um botão para encerramento do programa. </br>

## Tecnologias
Como esta é uma aplicação desktop com acesso a banco de dados. Precisei utilizar algumas tecnologias para confecção do meu programa:<br>
* <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/935px-Python-logo-notext.svg.png alt="Python" style="height: 32px; width: auto;"> <b>Python</b>: Linguagem de programação. <br><br>
* <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/935px-Python-logo-notext.svg.png alt="Tkinter" style="height: 32px; width: auto;"> <b>Tkinter</b>: Biblioteca padrão do Python para criação de interface gráfica. <br><br>
* <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/935px-Python-logo-notext.svg.png alt="Webbrowser" style="height: 32px; width: auto;"> <b>Webbrowser</b>: Biblioteca padrão do Python para controle do navegador web. <br><br>
* <img src=https://docs.peewee-orm.com/en/latest/_images/peewee3-logo.png alt="Peewee" style="height: 32px; width: auto;"> <b>Peewee</b>: ORM escrita em Python para conexão com banco de dados.<br><br>
* <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/1200px-SQLite370.svg.png alt="Sqlite" style="height: 32px; width: auto;"> <b>Sqlite</b>: SGBD relacional simples e que salva os dados dentro de um arquivo de extensão .db.