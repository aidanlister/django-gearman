from django.conf import settings
from gearman import GearmanClient, GearmanWorker

class DjangoGearmanClient(GearmanClient):
    """ Gearman client which automatically connects to configured server. """

    def __init__(self, **kwargs):
        return super(DjangoGearmanClient, self).__init__(
                settings.GEARMAN_SERVERS, **kwargs)


class DjangoGearmanWorker(GearmanWorker):
    """ Gearman workder which automatically connects to the configured server. """

    def __init__(self, **kwargs):
        return super(DjangoGearmanWorker, self).__init__(
                settings.GEARMAN_SERVERS, **kwargs)
