Feature: Login de usuário
  Como um usuário registrado
  Eu quero fazer login no blog
  Para que eu possa acessar minhas funcionalidades restritas

  Scenario: Usuário faz login com credenciais válidas
    Given que estou na página de login
    When eu preencho "email" com "usuario@example.com"
    And eu preencho "password" com "senha_segura"
    And eu clico em "Login"
    Then eu devo ver a mensagem "Login realizado com sucesso"

  Scenario: Usuário faz login com credenciais inválidas
    Given que estou na página de login
    When eu preencho "email" com "usuario@example.com"
    And eu preencho "password" com "senha_incorreta"
    And eu clico em "Login"
    Then eu devo ver a mensagem "Email ou senha incorretos"