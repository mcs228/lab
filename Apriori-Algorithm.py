# Apriori Algorithm Implementation
# Install mlxtend if not available:
# pip install mlxtend

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# ---- Step 1: Create Dataset ----
dataset = [
    ["Milk", "Bread", "Eggs"],
    ["Milk", "Bread"],
    ["Milk", "Apple"],
    ["Bread", "Eggs"],
    ["Milk", "Bread", "Apple", "Eggs"],
    ["Bread", "Apple"],
]

# ---- Step 2: Convert Dataset to One-Hot Encoded DataFrame ----
from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

print("Transaction Dataset:")
print(df)

# ---- Step 3: Apply Apriori Algorithm ----
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)
print("\nFrequent Itemsets:")
print(frequent_itemsets)

# ---- Step 4: Generate Association Rules ----
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)
print("\nAssociation Rules:")
print(rules[["antecedents", "consequents", "support", "confidence", "lift"]])
