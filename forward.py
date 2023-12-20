from sympy import *

# define theta symbols
theta_list = symbols('theta_0:7')

# define DH parameters table: d/theta/a/alpha
DH_table = Matrix([
    [1000, pi/2 + theta_list[1], 0, pi/2],
    [1000, pi + theta_list[2], 0, pi/2],
    [1000, pi/2 + theta_list[3], 5200, pi],
    [1000, theta_list[4], 5200, pi],
    [1000, -pi/2 + theta_list[5], 0, pi/2],
    [0, theta_list[6], 0, pi/2]
])

# define symbols
theta, alpha, a, d = symbols('theta alpha a d')

# define transform matrix
T_sym = Matrix([
    [cos(theta), -cos(alpha) * sin(theta),
     sin(alpha) * sin(theta), a * cos(theta)],
    [sin(theta), cos(alpha) * cos(theta),
     -sin(alpha) * cos(theta), a * sin(theta)],
    [0, sin(alpha), cos(alpha), d],
    [0, 0, 0, 1]
])

# print("The symbol transform matrix is:\n")
# print(print_latex(T_sym))

# define specific transform matrix from T0 to T6
T_spe = []
for i in range(6):
    T_spe += [T_sym.subs([(d, DH_table[i, 0]), (theta, DH_table[i, 1]),
                          (a, DH_table[i, 2]), (alpha, DH_table[i, 3])])]

# print("The specific transform matrix is:\n")
# print(print_latex(T_spe))

# multiply matrix
T_result = eye(4)
for i in range(6):
    T_result *= T_spe[i]

T_result = simplify(T_result)

print(print_latex(T_result))
