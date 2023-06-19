from intasend import APIService

publishable_key = "ISPubKey_test_8c36241c-8187-417a-931a-d40a5959b620"
token ="ISSecretKey_test_5b7f5039-31ef-4b4f-ace2-3aa249e2b345"
service = APIService(publishable_key=publishable_key,token=token,test=True)

response = service.collect.mpesa_stk_push(phone_number=254111383064,
                                  email="erastuseven@gmail.com", amount=5, narrative="Purchase")
print(response)