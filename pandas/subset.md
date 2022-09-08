* 获取指定列，传入column list即可，如df[['col1','col2']]返回一个DataFrame, 
df['col1']返回Series
* 条件判断
    * sample_data[sample_data['fre']>5]
    * sample_data[sample_data['action']=='WECHAT_WXA__PAGE_SHOW']
    * sample_data[sample_data['action'].isin(['UDE_362ZKHLROK7','WECHAT_WXA__PAGE_SHOW'])]
    * isin([]):sample_data['fre'].isin([5,8]),sample_data[sample_data['action'].isin(['UDE_362ZKHLROK7','WECHAT_WXA__PAGE_SHOW'])]
    * 多条件：或判断用“|”表示，与用“&”表示：
        * sample_data[(sample_data['fre']>=5) & (sample_data['fre']<=8)]   
        * sample_data[(sample_data['fre']>=5) | (sample_data['fre']<=8)]
    * 筛选不为Null的行, notna()和notnull()等价， isna(),isnull()
        * sample_data[sample_data['user_id'].notna()
*  select specific rows and columns from a DataFrame
    * loc:label-based selection,名称索引，row:可以使用名称和切片，column使用名称索引
        * loc[row_condi,col_names]
        * iloc与Python中 (:)的含义相同，包含（:）前的值，不包含（:）后的值
    * iloc:index-based selection只能使用切片索引，
        * iloc[row_slice,col_slice]
        * loc中使用(:)不仅包含（:）前的值，也包含（:）后的值
        
* 切片操作（slice index）:根据整数索引或者行标签选取数据
    * sample_data[0:2]
* python切片方式
    * [m:n] #切片操作，取a[m]~a[n-1]之间的内容，m\n可以为负，m>n时返回空
    * [m::n] #从a[m]开始，每跳|n|个取一个，当n为负时逆序取数，当n为正的时候，m为空则默认m=0，n为负时，m为空则默认为-1

    
