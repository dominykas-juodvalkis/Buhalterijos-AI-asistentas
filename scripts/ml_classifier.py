def infer_label_from_path(pathstr):
    low = pathstr.lower()
    if "balance" in low: return "Balance Sheet"
    if "cash" in low: return "Cash Flow"
    if "income" in low: return "Income Statement"
    if "notes" in low: return "Notes"
    return "Others"
