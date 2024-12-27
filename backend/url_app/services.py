from url_app.utils import generate_short_key
import traceback
from url_app.models import URL
from url_app.serializers import URLSerializer


class URLSrv:
    
    def __init__(self,user,data=None):
        self.user = user
        self.data = data
    
    def get_short_key(self):
        custom_alias = self.data.get('custom_alias',None)
        long_url = self.data.get('long_url',None)
        if custom_alias is not None:
            url_obj = URL.objects.filter(short_url_key=custom_alias)
            if len(url_obj)>0:
                return "alias already taken","S_01"
            else:
                self.data['short_url_key'] = custom_alias
                return "short url created","1"
        elif long_url is not None:
            short_key = generate_short_key(long_url)
            # url_obj = URL.objects.filter(short_url_key=short_key)
            # if len(url_obj)>0:
            #     long_url += "/"+str(self.user.id)
            #     short_key = generate_short_key(long_url)
            #     url_obj = URL.objects.filter(short_url_key=short_key)
            #     if len(url_obj)>0:
            #         return "cannot cerate short, use custom alias, or give unique key","S_02"
            #     #TODO: add case of custom unique key
            #     else:
            #         self.data['short_url_key'] = short_key
            #         self.data['long_url'] = long_url
            #         return "short url created","1"
            # else:
            self.data['short_url_key'] = short_key
            return "short url created","1"
        else:
            return "long url is required","S_03"
            

    
    def create_record(self):
        try :
            out_data = []
            if self.data:
                self.data['user'] = self.user.id
                msg,code = self.get_short_key()
                if code!="1":
                    return [],msg,code
                url_serializer = URLSerializer(data=self.data)
                if url_serializer.is_valid():
                    url_serializer.save()
                    return url_serializer.data,"Record Saved SuccessFully.","1"
                out_data = url_serializer.errors
            return out_data,"Error while creating a task record.","S_01"
        except Exception as ex:
            print(traceback.format_exc())        
            return str(ex),"Error while creating a task record.","S_02"
    
    def get_all_records(self,):
        try:
            all_task_queryset = URL.objects.filter(user_id=self.user.id)
            # if status is not None and status != "all":
                # status_val = status == 'completed'
                # all_task_queryset = all_task_queryset.filter(is_completed=status_val)
            url_serializer = URLSerializer(all_task_queryset,many=True)
            return url_serializer.data,"All Records fetched SuccessFully.","1"
        except Exception as ex:
            print(traceback.format_exc())        
            return str(ex),"Error while fetching all user task record.","S_03"
    
    
    def get_single_record(self,task_id):
        try:
            all_task_queryset = URL.objects.filter(id=task_id).first()
            url_serializer = URLSerializer(all_task_queryset)
            return url_serializer.data,"Single Record fetched SuccessFully.","1"
        except Exception as ex:
            print(traceback.format_exc())        
            return str(ex),"Error while fetching single task record.","S_04"
        
    def update_record(self,task_id):
        try :
            out_data = []
            if self.data:
                task_obj = URL.objects.filter(id=task_id).first()
                if task_obj:
                    url_serializer = URLSerializer(task_obj, data=self.data, partial=True)
                    if url_serializer.is_valid():
                        url_serializer.save()
                        return url_serializer.data,"Record Updated SuccessFully.","1"
                    out_data = url_serializer.errors
                else:
                    return "Task not found","Error while updating a task record.","S_05"
            return out_data,"Error while updating a task record.","S_06"
        except Exception as ex:
            print(traceback.format_exc())        
            return str(ex),"Error while updating a task record.","S_07"     
    
    def delete_record(self,task_id):
        try:
            task_obj = URL.objects.filter(id=task_id).first()
            if task_obj:
                task_obj.delete()
                return [],"Task deleted successfully.","1"
            else:
                return [],"Task not found.","S_09"
        except Exception as ex:
            print(traceback.format_exc())        
            return str(ex),"Error while deleting a task record.","S_10"
        
    def redirect_to_url(self,short_url_key):
        url_obj = URL.objects.filter(short_url_key=short_url_key)
        return url_obj.first().long_url if url_obj.exists() else None
        
