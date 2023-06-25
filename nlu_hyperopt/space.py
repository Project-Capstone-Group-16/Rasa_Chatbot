from hyperopt import hp


search_space = {"epochs": hp.qloguniform("epochs", 100, 200, 300)}