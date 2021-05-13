class simulationRouter(object): 
    """
    A router to control all database operations on models in the simulation application.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'simulation': #app name（如果該app不存在，則無法同步成功）
            return 'simulationdb' #simulationdb為settings中配置的database節點名稱，並非db name。
        return None
 
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'simulation':
            return 'simulationdb'
        return None
 
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the simulation app is involved.
        當 obj1 和 obj2 之間允許有關係時返回 True ，不允許時返回 False ，或者沒有 意見時返回 None 。
        """
        if obj1._meta.app_label == 'simulation' or \
           obj2._meta.app_label == 'simulation':
            return True
        return None
 

class analysisRouter(object): 
    """
    A router to control all database operations on models in the analysis application.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'analysis': 
            return 'analysisdb' 
        return None
 
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'analysis':
            return 'analysisdb'
        return None
 
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the analysis app is involved.
        當 obj1 和 obj2 之間允許有關係時返回 True ，不允許時返回 False ，或者沒有 意見時返回 None 。
        """
        if obj1._meta.app_label == 'analysis' or \
           obj2._meta.app_label == 'analysis':
            return True
        return None
