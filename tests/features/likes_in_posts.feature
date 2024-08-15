Feature: Curtidas em postagem
  Como um usuário autenticado
  Eu quero curtir postagens
  Para expressar minha apreciação pelo conteúdo

  Scenario: Usuário curte uma postagem
    Given que estou logado
    And que estou visualizando uma postagem
    When eu clico em "Curtir"
    Then eu devo ver a mensagem "Você curtiu esta postagem"
    And o número de curtidas deve aumentar

  Scenario: Usuário remove a curtida de uma postagem
    Given que estou logado
    And que estou visualizando uma postagem que já curti
    When eu clico em "Descurtir"
    Then eu devo ver a mensagem "Você removeu a curtida desta postagem"
    And o número de curtidas deve diminuir