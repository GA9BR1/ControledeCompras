import MySQLdb
from time import sleep
from prettytable import PrettyTable
from datetime import datetime


def conectar():
    """
    Função para conectar ao servidor
    """
    print('Conectando ao servidor...')
    try:
        conn = MySQLdb.connect(
            db='mydb',
            host='158.69.149.41',
            user='GA9',
            passwd='senha'
        )
        print('Conexão bem sucedida!')
        return conn
    except MySQLdb.Error as e:
        print(f'Erro na conexão ao MySQL Server: {e}')


def desconectar(conn):
    """
    Função para desconectar do servidor.
    """
    print('Desconectando do servidor...')
    if conn:
        conn.close()


def listarcompras():  # Lista todas as compras conjunta, inteiras.
    """
    Função para listar os produtos
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id, DATE_FORMAT(data, '%d/%m/%Y') AS 'Data da Compra' FROM compras;")
    compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta
    x = PrettyTable()
    x.field_names = ["Codigo da compra", "Data da compra"]
    x.align["Código da compra"] = "1"
    x.align["Data da compra"] = "1"
    x.padding_width = 1
    x.align = "c"
    if len(compras) > 0:
        print('Listando compras...')
        sleep(0.5)
        for compra in compras:
            x.add_row([compra[0], compra[1]])
        print(f'{x.get_string()}')
        escolha = str(input('Deseja listar alguma compra em específico [S/N]? '))
        if escolha in 'Ss':
            cod = int(input('Digite o Código da compra que você deseja listar: '))
            cursor.execute(f"""SELECT i.id, i.id_compra, DATE_FORMAT(c.data, '%d/%m/%Y') ,i.nome, i.descricao,
            f.nome AS fornecedor, e.nome AS empresa, i.preco AS Valor_Unitário, i.quantidade AS Quantidade ,
            SUM(i.preco * i.quantidade) AS Valor_Total
            FROM itens_compra AS i, fornecedores AS f, empresas AS e, compras AS c 
            WHERE i.id_fornecedor = f.id 
            AND i.id_empresa = e.id
            AND i.id_compra = c.id AND c.id = {cod}
            GROUP BY i.id;""")
            compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta!
            x = PrettyTable()
            x.field_names = ['CC', 'CCI', 'Data', 'Nome do produto', 'Descrição',
                             'Fornecedor',
                             'Empresa', 'Valor unitário', 'Quantidade', 'Valor total']
            print('Listando compras...')
            sleep(0.5)
            for compra in compras:
                x.add_row([compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6], compra[7],
                           compra[8], compra[9]])
            print(x)

    else:
        print('Não existem produtos cadastrados')


def listartodas():  # Lista Todas as compras individualmente.
    """
    Função para listar os produtos
    """
    cursor = conn.cursor()
    cursor.execute("""SELECT i.id, i.id_compra, DATE_FORMAT(c.data, '%d/%m/%Y') ,i.nome, i.descricao,
f.nome AS fornecedor, e.nome AS empresa, i.preco AS Valor_Unitário, i.quantidade AS Quantidade ,
SUM(i.preco * i.quantidade) AS Valor_Total
FROM itens_compra AS i, fornecedores AS f, empresas AS e, compras AS c 
WHERE i.id_fornecedor = f.id 
AND i.id_empresa = e.id
AND i.id_compra = c.id GROUP BY i.id;""")
    compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta
    x = PrettyTable()
    x.field_names = ['CC', 'CCI', 'Data', 'Nome do produto', 'Descrição',
                     'Fornecedor',
                     'Empresa', 'Valor unitário', 'Quantidade', 'Valor total']
    if len(compras) > 0:
        print('Listando compras...')
        sleep(0.5)
        for compra in compras:
            x.add_row([compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6], compra[7],
                       compra[8], compra[9]])
        print(x)
    else:
        print('Não existem produtos cadastrados')


def listarespecid(cod):  # Lista uma compra específica.
    """
    Função para listar os produtos
    """
    cursor = conn.cursor()
    cursor.execute(f"""SELECT i.id, i.id_compra, DATE_FORMAT(c.data, '%d/%m/%Y') ,i.nome, i.descricao,
