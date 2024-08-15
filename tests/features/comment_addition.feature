Feature: Adição de comentário
  Como um usuário autenticado
  Eu quero adicionar comentários nas postagens
  Para interagir com o conteúdo do blog

  Scenario: Usuário adiciona um comentário com sucesso
    Given que estou logado
    And que estou visualizando uma postagem
    When eu preen

cho "comment" com "Ótima postagem!"
    And eu clico em "Comentar"
    Then eu devo ver a mensagem "Comentário adicionado com sucesso"
    And eu devo ver o comentário "Ótima postagem!" na lista de comentários

  Scenario: Usuário tenta adicionar um comentário vazio
    Given que estou logado
    And que estou visualizando uma postagem
    When eu clico em "Comentar" sem preencher "comment"
    Then eu devo ver a mensagem "Comentário não pode ser vazio"