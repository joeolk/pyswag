from boto3 import client
from flask import Response


def get_resume():
    """ This function will return my resume
    returns:

    """
    s3 = client(
        's3',
        aws_access_key_id='AKIAVTMRRLGEXEKR32XL',
        aws_secret_access_key='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'
    )

    file = s3.get_object(Bucket='pyswag-joe', Key='JosephOlkowitzResume.pdf')

    return Response(
        file['Body'].read(),
        mimetype='application/pdf',
        headers={
            "Content-Disposition": "attachment;filename=JosephOlkowitzResume.pdf"}
    )
