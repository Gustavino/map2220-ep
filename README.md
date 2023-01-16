# Universidade de São Paulo - Instituto de Matemática e Estatística (IME-USP)

## MAP 2220 - Fundamentos de Análise Numérica

### Trabalho Computacional - Métodos numéricos para obtenção de raízes de polinômios

# Como executar

> Requisitos: Python 3.10+, matplotlib, tabulate, numpy, functools, argparse  

#### Comando para configuração do projeto
    pip install matplotlib tabulate numpy functools argparse  

### Descrição
Esse projeto foi organizado de tal forma que seja possível executar seus testes e análises através de linha de comando (shell, cmd, PowerShell, zshell, etc.) em grupos de testes / análises. Por exemplo, para executar todos os testes do relatório para o Método de Newton sem diferenças finitas, utiliza-se:  
```shell
python main.py --method newton --finite_diff False
ou
python main.py -m n -f False
```

A lista de cenários possíveis é a seguinte:
1. **Newton** do Item 1, sem diferenças finitas:
```shell
python main.py --method newton --finite_diff False
ou
python main.py -m n -f False
```
2. **Broyden** do Item 1, sem diferenças finitas:
```shell
python main.py --method broyden --finite_diff False
ou
python main.py -m b -f False
```
3. **Newton** do Item 2, com diferenças finitas:
```shell
python main.py --method newton --finite_diff True
ou
python main.py -m n -f True
```
4. **Broyden** do Item 2, com diferenças finitas:
```shell
python main.py --method broyden --finite_diff True
ou
python main.py -m b -f True
```
5. **Todo** o Item 1, Newton e Broyden sem diferenças finitas:
```shell
python main.py --item 1
ou
python main.py -i 1
```
6. **Todo** o Item 2, Newton e Broyden com diferenças finitas:
```shell
python main.py --item 2
ou
python main.py -i 2
```


# Enunciado
## 1. Dado o seguinte sistema de equações não-lineares, resolver os itens abaixo:

$$\begin{gathered} x_1 x_2+x_1-3 x_5=0 \\\\ 2 x_1 x_2+x_1+3 R_{10} x_2^2+x_2 x_3^2+R_7 x_2 x_3 +R_9 x_2 x_4+R_8 x_2-R
x_5=0, \\\\ 2 x_2 x_3^2+R_7 x_2 x_3+2 R_5 x_3^2+R_6 x_3-8 x_5=0, \\\\ R_9 x_2 x_4+2 x_4^2-4 R x_5=0, \\\\ x_1 x_2+x_1+R_{10}
x_2^2+x_2 x_3^2+R_7 x_2 x_3+R_9 x_2 x_4 +R_8 x_2+R_5 x_3^2+R_6 x_3+x_4^2-1=0 \\\\ 0.0001 \leq x_i \leq 100, \quad i=1,
\ldots, 5 \end{gathered}$$
* $R = 10$
* $R_5=0.193$
* $R_6=4.10622 \times 10^{-4}$
* $R_7= 5.45177 \times 10^{-4}$
* $R_8=4.4975 \times 10^{-7}$
* $R_9=3.40735 \times 10^{-5}$

A solução para o sistema em questão é $(0.003431,31.325636,0.068352,0.859530,0.036963)^T$.

a.  Partindo de $\vec{x}_0=(10,10,10,10,10)$, encontrar a solução para o sistema de equação não-lineares usando o método de Newton. Analisar os resultados (solução estimada, resíduo, convergência e tempo computacional necessário para convergência).

b. Repetir o exercício (a) utilizando o método de Broyden.

c. Comparar os resultados e comentá-los levando em contas as expectativas teóricas.

## 2. Em muitas aplicações, as funções $f_1,\text{ } f_2,\text{ } f_3,\text{ } f_4,\text{ } f_5$ não são conhecidas de forma explícita. Portanto, a matriz Jacobiana precisa ser obtida de forma aproximada, por diferenças finitas.

a. Repetir o problema anterior, utilizando o método de Newton, calculando a Jacobiana pelo método de diferenças finitas por expressões de 1ª e 2ª ordem.

b. Repetir o problema usando o método de Broyden.

c. Comparar os resultados e comentá-los levando em contas as expectativas teóricas.


## 3. Encontrar o maior número de soluções possíveis, e explicar as estratégias utilizadas, para o seguinte sistema de equações não-lineares:
$$
\begin{aligned}
x_1^2+x_3^2 & =1, \\
x_2^2+x_4^2 & =1, \\
x_5 x_3^3+x_6 x_4^3 & =0, \\
x_5 x_1^3+x_6 x_2^3 & =0, \\
x_5 x_1 x_3^2+x_6 x_2 x_4^2 & =0, \\
x_5 x_1^2 x_3+x_6 x_2^2 x_4 & =0 .
\end{aligned}
$$
