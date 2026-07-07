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

## Analysis Summary

This duplex appears to be a strong cash-flow investment based on the assumptions used. The property generates a 9.24% cap rate, indicating an above-average yield compared with many residential investment properties. With a DSCR of 1.51x, the net operating income comfortably covers the annual mortgage payments. The projected 12.41% cash-on-cash return means the investor earns approximately 12 cents annually for every dollar invested as a down payment, before taxes and appreciation.

## Pros

- Strong cash-on-cash return (12.4%)
- High DSCR (1.51x) provides a comfortable debt cushion
- Positive annual cash flow of approximately $5,742
- Cap rate above 9% suggests attractive income relative to purchase price

## Things to Verify

- Rental assumptions reflect current market rents
- Operating expenses (taxes, insurance, maintenance, vacancy) are realistic
- Capital expenditures (roof, HVAC, plumbing) are accounted for separately
- Neighborhood fundamentals and long-term appreciation potential
