import urllib.request
import json

FOLDER_ID = "b1grs9f7cacf81tr4vlc"
IAM_TOKEN = "CggaATEVAgAAABKABKfKZMIkkndHjx3xUDrNaK7PApkU6EVzutJI8ugTkiSC_s2VGJQzByCr-GrBSf2705lzGLeVTdGh-izy2hqqsdpF3zXUNaUnkIsSpR5qs7LQfHcjsmprxTdzCT3UnoKxYGFueyw0RyhAqdkBO3BWXgoPffC2jql_yw8qn2G1iaKrYaFGRMFKt5iLvkIlpDKjw4dZmzLE28Z5LJokLDDkVQ5u-W4IxV087Z1D-JkzkR1OikdvlgL0Yh_hXxsQRrCxxPK0uPLxLcuY9gfoVNsXiXnVud2ihNIzic_eFPdkVbaNXBzO0WyEQwwDD5AXgxsqT-p4IiYNDOr5j8GXFSB6yb3GR7b1wUrSSWIFdpvnoVMESerfylDinLC0oOmRVzyLjNTpUWX0pJXfonJGLek5KPKM9SQ_D_y9b88FuQLGTwcX2UkSZV1eUmGEQtxfR30KSrh9wCRJFsqDpNv7gX8JluE_4h5dWbM0QivocGti17kH3qVbc8kslDYZlsngANJfxyeabDzV2MvdDdZfr_FAcb_eGApXXEneu2_yOTuvWY7x6VMUebbzre6Z2e_h6EwogAY4d9EcHUsm7R1rl1XABpwuUfzwBPxPS8h8lqLhMIQazdAurSF9xAzpDdQUe45KVX4n4Ps9UDXxCgmIOvyh2NZY7k5jLyektaAPWK9UaqqcGmcKIDg0YmViYjgxYTZlMzQ4ODA5M2YzNjQ2Nzc5MzMxNjExEOzO1eIFGKyg2OIFIiUKFGFqZTFtaWM1NXRsdXVwaWtzMTFtEg1pdmFuLmtvdmFsZXY1WgAwAjgBSggaATEVAgAAAFABIPYE"

with open("file_9.ogg", "rb") as f:
    data = f.read()

params = "&".join([
    "topic=general",
    "folderId=%s" % FOLDER_ID,
    "lang=ru-RU"
])

url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize/?%s" % params, data=data)
url.add_header("Authorization", "Bearer %s" % IAM_TOKEN)
url.add_header("Transfer-Encoding", "chunked")

responseData = urllib.request.urlopen(url).read().decode('UTF-8')
decodedData = json.loads(responseData)

if decodedData.get("error_code") is None:
    print(decodedData.get("result"))