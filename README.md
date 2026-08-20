Sistema de Sustentabilidade

Sobre o projeto

Sistema desenvolvido em Python para realizar estimativas de consumo de água e energia. Os cálculos são armazenados em um banco de dados MySQL e podem ser consultados, atualizados e excluídos.

O sistema também apresenta dicas de sustentabilidade no menu principal.

Instalação

É necessário ter o Python  e o MySQL instalados.

Instale a biblioteca necessária:

O MySQL deve estar iniciado antes de executar o programa.

Banco de dados

O sistema cria automaticamente o banco:

hackaton

E as tabelas necessárias para armazenar os cálculos de água e energia.

É necessário configurar no código o usuário e a senha do MySQL.

Exemplo:

python
{
    "host": "localhost",
    "user": "root",
    "password": "SUA_SENHA",
    "database": "hackaton"
}



Como executar
Abra o terminal na pasta do projeto e execute:

python main.py

O programa verificará o banco de dados e abrirá o menu principal.

Menu principal

1 - Calculo de gasto de água
2 - Calculo de gasto de energia
0 - Sair do sistema

Água

Permite calcular o consumo de água com base no tempo do banho.

Também permite consultar, atualizar e excluir cálculos armazenados.

Energia

Permite estimar o consumo de:

Banho
Ar-condicionado
Televisão
Computador
Videogame

Os cálculos também podem ser consultados, atualizados e excluídos.

Observação

Os valores apresentados pelo sistema são estimativas baseadas nas fórmulas e potências definidas no código. O consumo real pode variar de acordo com o equipamento e suas condições de uso.

