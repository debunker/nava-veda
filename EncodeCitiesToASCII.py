
import unicodedata, pandas as pd, numpy as np,re


def convert(text):
    return unicodedata.normalize('NFKD', text).encode('us-ascii', 'ignore').decode('utf-8')
def extractID(text):
    return re.search('[0-9]+',text).group(0)
pd.options.display.float_format = '{:0f}'.format
df = pd.read_csv("C:/Users/hardik.joshi/Desktop/Expereo BI/Work/do_lu_expereooffices.csv")
df.head()
df.dtypes
df['B6_ID']
df['B6_ID']=df['B6_ID'].fillna(0).astype(np.int64)
df['business_address'] = df['business_address'].map(convert)
df['office_legal_name'] = df['office_legal_name'].map(convert)
df.astype(object).convert_objects()
df.to_csv(r'C:/Users/hardik.joshi/Desktop/Expereo BI/Work/MDM_expereo_offices-ascii.csv')
df.dtypes
df['city_id']
df['B6_ID']