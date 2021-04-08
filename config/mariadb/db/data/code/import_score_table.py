import pandas as pd
import pymysql
from sqlalchemy import create_engine

engine = create_engine(f'mysql+pymysql://root:qaz123456789@localhost:3306/experiment')
def import_ctvalue_data(tissue):
  df = pd.read_csv('../scorecard/ct_value_'+tissue+'.csv')
  # 將新建的DataFrame儲存為MySQL中的資料表，不儲存index列
  df.to_sql('CT_value_'+tissue, engine, index= False)
def import_foldchange_data(tissue):
  df = pd.read_csv('../scorecard/fold_change_'+tissue+'.csv')
  # 將新建的DataFrame儲存為MySQL中的資料表，不儲存index列
  df.to_sql('Fold_change_'+tissue, engine, index= False)
def import_score_data():
   df = pd.read_csv('../scorecard/results_scores.csv')
   df.to_sql('Score', engine, index= False)
tissues = ['ectoderm','endoderm','mesendoderm','mesoderm','selfrenewal','other','control']

'''
for ele in tissues:
  import_ctvalue_data(ele)
for i in range(5):
  import_foldchange_data(tissues[i])
import_score_data()
'''
