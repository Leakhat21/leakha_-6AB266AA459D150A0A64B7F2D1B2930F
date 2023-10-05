def linearsearchproduct(productList, targerProduct):
  indices = []
  for index, product in enumerate(productList):
    if (product == targerProduct):
      indices.append(index)
  return indices


products = ["shoes", "boots", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = "bata"
result = linearsearchproduct(products, target)
print(result)