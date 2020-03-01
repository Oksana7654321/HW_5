def filter_words(st):
    st = st.lower() 
    st_01 = st[0]
    st = st[1:]
    return ' '.join(str(st_01.upper() + st).split())