# Welcome to My First Python Project

This project focuses on elementary yet fundamental elements for those working with PID controllers.

<div align="center">
  <img src="https://github.com/kiabim/pid-controller-simulator/assets/134725155/14a84dfe-5c3e-43ca-9cba-2b99a69e074d"/>
  </div>

## Objective

<div align="justify">

The main objective of this project is to create a simple simulator for testing continuous systems with a single input and a single output, commonly referred to as SISO systems.
  
  </div>

## The Need for a PID Simulator

<div align="justify">

 For professionals working with PID controllers, it is well-known that many of the techniques used for tuning these controllers rely on empirical approaches, essentially involving trial and error. Consequently, even after applying tuning techniques, there is no guarantee that the system response will meet the user's expectations. Therefore, it becomes crucial to make adjustments to ensure that the user's desired outcome is achieved.
  
  The PID controller consists of three parameters (__Kp__, __Ki__, and __Kd__) that can be adjusted to modify the system's dynamics. The challenge lies in finding the optimal set of these parameters to achieve the desired results. This typically involves conducting successive tests, and the simulator proves to be invaluable in this regard. It aids in declaring variables and qualitatively analyzing the results through visual inspection.

In summary, this project aims to streamline and optimize the operator's time by providing a user-friendly and intuitive graphical interface for executing tests, eliminating the need for programming knowledge.
  
</div>




## How the PID Control Simulator Works
<div align="justify">

Before delving into the simulator's functioning, it's important to grasp the concept of a controller in general, not limited to just the PID controller. A controller receives input information (our reference signal) and makes modifications to the process to ensure the desired output value is achieved. Although it is not always possible due to various factors, that aspect is beyond the scope of this discussion. In essence, if we desire a temperature of X, the controller will work to ensure that the process's temperature reaches X.

To use the simulator effectively, users are required to possess knowledge of the model or plant being controlled. In this context, the process is described by a transfer function, denoted as G(s), which consists of a set of polynomials that mathematically describe the system.

The general form of G(s) is:

$$
G(s) = \frac{numerator}{denominator}
$$

Typically, every process can be mathematically represented by a model to conduct tests before practical implementation. For example, launching a space rocket incurs high production costs and poses significant risks. Therefore, it undergoes a series of simulations using a mathematical model (such as a transfer function or state-space model) to mitigate potential failures before the actual launch.

1. For the simulator, G(s) is formed by a numerator and a denominator, both comprising polynomials. Let's consider an example to clarify the process:

$$
G(s)= \frac{s+2}{s^2+5s +4}
$$

To input the transfer function correctly into the simulator, separate the significant values __by spaces and use commas__, as follows:

$$
G(s) = \frac{num}{den}
$$

$$
\begin{align*}
\text{{num}} &= \{1, 2\} \\
\text{{den}} &= \{1, 3, 5\}
\end{align*}
$$

For further illustration, let's consider another process described by the following transfer function:

$$
G(s)= \frac{6s^3 + 18s^2 + 22s + 155}{44s^4 + 7s^3 + 20s^2 + 13s + 74}
$$

$$
\begin{align*}
\text{{num}} &= \{6, 18, 22, 155\} \\
\text{{den}} &= \{44, 7, 20, 13, 74\}
\end{align*}
$$

2. To evaluate performance over time, the __"SIMULATION TIME"__ must be specified, representing the maximum duration of the simulation.

3. The next three slots are reserved for the PID controller parameters(__"Kp", "Ki", "Kd"__). Users can apply tuning techniques to obtain these parameters and make fine adjustments as necessary. Alternatively, one can choose arbitrary values through trial and error for testing purposes.



4. Regarding the __"INPUT"__, commonly referred to as the setpoint, the unit step function is frequently used in testing environments. The simulator offers three distinct inputs: unit step, square wave, and ramp. Users can select the desired input by modifying the dropdown menu.

5. Once the plant model, simulation time, PID controller parameters, and input signal are specified, the simulator is ready to display the results visually. Simply press the simulation button to initiate the process.

If you wish to make any changes, you can delete and rewrite the respective slots or press the __"CLEAN"__ button to start afresh.

  </div>
<p align="center">
  <img src="https://github.com/kiabim/pid-controller-simulator/assets/134725155/48b791e5-d0b0-4301-80dc-97f08c4cdc6c" alt="Imagem 1"/>
  <img src="https://github.com/kiabim/pid-controller-simulator/assets/134725155/c9343a41-3414-401f-9fa0-00fea7f12aa1" alt="Imagem 2"/>
</p>


