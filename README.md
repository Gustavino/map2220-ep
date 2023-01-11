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


## 3.  Encontrar o maior número de soluções possíveis, e explicar as estratégias utilizadas, para o seguinte sistema de equações não-lineares:
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




a



Dadas o sistema de equações  
(1)$x_1^2+x_3^2=1$
(2)$x_2^2+x_4^2=1$ 
(3)$x_5x_1x_3^2+x_6x_2x_4^2=0$ 
(4)$x_5x_1^2x_3+x_6x_2^2x_4=0$ 
(5)$x_5x_3^3+x_6x_4^3=0$ 
(6)$x_5x_1^3+x_6x_2^3=0$ 
Com isso temos as funções:  
$f_1(x) = x_1^2+x_3^2-1 = 0$ 
$f_2(x) = x_2^2+x_4^2-1 = 0$ 
$f_3(x) = x_5x_1x_3^2+x_6x_2x_4^2 = 0$ 
$f_4(x) = x_5x_1^2x_3+x_6x_2^2x_4 = 0$ 
$f_5(x) = x_5x_3^3+x_6x_4^3 = 0$ 
$f_6(x) = x_5x_1^3+x_6x_2^3 = 0$ 
Com Jacobiano:  
$$
  \frac {\partial f(x)}{\partial x_i} =   
  \begin{bmatrix}  
    2x_1 & 0 & 2x_3 & 0 & 0 & 0 \\  
    0 & 2x_2 & 0 & 2x_4 & 0 & 0 \\  
    x_5x_3^2 & x_6x_4^2 & 2x_5x_1x_3 & 2x_6x_2x_4 & x_1x_3^2 & x_2x_4^2 \\  
    2x_5x_1x_3 & 2x_6x_2x_4 & x_5x_1^2 & x_6x_2^2 & x_1^2x_3 & x_2^2x_4 \\  
    0 & 0 & 2x_5x_3 & 2x_6x_4 & x_3^3 & x_4^3 \\  
    x_5x1^2 & x_6x2^2 & 0 & 0 & x_1^3 & x_2^3   
  \end{bmatrix}  
 $$
Inicialmente olharemos os intervalos os valores possiveis para as variaveis.  
Por (1) e (2) temos dois circulos de raio 1 logo:  
$x_1 \in [-1,1]$ 
$x_2 \in [-1,1]$ 
$x_3 \in [-1,1]$ 
$x_4 \in [-1,1]$ 
Nos caso demais $x_5 \in \mathbb{R}$ e $x_6 \in \mathbb{R}$.  
Para podermos executar o método de Newton ou Broyden precisamos analisar os caso que impossibilitam a matrix de ser inversível.  
* Caso 1: se $x_1=0$. 
$x_3^2 = 1$ 
$x_2^2+x_4^2 = 1$ 
$x_6x_2x_4^2 = 0$ 
$x_6x_2^2x_4 = 0$ 
$x_5 = \pm x_6x_4^3$ 
$x_6x_2^3 = 0$ 
Então, temos as seguintes soluções:
Se $x_2=0$, então $x = (0, 0, \pm 1, \pm 1, \pm x_6, x_6 )$ 
Se $x_4=0$, então $x = (0, \pm 1, \pm 1, 0, 0, 0 )$ 
Se $x_6=0$, então $x = (0, x_2, \pm 1, \pm \sqrt{1-x_2}, 0, 0 )$ 

* Caso 2: se $x_2=0$. 
$x_1^2+x_3^2 = 1$ 
$x_4^2 = \pm 1$ 
$x_5x_1x_3^2 = 0$ 
$x_5x_1^2x_3 = 0$ 
$x_6 = \pm x_5x_3^3$ 
$x_5x_1^3 = 0$ 
Então, temos as seguintes soluções:
Se $x_1=0$, então $x = (0, 0, \pm 1, \pm 1, \pm x_5, x_5 )$ 
Se $x_3=0$, então $x = (\pm 1, 0, 0, \pm 1, 0, 0 )$
Se $x_5=0$, então $x = (x_1, 0, \pm \sqrt{1-x_1}, \pm 1, 0, 0 )$

* Caso 3: se $x_5=0$. 
$x_1^2+x_3^2-1 = 0$ 
$x_2^2+x_4^2-1 = 0$ 
$x_6x_2x_4^2 = 0$ 
$x_6x_2^2x_4 = 0$ 
$x_6x_4^3 = 0$ 
$x_6x_2^3 = 0$ 
Os casos $x_1 = 0$ ou $x_2 = 0$ ou $x_3 = 0$ ou $x_4 = 0$, já foram cobertos anteriormente restando somente:  
Se $x_6=0$, então $x = (x_1, x_2, \pm \sqrt{1-x_1}, \pm \sqrt{1-x_2}, 0, 0 )$ 
Com isso nos restas achar as soluções $x \neq 0$ que estejam no interior do circulo das funcoes (1) e (2), aí ja poderemos utilizar Newton para achamos as soluções:  
Multiplicando por 3 $f_3$ e $f_4$, e somando $f_3$, $f_4$, $f_5$, $f_6$ temos  
$x_5(x_1+x_3)^3+x_6(x_1+x_3)^3 =0$ 
$x = (x_1, x_2, \pm \sqrt{1-x_1}, \pm \sqrt{1-x_2}, x_5, \pm x5 \frac {(x_1+x_3)^3}{(x_2+x_4)^3}  )$ 
onde   
$x_1 \notin ]-1,1[$ e $x_1 \neq 0$ 
$x_2 \notin ]-1,1[$ e $x_3 \neq 0$ 
$x_5 \in \mathbb{R}$ e $x_5 \neq 0$ 
Outra maneira de resolver o sistema, pode se trocar o método de Newton pelo de Ponto Fixo pois nao depende do Jacobiano para descobrir, teria pior performance porém não precisaríamos nos preocupar se o Jocabiano é inversível ou não

![[Pasted image 20221228180205.png]]

![[Pasted image 20221228180228.png]]

