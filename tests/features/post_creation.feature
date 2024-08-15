Feature: Criação de postagem
  Como um usuário autenticado
  Eu quero criar postagens no blog
  Para compartilhar meu conteúdo com outros usuários

  Scenario: Usuário cria uma postagem com dados válidos
    Given que estou logado
    And que estou na página de criação de postagens
    When eu preencho "title" com "Minha Primeira Postagem"
    And eu preencho "body" com "Este é o conteúdo da minha primeira postagem"
    And eu clico em "Publicar"
    Then eu devo ver a mensagem "Postagem criada com sucesso"
    And eu devo ver a postagem "Minha Primeira Postagem" na lista de postagens

  Scenario: Usuário tenta criar uma postagem sem título
    Given que estou logado
    And que estou na página de criação de postagens
    When eu preencho "body" com "Este é o conteúdo da minha postagem"
    And eu clico em "Publicar"
    Then eu devo ver a mensagem "Título é obrigatório"