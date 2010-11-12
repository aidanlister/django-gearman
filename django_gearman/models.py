from django.conf import settings
import gearman
import pickle

class PickleDataEncoder(gearman.DataEncoder):
    """ Since this is a Django app, allow the passing of raw python objects. """
    @classmethod
    def encode(cls, encodable_object):
        return pickle.dumps(encodable_object)

    @classmethod
    def decode(cls, decodable_string):
        return pickle.loads(decodable_string)


class DjangoGearmanClient(gearman.GearmanClient):
    """ Gearman client which automatically connects to configured server. """
    data_encoder = PickleDataEncoder
    
    def __init__(self, **kwargs):
        return super(DjangoGearmanClient, self).__init__(
                settings.GEARMAN_SERVERS, **kwargs)


class DjangoGearmanWorker(gearman.GearmanWorker):
    """ Gearman workder which automatically connects to the configured server. """

    def __init__(self, **kwargs):
        return super(DjangoGearmanWorker, self).__init__(
                settings.GEARMAN_SERVERS, **kwargs)


