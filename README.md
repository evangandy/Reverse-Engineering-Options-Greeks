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
│   ├── 01_delta_exploration.ipynb     ✅ Delta (Δ) - First derivative basics
│   ├── 02_gamma_exploration.ipynb     ✅ Gamma (Γ) - Second derivative sensitivity  
│   ├── 03_theta_exploration.ipynb     🔄 Theta (Θ) - Time decay modeling
│   ├── 04_vega_exploration.ipynb      📋 Vega (ν) - Volatility sensitivity
│   └── 05_multi_greek_analysis.ipynb  📋 Greek interactions & portfolio effects
└── src/
    ├── __init__.py
    └── formulas.py                     🔄 Core Greek calculation functions
```

## Core Mathematical Concepts

**First Principles:**
- **Delta (Δ)** = ∂C/∂S - Rate of option price change vs. stock price  
- **Gamma (Γ)** = ∂²C/∂S² = ∂Δ/∂S - Rate of delta change vs. stock price
- **Theta (Θ)** = ∂C/∂t - Rate of option price change vs. time
- **Vega (ν)** = ∂C/∂σ - Rate of option price change vs. volatility

**Synthetic Data Challenges:**
- Random noise amplification in second derivatives
- Data consistency between generation and calculation  
- Constraint enforcement (0 ≤ Δ ≤ 1, Γ bounds, natural price floors)
- Multi-variable Greek interactions

## Key Discoveries

- **Gamma extreme sensitivity** - ±$0.01 noise → 40% gamma variation
- **Mathematical consistency critical** - Can't mix generated vs. calculated values
- **Constraint-based modeling** - Work backwards from realistic Greek ranges
- **Visual pattern recognition** - Graphs reveal mathematical relationships

---

*Self-directed quantitative finance exploration using calculus and programming to understand derivative relationships through experimentation.*