import matplotlib.pyplot as plt
import pandas as pd
import argparse
import numpy as np
import math


class Plot3D():
    def __init__(
            self,
            in_filename=None,
            input_col_nums=None,
            output_col_nums=None):
        """

        :param in_filename: 入力ファイル名
        :param input_col_nums: プロット入力値の列番号
        :param output_col_nums: プロット出力値の列番号
        """
        self.in_filename = in_filename
        self.input_col_nums = np.array(input_col_nums)
        self.output_col_nums = np.array(output_col_nums)

    def load_csv(self):
        """Load csv from self.in_file

        :return:
            values: 2d array. 値の2次元配列
            labels: 1d array. データラベルの1次元配列
        """
        return self.load_csv_from_file(self.in_filename)

    @classmethod
    def load_csv_from_file(cls, in_filename):
        """ Load csv file

        :param in_filename: input filename
        :return:
            values: 2d array. 値の2次元配列
            labels: 1d array. データラベルの1次元配列
        """
        if not in_filename:
            return None, None
        df = pd.read_csv(in_filename)
        return df.values, np.array(df.keys())

    def parse_in_out(self, values, labels):
        """Parse input and output array.

        :param values: 2d array
        :param labels: 1d array
        :return:
            input:  2d array. 入力値の2次元配列
            output: 1d array. 出力値の1次元配列.
            in_labels: 1d array. 入力データラベルの1次元配列
            out_labels: 1d array. 出力データラベルの1次元配列
        """
        input_array = None
        # output_array = np.ndarray()
        output_array = None
        for i, output_col_num in enumerate(self.output_col_nums):
            input_col_nums = self.input_col_nums[[i*2, i*2 + 1]]
            if input_array is not None:
                input_array = np.concatenate(
                    (input_array, values[:, input_col_nums]))
            else:
                input_array = values[:, input_col_nums]
            if output_array is not None:
                output_array = np.concatenate(
                    (output_array, values[:, output_col_num]))
            else:
                output_array = values[:, output_col_num]
        in_labels = labels[self.input_col_nums]
        out_labels = labels[self.output_col_nums]
        return input_array, output_array, in_labels, out_labels


if __name__ == '__main__':
    # 実行時オプション整形開始 #
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', default='csv/input.csv',
                        help='input filename default: csv/input.csv')
    parser.add_argument('-i', '--input', default=[3, 7, 3, 8, 3, 9], nargs='+',
                        help='input column number in input csv file.')
    parser.add_argument('-o', '--output', default=[4, 5, 6], nargs='+',
                        help='output column number in input csv file.')
    parser.add_argument('-s', '--size', default=[1],
                        help='size of marker')
    parser.add_argument('-c', '--color', default=[2],
                        help='color map value')
    args = parser.parse_args()
    in_filename = args.file
    input_col_nums = args.input
    if math.fmod(len(input_col_nums), 2):
        raise ValueError('入力値の指定数は2の倍数です。')
    output_col_nums = args.output
    if len(output_col_nums) != len(input_col_nums) / 2:
        raise ValueError('入力値 は 出力値の 倍の数指定してください。')
    # 実行時オプション整形終了 #

    # 初期化
    plot_3d = Plot3D(in_filename, input_col_nums, output_col_nums)
    # ファイル読み込み
    values, labels = plot_3d.load_csv()
    # 入出力整形
    X, y, x_labels, y_labels= plot_3d.parse_in_out(values, labels)
    print('X:', X, 'y:', y, '\nx_labels:', x_labels, y_labels)

    # import ipdb
    # ipdb.set_trace()

