# sql.py 
# const sql for backend

# sql_prob_get_by_id 
# params : id
sql_prob_get_by_id = '''
    SELECT A.[id]
      ,A.[MDL_TYP]
      ,A.[KDNR]
      ,A.[PBC]
      ,A.[PBD]
      ,A.[PBE]
      ,A.[MARK]
      ,A.[ND_TRAN]
      ,A.[QPZ]
      ,A.[FAP_KZ]
      ,A.[BA]
      ,A.[PB_STT]
      ,A.[FZG_VOL]
      ,A.[PRNR_STR]
      ,A.[KD_ORT]
      ,A.[LB_KZ]
      ,A.[PCD]
      ,A.[PS_KZ]
      ,A.[PB_EXT]
      ,A.[BEKANT_D]
      ,A.[END_D]
      ,A.[MOP1]
      ,A.[MOP2]
      ,A.[PLV]
      ,A.[USERNAME]
      ,A.[INS_D]
      ,A.[UPD_D]
      ,A.[TAXI]
      ,B.[name2]
  FROM [Prob].[dbo].[PB] as A 
LEFT OUTER JOIN [MQRDB].dbo.[User] as B on A.USERNAME = B.USERNAME 
where A.id = :id
    '''