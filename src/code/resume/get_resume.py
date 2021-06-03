from boto3 import client
from flask import Response


def get_resume():
    """ This function will return my resume
    returns:

    """
    s3 = client(
        's3',
    )

    file = s3.get_object(Bucket='pyswag-joe', Key='JosephOlkowitzResume.pdf')

    return Response(
        file['Body'].read(),
        mimetype='application/pdf',
        headers={
            "Content-Disposition": "attachment;filename=JosephOlkowitzResume.pdf"}
    )
