from django.db.backends.oracle import base, features


class DatabaseFeatures(features.DatabaseFeatures):
    minimum_database_version = (11,)

class DatabaseWrapper(base.DatabaseWrapper):
    features_class = DatabaseFeatures