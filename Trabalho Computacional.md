# Checklist geral - Apagar após dar check em todos / terminar o EP


- [ ] Informações requisitadas pelo professor para os exercícios 1 e 2 (analisar se o 3 precisa).
	- [ ] Apresentar a solução estimada em cada iteração
	- [ ] Medir tempo computacional de procedimentos
		- [ ] Escrever como a medida foi feita e porque ela é confiável.
		- [ ] Criar gráficos.

- [ ] Comentar código.

- [ ] Escrever fundamentação teórica sobre os métodos de Newton, Broyden e qualquer outro utilizado no projeto (diferenças finitas, jacobianas). Utilizar o RemaniFinal.pdf.
	- [ ] Mostrar quais são as expressões de diferenças finitas de 1a e 2a ordem.
	- [ ] Colocar as referências (Remani e outras referências do Wikipedia).

- [ ] Ter certeza de que cada resultado tem, no relatório, uma base teórica e um comentário se o resultado satisfez ou não as expectativas teóricas.
- [ ] Criar sumário (table of contents)
- [ ] Ter certeza de que as animações funcionam no PDF

## Fundamentação teórica

### Método de Newton

* Descrição geral para uma variável (com fórmula e descrição do algoritmo, usar GIF)
* Descrição para múltiplas variáveis (com fórmula e descrição do algoritmo)
	* Detalhamento em relação ao Jacobiano.
	* Detalhamento em relação ao erro.
	* Tentar encontrar o delta e o k para o problema que o professor deu. (página 70 do livro)

O método de Newton é um método iterativo para encontrar raízes de uma equação matemática. O método de Newton é mais simplesmente descrito para resolver equações de uma variável, mas é mais frequentemente utilizado em sistemas de equações.

##### Uma variável
Para usar o método de Newton, você precisa escolher uma estimativa inicial para a raiz da equação (chamada de $p_0$) e, em seguida, usar essa estimativa para calcular uma nova estimativa mais precisa (chamada de $p_1$). Esse processo é repetido até que a raiz seja encontrada com uma precisão suficiente. A formula de iteração é a seguinte:

