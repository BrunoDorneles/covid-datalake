import pandas as pd
import awswrangler as wr

def get_data(bucket, data):
    try:
        url = f"https://raw.githubusercontent.com/wcota/covid19br/master/{data}.csv"
        df = pd.read_csv(url)
        date = df['date'][0]
        wr.s3.to_parquet(df=df, path=f's3://{bucket}/{data}/{date}/{data}.parquet')
    except Exception as exc:
        raise exc

def lambda_handler(event, context):
    get_data('datalake-projeto-covid', 'cases-brazil-total')
    get_data('datalake-projeto-covid', 'cases-brazil-cities')