f.nome AS fornecedor, e.nome AS empresa, i.preco AS Valor_Unitário, i.quantidade AS Quantidade ,
SUM(i.preco * i.quantidade) AS Valor_Total
FROM itens_compra AS i, fornecedores AS f, empresas AS e, compras AS c 
WHERE i.id_fornecedor = f.id 
AND i.id_empresa = e.id
AND i.id_compra = c.id AND c.id = {cod}
GROUP BY i.id;""")
    compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta!
    x = PrettyTable()
    x.field_names = ['CC', 'CCI', 'Data', 'Nome do produto', 'Descrição',
                     'Fornecedor',
                     'Empresa', 'Valor unitário', 'Quantidade', 'Valor total']
    if len(compras) > 0:
        print('Listando compras...')
        sleep(0.5)
        for compra in compras:
            x.add_row([compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6], compra[7],
                       compra[8], compra[9]])
        print(x)
    else:
        print('Não existem produtos cadastrados')


def listarvalorprod(cod, valor):  # Lista uma compra pelo valor.
    """
    Função para listar os produtos
    """
    cursor = conn.cursor()
    if cod == 1:
        cursor.execute(f"""SELECT i.id, i.id_compra, DATE_FORMAT(c.data, '%d/%m/%Y') ,i.nome, i.descricao,
        f.nome AS fornecedor, e.nome AS empresa, i.preco AS Valor_Unitário, i.quantidade AS Quantidade ,
        SUM(i.preco * i.quantidade) AS Valor_Total
        FROM itens_compra AS i, fornecedores AS f, empresas AS e, compras AS c 
        WHERE i.id_fornecedor = f.id 
        AND i.id_empresa = e.id
        AND i.id_compra = c.id
        AND i.preco >= {valor}
        GROUP BY i.id;""")
        compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta!
        x = PrettyTable()
        x.field_names = ['CC', 'CCI', 'Data', 'Nome do produto', 'Descrição',
                         'Fornecedor',
                         'Empresa', 'Valor unitário', 'Quantidade', 'Valor total']
        if len(compras) > 0:
            print('Listando compras...')
            sleep(0.5)
            for compra in compras:
                x.add_row([compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6], compra[7],
                           compra[8], compra[9]])
            print(x)
        else:
            print('Não existem produtos cadastrados')
    if cod == 2:
        cursor.execute(f"""SELECT i.id, i.id_compra, DATE_FORMAT(c.data, '%d/%m/%Y') ,i.nome, i.descricao,
        f.nome AS fornecedor, e.nome AS empresa, i.preco AS Valor_Unitário, i.quantidade AS Quantidade ,
        SUM(i.preco * i.quantidade) AS Valor_Total
        FROM itens_compra AS i, fornecedores AS f, empresas AS e, compras AS c 
        WHERE i.id_fornecedor = f.id 
        AND i.id_empresa = e.id
        AND i.id_compra = c.id
        AND i.preco <= {valor}
        GROUP BY i.id;""")
        compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta!
        x = PrettyTable()
        x.field_names = ['CC', 'CCI', 'Data', 'Nome do produto', 'Descrição',
                         'Fornecedor',
                         'Empresa', 'Valor unitário', 'Quantidade', 'Valor total']
        if len(compras) > 0:
            print('Listando compras...')
            sleep(0.5)
            for compra in compras:
                x.add_row([compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6], compra[7],
                           compra[8], compra[9]])
            print(x)
        else:
            print('Não existem produtos cadastrados')


def listardataespec(data):  # Lista uma compras de uma data específica.
    cursor = conn.cursor()
    cursor.execute(f"""SELECT id, DATE_FORMAT(data, '%d/%m/%Y') AS 'Data da Compra' FROM compras
                   WHERE data = '{data}';""")
    compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta
    x = PrettyTable()
    x.field_names = ["Codigo da compra", "Data da compra"]
    x.align["Código da compra"] = "1"
    x.align["Data da compra"] = "1"
    x.padding_width = 1
    x.align = "c"
    if len(compras) > 0:
        print('Listando compras...')
        sleep(0.5)
        for compra in compras:
            x.add_row([compra[0], compra[1]])
        print(f'{x.get_string()}')
        decisao = str(input('Deseja listar a compra pelo código[S/N]: ')).strip()[0]

        if decisao in 'Ss':
            decisao2 = int(input('Digite o código da compra que deseja listar: '))
            cursor.execute(f"""SELECT i.id, i.id_compra, DATE_FORMAT(c.data, '%d/%m/%Y') ,i.nome, i.descricao,
            f.nome AS fornecedor, e.nome AS empresa, i.preco AS Valor_Unitário, i.quantidade AS Quantidade ,
            SUM(i.preco * i.quantidade) AS Valor_Total
            FROM itens_compra AS i, fornecedores AS f, empresas AS e, compras AS c 
            WHERE i.id_fornecedor = f.id 
            AND i.id_empresa = e.id
            AND i.id_compra = c.id AND i.id_compra = {decisao2}
            GROUP BY i.id;""")
            compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta
            x = PrettyTable()
            x.field_names = ['CC', 'CCI', 'Data', 'Nome do produto', 'Descrição',
                             'Fornecedor',
                             'Empresa', 'Valor unitário', 'Quantidade', 'Valor total']
            print('Listando compras...')
            sleep(0.5)
            for compra in compras:
                x.add_row([compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6], compra[7],
                           compra[8], compra[9]])
            print(x)
    else:
        print('Não existem produtos cadastrados')


def listar_mes_atual_compras_interias():
    """
    Função para listar os produtos
    """
    cursor = conn.cursor()
    cursor.execute("""SELECT id, DATE_FORMAT(data, '%d/%m/%Y') AS 'Data da Compra' FROM compras
    WHERE MONTH(CURDATE()) = MONTH(data);""")
    compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta
    x = PrettyTable()
    x.field_names = ["Codigo da compra", "Data da compra"]
    x.align["Código da compra"] = "1"
    x.align["Data da compra"] = "1"
    x.padding_width = 1
    x.align = "c"
    if len(compras) > 0:
        print('Listando compras...')
        sleep(0.5)
        for compra in compras:
            x.add_row([compra[0], compra[1]])
        print(f'{x.get_string()}')


def listar_compras_mes_atual(qual7, cod=0):
    """
    Função para listar os produtos
    """
    cursor = conn.cursor()
    if qual7 == 1:
        cursor.execute(f"""SELECT i.id, i.id_compra, DATE_FORMAT(c.data, '%d/%m/%Y') ,i.nome, i.descricao,
        f.nome AS fornecedor, e.nome AS empresa, i.preco AS Valor_Unitário, i.quantidade AS Quantidade ,
        SUM(i.preco * i.quantidade) AS Valor_Total
        FROM itens_compra AS i, fornecedores AS f, empresas AS e, compras AS c 
        WHERE i.id_fornecedor = f.id 
        AND i.id_empresa = e.id
        AND i.id_compra = c.id
        AND MONTH(CURDATE()) = MONTH(c.data)
        GROUP BY i.id;""")
        compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta!
        x = PrettyTable()
        x.field_names = ['CC', 'CCI', 'Data', 'Nome do produto', 'Descrição',
                         'Fornecedor',
                         'Empresa', 'Valor unitário', 'Quantidade', 'Valor total']
        if len(compras) > 0:
            print('Listando compras...')
            sleep(0.5)
            for compra in compras:
                x.add_row([compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6], compra[7],
                           compra[8], compra[9]])
            print(x)
        else:
            print('Não existem produtos cadastrados')
    if qual7 == 2:
        cursor.execute(f"""SELECT i.id, i.id_compra, DATE_FORMAT(c.data, '%d/%m/%Y') ,i.nome, i.descricao,
        f.nome AS fornecedor, e.nome AS empresa, i.preco AS Valor_Unitário, i.quantidade AS Quantidade ,
        SUM(i.preco * i.quantidade) AS Valor_Total
        FROM itens_compra AS i, fornecedores AS f, empresas AS e, compras AS c 
        WHERE i.id_fornecedor = f.id 
        AND i.id_empresa = e.id
        AND i.id_compra = c.id
        AND MONTH(CURDATE()) = MONTH(c.data)
        AND i.id_compra = {cod}
        GROUP BY i.id;""")
        compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta!
        x = PrettyTable()
        x.field_names = ['CC', 'CCI', 'Data', 'Nome do produto', 'Descrição',
                         'Fornecedor',
                         'Empresa', 'Valor unitário', 'Quantidade', 'Valor total']
        if len(compras) > 0:
            print('Listando compras...')
            sleep(0.5)
            for compra in compras:
                x.add_row([compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6], compra[7],
                           compra[8], compra[9]])
            print(x)
        else:
            print('Não existem produtos cadastrados')


def comparacao_mesatual_mespassado():
    """
    Função para listar os produtos
    """
    cursor = conn.cursor()
    cursor.execute("""SELECT id, DATE_FORMAT(data, '%d/%m/%Y') AS 'Data da Compra' FROM compras
                   WHERE MONTH(data) = MONTH(CURDATE())""")
    compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta
    x = PrettyTable()
    x.field_names = ["Codigo da compra", "Data da compra"]
    x.align["Código da compra"] = "1"
    x.align["Data da compra"] = "1"
    x.padding_width = 1
    x.align = "c"
    if len(compras) > 0:
        print('Listando compras...')
        print()
        sleep(1)
        for compra in compras:
            x.add_row([compra[0], compra[1]])
        print('-' * 50, end='MÊS ATUAL')
        print('-' * 50)
        print(f'{x.get_string()}')

    cursor = conn.cursor()
    cursor.execute(f"""SELECT i.id, i.id_compra, DATE_FORMAT(c.data, '%d/%m/%Y') ,i.nome, i.descricao,
    f.nome AS fornecedor, e.nome AS empresa, i.preco AS Valor_Unitário, i.quantidade AS Quantidade ,
    SUM(i.preco * i.quantidade) AS Valor_Total
    FROM itens_compra AS i, fornecedores AS f, empresas AS e, compras AS c 
    WHERE i.id_fornecedor = f.id 
    AND i.id_empresa = e.id
    AND i.id_compra = c.id
    AND MONTH(CURDATE()) = MONTH(c.data)
    GROUP BY i.id;""")
    compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta!
    x = PrettyTable()
    x.field_names = ['CC', 'CCI', 'Data', 'Nome do produto', 'Descrição',
                     'Fornecedor',
                     'Empresa', 'Valor unitário', 'Quantidade', 'Valor total']
    if len(compras) > 0:
        sleep(0.5)
        for compra in compras:
            x.add_row([compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6], compra[7],
                       compra[8], compra[9]])
        print(x)
    else:
        print('Não existem produtos cadastrados')

    cursor = conn.cursor()
    cursor.execute("""SELECT id, DATE_FORMAT(data, '%d/%m/%Y') AS 'Data da Compra' FROM compras
                   WHERE MONTH(data) = MONTH(CURDATE()) -1 """)
    compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta
    x = PrettyTable()
    x.field_names = ["Codigo da compra", "Data da compra"]
    x.align["Código da compra"] = "1"
    x.align["Data da compra"] = "1"
    x.padding_width = 1
    x.align = "c"
    if len(compras) > 0:
        print('Listando compras...')
        print()
        sleep(1)
        for compra in compras:
            x.add_row([compra[0], compra[1]])
        print('-' * 50, end='MÊS ANTERIOR')
        print('-' * 50)
        print(f'{x.get_string()}')

    cursor.execute(f"""SELECT i.id, i.id_compra, DATE_FORMAT(c.data, '%d/%m/%Y') ,i.nome, i.descricao,
    f.nome AS fornecedor, e.nome AS empresa, i.preco AS Valor_Unitário, i.quantidade AS Quantidade ,
    SUM(i.preco * i.quantidade) AS Valor_Total
    FROM itens_compra AS i, fornecedores AS f, empresas AS e, compras AS c 
    WHERE i.id_fornecedor = f.id 
    AND i.id_empresa = e.id
    AND i.id_compra = c.id
    AND MONTH(c.data) = MONTH(CURDATE()) -1 
    GROUP BY i.id;""")
    compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta!
    x = PrettyTable()
    x.field_names = ['CC', 'CCI', 'Data', 'Nome do produto', 'Descrição',
                     'Fornecedor',
                     'Empresa', 'Valor unitário', 'Quantidade', 'Valor total']
    if len(compras) > 0:
        sleep(1.0)
        for compra in compras:
            x.add_row([compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6], compra[7],
                       compra[8], compra[9]])
        print(x)
    else:
        print('Não existem produtos cadastrados')


def comparacao_anoatual_anopassado():
    """
    Função para listar os produtos
    """
    cursor = conn.cursor()
    cursor.execute("""SELECT id, DATE_FORMAT(data, '%d/%m/%Y') AS 'Data da Compra' FROM compras 
    WHERE YEAR(data) = YEAR(CURDATE());""")
    compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta
    x = PrettyTable()
    x.field_names = ["Codigo da compra", "Data da compra"]
    x.align["Código da compra"] = "1"
    x.align["Data da compra"] = "1"
    x.padding_width = 1
    x.align = "c"
    if len(compras) > 0:
        print('Listando compras...')
        print()
        sleep(1)
        for compra in compras:
            x.add_row([compra[0], compra[1]])
        print('-' * 50, end='ANO ATUAL')
        print('-' * 50)
        print(f'{x.get_string()}')

    cursor = conn.cursor()
    cursor.execute(f"""SELECT i.id, i.id_compra, DATE_FORMAT(c.data, '%d/%m/%Y') ,i.nome, i.descricao,
    f.nome AS fornecedor, e.nome AS empresa, i.preco AS Valor_Unitário, i.quantidade AS Quantidade ,
    SUM(i.preco * i.quantidade) AS Valor_Total
    FROM itens_compra AS i, fornecedores AS f, empresas AS e, compras AS c 
    WHERE i.id_fornecedor = f.id 
    AND i.id_empresa = e.id
    AND i.id_compra = c.id
    AND YEAR(CURDATE()) = YEAR(c.data)
    GROUP BY i.id;""")
    compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta!
    x = PrettyTable()
    x.field_names = ['CC', 'CCI', 'Data', 'Nome do produto', 'Descrição',
                     'Fornecedor',
                     'Empresa', 'Valor unitário', 'Quantidade', 'Valor total']
    if len(compras) > 0:
        sleep(0.5)
        for compra in compras:
            x.add_row([compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6], compra[7],
                       compra[8], compra[9]])
        print(x)
    else:
        print('Não existem produtos cadastrados')

    cursor = conn.cursor()
    cursor.execute("""SELECT id, DATE_FORMAT(data, '%d/%m/%Y') AS 'Data da Compra' FROM compras
                   WHERE YEAR(data) = YEAR(CURDATE()) -1 """)
    compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta
    x = PrettyTable()
    x.field_names = ["Codigo da compra", "Data da compra"]
    x.align["Código da compra"] = "1"
    x.align["Data da compra"] = "1"
    x.padding_width = 1
    x.align = "c"
    if len(compras) > 0:
        print('Listando compras...')
        print()
        sleep(1)
        for compra in compras:
            x.add_row([compra[0], compra[1]])
        print('-' * 50, end='ANO ANTERIOR')
        print('-' * 50)
        print(f'{x.get_string()}')

    cursor.execute(f"""SELECT i.id, i.id_compra, DATE_FORMAT(c.data, '%d/%m/%Y') ,i.nome, i.descricao,
    f.nome AS fornecedor, e.nome AS empresa, i.preco AS Valor_Unitário, i.quantidade AS Quantidade ,
    SUM(i.preco * i.quantidade) AS Valor_Total
    FROM itens_compra AS i, fornecedores AS f, empresas AS e, compras AS c 
    WHERE i.id_fornecedor = f.id 
    AND i.id_empresa = e.id
    AND i.id_compra = c.id
    AND YEAR(c.data) = YEAR(CURDATE()) -1 
    GROUP BY i.id;""")
    compras = cursor.fetchall()  # Transformar numa lista o retorno da consulta!
    x = PrettyTable()
    x.field_names = ['CC', 'CCI', 'Data', 'Nome do produto', 'Descrição',
                     'Fornecedor',
                     'Empresa', 'Valor unitário', 'Quantidade', 'Valor total']
    if len(compras) > 0:
        sleep(1.0)
        for compra in compras:
            x.add_row([compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6], compra[7],
                       compra[8], compra[9]])
        print(x)
    else:
        print('Não existem produtos cadastrados')


def inserir():
    """
    Função para inserir um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    nome = input("Informe o nome do produto: ")
    preco = float(input("Informe o preço do produto: "))
    estoque = int(input("Informe a quantidade em estoque: "))

    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque})")
    conn.commit()
    print('Inserindo produto...')

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi inserido com sucesso.')
    else:
        print(f'Não foi possível inserir o produto.')
    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do produto: '))
    nome = input('Informe o novo nome do produto: ')
    preco = float(input('Informe o novo preço do produto: '))
    estoque = int(input('Informe a nova quantidade em estoque: '))

    cursor.execute(f"UPDATE produtos SET nome = '{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}")
    conn.commit()
    print('Atualizando produto...')
    if cursor.rowcount == 1:
        print(f'O produto {nome} foi atualizado com sucesso.')
    else:
        print('Erro ao atualizar o produto.')
    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """
    print('Deletando produto...')
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do produto: '))

    cursor.execute(f'DELETE FROM produtos WHERE id={codigo}')
    conn.commit()
    if cursor.rowcount == 1:
        print('Produto excluído com sucesso.')
    else:
        print(f'Erro ao excluir o produto com id = {codigo}')
    desconectar(conn)


def menu():
    print('-' * 100)
    print(f"\033[31m{'                          ESCOLHA A OPERAÇÃO QUE DESEJA EXECUTAR'}\033[0;0m")
    print('-' * 100)
    print()
    print('1- Para listar as compras conjuntas.')
    print('2- Para listar todas as compras.')
    print('3- Para listar uma compra específica.')
    print('4- Para listar pelo valor do produto.')
    print('5- Para listar por uma data específica.')
    print('6- Para listar as compras e compras conjuntas do mês atual')
    print('7- Para listar o mês autual e o mês anterior')
    print('8 - Para listar o ano atual e o ano anterior')


conn = conectar()


def principal():
    while True:
        sleep(0.5)
        menu()
        sleep(0.5)
        print('-' * 100)
        qual = int(input('Digite o número da operação que deseja executar: '))
        if qual == 1:
            listarcompras()
            op = str(input('Deseja fazer mais alguma operação [S/N]? ')).strip()[0]
            if op not in 'Ss':
                break
            if op in 'Ss':
                continue
        if qual == 2:
            listartodas()
            op = str(input('Deseja fazer mais alguma operação [S/N]? ')).strip()[0]
            if op not in 'Ss':
                break
            if op in 'Ss':
                continue
        if qual == 3:
            qual1 = int(input('Qual o código da compra que você deseja consultar? '))
            listarespecid(qual1)
            op = str(input('Deseja fazer mais alguma operação [S/N]? ')).strip()[0]
            if op not in 'Ss':
                break
            if op in 'Ss':
                continue
        if qual == 4:
            qual2 = int(input('Deseja listar valores maiores ou iguais que, ou menores ou iguais que [1 ou 2]: '))
            qual3 = float(input('Qual o preço de referencia? '))
            listarvalorprod(qual2, qual3)
            op = str(input('Deseja fazer mais alguma operação [S/N]? ')).strip()[0]
            if op not in 'Ss':
                break
            if op in 'Ss':
                continue
        if qual == 5:
            qual4 = str(input('Digite a data da compra que deseja listar, nesse formato dd-mm-yyyy: '))
            data = datetime.strptime(f'{qual4}', "%d-%m-%Y").date()
            data = str(data)
            listardataespec(data)
            op = str(input('Deseja fazer mais alguma operação [S/N]? ')).strip()[0]
            if op not in 'Ss':
                break
            if op in 'Ss':
                continue
        if qual == 6:
            listar_mes_atual_compras_interias()
            qual7 = int(input('Deseja listar todas as compras, ou deseja listar uma compra específica [1/2]: '))
            if qual7 == 2:
                cod = int(input('Qual o código da compra que você deseja listar: '))
                listar_compras_mes_atual(qual7, cod)
            if qual7 == 1:
                listar_compras_mes_atual(qual7)
            op = str(input('Deseja fazer mais alguma operação [S/N]? ')).strip()[0]
            if op not in 'Ss':
                break
            if op in 'Ss':
                continue
        if qual == 7:
            comparacao_mesatual_mespassado()
            op = str(input('Deseja fazer mais alguma operação [S/N]? ')).strip()[0]
            if op not in 'Ss':
                break
            if op in 'Ss':
                continue
        if qual == 8:
            comparacao_anoatual_anopassado()
            op = str(input('Deseja fazer mais alguma operação [S/N]? ')).strip()[0]
            if op not in 'Ss':
                break
            if op in 'Ss':
                continue
