import logging

import azure.functions as func


def main(documents: func.DocumentList) -> str:
    if documents:
        print(documents[0]['id'])
        logging.info('Document id: %s', documents[0]['id'])
