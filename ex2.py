from enum import Enum
from functools import partial
from typing import List, Union

import numpy as np

from ex1 import exercise_function, broyden, newton
from utils.utils import unwrap_matrix_as_list


class Order(Enum):
    FIRST = 1
    SECOND = 2


def jacobian_with_finite_differences(
        function: callable, order: Order, step_size: float, func_values: Union[List[float], np.matrix]
):
    def forward_differences(row, indicator, step):
        return (function(values + indicator * step)[row] - function(values)[row]) / step

    def second_order(row, indicator, step):
        return (function(values + indicator * step)[row] - function(
            values - indicator * step)[row]) / (2 * step)

    # todo: olhar o erro abaixo
    raise NotImplementedError("dar uma olhada no forward differences e no centered differences")

    values = func_values if not type(func_values) is np.matrix else unwrap_matrix_as_list(func_values)
    order = forward_differences if order == Order.FIRST else second_order

    num_of_columns = len(values)
    num_of_rows = len(function(values))

    jacobian = np.zeros(num_of_rows * num_of_columns).reshape(num_of_rows, num_of_columns)
    for row in range(num_of_rows):
        for column in range(num_of_columns):
            indicator = np.zeros(num_of_columns)
            indicator[column] = 1
            jacobian[row][column] = order(row, indicator, step_size)

    return jacobian


# todo: a alma desse exercício 2 é entender a influência da jacobiana na velocidade de convergência e como
#  aproximações melhores ou piores podem divergir dos valores exatos em relação a velocidade de convergência.
#  Escrever teste que varia o passo h, printa as jacobianas e as velocidades de convergência.
#  Criar gráficos que expressem a convergência dos resultados em função dos passos e comparar com o valor exato da jacobiana.
def _main():
    # order = Order.FIRST
    # todo: relatorio: para valores muito pequenos -> singular matrix.
    # todo: relatorio: para valores bons (definir intervalo) -> de 12 a 14 iterações
    # todo: relatorio: para valores crescentes -> mais e mais iterações até não convergir mais.

    order = Order.SECOND
    # todo: relatorio: comparar mesmo valores de step para os dois tipos de derivada (first e second order).
    # todo: relatorio: para valores muito pequenos -> aumenta o numero de iteracoes (erro aumenta em que parte?)
    #  ate chegar em singular matrix.
    # todo: relatorio: para valores bons (definir intervalo: 0.001 ate 0.00000000001?) -> de 12 a 14 iterações
    # todo: relatorio: para valores crescentes -> mais e mais iterações até não convergir mais.
    # todo: qualquer valor funciona?!?!?!
    # todo: aparentemente, o de segunda ordem é mais estável em torno de uma solução. Isto é, muitos valores de passo resultam na mesma quantidade de iterações.
    #  @Entender a relação entre quantidade de passos, jacobiano e velocidade de convergência@.
    #  Existem pontos onde há aprimoração, porém são complexos de serem encontrados.
    #  Por exemplo, de 1e-1 até 1e-9 resulta em 19 iterações, mas 1e-10 faz em 17 iteraões,
    #   e de 1e-11 até 1e-15 volta pra 19, depois disso é matriz não inversível.

    step_size = 0.0000001
    jacobian = partial(jacobian_with_finite_differences, exercise_function, order, step_size)

    x_0 = [10., 10., 10., 10., 10.]
    result = newton(x_0, exercise_function, jacobian, 1e-10)
    print(f"A solução para esse sistema de equações, utilizando o método de Newton, é: {result}.")

    # x_0 = np.matrix([10., 10., 10., 10., 10.]).T
    x_0 = np.matrix([1., 30., 1., 1., 1.]).T
    result = broyden(x_0, exercise_function, jacobian, 1e-10)
    print(f"A solução para esse sistema de equações, utilizando o método de Broyden, é: {result}.")


if __name__ == '__main__':
    _main()
