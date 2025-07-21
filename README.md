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
│   └── 05_rho.ipynb       🔄 Rho (ρ) - Interest rate sensitivity
└── src/
   ├── __init__.py
   └── formulas.py        🔄 Core Greek calculation functions
```

## Core Mathematical Concepts

**First Principles:**

$$\text{Delta } (\Delta) = \frac{\partial C}{\partial S} \text{ - Rate of option price change vs. stock price}$$

$$\text{Gamma } (\Gamma) = \frac{\partial^2 C}{\partial S^2} = \frac{\partial \Delta}{\partial S} \text{ - Rate of delta change vs. stock price}$$

$$\text{Theta } (\Theta) = \frac{\partial C}{\partial t} \text{ - Rate of option price change vs. time}$$

$$\text{Vega } (\nu) = \frac{\partial C}{\partial \sigma} \text{ - Rate of option price change vs. volatility}$$

## Learning Journey & Insights

**Coming Soon:**

- 🚧 This section will document key discoveries and technical takeaways after project completion
- 📝 Will include insights on delta dynamics, gamma behavior, theta decay patterns, and volatility effects
- 🔍 Mathematical intuition and connections between derivatives and market behavior
- 💡 Technical implementation details and optimization approaches

---

*Self-directed quantitative finance exploration using calculus and programming to understand derivative relationships through experimentation.*