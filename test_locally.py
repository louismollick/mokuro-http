from mokuro.lambda_function import lambda_handler

if __name__ == "__main__":
    event = {
        'pathParameters': {
            'img': 'https://www.mokuro.moe/manga/Dorohedoro/Dorohedoro%20v01/DH_01%20016.JPG'
        }
    }
    context = []
    lambda_handler(event, context)