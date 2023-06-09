import sys
import subprocess
import urllib3
from minio import Minio
from minio import Minio
from minio.credentials import StaticProvider

verify = False



def run_spider():
    result = subprocess.run(["scrapy", "runspider", "crypto_spider.py"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

if __name__ == "__main__":
    run_spider()
    verify = True

if verify:

# Configurar informações de acesso ao MinIO
    minio_client = Minio('172.21.16.154:9001',
                     access_key='21007062',
                     secret_key='21007062',
                     secure=False)

# Fazer o upload do arquivo
    bucket_name = 'main'
    file_path = './dados.txt'
    object_name = 'dados.txt'

    minio_client.fput_object(bucket_name, object_name, file_path)

    print(f"Arquivo '{file_path}' enviado com sucesso para o bucket '{bucket_name}' no MinIO.")


