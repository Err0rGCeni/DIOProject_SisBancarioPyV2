# Otimizando o Sistema Bancário com Funções Python

Desafio introdutório de Python para criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

## Depósito

- Depositar valores positivos na conta;
- Apenas 1 usuário;
- Depósitos armazenados e exibidos na operação de extrato;

## Saque

- 3 Saques diários com limite máximo de R$ 500,00;
- Informar ao usuário caso não tenha saldo suficiente em conta.
- Saques armazenados e exibidos na operação de extrato;

## Extrato

- Listar todos os depósitos e saques realizados na conta;
- Ao fim, exibir o saldo atual da conta;
- Se extrato em branco, exibir mensagem;
- Valores no formato R$ xxx.xx;

## Otimização

- Separar as funções existentes de saque, depósito e extrato em funções.
- **Saque**:
  - Receber argumentos apenas por nome (keyword only): saldo, valor, extrato, limite, numero_saques, limite_saques.
  - Retorno: saldo e extrato.
- **Depósito**:
  - Receber argumentos apenas por posição (positional only): saldo, valor, extrato.
  - Retorno: saldo e extrato.
- **Extrato**:
  - Receber argumentos por posição e nome (positional: saldo e keyword: extrato)
- Nova função: **Cadastrar usuário**;
  - Armazenar os usuários em uma lista (nome, data de nascimento, cpf:number e endereço:string);
- Nova Função: **Cadastrar conta bancária** (vinculada a um usuário);
  - Armazenar contas em uma lista (agência:string, número:sequential number, usuário).
