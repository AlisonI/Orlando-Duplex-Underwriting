# Orlando Duplex Underwriting Model

A Python-based financial underwriting model for evaluating a duplex acquisition in Orlando, FL.

## Metrics Analyzed
- Net Operating Income (NOI)
- Cap Rate
- Cash-on-Cash Return
- Debt Service Coverage Ratio (DSCR)
- 5-Year Internal Rate of Return (IRR)

## Assumptions
- Purchase Price: $185,000
- Down Payment: 25%
- Interest Rate: 7.25% (30-year fixed)
- Rent: $1,250/unit/month
- Vacancy Rate: 5%
- Expense Ratio: 40%
- Hold Period: 5 years
- Exit Cap Rate: 6.5%

## Tools Used
- Python
- NumPy

## How to Run
```bash
python orlando_duplex_underwriting.py
```

## Sample Output
```
=============================================
ORLANDO DUPLEX UNDERWRITING SUMMARY
Purchase Price: $ 185,000
Down Payment (25%): $ 46,250
Loan Amount: $ 138,750
Monthly Payment: $ 947

Gross Rents (Yr 1): $ 30,000
Effective Gross Inc: $ 28,500
Operating Expenses: $ 11,400
NOI: $ 17,100
Annual Debt Service: $ 11,358
Annual Cash Flow: $ 5,742

Cap Rate: 9.24%
Cash-on-Cash Return: 12.41%
DSCR: 1.51x
```

