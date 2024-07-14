import json
from loguru import logger
from celery import Celery
from mokuro.manga_page_ocr import MangaPageOcr
from mokuro.utils import NumpyEncoder

run_model = MangaPageOcr()

app = Celery("mokuro", broker="redis://", backend="redis://", task_ignore_result=True)


@app.task(name="mokuro")
def mokuro(manga_id, volume_number, page_number, img_path):
    try:
        logger.info(f'Received img_path from queue "{img_path}"')
        result = run_model(img_path)
        result_json = json.dumps(result, ensure_ascii=False, cls=NumpyEncoder)
        app.send_task(
            "mokuro_result",
            args=[manga_id, volume_number, page_number, img_path, result_json],
            queue="mokuro_result",
        )
        logger.info(f'Successfully OCR\'d img_path from queue "{img_path}"')
    except Exception as e:
        logger.error(f'Failed to OCR from img_path from queue "{img_path}": {e}')
    return True
