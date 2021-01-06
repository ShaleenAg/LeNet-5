pd.DataFrame(np.transpose(np.unique(train['labels'], 
                                    return_counts=True)),columns=['Label','Count']).plot(x='Label',\
                                         y='Count',kind='bar',legend=False,figsize=(8,6));