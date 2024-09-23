import sqlalchemy as sqla
from sqlalchemy import String, Integer, Float, ForeignKey, Column, create_engine, MetaData, Table, text

engine = create_engine('sqlite:///aluno_disciplina_11.db')
metadata = MetaData()

aluno_table = Table('alunos', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String, nullable=False),
    Column('email', String, nullable=False)
)

disciplina_table = Table('disciplinas', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('nome_disciplina', String, nullable=False),
    Column('nota', Float, nullable=False),
    Column('aluno_id', Integer, ForeignKey('alunos.id'))
)

metadata.drop_all(engine)

metadata.create_all(engine)

try:
    with engine.connect() as conn:
        conn.execute(aluno_table.insert().values(nome='Pedro', email ='pedro@email.com'))
        conn.execute(aluno_table.insert().values(nome='Paulo Torres', email ='paulotorres@email.com'))
        conn.commit()
except Exception as e:
    print(f'Erro ao inserir dados na tabela alunos: {e}')

nota_maxima = 10
try:
    with engine.connect() as conn:
        conn.execute(disciplina_table.insert().values(nome_disciplina='Python para Dados', nota=7, aluno_id=2))
        conn.execute(disciplina_table.insert().values(nome_disciplina='Projeto de Bloco', nota=8, aluno_id=1))
        conn.commit()
        result = conn.execute(disciplina_table.select())
        print('Tabela disciplina com alunos inseridos: ')
        for row in result:
            print(row)
        input('Aguardando conferir tabela...')
    
        conn.execute(text("""UPDATE disciplinas
                        SET nota = :nota
                        WHERE nome_disciplina = 'Python para Dados' AND aluno_id = (SELECT id FROM alunos WHERE nome = 'Paulo Torres')
                        """), {'nota': nota_maxima})
        conn.commit()
        result = conn.execute(disciplina_table.select())
        print('Tabela disciplina com nota atualizada: ')
        for row in result:
            print(row)

except Exception as e:
    print(f'Erro ao manipular dados na tabela disciplinas: {e}')
