def create_html(file1,param1,dict1):
    import pandas as pd
    input_name =param1
    df = pd.DataFrame(dict1)
    index = df.loc[df['usn'] == input_name].index[0]
    name = dict1['names'][index]
    email = dict1['email'][index]
    branch = dict1['subjects'][index]
    m_number = dict1['mobile_number'][index].astype(str)
    photo=dict1['photo'][index]
    file1.seek(0)
    info1 =file1.read()
    info1 = info1.decode()
    info1 = info1.replace('$NAME',name)
    info1 = info1.replace('$BRANCH',branch)
    info1 = info1.replace('$EMAIL',email)
    info1 = info1.replace('$PHONE',m_number)
    info1 = info1.replace('$PHOTO',photo)
    print(info1)
    return info1
    
