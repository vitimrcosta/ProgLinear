# ProgLinear - Maximização de Lucro com Programação Linear

Este projeto resolve um problema de programação linear para maximizar o lucro de uma fábrica que produz dois tipos de peças (A e B), considerando restrições de tempo de produção e capacidade de armazenamento.

---

## **Descrição do Problema**

Uma fábrica produz dois tipos de peças, A e B. O lucro por unidade da peça A é de R$ 120,00, enquanto o lucro por unidade da peça B é de R$ 140,00. Para fabricar uma unidade da peça A, a empresa precisa de 3 horas, e para fabricar uma unidade da peça B, são necessárias 2 horas. A disponibilidade total de tempo de produção é de 150 horas por mês. Além disso, devido à capacidade de armazenamento e demanda do mercado, a produção mensal não pode exceder 50 unidades da peça A e 40 unidades da peça B.

O objetivo é determinar quantas unidades de cada peça devem ser produzidas para maximizar o lucro total.

---

## **Solução**

O problema foi resolvido usando **programação linear** com a biblioteca **PuLP** em Python. A solução encontra os valores ótimos de produção para as peças A e B, considerando as restrições de tempo e capacidade.

---

## **Como Executar o Código**

### **Pré-requisitos**
1. Instale o Python 3.x: [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Instale a biblioteca PuLP:
   ```bash
   pip install pulp
3. Para compilar o programa
   ````python maximizar_lucro.py