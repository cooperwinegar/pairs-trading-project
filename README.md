# Pairs Trading Strategy Backtester (In Progress)

This is a Python-based project to implement and test a statistical arbitrage pairs trading strategy.

### Goal
The goal is to identify two co-integrated stocks and trade on the divergence and convergence of their price spread.

### Tech Stack
* **Python**
* **Pandas**
* **statsmodels**
* **yfinance**
* **matplotlib**

### Project Plan / To-Do
- [ ] **Setup:** Initial project setup, virtual env, and GitHub repo.
- [ ] **Data Retrieval:** Download historical price data.
- [ ] **Statistical Testing:** Use `statsmodels` to test for co-integration.
- [ ] **Signal Generation:** Calculate z-score of the spread to generate trade signals.
- [ ] **Backtesting Engine:** Simulate trades and calculate P&L.
- [ ] **Performance Metrics:** Calculate Sharpe Ratio, Max Drawdown, etc.