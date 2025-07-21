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

**Project Complete!** Key discoveries from reverse-engineering the Greeks:

### 🎯 **Delta (Δ) - The Intuitive Greek**
- **Most accessible concept**: Simple ratio of option price change to stock price change
- **Linear relationship**: Direct 1:1 correlation makes it easy to understand and predict
- **Foundation building**: Perfect starting point for understanding derivative relationships
- **Practical application**: Immediate hedge ratio calculations for portfolio management

### ⚡ **Gamma (Γ) - The Sensitivity Amplifier** 
- **Extremely sensitive**: Second derivative creates rapid acceleration effects
- **Consistency indicator**: Stable gamma values may signal reliable, well-behaved securities
- **Risk multiplier**: Small stock moves create disproportionate delta changes
- **Mathematical insight**: Curvature measurement reveals non-linear option behavior

### ⏰ **Theta (Θ) - The Time Value Mystery**
- **Complex time mechanics**: Most mathematically rich Greek involving time value of money
- **Decay acceleration**: Non-linear time decay patterns create fascinating modeling challenges  
- **Financial theory intersection**: Deep connections to present value calculations and risk-free rates
- **Strategic implications**: Time decay strategies form core of many options trading approaches

### 🌊 **Vega (ν) - The High-Leverage Beast**
- **Maximum leverage potential**: Volatility changes create the largest price swings
- **Risk amplification**: Volatility and risk are intrinsically linked, making vega dangerous
- **Market psychology**: Captures fear and greed through uncertainty pricing
- **Modeling complexity**: Requires sophisticated volatility forecasting and regime detection

### 💤 **Rho (ρ) - The Forgotten Greek**
- **Least impactful**: Minimal day-to-day relevance for most trading strategies
- **Interest rate dependency**: Only matters during significant Fed policy changes
- **Long-term bias**: More relevant for LEAPS and long-dated option strategies
- **Academic completeness**: Important for theoretical models but practical afterthought

---

## Final Reflections

This project demonstrated that **reverse engineering** complex financial concepts through synthetic data and mathematical modeling creates deeper understanding than traditional textbook approaches. By building each Greek from first principles—starting with simple ratios and evolving into sophisticated derivative relationships—we uncovered the intuitive logic behind options pricing.

The Greeks are no longer mysterious black box formulas—they're logical extensions of basic mathematical relationships that any motivated learner can understand, implement, and apply.

*Learning through building beats learning through reading.*