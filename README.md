# BOOK-API

API para criação de livros. Nela são mantidas informações de um livro criado, suas páginas e as ilustrações.

## Começando

## :heavy_check_mark: Pré-requisitos

- Docker (versão 20.10.6, build 370c289)
- Docker-compose (versão 1.21.2, build a133471)
- HTTP Client (Recomendação: Postman) - Utilizados para os testes
- Permissão para execução de comandos através do Makefile

> **⚠ WARNING**  
> Foram constatados problemas ao executar o projeto com algumas outras versões do docker-compose.

> Alguns comandos do Makefile utilizam recursos do linux, então leia com atenção as etapas pois pode ser sugerido uma etapa alternativa dependendo do sistema operacional.

## :arrow_forward: Execução

1 - Clone o projeto:

```
$ git clone https://github.com/geovanymds/book-api.git
```

2 - Abra o terminal dentro do diretório do projeto.

3 - Primeiro é preciso copiar as variáveis de ambiente do arquivo .env.example. Caso esteja utilizando o linux, pode utilizar o comando abaixo:

```
$ make copy
```

No windows a alternativa é copiar o conteúdo do arquivo original manualmente para o de destino.

4 - Na primeira inicialização utilize o seguinte comando no terminal:

```
$ make build
```

Nas próximas execuções é possível utilizar `$ make up` para iniciar o projeto ou `$ make stop` para parar o container. A aplicação pode demorar alguns segundos para iniciar, então aguarde a exibição da log 'INFO: Application startup complete.' no terminal.

5 - Para verificar se o servidor está sendo executado, abra o navegador e vá para o endereço <http://localhost:8000/>. A mensagem abaixo deverá ser exibida no navegador:
</br>
![Service up.](./docs/assets/images/service_up.png)

## :test_tube: Como usar

A documentação das rotas está disponível através do Swagger no link <http://localhost:8000/docs>. Para auxiliar ainda está disponível no diretório docs/collections a collection e as variáveis de ambiente para serem utilizadas no Postman. É recomendável utilizar este Cliente HTTP pois as chamadas já estão prontas, porém é possível também utilizar outro com as informações fornecidas pelo Swagger.

1 - Importe as collections no postman

2 - Importe as variáveis de ambiente

3 - Para realizar os testes será utilizado o seguinte fluxo:

**CRIAR LIVRO** -> **ADICIONAR PÁGINAS** -> **ADICIONAR IMAGENS** -> **RECUPERAR INFORMAÇÕES DO LIVRO**

> Esta é somente uma sugestão de testes, pois outros podem ser realizados pelo usuário.

4 - Crie um livro através da chamada **Create Book**. Todos os campos do corpo da requisição são obrigatórios. Ela retorna, dentre outras informações, o atributo **magic_code**. Ele será utilizado para recuperar informações do livro e adicioná-las também, então guarde-o.

5 - Execute a chamada **Attach page** para adicionar uma página ao livro. Note que o código mágico deve ser fornecido aqui, no corpo darequisição. É possível executá-la até 6 vezes para o mesmo livro, de forma que o número da página esteja entre 1 e 6, inclusive, não se repita em chamadas posteriores e o máximo de caracteres para o campo text são 1500.

6 - Execute a imagem **Attach image** para adicionar ilustrações ao livro. Ela recebe como parâmetro da rota atributo **magic_code** e também pode ser executada até 6 vezes para o mesmo livro e o corpo da requisição é do tipo form-data. São aceitos os formatos .png, .jpeg e .jpg.

![](./docs/assets/gifs/calls_example.gif)

Ainda é possível visualizar as imagens armazenadas com as urls fornecidas na última chamada.

7 - Para a execução de testes unitários, utilize o comando abaixo. Mas atenção, os containers precisam estar sendo executados:

```
$ make test
```

## :small_blue_diamond: :small_blue_diamond: :small_blue_diamond: Outros recursos

Durante a execução do docker-compose são instanciados dois serviços, o da api e o do banco de dados (Postgres).

:arrow_right: Acesso ao banco de dados:

```
$ make db
```

