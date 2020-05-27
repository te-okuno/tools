# storeSelected.py

選択されたコンポーネントを一時保存するツール。

- 複数オブジェクトに対応
- リストをダブルクリックでオブジェクトを選択
- Selectボタンでコンポーネント選択
- reloadボタンから選択しているものでリストを更新

## 手順
1. 頂点、エッジ、面の選択状態からツール起動、または選択状態からreloadボタンを押すとオブジェクト名がリストに登録される
2. リストのオブジェクト名を選択し、Selectボタンで選択状態になる

## 起動方法
```
import sys
sys.path.append(スクリプトを置いているフォルダパス)
import storeSelected
storeSelected.ObjListWindow()
```
