import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MinMaxScaler


class DataUtil:
    def __init__(self, n_row=300, path_list=[], n_time_step=30, n_features=9):
        self.n_row = n_row
        self.path_list = path_list
        self.n_time_step = n_time_step
        self.n_features = n_features
        self.col_names = ['time_stamp', 'id', 'dlc', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'R']
        self.label_to_activity = {0: 'DoS', 1: 'Fuzzy', 2: 'RPM', 3: 'gear', 4: 'Normal'}
        self.activity_to_label = {'DoS': 0, 'Fuzzy': 1, 'RPM': 2, 'gear': 3, 'Normal': 4}
        self.scale_columns = ['id', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7']
        self.scalar = MinMaxScaler()
        self.final_data = None

    def create_int_feature(self, data_frame, label):
        data_frame = data_frame.dropna()
        feature_list = []
        row_num = data_frame.shape[0]
        for col in data_frame.columns:
            data_frame[col] = data_frame[col].apply(int, base=16)
        data_frame[self.scale_columns] = self.scalar.fit_transform(data_frame[self.scale_columns])
        for i in range(0, row_num, self.n_time_step):
            if row_num >= i + self.n_time_step:
                tem_file = data_frame.iloc[i:i + self.n_time_step, :].values
                feature_list.append(tem_file)
        feature_df = pd.DataFrame(data={"features": feature_list, "label": [label] * len(feature_list)})
        return feature_df

    def read_files(self, is_shuffle=True):
        feature_df = []
        for file_path in self.path_list:
            if "DoS".lower() in file_path.lower():
                dos_data = pd.read_csv(file_path, nrows=self.n_row, header=None)
                dos_data.columns = self.col_names
                dos_data = dos_data.drop(['time_stamp', 'dlc', 'R'], axis=1)
                dos_feature_df = self.create_int_feature(dos_data, 0)
                feature_df.append(dos_feature_df)
            elif 'Fuzzy'.lower() in file_path.lower():
                fuzzy_data = pd.read_csv(file_path, nrows=self.n_row, sep=',', header=None)
                fuzzy_data.columns = self.col_names
                fuzzy_data = fuzzy_data.drop(['time_stamp', 'dlc', 'R'], axis=1)
                fuzzy_feature_df = self.create_int_feature(fuzzy_data, 1)
                feature_df.append(fuzzy_feature_df)
            elif 'gear'.lower() in file_path.lower():
                gear_data = pd.read_csv(file_path, nrows=self.n_row, sep=',', header=None)
                gear_data.columns = self.col_names
                gear_data = gear_data.drop(['time_stamp', 'dlc', 'R'], axis=1)
                gear_feature_df = self.create_int_feature(gear_data, 2)
                feature_df.append(gear_feature_df)
            elif 'RPM'.lower() in file_path.lower():
                rpm_data = pd.read_csv(file_path, nrows=self.n_row, sep=',', header=None)
                rpm_data.columns = self.col_names
                rpm_data = rpm_data.drop(['time_stamp', 'dlc', 'R'], axis=1)
                rpm_feature_df = self.create_int_feature(rpm_data, 3)
                feature_df.append(rpm_feature_df)
            else:
                norm_data = pd.read_csv(file_path, nrows=self.n_row, sep=',', header=None)
                norm_data.columns = self.col_names[:11]
                norm_data = norm_data.drop(['time_stamp', 'dlc'], axis=1)
                norm_feature_df = self.create_int_feature(norm_data, 4)
                feature_df.append(norm_feature_df)
        self.final_data = pd.concat(feature_df, ignore_index=True)
        if is_shuffle:
            self.final_data = shuffle(self.final_data)
        return self.final_data

    def get_train_data(self):
        onehot_encoder = LabelBinarizer()
        features = np.concatenate(self.final_data.features.values)
        features = features.reshape(-1, self.n_time_step, self.n_features)
        transfomed_label = onehot_encoder.fit_transform(self.final_data.label)
        return features, transfomed_label
