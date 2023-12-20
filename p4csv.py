import pandas as pd
from pprint import pprint
from sklearn.feature_selection import mutual_info_classif
from collections import Counter

def id3(df,attribute_names,target_attribute,default_class=None):
    cnt = Counter(x for x in df[target_attribute])
    if len(cnt) == 1:
        return next(iter(cnt))
    elif df.empty or (not attribute_names):
        return default_class
    else:
        gainz = mutual_info_classif(df[attribute_names],df[target_attribute],discrete_features=True)
        index_of_max = gainz.tolist().index(max(gainz))
        best_attr = attribute_names[index_of_max]
        tree = {best_attr:{}}
        remaining_attribute_names = [i for i in attribute_names if i!=best_attr]

        for att_val,data_subset in df.groupby(best_attr):
            subtree = id3(data_subset,remaining_attribute_names,target_attribute,default_class=None)
            tree[best_attr][att_val] = subtree
    
    return tree

df = pd.read_csv('C:/Users/sughosh_sv/Downloads/tennis.csv')

attribute_names = df.columns.tolist()
attribute_names.remove('PlayTennis')
print(df)

for col in df.select_dtypes("object"):
    df[col],_ = df[col].factorize()

print(df)
tree = id3(df,attribute_names,'PlayTennis')
pprint(tree)



