from google import genai
from google.colab import userdata

# Gemini API client
api_key = userdata.get('GOOGLE_API_KEY')
client = genai.Client(api_key=api_key)

FEW_SHOT_EXAMPLES = [
    ("Balance Sheet example: Assets 100000 Liabilities 40000", "Balance Sheet"),
    ("Cash Flow Statement showing cash from operations: 5000", "Cash Flow"),
    ("Income Statement: Revenue 150000 Net Income 12000", "Income Statement"),
    ("Notes: accounting policies and footnotes for financial statements", "Notes"),
    ("Invoice for office supplies purchased", "Others"),
]

def classify_with_gemini_text(text, max_input_chars=3800):
    shots = "\n\n".join([f"Document: {s}\nLabel: {l}" for s,l in FEW_SHOT_EXAMPLES])
    sample = text[:max_input_chars].replace("\n"," ")
    prompt = (
        f"{shots}\n\nInstruction: Return exactly one label (case-sensitive): "
        "Balance Sheet, Cash Flow, Income Statement, Notes, Others.\n\n"
        f"Document: {sample}\nLabel:"
    )
    resp = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    out = resp.text.strip()
    for label in ["Balance Sheet","Cash Flow","Income Statement","Notes","Others"]:
        if label.lower() in out.lower(): return label
    return out.splitlines()[0].strip().split()[0][:40]
