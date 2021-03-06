from Base.BaseStatistics import countSum, countInfo
from Base.BaseYaml import getYam
from Base.BaseOperate import OperateElement
from Base.BaseLog import myLog


class FirstOpen:
    '''
    kwargs: WebDriver driver, String path(yaml配置参数)
    isOperate: 操作失败，检查点就失败
    testInfo：
    testCase：
    '''

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        self.path = kwargs["path"]
        self.operateElement = OperateElement(self.driver)
        self.isOperate = True
        self.testInfo = getYam(self.path)["testinfo"]
        self.testCase = getYam(self.path)["testcase"]


    '''
    操作步骤
    logTest 日记记录器
    '''

    def operate(self, logTest):
        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo, logTest)

            if not result:
                print("操作失败")
                self.isOperate = False
                break

    '''
    检查点
    caseName:函数名
    logTest 记录日志：一个手机记录单独记录一个日志
    '''

    def checkPoint(self, caseName, logTest, devices):
        result = False
        if not self.isOperate:
            print("操作失败,检查点失败")
            # return self.isOperate
        else:
            check = getYam(self.path)["check"]
            result = self.operateElement.findElement(check)  # 检查点

        countSum(result)
        countInfo(result=result, testInfo=self.testInfo, caseName=caseName, driver=self.driver, logTest=logTest, devices=devices)
        return result
