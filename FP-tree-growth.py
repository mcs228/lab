# FP-Growth Algorithm Implementation
# Install mlxtend if not available:
# pip install mlxtend
import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

# ---- Step 1: Create a simple transaction dataset ----
dataset = [
    ["Milk", "Bread", "Eggs"],
    ["Milk", "Bread"],
    ["Milk", "Apple"],
    ["Bread", "Eggs"],
    ["Milk", "Bread", "Apple", "Eggs"],
    ["Bread", "Apple"],
]

# ---- Step 2: Convert dataset to one-hot encoded DataFrame ----
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

print("Transaction Dataset:")
print(df)

# ---- Step 3: Apply FP-Growth algorithm ----
frequent_itemsets = fpgrowth(df, min_support=0.3, use_colnames=True)
print("\nFrequent Itemsets using FP-Growth:")
print(frequent_itemsets)

# ---- Step 4: Generate association rules ----
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)
print("\nAssociation Rules:")
print(rules[["antecedents", "consequents", "support", "confidence", "lift"]])
