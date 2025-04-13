# Portal de Eventos

Bem-vindo ao **Portal de Eventos**, um projeto frontend desenvolvido para facilitar a criação, gerenciamento e participação em eventos. Este portal é intuitivo e responsivo, proporcionando uma experiência fluida aos usuários.

## 📋 Funcionalidades

- **Adicionar Evento**: Crie novos eventos com detalhes como nome, data, local e descrição.
- **Inscrever-se no Evento**: Permita que os usuários se inscrevam rapidamente nos eventos disponíveis.
- **Listar Todos os Eventos**: Exiba uma lista de todos os eventos criados.
- **Design Responsivo**: Desenvolvido com **Bootstrap**, garantindo uma interface amigável e responsiva.
---

## Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas, é bem simples o processo.

Após clonar o repositório, é necessário ir ao diretório raiz do projeto, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
