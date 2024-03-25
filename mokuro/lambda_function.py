from loguru import logger
from mokuro.manga_page_ocr import MangaPageOcr
import json
import numpy as np

run_model = MangaPageOcr()

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.generic):
            return obj.item()
        return json.JSONEncoder.default(self, obj)

def lambda_handler(event, context):
    img_path = event['pathParameters']['img']
    try:
        result = run_model(img_path)
        logger.info(f'Successfully OCR\'d file "{img_path}"')
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(result, ensure_ascii=False, cls=NumpyEncoder)
        }
    except Exception as e:
        logger.error(f'Failed OCR of file "{img_path}": {e}')
        return e