$$ p_{n}= p_{n-1} -\frac{f(p_{n-1})}{f'(p_{n-1})} $$

O método de Newton é conhecido por ser rápido e preciso, mas é necessário ter cuidado ao escolher a estimativa inicial, pois ela pode afetar a precisão do resultado final. Além disso, o método de Newton **pode falhar se a derivada da função em algum ponto da iteração não existir** ou **se a estimativa inicial estiver muito longe da raiz verdadeira**.
Essa última ressalva é verdadeira devido a seguinte fórmula:

$$f(p) = f(p_0) + (p-p_0) * f'(p_0) + \frac{(p-p_0)^2}{2} * f''(\varepsilon(p)) $$

Note que, se $p_0$ (ponto inicial) for próximo o suficiente de $p$, o termo quadrático pode ser removido e fórmula de iteração é deduzida manipulando os termos restantes (lembrando que $f(p) = 0$). Entretanto, caso a estimativa inicial seja distante da raiz $p$ de tal forma que o termo quadrático não se torne desprezível, muito dificilmente o método converjirá para alguma solução (salvo situações, onde, por exemplo, a função contém múltiplas raízes e o ponto inicial se aproxima de uma raiz não esperada). 

Animações com demonstração do método para uma variável:

1. Função com o desenho da tangente em cada ponto da iteração
 !["Newton with tangent - GIF"](assets/NewtonIteration_Ani.gif)
 
 2. Método de Newton com o cálculo do erro em relação ao valor verdadeiro da raiz
!["Newton method with absolute error - GIF"](assets/newton-method-with-error.gif)

Note que, na animação acima, a partir de certo ponto $x = x_0$, o erro decresce muito em poucas iterações. 

O algoritmo em Python pode ser encontrado no apêndice.

##### Múltiplas variáveis

O método de Newton para sistemas de equações não lineares é semelhante ao método de Newton para equações de uma variável. A principal diferença é que, em vez de trabalhar com uma única equação, o processo é feito utilizando um sistema de equações.

O processo é o seguinte:

1. Escolha uma estimativa inicial para as raízes do sistema (chamadas de $p_0$).
2. Use a estimativa inicial para calcular uma nova estimativa mais precisa (chamada de $p_1$). Para fazer isso, você precisa resolver o sistema de equações usando a estimativa inicial como valores para as variáveis.
3.  Repita o processo até que a raiz seja encontrada com uma precisão suficiente.

Como no caso de equações de uma variável, é importante escolher uma estimativa inicial razoavelmente próxima das raízes verdadeiras para garantir que o método de Newton funcione corretamente. Além disso, é possível que o método de Newton **falhe se as derivadas parciais da equação não existirem** ou **se a estimativa inicial estiver muito longe das raízes verdadeiras**.

O processo iterativo para o caso de sistemas não lineares é o seguinte:

* Define-se uma função $G$:
  $$G(x) = x - J(x)^{-1}F(x) $$
  Onde $x = x_0$ é a estimativa inicial, $J$ é a matriz jacobiana de $F$ e $F$ é a função a qual deseja-se encontrar a raiz. A seguir, é definida a fórmula de iteração:
 
$$ x^{(k)} = G(x^{(k-1)}) = x^{(k-1)} - J(x^{(k-1)})^{-1}F(x^{(k-1)}) $$

Este é o algoritmo iterativo utilizado para as aplicações-problema do projeto e seu código fonte em Python está no apêndice no final deste documento.


O algoritmo para resolver um sistema de equações não lineares é semelhante, mas envolve a resolução do sistema de equações em cada iteração ao invés de apenas uma equação.

O algoritmo para resolver um sistema de equações não lineares usando o método de Newton é o seguinte:

1. Escolha uma estimativa inicial x0 para as raízes do sistema. x0 é um vetor contendo as estimativas iniciais para cada variável do sistema.
2. Calcule o Jacobiano da função F em x0. O Jacobiano é uma matriz de derivadas parciais que é usada para aproximar o comportamento da função em uma região próxima de x0.
3. Calcule o vetor de residuos R em x0. O vetor de residuos é dado por R(x0) = F(x0).
4. Calcule a correção x1 usando a fórmula: x1 = x0 - Jacobiano^(-1) * R
5. Repita os seguintes passos até que a precisão desejada seja atingida: a. Defina x0 como x1. b. Calcule o Jacobiano da função F em x0. c. Calcule o vetor de residuos R em x0. d. Calcule a correção x1 usando a fórmula: x1 = x0 - Jacobiano^(-1) * R

Onde F é o sistema de equações não lineares e Jacobiano^(-1) é a inversa da matriz Jacobiano.

Qual a importância do jacobiano para esse método?

O Jacobiano é uma matriz de derivadas parciais que é usada no método de Newton para aproximar o comportamento da função em uma região próxima de uma dada estimativa. Ele é uma ferramenta importante para o método de Newton, pois ajuda a encontrar a direção de maior declive da função, o que é essencial para encontrar rapidamente as raízes do sistema.

Sem o Jacobiano, seria necessário calcular as derivadas parciais da função individualmente, o que poderia ser bastante trabalhoso. 

Em resumo, o Jacobiano é um componente importante do método de Newton para sistemas de equações não lineares, pois permite aproximar o comportamento da função de forma rápida e precisa, o que facilita a busca pelas raízes do sistema.

No algoritmo do método de Newton para sistemas de equações não lineares, o vetor de resíduos $R$ é dado por $R(x) = F(x)$, onde $F$ é o sistema de equações não lineares e $x$ é o vetor de variáveis. Portanto, o vetor de resíduos representa o valor das equações no ponto $x$, onde cada resíduo $r^{(n)}$ é definido como $r^{(n)} = F(x^{(n)}) -F(x^{(n-1)})$, para n > 0.

Durante a execução do algoritmo, o objetivo é minimizar o valor do vetor de resíduos até que ele se torne suficientemente pequeno, o que significa que as raízes do sistema foram encontradas com precisão suficiente. Portanto, o comportamento esperado para o vetor de resíduos ao longo da execução do algoritmo é que ele diminua progressivamente até atingir um valor suficientemente pequeno.

Ou seja, 

## APÊNDICE (COLOCAR ALGORITMOS)

1. NEWTON UMA VARIAVEL

algoritmo para resolver uma equação de uma variável usando o método de Newton é o seguinte:
1.  Escolha uma estimativa inicial x0 para a raiz da equação.
2.  Calcule x1 usando a fórmula: x1 = x0 - f(x0) / f'(x0)
3.  Repita os seguintes passos até que a precisão desejada seja atingida: a. Defina x0 como x1. b. Calcule x1 usando a fórmula: x1 = x0 - f(x0) / f'(x0)

Onde f(x) é a equação original e f'(x) é a derivada da equação.
