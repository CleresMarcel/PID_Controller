import numpy as np
from lib import Car, PID, Tank
import matplotlib.pyplot as plt
import control as ctrl


def main():
    # -------- Configuration --------

    # Simulation parameters
    
    time_step = 0.1
    end_time = 25
    length = round(end_time/time_step)

    t = np.zeros(length)
    stp = np.zeros(length)
    v = np.zeros(length)
    command = np.zeros(length)

    # Car parameters

    m = 2140
    b = 0.33
    F_max_0 = 22000
    F_max_max = 1710
    v_max = 72

    # PID parameters

    Kp = 800.0
    Ki = 70.0
    Kaw = 1.0
    Kd = 20.0
    T_C = 1.0

    # LUGAR DAS RAIZES !!!

    num = [Kd, Kp, Ki]
    den = [1, 2, 3, 4]
    test = ctrl.TransferFunction(num, den)
    plt.figure()
    ctrl.root_locus(test)
    plt.title('Root Locus Plot of PID Controller To the car')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.grid(True)
    plt.show()

    # Initialize PID controller
    pid = PID(Kp, Ki, Kd, Kaw, T_C, time_step, F_max_0, 0, 30000)


    # Initialize car with given parameters
    car = Car(m, b, F_max_0, F_max_max, v_max, time_step)

    # Iterate through time steps
    for idx in range(0, length):
        t[idx] = idx*time_step
        # Set setpoint
        stp[idx] = 42
        
        # Execute the control loop
        v[idx] = car.v
        pid.Step(v[idx], stp[idx])
        command[idx] = pid.command_sat
        car.Step(command[idx])  

    # Plot speed response

    plt.subplot(2, 1, 1)
    plt.plot(t, v, label="Response")
    plt.plot(t, stp, '--', label="Setpoint")
    plt.xlabel("Time [s]")
    plt.ylabel("Speed [m/s]")
    plt.legend()
    plt.grid()

    # Plot command force

    plt.subplot(2, 1, 2)
    plt.plot(t, command, label="Command")
    plt.xlabel("Time [s]")
    plt.ylabel("Force [N]")
    plt.legend()
    plt.grid()

    # Display the plots

    plt.show()
    pid.print_pid_equation()

    v[idx] = car.v
    pid.print_pid_function(v[idx], stp[idx])  # Imprimir o valor da função PID
    pid.Step(v[idx], stp[idx])
    command[idx] = pid.command_sat
    car.Step(command[idx])




# PARA O TANQUE:


    time_step = 0.1
    end_time = 25
    length = round(end_time / time_step)

    t = np.zeros(length)
    stp = np.zeros(length)
    level = np.zeros(length)
    command = np.zeros(length)

    # Tank parameters

    A = 2.0  # m^2 (área da seção transversal do tanque)
    Q_out = 0.5  # m^3/s (taxa de saída do tanque)
    max_level = 10  # m (nível máximo do tanque)

    # PID parameters

    Kp = 800.0
    Ki = 70.0
    Kaw = 1.0
    Kd = 20.0
    T_C = 1.0

    # lugar das raizes para o tank.
    num = [Kd, Kp, Ki]
    den = [10, 0.5, 4]
    test = ctrl.TransferFunction(num, den)
    plt.figure()
    ctrl.root_locus(test)
    plt.title('Root Locus Plot of PID Controller to the tank')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.grid(True)
    plt.show()

    # Initialize PID controller
    pid = PID(Kp, Ki, Kd, Kaw, T_C, time_step, 30000, 0, 30000)

    # Initialize tank with given parameters
    tank = Tank(A, Q_out, max_level, time_step)

    # Iterate through time steps
    for idx in range(0, length):
        t[idx] = idx * time_step
        # Set setpoint
        stp[idx] = 42

        # Execute the control loop
        level[idx] = tank.level
        pid.Step(level[idx], stp[idx])
        command[idx] = pid.command_sat
        tank.Step(command[idx])

    # Plot level response

    plt.subplot(2, 1, 1)
    plt.plot(t, level, label="Level")
    plt.plot(t, stp, '--', label="Setpoint")
    plt.xlabel("Time [s]")
    plt.ylabel("Level [m]")
    plt.legend()
    plt.grid()

    # Plot command flow rate

    plt.subplot(2, 1, 2)
    plt.plot(t, command, label="Command")
    plt.xlabel("Time [s]")
    plt.ylabel("Flow Rate [m^3/s]")
    plt.legend()
    plt.grid()

    # Display the plots



    plt.show()




main()