Aqui é solicitada a senha do banco e ela é encontrada nos arquivos .env e .env.example. Dentro do terminal do sgdb ainda é possível realizar consultas e alterações no banco e tabelas através de queries.

:arrow_right: Acesso ao container da api:

```
$ make api
```

Foi utilizado para instalação de dependências dentro do container.

:arrow_right: Atualização do requirements.txt:

```
$ make freeze
```

Ao entrar no container do banco é possível executar queries SQL além de alguns comandos úteis:

Sair do container:

```
$ \q
```

Exibir alguma tabela:

```
$ \dt {table_name}
```

Também foi criada uma rota para recuperação de todos os livros. Ela retorna somente o título e código mágico. Foi pensada para caso o usuário esqueça de guardar o código mágico.

## :hammer_and_wrench: Construído com

- [asyncpg](https://github.com/MagicStack/asyncpg) - Dependência comunicação com o SGDB
- [fastapi](https://github.com/tiangolo/fastapi) - Framework paraconstrução da api
- [pydantic](https://github.com/samuelcolvin/pydantic) - Validação das propriedades das requests
- [python-multipart](https://github.com/andrew-d/python-multipart) - Tratamento de requisições com body tipo form-data
- [tortoise-orm](https://github.com/tortoise/tortoise-orm) - ORM para mapeamento dos registros no banco para objetos
- [uvicorn](https://github.com/encode/uvicorn) - Instanciar servidor

## :small_orange_diamond: :small_orange_diamond: :small_orange_diamond: Próximos passos

- Implementação de testes
- Armazenar as imagens em um serviço em nuvem como o S3 ou Cloud Filestore por exemplo

## :pencil2: Decisões tomadas

Durante o processo de desenvolvimento me deparei com algumas escolhas que impactariam na solução. Foi optado pelo docker-compose para facilitar a configuração do ambiente da(s) pessoa(s) que ira(ão) rodar a aplicação, além de ser mais simples gerenciar os recursos necessários e padronizar as versões utilizadas. Para as tecnologias envolvidas na api optei pelas que já tinha algum conhecimento que poderiam facilitar o cumprimento de alguns requisitos do desafio. Já tinha conhecimento, por exemplo, que o FastAPI automatizava o desenvolvimento do Swagger. Para realizar o upload pensei em alguma solução simples e que fosse fácil de ser testada pelo avaliador, por isso a opção de utilizar um form-data, em detrimento de subir uma string base64 por exemplo. Ainda sobre o upload foi escolhido salvar os arquivos no servidor para (novamente) facilitar a configuração de ambiente, pois outra alternativa (mais adequada para o ambiente real) seria o upload em algum serviço na nuvem. Por fim, para gerar o código único foi utilizado uma função que sorteava 6 letras, porém ainda era verificado se o valor gerado já não existia no banco. A probabilidade de serem gerados dois ou mais códigos iguais é baixa, mas ainda foi feita essa validação para contornar a dificuldade em achar algum tipo de codificação que atendesse aos requisitos. Foram encontradas algumas dificuldades para implementar os testes, porém foi possível fazê-los para pelo menos dois serviços, livros e páginas. A dificuldade inicial foi em descobrir como contornar a comunicação com o banco, porém foi possível com uma bibliteca para mockar o retorno. Outro detalhe interessante durante o desenvolvimento foi o comportamento inicial dos containers: a api tentava se conectar ao banco mesmo antes do postgres estar pronto, então algumas logs de erros eram geradas. Como solução para isso foi adicionado um comando encontrado (por acaso) enquanto procurava como fazer os testes. Um último detalhe interessante é que o código mágico como parâmetro na rota de upload foi utilizada por uma feliz conveniência. Como não estava sendo possível usar o model do Pydantic junto com o form-data, utilizar o parâmetro permitiu que a rota não fosse acessada sem ele, suprindo a necessidade da validação pelo model.

## :fox_face: Curiosidades

- O limite de caracteres do campo texto das páginas foi escolhido utilizando uma página do livro O Pequeno Príncipe como base.
- ANOTANDO: Listas não têm a propriedade .length no Python.
