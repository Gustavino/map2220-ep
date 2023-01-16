import argparse

from broyden.ex1 import ex1_broyden_procedures
from broyden.ex2 import ex2_broyden_procedures
from newton.ex1 import ex1_newton_procedures
from newton.ex2 import ex2_newton_procedures


def newton_1_procedures():
    print("## SOLUÇÃO ##")
    ex1_newton_procedures.estimate_solution()
    print()
    print("## RESÍDUO ##")
    ex1_newton_procedures.estimate_residual()
    print()
    print("## TEMPO ##")
    ex1_newton_procedures.simulate_time_for_newton()


def broyden_1_procedures():
    print("## LIMITES DO DOMINIO DE BROYDEN ##")
    ex1_broyden_procedures.simulate_domain_limits_for_broyden()
    print()
    print("## SOLUÇÃO ##")
    ex1_broyden_procedures.estimate_solution()
    print()
    print("## RESÍDUO ##")
    ex1_broyden_procedures.estimate_residual()
    print()
    print("## TEMPO ##")
    ex1_broyden_procedures.simulate_time_for_broyden()


def newton_2_procedures():
    print("## PASSOS DO JACOBIANO ##")
    ex2_newton_procedures.simulate_jacobian_steps()
    print()
    print("## SOLUÇÃO ##")
    ex2_newton_procedures.estimate_solution()
    print()
    print("## RESÍDUO ##")
    ex2_newton_procedures.estimate_residual()
    print()
    print("## TEMPO ##")
    ex2_newton_procedures.simulate_time_for_newton()


def broyden_2_procedures():
    print("## LIMITES DO DOMINIO DE BROYDEN ##")
    ex2_broyden_procedures.simulate_domain_limits_for_broyden()
    print()
    print("## PASSOS DO JACOBIANO ##")
    ex2_broyden_procedures.simulate_jacobian_steps()
    print()
    print("## SOLUÇÃO ##")
    ex2_broyden_procedures.estimate_solution()
    print()
    print("## RESÍDUO ##")
    ex2_broyden_procedures.estimate_residual()
    print()
    print("## TEMPO ##")
    ex2_broyden_procedures.simulate_time_for_broyden()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", metavar="", required=False, help="Method (Broyden or Newton) in which the analysis should be "
                                                                           "done.")
    parser.add_argument("-f", "--finite_diff", metavar="", required=False, type=lambda x: (str(x).lower() == 'true'),
                        help="Whether the jacobian should be calculated using finite differences or not.")
    parser.add_argument("-i", "--item", metavar="", required=False, help="Can replace the --method parameter. The values can be 1 or 2.")
    return parser.parse_args()


def run_analysis(args):
    if args.method:
        if args.finite_diff is None:
            raise NameError(
                "Parâmetro incorreto. Quando utilizando -m ou --method, é necessário enviar {-f / -finite_diff} {False / True}.")

        use_finite_differences = args.finite_diff
        if use_finite_differences:
            if args.method == 'newton' or args.method == 'n':
                newton_2_procedures()
            else:
                broyden_2_procedures()
        else:
            if args.method == 'newton' or args.method == 'n':
                newton_1_procedures()
            elif args.method == 'broyden' or args.method == 'b':
                broyden_1_procedures()
            else:
                raise NameError("Parâmetro incorreto. Sua lista de parâmetros deve conter '-m n' / '-m newton' ou '-m b' / '-m broyden'.")
    elif args.item:
        if args.item == "1":
            print("@@@@ PROCEDIMENTOS DE NEWTON @@@@")
            newton_1_procedures()
            print("@@@@ PROCEDIMENTOS DE BROYDEN @@@@")
            broyden_1_procedures()
        elif args.item == "2":
            print("@@@@ PROCEDIMENTOS DE NEWTON @@@@")
            newton_2_procedures()
            print("@@@@ PROCEDIMENTOS DE BROYDEN @@@@")
            broyden_2_procedures()
        else:
            raise NameError("Parâmetro incorreto. O valor de --item ou -i deve ser 1 ou 2.")
    else:
        raise NameError("Parâmetro incorreto ou faltando. Sua lista de parâmetros deve conter '-m n' / '-m newton', '-m b' / '-m broyden' "
                        "ou '-i 1' / '-i 2'.")


def _main():
    args = get_args()
    run_analysis(args)


if __name__ == '__main__':
    _main()
