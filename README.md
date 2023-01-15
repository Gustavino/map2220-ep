# Universidade de São Paulo - Instituto de Matemática e Estatística (IME-USP)

## MAP 2220 - Fundamentos de Análise Numérica

### Trabalho Computacional - Métodos numéricos para obtenção de raízes de polinômios

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
