from tkinter import *
import psycopg2

connection = psycopg2.connect(database = 'locadoraveiculos',
                              user = 'postgres',
                              host = 'localhost',
                              password = '345473')

def cadastrarFuncionario():
    def cadastrar():
        nome1 = str(nome.get())
        sexo1 = str(sexo.get())
        datanascimento1 = str(datanascimento.get())
        logradouro1 = str(logradouro.get())
        numero1 = str(numero.get())
        bairro1 = str(bairro.get())
        complemento1 = str(complemento.get())
        municipio1 = str(municipio.get())
        uf1 = str(uf.get())
        salario1 = str(salario.get())

        cursor = connection.cursor()
        sql = """INSERT INTO funcionario(nome, sexo, datanascimento, logradouro, numero, bairro, complemento, municipio, uf, salario)
                  VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
        cursor.execute(sql.format(nome1, sexo1, datanascimento1, logradouro1, numero1, bairro1, complemento1, municipio1, uf1, salario1))
        connection.commit()

    janela = Tk()
    janela.title('Cadastro Funcionário')

    lab1 = Label(janela, text = 'Nome:')
    lab1.place(x = 20, y = 1)
    nome = Entry(janela, width = 50)
    nome.place(x = 20, y = 20)

    lab2 = Label(janela, text = 'Sexo(M ou F):')
    lab2.place(x = 20, y = 40)
    sexo = Entry(janela, width = 50)
    sexo.place(x = 20, y = 60)

    lab3 = Label(janela, text = 'Data de Nascimento(Ano-Mês-Dia):')
    lab3.place(x = 20, y = 80)
    datanascimento = Entry(janela, width = 50)
    datanascimento.place(x = 20, y = 100)

    lab4 = Label(janela, text = 'Logradouro:')
    lab4.place(x = 20, y = 120)
    logradouro = Entry(janela, width = 50)
    logradouro.place(x = 20, y = 140)

    lab5 = Label(janela, text = 'Número:')
    lab5.place(x = 20, y = 160)
    numero = Entry(janela, width = 50)
    numero.place(x = 20, y = 180)

    lab6 = Label(janela, text = 'Bairro:')
    lab6.place(x = 20, y = 200)
    bairro = Entry(janela, width = 50)
    bairro.place(x = 20, y = 220)

    lab7 = Label(janela, text = 'Complemento(Opcional):')
    lab7.place(x = 20, y = 240)
    complemento = Entry(janela, width = 50)
    complemento.place(x = 20, y = 260)

    lab8 = Label(janela, text = 'Município:')
    lab8.place(x = 20, y = 280)
    municipio = Entry(janela, width = 50)
    municipio.place(x = 20, y = 300)

    lab9 = Label(janela, text = 'UF:')
    lab9.place(x = 20, y = 320)
    uf = Entry(janela, width = 50)
    uf.place(x = 20, y = 340)

    lab10 = Label(janela, text = 'Salário:')
    lab10.place(x = 20, y = 360)
    salario = Entry(janela, width = 50)
    salario.place(x = 20, y = 380)

    cadastrar = Button(janela, text = 'Cadastrar', bg = '#E0FFFF', command = cadastrar)
    cadastrar.place(x = 130, y = 410)

    janela['bg'] = '#36648B'
    janela.geometry('350x450')
    janela.mainloop()


def alterarFuncionario():
    def alterar():
        nome1 = str(nome.get())
        sexo1 = str(sexo.get())
        datanascimento1 = str(datanascimento.get())
        logradouro1 = str(logradouro.get())
        numero1 = str(numero.get())
        bairro1 = str(bairro.get())
        complemento1 = str(complemento.get())
        municipio1 = str(municipio.get())
        uf1 = str(uf.get())
        salario1 = str(salario.get())
        idfuncionario1 = str(idfuncionario.get())

        cursor = connection.cursor()
        sql =  """UPDATE funcionario
                SET nome = '{}', sexo = '{}', datanascimento = '{}', logradouro = '{}', numero = '{}', bairro = '{}', complemento = '{}', municipio = '{}', uf = '{}', salario = '{}' 
                WHERE idfuncionario = {}"""
        cursor.execute(sql.format(nome1, sexo1, datanascimento1, logradouro1, numero1, bairro1, complemento1, municipio1, uf1, salario1, idfuncionario1))
        connection.commit()

    janela = Tk()
    janela.title('Alterar Funcionário')

    lab1 = Label(janela, text = 'Nome:')
    lab1.place(x = 20, y = 1)
    nome = Entry(janela, width = 50)
    nome.place(x = 20, y = 20)

    lab2 = Label(janela, text = 'Sexo(M ou F):')
    lab2.place(x = 20, y = 40)
    sexo = Entry(janela, width = 50)
    sexo.place(x = 20, y = 60)

    lab3 = Label(janela, text = 'Data de Nascimento(Ano-Mês-Dia):')
    lab3.place(x = 20, y = 80)
    datanascimento = Entry(janela, width = 50)
    datanascimento.place(x = 20, y = 100)

    lab4 = Label(janela, text = 'Logradouro:')
    lab4.place(x = 20, y = 120)
    logradouro = Entry(janela, width = 50)
    logradouro.place(x = 20, y = 140)

    lab5 = Label(janela, text = 'Número:')
    lab5.place(x = 20, y = 160)
    numero = Entry(janela, width = 50)
    numero.place(x = 20, y = 180)

    lab6 = Label(janela, text = 'Bairro:')
    lab6.place(x = 20, y = 200)
    bairro = Entry(janela, width = 50)
    bairro.place(x = 20, y = 220)

    lab7 = Label(janela, text = 'Complemento(Opcional):')
    lab7.place(x = 20, y = 240)
    complemento = Entry(janela, width = 50)
    complemento.place(x = 20, y = 260)

    lab8 = Label(janela, text = 'Município:')
    lab8.place(x = 20, y = 280)
    municipio = Entry(janela, width = 50)
    municipio.place(x = 20, y = 300)

    lab9 = Label(janela, text = 'UF:')
    lab9.place(x = 20, y = 320)
    uf = Entry(janela, width = 50)
    uf.place(x = 20, y = 340)

    lab10 = Label(janela, text = 'Salário:')
    lab10.place(x = 20, y = 360)
    salario = Entry(janela, width = 50)
    salario.place(x = 20, y = 380)

    lab11 = Label(janela, text = 'idFuncionario:')
    lab11.place(x = 20, y = 400)
    idfuncionario = Entry(janela, width = 50)
    idfuncionario.place(x = 20, y = 420)

    alterar = Button(janela, text = 'Alterar', bg = '#E0FFFF', command = alterar)
    alterar.place(x = 130, y = 450)

    janela['bg'] = '#36648B'
    janela.geometry('350x490')
    janela.mainloop()


def excluirFuncionario():
    def excluir():
        idfuncionario1 = str(idfuncionario.get())

        cursor = connection.cursor()
        sql =  """DELETE FROM funcionario
                WHERE idfuncionario = {}"""
        cursor.execute(sql.format(idfuncionario1))
        connection.commit()

    janela = Tk()
    janela.title('Excluir Funcionário')

    lab1 = Label(janela, text = 'idFuncionario:')
    lab1.place(x = 20, y = 1)
    idfuncionario = Entry(janela, width = 50)
    idfuncionario.place(x = 20, y = 20)

    excluir = Button(janela, text = 'Excluir', bg = '#E0FFFF', command = excluir)
    excluir.place(x = 130, y = 50)

    janela['bg'] = '#36648B'
    janela.geometry('350x90')
    janela.mainloop()


def acessoFuncionario():
    janela = Tk()
    janela.title('Informações Funcionário')

    bt1 = Button(janela, text = 'Cadastrar Funcionário', bg = '#E0FFFF', command = cadastrarFuncionario)
    bt1.grid(row = 1, column = 0)

    bt2 = Button(janela, text = 'Alterar dado', bg = '#E0FFFF', command = alterarFuncionario)
    bt2.grid(row = 1, column = 1)

    bt3 = Button(janela, text = 'Excluir dado', bg = '#E0FFFF', command = excluirFuncionario)
    bt3.grid(row = 1, column = 2)

    cursor = connection.cursor()
    sql = "SELECT * FROM funcionario"
    cursor.execute(sql)

    listaridfuncionario = Listbox(janela, width = 10, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listaridfuncionario.place(x = 0, y = 30)

    listarnome = Listbox(janela, width = 20, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarnome.place(x = 30, y = 30)

    listarsexo = Listbox(janela, width = 10, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarsexo.place(x = 150, y = 30)

    listardatanascimento = Listbox(janela, width = 15, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listardatanascimento.place(x = 170, y = 30)

    listarlogradouro = Listbox(janela, width = 15, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarlogradouro.place(x = 240, y = 30)

    listarnumero = Listbox(janela, width = 10, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarnumero.place(x = 320, y = 30)

    listarbairro = Listbox(janela, width = 10, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarbairro.place(x = 350, y = 30)

    listarcomplemento = Listbox(janela, width = 20, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarcomplemento.place(x = 410, y = 30)

    listarmunicipio = Listbox(janela, width = 12, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarmunicipio.place(x = 530, y = 30)

    listaruf = Listbox(janela, width = 10, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listaruf.place(x = 600, y = 30)

    listarsalario = Listbox(janela, width = 15, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarsalario.place(x = 630, y = 30)

    funcionario = cursor.fetchall()
    for i in funcionario:
        listaridfuncionario.insert(END, i[0])
        listarnome.insert(END, i[1])
        listarsexo.insert(END, i[2])
        listardatanascimento.insert(END, i[3])
        listarlogradouro.insert(END, i[4])
        listarnumero.insert(END, i[5])
        listarbairro.insert(END, i[6])
        listarcomplemento.insert(END, i[7])
        listarmunicipio.insert(END, i[8])
        listaruf.insert(END, i[9])
        listarsalario.insert(END, i[10])

    janela.geometry('740x530')
    janela['bg'] = '#36648B'
    janela.mainloop()


def cadastrarCliente():
    def cadastrar():
        nome1 = str(nome.get())
        sexo1 = str(sexo.get())
        logradouro1 = str(logradouro.get())
        numero1 = str(numero.get())
        bairro1 = str(bairro.get())
        complemento1 = str(complemento.get())
        municipio1 = str(municipio.get())
        uf1 = str(uf.get())
        telefone1 = str(telefone.get())

        cursor = connection.cursor()
        sql = """INSERT INTO cliente(nome, sexo, logradouro, numero, bairro, complemento, municipio, uf, telefone)
                  VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
        cursor.execute(sql.format(nome1, sexo1,logradouro1, numero1, bairro1, complemento1, municipio1, uf1, telefone1))
        connection.commit()

    janela = Tk()
    janela.title('Cadastro Cliente')

    lab1 = Label(janela, text = 'Nome:')
    lab1.place(x = 20, y = 1)
    nome = Entry(janela, width = 50)
    nome.place(x = 20, y = 20)

    lab2 = Label(janela, text = 'Sexo(M ou F):')
    lab2.place(x = 20, y = 40)
    sexo = Entry(janela, width = 50)
    sexo.place(x = 20, y = 60)

    lab3 = Label(janela, text = 'Logradouro:')
    lab3.place(x = 20, y = 80)
    logradouro = Entry(janela, width = 50)
    logradouro.place(x = 20, y = 100)

    lab4 = Label(janela, text = 'Número:')
    lab4.place(x = 20, y = 120)
    numero = Entry(janela, width = 50)
    numero.place(x = 20, y = 140)

    lab5 = Label(janela, text = 'Bairro:')
    lab5.place(x = 20, y = 160)
    bairro = Entry(janela, width = 50)
    bairro.place(x = 20, y = 180)

    lab6 = Label(janela, text = 'Complemento(Opcional):')
    lab6.place(x = 20, y = 200)
    complemento = Entry(janela, width = 50)
    complemento.place(x = 20, y = 220)

    lab7 = Label(janela, text = 'Município:')
    lab7.place(x = 20, y = 240)
    municipio = Entry(janela, width = 50)
    municipio.place(x = 20, y = 260)

    lab8 = Label(janela, text = 'UF:')
    lab8.place(x = 20, y = 280)
    uf = Entry(janela, width = 50)
    uf.place(x = 20, y = 300)

    lab9 = Label(janela, text = 'Telefone((00)000-000-000):')
    lab9.place(x = 20, y = 320)
    telefone = Entry(janela, width = 50)
    telefone.place(x = 20, y = 340)

    cadastrar = Button(janela, text = 'Cadastrar', bg = '#E0FFFF', command = cadastrar)
    cadastrar.place(x = 130, y = 370)

    janela['bg'] = '#36648B'
    janela.geometry('350x410')
    janela.mainloop()


