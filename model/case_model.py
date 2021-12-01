# coding = utf-8
class steps_model():
    sort = '' # 执行步骤
    action = '' # 对应的操作
    searchType = '' # 获取元素的方式
    searchValue = '' # 获取元素的具体值
    searchBy = '' # 获取复数元素的方式,By.XX
    searchIndex = '' # 获取复数元素时，取的哪个下标
    validataData = '' # 特殊处理的值
    validateAttr = '' # 断言需要拿到的属性值

    # def __init__(self,sort,action,searchType,searchValue,searchBy=None,searchIndex=None,validataData=None,validateAttr=None):
    #     self.sort = sort
    #     self.action = action
    #     self.searchType = searchType
    #     self.searchValue = searchValue
    #     self.searchBy = searchBy
    #     self.searchIndex = searchIndex
    #     self.validataData = validataData
    #     self.validateAttr = validateAttr
