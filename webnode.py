
class WebNode:
    #全ノード共通ドメイン　いらないかも...
    domain = https://home.komatsu
    def __init__(self, path, type, parent):
        self.path = path
        self.type = type
        self.parent = []
        self.parent.append(parent)
        self.children = []
    
    #親ページの追加
    def addParent(self, parent):
        self.parent.append(parent)

    #子ページの追加
    def addChild(self, child):
        self.parent.append(child)