def alterarCliente():
    def alterar():
        nome1 = str(nome.get())
        sexo1 = str(sexo.get())
        logradouro1 = str(logradouro.get())
        numero1 = str(numero.get())
        bairro1 = str(bairro.get())
        complemento1 = str(complemento.get())
        municipio1 = str(municipio.get())
        uf1 = str(uf.get())
        telefone1 = str(telefone.get())
        idcliente1 = str(idcliente.get())

        cursor = connection.cursor()
        sql =  """UPDATE cliente
                SET nome = '{}', sexo = '{}', logradouro = '{}', numero = '{}', bairro = '{}', complemento = '{}', municipio = '{}', uf = '{}', telefone = '{}' 
                WHERE idcliente = {}"""
        cursor.execute(sql.format(nome1, sexo1, logradouro1, numero1, bairro1, complemento1, municipio1, uf1, telefone1, idcliente1))
        connection.commit()

    janela = Tk()
    janela.title('Alterar Dado Cliente')

    lab1 = Label(janela, text = 'Nome:')
    lab1.place(x = 20, y = 1)
    nome = Entry(janela, width = 50)
    nome.place(x = 20, y = 20)

    lab2 = Label(janela, text = 'Sexo(M ou F):')
    lab2.place(x = 20, y = 40)
    sexo = Entry(janela, width = 50)
    sexo.place(x = 20, y = 60)

    lab3 = Label(janela, text = 'Logradouro:')
    lab3.place(x = 20, y = 80)
    logradouro = Entry(janela, width = 50)
    logradouro.place(x = 20, y = 100)

    lab4 = Label(janela, text = 'Número:')
    lab4.place(x = 20, y = 120)
    numero = Entry(janela, width = 50)
    numero.place(x = 20, y = 140)

    lab5 = Label(janela, text = 'Bairro:')
    lab5.place(x = 20, y = 160)
    bairro = Entry(janela, width = 50)
    bairro.place(x = 20, y = 180)

    lab6 = Label(janela, text = 'Complemento(Opcional):')
    lab6.place(x = 20, y = 200)
    complemento = Entry(janela, width = 50)
    complemento.place(x = 20, y = 220)

    lab7 = Label(janela, text = 'Município:')
    lab7.place(x = 20, y = 240)
    municipio = Entry(janela, width = 50)
    municipio.place(x = 20, y = 260)

    lab8 = Label(janela, text = 'UF:')
    lab8.place(x = 20, y = 280)
    uf = Entry(janela, width = 50)
    uf.place(x = 20, y = 300)

    lab9 = Label(janela, text = 'Telefone((00)000-000-000):')
    lab9.place(x = 20, y = 320)
    telefone = Entry(janela, width = 50)
    telefone.place(x = 20, y = 340)

    lab10 = Label(janela, text = 'idCliente:')
    lab10.place(x = 20, y = 360)
    idcliente = Entry(janela, width = 50)
    idcliente.place(x = 20, y = 380)

    alterar = Button(janela, text = 'Alterar', bg = '#E0FFFF', command = alterar)
    alterar.place(x = 130, y = 430)

    janela['bg'] = '#36648B'
    janela.geometry('350x470')
    janela.mainloop()


