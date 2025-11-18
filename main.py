 
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Criando a engine para o banco de dados SQLite
engine = create_engine("sqlite:///name.db")

# #criar engine para o banco de dados postgresql
# create_engine("postgresql+psycopg2://user:password@localhost/dbname")

# #criar engine para o banco de dados mysql
# create_engine("mysql+pymysql://user:password@localhost/dbname")


Base = declarative_base() #poder mágico de transformar classes em tabelas do banco de dados

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer, nullable= False)
    endereco = Column(String(150), default= "Rua das pedras, 10")
    created_at = Column(DateTime, default=datetime.now)
    uptaded_at = Column(DateTime)

    def __repr__(self):
        return f"<Usuario(nome='{self.nome}, idade= {self.idade}, endereço={self.endereco}')>"


# Criando todas as nossa tabelas no banco 
Base.metadata.create_all(engine)

# Criar nossa sessão 
Section = sessionmaker(bind=engine)
section = Section()

def add_many(): 
    lista_usuario = [
        Usuario(nome="Angelo", idade=33, endereco="Rua A"),
        Usuario(nome="Bruno", idade=15, endereco="Rua B"),
        Usuario(nome="Daniel", idade=26, endereco="Rua C"),
        Usuario(nome="Maria", idade=85, endereco="Rua D"),
        Usuario(nome="Jose", idade=59, endereco="Rua E")
    ]

    section.add_all(lista_usuario)
    section.commit()

add_many()


def add_user(nome, idade, endereco): 
    usuario_add = Usuario(nome=nome, idade=idade, endereco=endereco)
    section.add(usuario_add)
    section.commit()
    print(f"{usuario_add.id} - {usuario_add.nome} - {usuario_add.idade} - {usuario_add.endereco}")


def list_all(): 
    lista_usuarios = section.query(Usuario).all()
    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.idade} - {usuario.endereco}")


#filtar usuarios 
def filter_idade(idade): 
    filter_idade = section.query(Usuario).filter(Usuario.idade > idade).all()
    for usuario_idosos in filter_idade:
        print(f"{usuario_idosos.id} - {usuario_idosos.nome} - {usuario_idosos.idade} - {usuario_idosos.endereco}")

# Atualizar um usuario 
def uptade_user(id, nome, idade, endereco):
    usuario_updtade = section.query(Usuario).filter(Usuario.id == id).first()
    usuario_updtade.nome = nome
    usuario_updtade.idade = idade
    usuario_updtade.endereco = endereco
    usuario_updtade.uptaded_at = datetime.now()
    section.commit()
    print(f"Usuário atualziado com sucesso: {usuario_updtade.id} - {usuario_updtade.nome}")


#deletar 
def remove_user(id): 
    usuario_remove = section.query(Usuario).filter(Usuario.id == id).first()
    section.delete(usuario_remove)
    section.commit()
    print(f"Usuário removido com sucesso: {usuario_remove.id} - {usuario_remove.nome}")


def menu(): 
    print("\n" + "=" * 50)
    print("SISTEMA USUARIO")
    print("1 - Adicionar um usuário")
    print("2 - Listar todos usuários")
    print("3 - Filtrar por idade")
    print("4 - Atulizar um usuário")
    print("5 - Removder um usuário")
    print("0 - Sair")
    print("=" * 50)

def main():
    while True: 
        menu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome: * ").strip()
            idade =int(input("idade: * ").strip())
            endereco = input("endereco: * ").strip()
            add_user(nome, idade, endereco)

        elif opcao == "2":
            list_all()

        elif opcao == "3":
            idade =int(input("idade: * ").strip())
            filter_idade(idade)

        elif opcao == "4": 
            while True: 
                try:
                    id = int(input("Informe o id do usuário a ser atualziado: * ").strip())
                    break
                except ValueError: 
                    print("ID não é válido!")

            nome = input("Nome: * ").strip()
            idade = int(input("idade: * ").strip())
            endereco = input("endereco: * ").strip()

            uptade_user(id, nome, idade, endereco)

        elif opcao == "5": 
            id = int(input("Informe o id do usuário a ser excluído: * ").strip())
            remove_user(id)

        elif opcao == "0": 
            section.close()
            print("\n Encerrando..")
            break

        else: 
            print("Opção inválida, tente novamente... ")

        input("\n Pressione ENTER para continuar... ")

main()