# Checklist geral - Apagar após dar check em todos / terminar o EP


- [ ] Informações requisitadas pelo professor para os exercícios 1 e 2 (analisar se o 3 precisa).
    - [ ] Apresentar a solução estimada em cada iteração
    - [ ] Medir tempo computacional de procedimentos
        - [ ] Escrever como a medida foi feita e porque ela é confiável.
        - [ ] Criar gráficos.

- [ ] Comentar código.

- [x] Escrever fundamentação teórica
    - [x] Newton (e Jacobiana)
    - [x] Broyden
    - [x] Diferenças finitas
- [ ] Colocar as referências (RemaniFinal.pdf e outras referências do Wikipedia).

- [ ] Ter certeza de que cada resultado tem, no relatório, uma base teórica e um comentário se o resultado satisfez ou não as expectativas teóricas.
- [ ] Criar sumário (table of contents)
- [ ] Ter certeza de que as animações funcionam no PDF
- [ ] Explicitar as especificações do computador onde os tempos foram testados

# Fundamentação teórica

## Método de Newton

O método de Newton é um método iterativo para encontrar raízes de uma equação matemática. O método de Newton é mais simplesmente descrito para resolver equações
de uma variável, mas é mais frequentemente utilizado em sistemas de equações.

### Uma variável
Para usar o método de Newton, você precisa escolher uma estimativa inicial para a raiz da equação (chamada de $p_0$) e, em seguida, usar essa estimativa para 
calcular uma nova estimativa mais precisa (chamada de $p_1$). Esse processo é repetido até que a raiz seja encontrada com uma precisão suficiente. A formula de 
iteração é a seguinte:

