#packages
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def read_data():
	#given data
	odf=pd.read_csv('breast-cancer-wisconsin.csv')
	return odf

def get_headers(dataset):
	return dataset.columns.values

def add_headers(dataset,headers):
	dataset.columns=headers
	return dateset

def data_file_csv():
	pd.to_csv('breast-cancer-wisconsin.csv')

def split_dataset(dataset,train_percentage,feature_headers,target_headers):
	train_x,test_x,train_y,test_y=train_test_split(dataset[feature_headers],dataset[target_headers],train_size=train_percentage)
	return train_x,test_x,train_y,test_y

def handle_missing_values(dataset,missing_values_header,missing_label):
	t=missing_values_header

	x=(dataset[t]!=missing_label)

	return dataset[x]

def random_forest_classifier(features,targets):
	clf=RandomForestClassifier()
	clf.fit(features,targets)
	return clf

def dataset_statistics(dataset):
	print(dataset.describe())

def main():
	dataset=read_data()
	dataset_statistics(dataset)
	HEADERS=get_headers(dataset)
	dataset=handle_missing_values(dataset,HEADERS[6],'?')

	train_x,test_x,train_y,test_y=split_dataset(dataset,0.7,HEADERS[1:-1],HEADERS[-1])
	print("train_X shape :",train_x.shape)
	print("train_y shape :",train_y.shape)
	print("test_X shape :",test_x.shape)
	print("test_y shape :",test_y.shape)
	



main()