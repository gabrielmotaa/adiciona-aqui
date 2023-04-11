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