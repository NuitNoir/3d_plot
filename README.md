# 3d_plot
3d plot by python matplotlib.

## パッケージインストール
```commandline
pip install -r requirements.txt
```

## 入力csvファイルの設置
csv ディレクトリ配下に入力csvファイルを置く
```commandline
csv/input.csv
```

## 実行
```commandline
python main.py
```

## 実行オプション
実行オプションの表示
```commandline
python main.py --help
```

- -h, --help
  - 実行オプションの表示
  - 使用例) -h (引数なし)
- -f, --file
  - 入力ファイルの指定
  - デフォルト値: csv/input.csv
  - 使用例) -f csv/input2.csv
- -i, --input
  - 入力ファイルにおける入力値の列番号 (0 origin)
  - デフォルト値: 2
  - 使用例) -i 1
- -o, --output
  - 入力ファイルにおける出力値の列番号 (0 origin)
  - デフォルト値: 0, 1
  - 使用例) -o 1, 2
  