$$ p_{n}= p_{n-1} -\frac{f(p_{n-1})}{f'(p_{n-1})} $$

O método de Newton é conhecido por ser rápido e preciso, mas é necessário ter cuidado ao escolher a estimativa inicial, pois ela pode afetar a precisão do 
resultado final. Além disso, o método de Newton **pode falhar se a derivada da função em algum ponto da iteração não existir** ou **se a estimativa inicial 
estiver muito longe da raiz verdadeira**.
Essa última ressalva é verdadeira devido a seguinte fórmula:

$$f(p) = f(p_0) + (p-p_0) * f'(p_0) + \frac{(p-p_0)^2}{2} * f''(\varepsilon(p)) $$

Note que, se $p_0$ (ponto inicial) for próximo o suficiente de $p$, o termo quadrático pode ser removido e fórmula de iteração é deduzida manipulando os termos 
restantes (lembrando que $f(p) = 0$). Entretanto, caso a estimativa inicial seja distante da raiz $p$ de tal forma que o termo quadrático não se torne 
desprezível, muito dificilmente o método converjirá para alguma solução (salvo situações, onde, por exemplo, a função contém múltiplas raízes e o ponto 
inicial se aproxima de uma raiz não esperada). 

Animações com demonstração do método para uma variável:

1. Função com o desenho da tangente em cada ponto da iteração  
   !["Newton with tangent - GIF"](assets/NewtonIteration_Ani.gif)
 
2. Método de Newton com o cálculo do erro em relação ao valor verdadeiro da raiz  
   !["Newton method with absolute error - GIF"](assets/newton-method-with-error.gif)

Note que, na animação acima, a partir de certo ponto $x = x_0$, o erro decresce muito em poucas iterações. 

O algoritmo em Python pode ser encontrado no apêndice.

### Múltiplas variáveis

O método de Newton para sistemas de equações não lineares é semelhante ao método de Newton para equações de uma variável. A principal diferença é que, em vez de
trabalhar com uma única equação, o processo é feito utilizando um sistema de equações.

O processo é o seguinte:

1. Escolha uma estimativa inicial para as raízes do sistema (chamadas de $p_0$).
2. Use a estimativa inicial para calcular uma nova estimativa mais precisa (chamada de $p_1$). Para fazer isso, você precisa resolver o sistema de equações 
   usando a estimativa inicial como valores para as variáveis.
3.  Repita o processo até que a raiz seja encontrada com uma precisão suficiente.

Como no caso de equações de uma variável, é importante escolher uma estimativa inicial razoavelmente próxima das raízes verdadeiras para garantir que o método 
de Newton funcione corretamente. Além disso, é possível que o método de Newton **falhe se as derivadas parciais da equação não existirem** ou **se a estimativa 
inicial estiver muito longe das raízes verdadeiras**.

O processo iterativo para o caso de sistemas não lineares é o seguinte:

* Define-se uma função $G$:
  $$G(x) = x - J(x)^{-1}F(x)$$
 Onde $x = x_0$ é a estimativa inicial, $J$ é a matriz jacobiana de $F$ e $F$ é a função a qual deseja-se encontrar a raiz. A seguir, é definida a 
  fórmula de iteração:
 
$$x^{(k)} = G(x^{(k-1)}) = x^{(k-1)} - J(x^{(k-1)})^{-1}F(x^{(k-1)})$$
 Este é o algoritmo iterativo utilizado para as aplicações-problema do projeto e seu código fonte em Python está no apêndice no final deste documento.

* **Qual a importância do jacobiano para esse método?**
  
  O Jacobiano é uma matriz de derivadas parciais que é usada no método de Newton para aproximar o comportamento da função em uma região próxima de uma dada 
  estimativa. Ele é uma ferramenta importante para o método de Newton, pois ajuda a encontrar a direção de maior declive da função, o que é essencial para 
  encontrar rapidamente as raízes do sistema.
  
  Sem o Jacobiano, seria necessário calcular as derivadas parciais da função individualmente, o que poderia ser bastante trabalhoso. 
  
  Em resumo, o Jacobiano é um componente importante do método de Newton para sistemas de equações não lineares, pois permite aproximar o comportamento da função
  de forma rápida e precisa, o que facilita a busca pelas raízes do sistema.
  

* **Como é caracterizado o vetor de resíduos?**  
  
  No algoritmo do método de Newton para sistemas de equações não lineares, o vetor de resíduos $R$ é dado por $R(x) = r^{(n)} = F(x^{(n)}) -F(x^{(n-1)})$, para 
  $n>0$ onde $F$ é o sistema de equações não lineares e $x$ é o vetor de variáveis.
  
  Durante a execução do algoritmo, o objetivo é minimizar o valor do vetor de resíduos até que ele se torne suficientemente pequeno, o que significa que as 
  raízes do sistema foram encontradas com precisão suficiente. Portanto, o comportamento esperado para o vetor de resíduos ao longo da execução do algoritmo é 
  que ele diminua progressivamente até atingir um valor suficientemente pequeno.


* **Como é calculada a convergência?**  
  A convergência do método de Newton pode ser definida como a diferença entre dois resíduos subsequentes ($|r^{(n)} - r^{(n-1)}| < TOL$, onde $TOL$ é a 
  tolerância de precisão) ou, como implementado no algoritmo utilizado nos resultados desse relatório, alguma norma aplicada sobre o vetor $y$ solução do 
  sistema de equações $J(x)y = -F(x)$.  
  O vetor $y$ pode ser interpretado como o passo e, uma vez que sua norma é pequena o suficiente, 
  pode-se dizer que o algoritmo convergiu. 
  
## Método de Broyden

O método de Broyden é um método iterativo para encontrar raízes de equações não lineares. Ele é semelhante ao método de Newton, 
mas em vez de calcular a inversa da matriz Jacobiana em cada iteração, o método de Broyden usa uma aproximação da matriz Jacobiana. Devido a essa aproximação, 
o método de Broyden é categorizado como um método quasi-Newton.  
O método é particularmente útil para casos onde é difícil calcular a matriz Jacobiana exata ou onde ela é muito cara de calcular.  
O método de Broyden é uma generalização para maiores dimensões do **método das secantes**.
* **Desempenho vs Newton**:  
  Em notação Big O, o número de cálculos necessários para o método de Newton é $O(n^3)$, onde $n$ é o número de incógnitas. 
  Isso se deve ao fato de que é necessário calcular a inversa da matriz Jacobiana, que é uma operação de complexidade $O(n^3)$ para matrizes $n{\times}n$.  
  
  Em contrapartida, o número de cálculos necessários para o método de Broyden é $O(n^2)$.  
  Isso acontece porque, em vez de calcular a inversa da matriz Jacobiana, o método de Broyden usa uma aproximação da matriz Jacobiana e atualiza essa 
  aproximação a cada iteração. Essas operações são de complexidade $O(n^2)$.
  
O algoritmo implementando o método de Broyden está localizado no apêndice.

## Diferenças finitas
Diferenças finitas é uma técnica numérica utilizada para aproximar derivadas de uma função em um ponto específico. Ela consiste em utilizar a diferença entre o
valor da função em um ponto e o valor da função em um ponto próximo, dividida pela diferença entre os pontos, para obter uma aproximação da derivada.  

A aproximação obtida é chamada de diferença finita, e a precisão da aproximação depende da diferença entre os pontos. Para uma boa precisão, 
é necessário tornar o passo $h$ muito pequeno
Diferenças finitas são comumente utilizadas para calcular derivadas de funções que não podem ser derivadas analiticamente, ou para obter derivadas aproximadas 
de funções que são difíceis de serem derivadas analiticamente.

As diferenças finitas utilizadas no projeto, a pedido do enunciado, foram as seguintes: 

* Forward differences:
$$f'(x_0) = \frac{f(x_0 + h) - f(x_0)}{h} - \frac{h}{2} f''(\varepsilon)$$
  
* Centered differences:
$$f'(x_0) = \frac{1}{2h}[f(x_0 + h) - f(x_0 - h)] - \frac{h^2}{6} f^{(3)}(\varepsilon_1)$$

As diferenças centrais têm como termo dominante do erro $O(n^2)$, portanto, é esperado que seja mais precisa devido ao seu menor erro de truncamento.  

# Resolução dos exercícios e resultados

## Item 1

> a. Partindo de $\vec{x}_0=(10,10,10,10,10)$, encontrar a solução para o sistema de equação não-lineares usando o método de Newton. Analisar os resultados 
> (solução estimada, resíduo, convergência e tempo computacional necessário para convergência).

## APÊNDICE (COLOCAR ALGORITMOS)

1. NEWTON UMA VARIAVEL

algoritmo para resolver uma equação de uma variável usando o método de Newton é o seguinte:
1.  Escolha uma estimativa inicial x0 para a raiz da equação.
2.  Calcule x1 usando a fórmula: x1 = x0 - f(x0) / f'(x0)
3.  Repita os seguintes passos até que a precisão desejada seja atingida: a. Defina x0 como x1. b. Calcule x1 usando a fórmula: x1 = x0 - f(x0) / f'(x0)

Onde f(x) é a equação original e f'(x) é a derivada da equação.

2. newton multiplas variaveis

3. broyden
