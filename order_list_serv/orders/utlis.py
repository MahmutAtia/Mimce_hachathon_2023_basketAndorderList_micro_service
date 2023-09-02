def get_product_id_list(arr):
       out = [dict(item)["product_id"] for item in arr]
       return out