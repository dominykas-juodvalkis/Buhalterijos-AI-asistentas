import re

def map_to_accounting(label, text, total=None):
    if label == "Income Statement": debit, credit = "7000 Revenue", "4430 Accounts Payable"
    elif label == "Balance Sheet": debit, credit = "1000 Assets", "2000 Equity/Liabilities"
    elif label == "Cash Flow": debit, credit = "1500 Cash", "6000 Cash Flow Adjustment"
    elif label == "Notes": debit, credit = "9999 Notes", "0000"
    else: debit, credit = "6300 General Expense", "4430 Accounts Payable"
    
    if total is not None: amt = total
    else:
        m = re.search(r"(Total|AMOUNT|Amount)[: ]+([0-9,.]+)", text, re.IGNORECASE)
        amt = float(m.group(2).replace(",","")) if m else None
    return {"debit": debit, "credit": credit, "amount": amt}
