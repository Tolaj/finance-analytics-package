# 📘 finanalytics  
### Professional Python Toolkit for Financial Mathematics & Quantitative Finance

![License](https://img.shields.io/badge/license-MIT-blue.svg)  
![Python](https://img.shields.io/badge/python-3.9+-blue)  
![Status](https://img.shields.io/badge/status-active-success)

---

## 📄 Documentation

See full documentation and guidelines:

- **Contribution Guidelines** → [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)  
- **Commit Rules** → [docs/COMMIT_RULES.md](docs/COMMIT_RULES.md)  
- **Code of Conduct** → [docs/CODE_OF_CONDUCT.md](docs/CODE_OF_CONDUCT.md)  
- **Bug Report Template** → [.github/ISSUE_TEMPLATE/bug_report.md](.github/ISSUE_TEMPLATE/bug_report.md)  
- **Feature Request Template** → [.github/ISSUE_TEMPLATE/feature_request.md](.github/ISSUE_TEMPLATE/feature_request.md)  
- **Pull Request Template** → [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md)



---
## 📌 Overview  
finanalytics is a comprehensive Python package for performing core financial analytics, including:

- Time value of money  
- Cash flow evaluation (IRR, NPV, Payback)  
- Loan amortization  
- Depreciation  
- Bond valuation  
- Financial visualization  

Ideal for:
- Finance students  
- Analysts  
- Academics  
- Business professionals  

---

## 📂 Package Structure
```
finanalytics/
│── time_value.py
│── cashflow.py
│── loans.py
│── depreciation.py
│── bonds.py
│── visualization.py
│── __init__.py
docs/
│── CONTRIBUTING.md
│── CODE_OF_CONDUCT.md
│── COMMIT_RULES.md
.github/
│── ISSUE_TEMPLATE/
│   ├── bug_report.md
│   └── feature_request.md
│── PULL_REQUEST_TEMPLATE.md
```

---

## 🔧 Installation
pip install numpy matplotlib

Clone the repository:

git clone https://github.com/<your-username>/finanalytics
cd finanalytics

---

## 🧠 Usage Example
from finanalytics.time_value import future_value

print(future_value(1000, 0.08, 5))

---

## 📄 Documentation
See full documentation:

- Contribution Guidelines → docs/CONTRIBUTING.md  
- Commit Rules → docs/COMMIT_RULES.md  
- Code of Conduct → docs/CODE_OF_CONDUCT.md  

---

## 🧪 Examples
Run examples:

python examples/demo_examples.py

---

## 📜 License  
MIT License
