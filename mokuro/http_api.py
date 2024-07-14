import json
from loguru import logger
from flask import Flask, request
from urllib.parse import urlparse, quote
from mokuro.manga_page_ocr import MangaPageOcr
from mokuro.utils import NumpyEncoder

run_model = MangaPageOcr()

app = Flask(__name__)


def make_safe_url(url: str) -> str:
    """
    Returns a parsed and quoted url
    """
    _url = urlparse(url)
    query = ("?" + quote(_url.query)) if _url.query else ""
    url = _url.scheme + "://" + _url.netloc + quote(_url.path) + query
    return url


@app.route("/")
def mokuro():
    img_path_str = request.args.get("src", None, type=str)
    if not img_path_str:
        return "Missing 'src' query parameter.", 400
    try:
        img_path = make_safe_url(img_path_str)
        logger.info(f'Received src "{img_path}"')
        result = run_model(img_path)
        logger.info(f'Successfully OCR\'d file "{img_path}"')
        return json.dumps(result, ensure_ascii=False, cls=NumpyEncoder), 200
    except Exception as e:
        logger.error(f'Failed OCR of file "{img_path_str}": {e}')
        return e
