from matplotlib.pyplot import plot, show
from numpy import linspace, zeros, exp, array
import scipy.linalg

def heat_eq_1_d_impl(init):
    L = 1.
    a = 1
    T = 10    
    F = 0.5
    Nx = 50

    x = linspace(0, L, Nx + 1)  # mesh points in space
    dx = x[1] - x[0]
    t = linspace(0, T, Nx + 1)  # mesh points in time
    u = zeros(Nx + 1)  # unknown u at new time level
    u_1 = zeros(Nx + 1)  # u at the previous time level
    dt = F * dx ** 2 / a
    Nt = int(round(T / float(dt)))

    # Data structures for the linear system
    A = zeros((Nx + 1, Nx + 1))
    b = zeros(Nx + 1)

    for i in range(1, Nx):
        A[i, i - 1] = -F
        A[i, i + 1] = -F
        A[i, i] = 1 + 2 * F
    A[0, 0] = A[Nx, Nx] = 1

    # Set initial condition u(x,0) = I(x)
    u_1 = array(init)

    for n in range(0, Nt):
        # Compute b and solve linear system
        for i in range(1, Nx):
            b[i] = -u_1[i]
        b[0] = b[Nx] = 0
        u[:] = scipy.linalg.solve(A, b)

        # Update u_1 before next step
        u_1[:] = u
        if n % 10 == 0:
            plot(x, -u_1)
    show()

def initial_conditions(t1, t2, t3, point_num):
    res = [t1] * int(point_num/ 4) + [t2] * int(point_num / 2) + [t3] * int(point_num + 1 / 4)
    return res

res = initial_conditions(0, 1, 0, 51)

heat_eq_1_d_impl(res)
