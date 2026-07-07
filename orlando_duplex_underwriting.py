import numpy as np

# ── Property Inputs ──────────────────────────────────────
purchase_price = 185000
down_payment_pct = 0.25
interest_rate = 0.0725
loan_term_years = 30
units = 2
rent_per_unit = 1250
vacancy_rate = 0.05
hold_years = 5
exit_cap_rate = 0.065
annual_rent_growth = 0.03
annual_expense_growth = 0.02

# ── Financing ────────────────────────────────────────────
down_payment = purchase_price * down_payment_pct
loan_amount = purchase_price - down_payment
monthly_rate = interest_rate / 12
n_payments = loan_term_years * 12
monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate)**n_payments) / ((1 + monthly_rate)**n_payments - 1)
annual_debt_service = monthly_payment * 12

# ── Year 1 Income & Expenses ─────────────────────────────
gross_rents = rent_per_unit * units * 12
effective_gross_income = gross_rents * (1 - vacancy_rate)
operating_expenses = effective_gross_income * 0.40
noi = effective_gross_income - operating_expenses

# ── Key Metrics ──────────────────────────────────────────
cap_rate = noi / purchase_price
cash_flow = noi - annual_debt_service
coc_return = cash_flow / down_payment
dscr = noi / annual_debt_service

# ── IRR Analysis ─────────────────────────────────────────
cash_flows = [-down_payment]
for year in range(1, hold_years + 1):
    yr_noi = noi * ((1 + annual_rent_growth) ** (year - 1))
    yr_cf = yr_noi - annual_debt_service
    if year == hold_years:
        exit_noi = noi * ((1 + annual_rent_growth) ** hold_years)
        exit_value = exit_noi / exit_cap_rate
        remaining_balance = loan_amount * ((1 + monthly_rate)**(n_payments) - (1 + monthly_rate)**(hold_years*12)) / ((1 + monthly_rate)**n_payments - 1)
        net_proceeds = exit_value - remaining_balance
        yr_cf += net_proceeds
    cash_flows.append(yr_cf)

irr = np.irr(cash_flows) if hasattr(np, 'irr') else None

# ── Print Results ────────────────────────────────────────
print("=" * 45)
print("   ORLANDO DUPLEX UNDERWRITING SUMMARY")
print("=" * 45)
print(f"Purchase Price:        ${purchase_price:>10,.0f}")
print(f"Down Payment (25%):    ${down_payment:>10,.0f}")
print(f"Loan Amount:           ${loan_amount:>10,.0f}")
print(f"Monthly Payment:       ${monthly_payment:>10,.0f}")
print()
print(f"Gross Rents (Yr 1):    ${gross_rents:>10,.0f}")
print(f"Effective Gross Inc:   ${effective_gross_income:>10,.0f}")
print(f"Operating Expenses:    ${operating_expenses:>10,.0f}")
print(f"NOI:                   ${noi:>10,.0f}")
print(f"Annual Debt Service:   ${annual_debt_service:>10,.0f}")
print(f"Annual Cash Flow:      ${cash_flow:>10,.0f}")
print()
print(f"Cap Rate:              {cap_rate*100:>9.2f}%")
print(f"Cash-on-Cash Return:   {coc_return*100:>9.2f}%")
print(f"DSCR:                  {dscr:>9.2f}x")
if irr:
    print(f"5-Year IRR:            {irr*100:>9.2f}%")
print("=" * 45)