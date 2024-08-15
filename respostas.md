# Docker
- ##### O que é Docker e quais são suas principais vantagens no desenvolvimento de aplicações web?
    Docker é uma plataforma para criação e execuçaõ de aplicações em containers. Vantagens: portabilidade, isolamento, escalabilidade e eficiência.
    
- ##### Explique a diferença entre um Dockerfile e um arquivo docker-compose.yml.
    *Dockerfile*: Define a configuração e os passos para construir uma imagem Docker.
    *docker-compose.yml*: Define e gerencia múltiplos containers e suas configurações em uma aplicação.
    
- ##### O que são volumes e networks no contexto do Docker e como eles são utilizados?
    *Volumes*: Persistem dados fora do container, úteis para armazenamento de dados persistentes.
    *Networks*: Permitem comunicação entre containers, criando redes isoladas para serviços.
    
- ##### Como você configuraria um serviço de banco de dados PostgreSQL utilizando Docker Compose?
    ```yaml
    services:
        prj-db:
            image: postgres:16
            container_name: prj-db
            hostname: prj-db
            environment:
              POSTGRES_USER: ${POSTGRES_USER:-postgres}
              POSTGRES_PASSWORD: ${POSTGRES_PWD:-postgres}
              POSTGRES_DB: ${DEFAULT_DATABASE:-sdb}
              PGDATA: /data/postgres
            restart: always
            env_file:
              - .env
            ports:
              - "${POSTGRES_PORT:-5432}:${POSTGRES_PORT:-5432}"
            volumes:
              - postgres:/data/postgres
              - ./sql:/docker-entrypoint-initdb.d
            networks:
              - prj-network
    volumes:
      postgres:
      ```
# SQLAlchemy e PostgreSQL

- ##### O que é SQLAlchemy e como ele facilita o mapeamento objeto-relacional (ORM)?
    SQLAlchemy é uma biblioteca ORM que mapeia classes Python para criação de tabelas de banco de dados, simplificando operações SQL com objetos.

- ##### Explique o uso de session em SQLAlchemy. Qual é o papel dela no contexto de uma aplicação web?
    A Session gerencia transações e operações de leitura e escrita com o banco de dados, garantindo a persistência e consistência dos dados.

- ##### O que são migrations no contexto do SQLAlchemy e por que elas são importantes?
    Migrations são alterações no esquema do banco de dados gerenciadas por ferramentas como Alembic, importantes para versionar e aplicar mudanças na estrutura do banco de dados.

- ##### Descreva a diferença entre uma relação one-to-many e many-to-many no contexto do SQLAlchemy. Dê exemplos de cada uma.
    **One-to-Many**: Uma entidade tem várias instâncias relacionadas a uma entidade, mas cada instância da segunda está associada a apenas uma da primeira. Exemplo: Post e Like.
    **Many-to-Many**: Várias instâncias de uma entidade podem estar associadas a várias instâncias de outra, usando uma tabela associativa. Exemplo: Compra e produto.

# Flask-Admin
- ##### O que é Flask-Admin e quais são seus principais usos em uma aplicação Flask?
    Flask-Admin é uma extensão para criar uma interface administrativa para gerenciar dados da aplicação.

- ##### Como você configuraria uma view administrativa para gerenciar uma entidade User utilizando Flask-Admin?

    ```python
    from flask_admin import Admin
    from flask_admin.contrib.sqla import ModelView
    
    def config_admin(app):
        admin = Admin(app, name='MyApp')
        admin.add_view(ModelView(User, db.session))
    ```
- ##### Quais são os benefícios de utilizar Flask-Admin em uma aplicação web?
    Rapidez na configuração, facilidade de uso e personalização da interface administrativa.

# Flask-Login e Autenticação

- ##### O que é Flask-Login e como ele auxilia na gestão de autenticação de usuários em uma aplicação Flask?
    Flask-Login facilita o gerenciamento de sessões e autenticação de usuários.

- ##### O que são tokens de autenticação e como eles podem ser utilizados para manter sessões seguras?
    Tokens de autenticação são strings seguras geradas para identificar e autenticar usuários, mantendo sessões seguras sem necessidade de reautenticação constante.

