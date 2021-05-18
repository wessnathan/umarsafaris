AWS_ACCESS_KEY_ID = 'AKIA3PGB4EV7E3VZP6P4'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'umarsafaris'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

#AWS_LOCATION = 'static'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
#ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

#DEFAULT_FILE_STORAGE = 'safarisapp.settings.aws.storage_backends.MediaStorage'