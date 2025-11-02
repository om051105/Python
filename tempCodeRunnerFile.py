# 1. Load dataset (small, clean, great for beginners)
iris = datasets.load_iris()
X = iris.data      # features (sepal/petal lengths & widths)
y = iris.target    # labels (0,1,2 for species)