import numpy as np
import pandas as pd

def convert(d):
	col = d.columns
	for c in col:
		u = d[c].unique()
		tmp_dict = {}
		tmp_val = [ [v,i] for i,v in zip(range(len(u)),u)]
		dict_val = dict(tmp_val)
		conv_val = [dict_val[i] for i in d[c].values]
		d.loc[:,c] = conv_val
	return d


if __name__ == '__main__':

	a = [chr(i + ord('A')) for i in np.random.randint(1,24,50)]
	b = [chr(i + ord('A')) for i in np.random.randint(1,24,50)]
	c = [chr(i + ord('A')) for i in np.random.randint(1,24,50)]

	X = np.concatenate([[a,b,c]],axis=0)
	X = np.transpose(X)
	X = pd.DataFrame(X)
	X.columns = ['happy','pappy','smappy']
	#print X

	print convert(X)

