import base64

base64_encoded = 'c2hvcElkOjEyMzQuc2NpZDo0MzIxLmN1c3RvbWVyTnVtYmVyOmFiYzAwMC5zaG9wQXJ0aWNsZUlkOjU2Nzg5MC5wYXltZW50VHlwZTpBQy5vcmRlck51bWJlcjphYmMxMTExMTExLmN1c3ROYW1lOkpvaG4gRG9lLmN1c3RBZGRyOtCc0L7RgdC60LLQsCwg0LAv0Y8gMTAwLm9yZGVyRGV0YWlsczrQodGH0LDRgdGC0YzQtSDQtNC70Y8g0LLRgdC10YUsINCyINC/0LDQutC10YLQuNC60LDRhSwg0YDQvtGB0YHRi9C/0YzRjg=='

def decoding_of_base64(base64_encoded):
    decoded_receipt = dict(tuple(element.split(':')) 
    for element in base64.b64decode(base64_encoded).decode("utf-8").split('.'))
    return decoded_receipt
    
def tranfering_number_string_to_integers(decoded_receipt):
    decoded_receipt.update((key, int(decoded_receipt[key])) 
    for key in decoded_receipt if decoded_receipt[key].isnumeric() == True)
    return decoded_receipt  
    
if __name__ == '__main__': 
    decoded_receipt = decoding_of_base64(base64_encoded)
    dict_with_receipt_info = tranfering_number_string_to_integers(decoded_receipt)
    print(dict_with_receipt_info)