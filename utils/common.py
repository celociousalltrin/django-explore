def get_child_data(data,keys):
    if data:
        result={}
        for key in keys:
            result.setdefault(key,getattr(data,key))
        return result
    else:
        return None