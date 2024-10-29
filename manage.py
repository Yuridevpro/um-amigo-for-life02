#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import execute_from_command_line
from django.db import connections

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adote.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Verificação da conexão com o banco de dados
    database = connections['default']
    if database is not None:
        print("Conexão com o banco de dados estabelecida.")
    else:
        print("Erro: Falha ao conectar ao banco de dados.") 

    # Executa os comandos do Django
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()