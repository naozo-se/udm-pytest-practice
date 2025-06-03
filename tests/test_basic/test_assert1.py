x_sum = 1 + 1
assert x_sum == 2, "1+1は2です"
print("数値チェックOK")


hello = "hello" + " " + "world"
assert hello == "hello world", "文字列の結合が間違っています"
print("文字列チェックOK")


items = []
items.append("python")
items.append("python3")
assert items == ["python", "python3"], "アイテムが間違っています"
print("リストチェックOK")