- ##### Explique o conceito de "decorators" em Flask e como eles são usados para proteger rotas.
    Decorators são funções que alteram o comportamento de outras funções ou métodos. Em Flask, são usados para proteger rotas, como @jwt_required para garantir que apenas usuários autenticados acessem uma rota.

# Flask-History
- ##### O que é Flask-History e quais são seus principais usos em uma aplicação Flask?
    Flask-History é uma extensão que rastreia alterações em dados e mantém um histórico das mudanças.

- ##### Como você configuraria o Flask-History para rastrear alterações em uma entidade Post?
    ```python
    from sqlalchemy_history import make_versioned
    from flaskr.plugin.flask_plugin import FlaskPlugin
    
    def config_versioning():
        make_versioned(plugins=[FlaskPlugin()])
    ```

- ##### Quais são os benefícios de manter um histórico de alterações em uma aplicação web?
    Permite rastrear mudanças, auditar dados e reverter alterações se necessário.

# Redis
- ##### O que é Redis e quais são suas principais vantagens em comparação com outros bancos de dados?
    Redis é um banco de dados em memória, chave-valor, conhecido por sua alta performance e suporte a estruturas de dados avançadas.

- ##### Explique como configurar o Redis para armazenamento de sessões em uma aplicação Flask.
    ```python
    from flask import request, make_response
    import flaskr.config_app as ca
    from functools import wraps
    from redis import Redis
    import hashlib
    
    redis_instance = Redis(host=ca.REDIS_HOST, port=ca.REDIS_PORT, password=ca.REDIS_PWD, decode_responses=True)
    
    def store_token_in_redis(token):
        key = hashlib.md5(token.encode()).hexdigest()
        redis_instance.set(key , token, ex=ca.REDIS_EXPIRATION_TIME)
        return key
    
    def get_token_from_redis(access_key):
        return redis_instance.get(access_key)
    
    def jwt_required():
        def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                auth_header = request.headers.get('Authorization')
                if not auth_header or not auth_header.startswith('Bearer '):
                    return make_response({"msg": "Missing or invalid Authorization header"}, 400)
    
                access_key = auth_header.split(" ")[1]
                if not access_key:
                    return make_response({"message": "Missing access key"}, 400)
    
                token = get_token_from_redis(access_key)
                if not token:
                    return make_response({"message": "Invalid access key"}, 401)
    
                return fn(*args, **kwargs)
            return wrapper
        return decorator
    ```
- ##### Como o uso de Redis pode melhorar a performance de uma aplicação web?
    Redis melhora a performance ao fornecer armazenamento rápido e em memória para dados temporários e caching.

- ##### O que são operações atômicas em Redis e como elas garantem a integridade dos dados?
    Operações atômicas em Redis garantem que comandos sejam executados sem interrupção, mantendo a integridade dos dados em cenários de alta concorrência.

# Desenvolvimento Web com Flask
- ##### Explique a arquitetura MVC (Model-View-Controller) e como ela é aplicada em uma aplicação Flask.
    MVC separa a aplicação em Model, View e Controller. Em Flask, o Model é representado pelos modelos SQLAlchemy, a View são as templates Jinja2, e o Controller são as rotas e funções de view.

- ##### Quais são as diferenças entre métodos HTTP (GET, POST, PUT, DELETE) e como eles são utilizados em rotas Flask?
    GET: Recupera as informações do servidor.
    POST: Salva as informações no servidor.
    PUT: Atualiza as informações do servidor.
    DELETE: Remove as informações do servidor.

- ##### Como você configuraria uma aplicação Flask para diferentes ambientes (desenvolvimento, teste, produção)?
    Usando variáveis de ambiente e assim configurando o projeto.

# Testes com Behave
- ##### O que é a biblioteca Behave e qual é sua utilidade em testes de software?
    Behave é uma biblioteca para testes BDD que permite escrever testes em linguagem mais humana, facilitando a colaboração entre desenvolvedores e stakeholders.
    
- ##### Explique a estrutura básica de um arquivo de feature no Behave.
    Um arquivo de feature descreve um comportamento do sistema em linguagem mais humana, com seções Feature, Scenario, e passos Given, When, Then.
    
- ##### Quais são os componentes principais de um cenário de teste em Behave (Given, When, Then)?
    Given: Configura o contexto inicial.
    When: Descreve a ação realizada.
    Then: Define o resultado esperado.