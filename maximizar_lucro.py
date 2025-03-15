# Importar a biblioteca PuLP
import pulp

# Definir o problema de maximização
problema = pulp.LpProblem("Maximizar_Lucro", pulp.LpMaximize)

# Definir as variáveis de decisão (x e y devem ser inteiros e não negativos)
x = pulp.LpVariable('x', lowBound=0, cat='Integer')  # Quantidade da peça A
y = pulp.LpVariable('y', lowBound=0, cat='Integer')  # Quantidade da peça B

# Definir a função objetivo (maximizar o lucro)
problema += 120 * x + 140 * y, "Lucro"

# Adicionar as restrições
problema += 3 * x + 2 * y <= 150, "Restricao_Tempo"
problema += x <= 50, "Restricao_Peca_A"
problema += y <= 40, "Restricao_Peca_B"

# Resolver o problema
problema.solve()

# Exibir os resultados
print(f"Status: {pulp.LpStatus[problema.status]}")
print(f"Quantidade da peça A (x): {pulp.value(x)}")
print(f"Quantidade da peça B (y): {pulp.value(y)}")
print(f"Lucro máximo: R$ {pulp.value(problema.objective)}")