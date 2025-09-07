# Solid-State Physics Calculation Scripts

This repository contains a collection of Python scripts designed for the analysis of experimental data in the field of solid-state physics and materials science. Each script implements a specific physical model to extract key parameters from linearized experimental plots.

---

## Scripts Included

### 1. Arrhenius Parameter Calculator (`arrhenius_parameter_calculator.py`)

#### **Theoretical Background**

This script analyzes data based on the **Arrhenius equation**, which describes the temperature dependence of reaction rates. It is commonly used to determine the activation energy ($E_a$) of a thermally activated process.

The equation is:
$$
\text{rate} = A \cdot e^{-E_a / (k_B T)}
$$
For analysis, this is often linearized by taking the natural logarithm. When plotting $\ln(\text{rate})$ versus $1000/T$, the equation becomes a straight line:
$$
\ln(\text{rate}) = \ln(A) - \frac{E_a}{1000 \cdot k_B} \left( \frac{1000}{T} \right)
$$

#### **Functionality**
The script calculates the **activation energy ($E_a$)** and the **pre-exponential factor ($A$)** from the slope and y-intercept of this linear plot.

* **Inputs:**
    * `a`: The slope of the `ln(rate)` vs. `1000/T` plot.
    * `b`: The y-intercept.
* **Calculations:**
    * Activation Energy: $E_a = -a \cdot 1000 \cdot k_B$
    * Pre-exponential Factor: $A = e^b$

---

### 2. Mott VRH Parameter Calculator (`mott_vrh_parameter_calculator.py`)

#### **Theoretical Background**

This script is based on the **Mott Variable Range Hopping (VRH)** model, which describes charge transport in disordered materials (like amorphous semiconductors) at low temperatures.

For a 3-dimensional system, the temperature-dependent conductivity ($\sigma$) is given by:
$$
\sigma(T) = \sigma_0 \exp\left[-\left(\frac{T_0}{T}\right)^{1/4}\right]
$$
This equation can be linearized by plotting $\ln(\sigma)$ versus $T^{-1/4}$:
$$
\ln(\sigma) = \ln(\sigma_0) - (T_0)^{1/4} \cdot T^{-1/4}
$$

#### **Functionality**
The script calculates the **characteristic temperature ($T_0$)** and the **conductivity pre-factor ($\sigma_0$)** from the slope and y-intercept of this linear plot.

* **Inputs:**
    * `a`: The slope of the `ln(σ)` vs. `T^(-1/4)` plot.
    * `b`: The y-intercept.
* **Calculations:**
    * Characteristic Temperature: $T_0 = (-a)^4$
    * Pre-factor: $\sigma_0 = e^b$

---

## How to Use

1.  Perform a linear fit on your experimental data according to the appropriate model.
2.  Open the relevant Python script (`.py` file).
3.  Update the values of the `a` (slope) and `b` (intercept) variables at the top of the file.
4.  Run the script to obtain the calculated physical parameters.
