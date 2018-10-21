import pickle

dow={1:'mon',2:'tue',3:'wed',4:'thurs'}

pickle.dump(dow,open('pickle_file.pkl','wb'))

kk=pickle.load(open('pickle_file.pkl','rb'))
