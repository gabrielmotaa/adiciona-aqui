# Adiciona Aqui
Projeto Integrador I - UNIVESP

## Descrição

Uma plataforma colaborativa onde usuários podem cadastrar novos comércios e serviços que ainda não tenham presença digital, para que os mesmos sejam inseridos posteriormente no Google Maps.

## Como rodar?

Se estiver no Windows:
```commandline
> python -m venv venv
> .\venv\Scripts\activate
(venv) > pip install -r .\requirements\base.txt
(venv) > python manage.py migrate
(venv) > python manage.py runserver
```

Se estiver no Linux:
```commandline
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements/base.txt
(venv) $ python manage.py migrate
(venv) $ python manage.py runserver
```

Se quiser acessar a área admin, deve criar um *superuser*, sendo necessário um e-mail e senha:
```commandline
(venv) $ python manage.py createsuperuser
```

Para popular o banco de dados com categorias:
```commandline
(venv) $ python manage.py populate_categories
```

## Desenvolvimento

Primeiramente, é necessário instalar as dependências de desenvolvimento:
```commandline
(venv) $ pip install -r requirements/dev.txt
```

O projeto usa tailwindcss, logo é preciso ter um processo rodando ao fazer modificações e também criar o build final ao terminar.

Comando em desenvolvimento:
```commandline
(venv) $ tailwindcss -o static/css/styles.css --watch
```

Para fazer o build final:
```commandline
(venv) $ tailwindcss -o static/css/styles.css --minify
```

Ao fazer mudanças no template, para garantir um padronização, é possível rodar o djhtml:
```commandline
(venv) $ djhtml templates/
```

### Tradução

Para criar os arquivos `.po`:
```commandline
(venv) $ ./manage.py makemessages --all -i venv
```

Assim que os arquivos `.po` estiverem preenchidos, para compilar os arquivos `.mo`:
```commandline
(venv) $ ./manage.py compilemessages -i venv
```
