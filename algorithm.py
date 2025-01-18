import numpy as np
def GD(g, omega, lmbda):
    """
    Gradient Descent algorithm
    Args:
        g: masked image of size (M, N, 3)
        omega: Binary mask of size (M, N) indicating missing regions (1 for missing, 0 otherwise).
        lmbda: Regularization parameter controlling the smoothness of the solution
    Returns:
        numpy.ndarray: Inpainted image of size (M, N, 3).
    """
    num_iterations = 20000
    alpha = 0.01
    u = g.copy()
    M, N, _ = u.shape

    for iteration in range(num_iterations):
        gradient = np.zeros((M, N, 3))
        for c in range(3):
            data_term = 2 * omega * (u[:, :, c] - g[:, :, c])
            reg_term = np.zeros((M, N))
            # pixels without constraints
            reg_term[:-1, :-1] = -2 * lmbda * ((u[1:, :-1, c] - u[:-1, :-1, c]) + (u[:-1, 1:, c] - u[:-1, :-1, c]))
            # pixels on the right border
            reg_term[:-1, -1] = -2 * lmbda * (u[1:, -1, c] - u[:-1, -1, c])
            # pixels on the bottom border
            reg_term[-1, :-1] = -2 * lmbda * (u[-1, 1:, c] - u[-1, :-1, c])
            # pixel on the bottom right corner
            reg_term[-1, -1] = 0   
            gradient[:, :, c] = data_term + reg_term

        gradientMag = np.linalg.norm(gradient)
        u -= alpha * gradient
        if iteration == num_iterations - 1:
            print(f"Final Gradient Magnitude: {gradientMag:.4e}")

    return u