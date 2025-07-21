# Simple Greeks Learning Project

> 📚 **Reverse Engineering Options Greeks Through Mathematical Modeling**

## Learning Approach

**Mathematical Foundation → Synthetic Data → Problem Discovery → Solution Engineering**

- **Pure math concepts** - Start with derivatives (∂C/∂S, ∂²C/∂S²) and build intuition
- **Reverse engineering** - Work backwards from target Greek values to understand relationships  
- **Controlled experimentation** - Add noise, constraints, and edge cases to test models
- **Problem-driven learning** - Encounter real modeling challenges and develop solutions

## Project Structure

```
Simple Greeks Learning Project/
├── README.md
├── notebooks/
│   ├── 01_delta.ipynb     ✅ Delta (Δ) - First derivative basics
│   ├── 02_gamma.ipynb     ✅ Gamma (Γ) - Second derivative sensitivity  
│   ├── 03_theta.ipynb     ✅ Theta (Θ) - Time decay modeling
│   ├── 04_vega.ipynb      ✅ Vega (ν) - Volatility sensitivity
│   └── 05_rho.ipynb       ✅ Rho (ρ) - Interest rate sensitivity
└── src/
   ├── __init__.py
   └── formulas.py        ✅ Core Greek calculation functions
```

## Core Mathematical Concepts

**First Principles:**

$$\text{Delta } (\Delta) = \frac{\partial C}{\partial S} \text{ - Rate of option price change vs. stock price}$$

$$\text{Gamma } (\Gamma) = \frac{\partial^2 C}{\partial S^2} = \frac{\partial \Delta}{\partial S} \text{ - Rate of delta change vs. stock price}$$

$$\text{Theta } (\Theta) = \frac{\partial C}{\partial t} \text{ - Rate of option price change vs. time}$$

$$\text{Vega } (\nu) = \frac{\partial C}{\partial \sigma} \text{ - Rate of option price change vs. volatility}$$

$$\text{Rho } (\rho) = \frac{\partial C}{\partial r} \text{ - Rate of option price change vs. interest rate}$$

## Learning Journey & Insights

**Project Complete** Key discoveries from reverse-engineering the Greeks:

## Learning Journey & Insights

**Project Complete!** Key discoveries from reverse-engineering the Greeks:

## Learning Journey & Insights

> *In-depth mathematical modeling and analytical solution learnings are documented in the individual notebooks*

**Project Complete!** Key discoveries from reverse-engineering the Greeks:

### 🎯 **Delta (Δ) - Intuitive Greek**
The most accessible Greek to understand - a simple ratio showing how option prices move relative to stock prices. When a stock goes up $1, the option moves by the delta amount. This linear relationship makes it easy to build intuition about derivatives and served as good foundation to start this project.

### ⚡ **Gamma (Γ) - The Sensitivity Amplifier** 
Second derivatives reveal the wild, non-linear nature of options. Gamma amplifies everything - tiny stock moves can cause massive delta swings. This extreme sensitivity to market noise taught me that consistent gamma values might indicate well-behaved securities, while erratic gamma signals could be a massive headache in a high pressure trading situation.

### ⏰ **Theta (Θ) - Time Value**
From my understanding the most mathematically complex Greek, involving intricate time decay mechanics and present value calculations. Theta reveals how options lose value as expiration approaches. The acceleration patterns and connections to risk-free rates make this the most theoretically rich Greek to model.

### 🌊 **Vega (ν) - Volatility**
Volatility changes create the largest price swings, from my learning making vega potentially the most dangerous Greek. Vega could have a range of applications but I thought the most interesting one is as it relates to market psychology.

### 💤 **Rho (ρ) - The Forgotten Greek**
The least impactful Greek for most trading strategies. Interest rate sensitivity only matters during major Fed policy shifts or for long-dated options. While important for theoretical completeness, rho came across as a academic afterthough.

---

## Final Reflections

This project demonstrated that **reverse engineering** complex financial concepts through synthetic data and mathematical modeling creates deeper understanding than traditional textbook approaches. By building each Greek from first principles, starting with simple ratios and evolving into sophisticated derivative relationships, I attempted to uncover the intuitive logic behind options pricing.

*Learning through building beats learning through reading.*