def excluirCliente():
    def excluir():
        idcliente1 = str(idcliente.get())

        cursor = connection.cursor()
        sql =  """DELETE FROM cliente
                WHERE idcliente = {}"""
        cursor.execute(sql.format(idcliente1))
        connection.commit()

    janela = Tk()
    janela.title('Excluir Cliente')

    lab1 = Label(janela, text = 'idCliente:')
    lab1.place(x = 20, y = 1)
    idcliente = Entry(janela, width = 50)
    idcliente.place(x = 20, y = 20)

    excluir = Button(janela, text = 'Excluir', bg = '#E0FFFF', command = excluir)
    excluir.place(x = 130, y = 50)

    janela['bg'] = '#36648B'
    janela.geometry('350x90')
    janela.mainloop()


def acessoCliente():
    janela = Tk()
    janela.title('Informações Clientes')

    bt1 = Button(janela, text = 'Cadastrar cliente', bg = '#E0FFFF', command = cadastrarCliente)
    bt1.grid(row = 1, column = 0)

    bt2 = Button(janela, text = 'Alterar dado', bg = '#E0FFFF', command = alterarCliente)
    bt2.grid(row = 1, column = 1)

    bt3 = Button(janela, text = 'Excluir dado', bg = '#E0FFFF', command = excluirCliente)
    bt3.grid(row = 1, column = 2)

    cursor = connection.cursor()
    sql = "SELECT * FROM cliente"
    cursor.execute(sql)

    listaridcliente = Listbox(janela, width = 10, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listaridcliente.place(x = 0, y = 30)

    listarnome = Listbox(janela, width = 20, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarnome.place(x = 30, y = 30)

    listarsexo = Listbox(janela, width = 10, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarsexo.place(x = 150, y = 30)

    listarlogradouro = Listbox(janela, width = 15, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarlogradouro.place(x = 170, y = 30)

    listarnumero = Listbox(janela, width = 10, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarnumero.place(x = 250, y = 30)

    listarbairro = Listbox(janela, width = 10, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarbairro.place(x = 280, y = 30)

    listarcomplemento = Listbox(janela, width = 20, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarcomplemento.place(x = 340, y = 30)

    listarmunicipio = Listbox(janela, width = 12, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarmunicipio.place(x = 460, y = 30)

    listaruf = Listbox(janela, width = 10, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listaruf.place(x = 530, y = 30)

    listartelefone = Listbox(janela, width = 15, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listartelefone.place(x = 560, y = 30)

    cliente = cursor.fetchall()
    for i in cliente:
        listaridcliente.insert(END, i[0])
        listarnome.insert(END, i[1])
        listarsexo.insert(END, i[2])
        listarlogradouro.insert(END, i[3])
        listarnumero.insert(END, i[4])
        listarbairro.insert(END, i[5])
        listarcomplemento.insert(END, i[6])
        listarmunicipio.insert(END, i[7])
        listaruf.insert(END, i[8])
        listartelefone.insert(END, i[9])

    janela.geometry('670x530')
    janela['bg'] = '#36648B'
    janela.mainloop()


def cadastrarVeiculo():
    def cadastrar():
        modelo1 = str(modelo.get())
        ano1 = str(ano.get())

        cursor = connection.cursor()
        sql = """INSERT INTO veiculo(modelo, ano)
                  VALUES ('{}', '{}')"""
        cursor.execute(sql.format(modelo1, ano1))
        connection.commit()

    janela = Tk()
    janela.title('Cadastro Veículo')

    lab1 = Label(janela, text = 'Modelo:')
    lab1.place(x = 20, y = 1)
    modelo = Entry(janela, width = 50)
    modelo.place(x = 20, y = 20)

    lab2 = Label(janela, text = 'Ano:')
    lab2.place(x = 20, y = 40)
    ano = Entry(janela, width = 50)
    ano.place(x = 20, y = 60)

    cadastrar = Button(janela, text = 'Cadastrar', bg = '#E0FFFF', command = cadastrar)
    cadastrar.place(x = 130, y = 90)

    janela['bg'] = '#36648B'
    janela.geometry('350x130')
    janela.mainloop()


def alterarVeiculo():
    def alterar():
        modelo1 = str(modelo.get())
        ano1 = str(ano.get())
        idveiculo1= str(idveiculo.get())

        cursor = connection.cursor()
        sql =  """UPDATE veiculo
                SET modelo = '{}', ano = '{}'
                WHERE idveiculo = {}"""
        cursor.execute(sql.format(modelo1, ano1, idveiculo1))
        connection.commit()

    janela = Tk()
    janela.title('Alterar Dado Veículo')

    lab1 = Label(janela, text = 'Modelo:')
    lab1.place(x = 20, y = 1)
    modelo = Entry(janela, width = 50)
    modelo.place(x = 20, y = 20)

    lab2 = Label(janela, text = 'Ano:')
    lab2.place(x = 20, y = 40)
    ano = Entry(janela, width = 50)
    ano.place(x = 20, y = 60)

    lab3 = Label(janela, text = 'idVeiculo:')
    lab3.place(x = 20, y = 80)
    idveiculo = Entry(janela, width = 50)
    idveiculo.place(x = 20, y = 100)

    alterar = Button(janela, text = 'Alterar', bg = '#E0FFFF', command = alterar)
    alterar.place(x = 130, y = 130)

    janela['bg'] = '#36648B'
    janela.geometry('350x170')
    janela.mainloop()


def excluirVeiculo():
    def excluir():
        idveiculo1 = str(idveiculo.get())

        cursor = connection.cursor()
        sql =  """DELETE FROM veiculo
                WHERE idveiculo = {}"""
        cursor.execute(sql.format(idveiculo1))
        connection.commit()

    janela = Tk()
    janela.title('Excluir Veículo')

    lab1 = Label(janela, text = 'idVeiculo:')
    lab1.place(x = 20, y = 1)
    idveiculo = Entry(janela, width = 50)
    idveiculo.place(x = 20, y = 20)

    alterar = Button(janela, text = 'Excluir', bg = '#E0FFFF', command = excluir)
    alterar.place(x = 130, y = 50)

    janela['bg'] = '#36648B'
    janela.geometry('350x90')
    janela.mainloop()


def acessoVeiculo():
    janela = Tk()
    janela.title('Informações Veículos')

    bt1 = Button(janela, text = 'Cadastrar veículo', bg = '#E0FFFF', command = cadastrarVeiculo)
    bt1.grid(row = 1, column = 0)

    bt2 = Button(janela, text = 'Alterar dado', bg = '#E0FFFF', command = alterarVeiculo)
    bt2.grid(row = 1, column = 1)

    bt3 = Button(janela, text = 'Excluir dado', bg = '#E0FFFF', command = excluirVeiculo)
    bt3.grid(row = 1, column = 2)

    cursor = connection.cursor()
    sql = "SELECT * FROM veiculo"
    cursor.execute(sql)

    listaridveiculo = Listbox(janela, width = 10, height = 30, bg='#36648B',fg = 'white', bd =1, relief = "solid" )
    listaridveiculo.place(x = 0, y = 30)

    listarveiculo = Listbox(janela, width = 15, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarveiculo.place(x = 30, y = 30)

    listarano = Listbox(janela, width = 25, height = 30, bg = '#36648B', fg = 'white', bd = 1, relief = "solid")
    listarano.place(x = 120, y = 30)

    veiculo = cursor.fetchall()
    for i in veiculo:
        listaridveiculo.insert(END, i[0])
        listarveiculo.insert(END, i[1])
        listarano.insert(END, i[2])

    janela.geometry('290x530')
    janela['bg'] = '#36648B'
    janela.mainloop()

janela = Tk()
janela.title('Locadora de Veículos')

texto = Label(janela, text = 'Qual informação você deseja acessar?', bg = '#36648B')
texto.grid(row = 0, column = 1, padx = 10, pady = 10)

bt1 = Button(janela, width = 30, text = 'Funcionário', bg = '#E0FFFF', command = acessoFuncionario)
bt1.grid(row = 1, column = 0, padx = 10, pady = 10)

bt2 = Button(janela, width = 30, text = 'Cliente', bg = '#E0FFFF', command = acessoCliente)
bt2.grid(row = 1, column = 1, padx = 10, pady = 10)

bt3 = Button(janela, width = 30, text = 'Veículo', bg = '#E0FFFF', command = acessoVeiculo)
bt3.grid(row = 1, column = 2, padx = 10, pady = 10)

janela['bg'] = '#36648B'
janela.mainloop()